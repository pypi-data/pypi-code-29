import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("serverlessrepo", *args, **kwargs)

    def create_application(
        self,
        _request: shapes.CreateApplicationRequest = None,
        *,
        author: str,
        description: str,
        name: str,
        home_page_url: str = ShapeBase.NOT_SET,
        labels: typing.List[str] = ShapeBase.NOT_SET,
        license_body: str = ShapeBase.NOT_SET,
        license_url: str = ShapeBase.NOT_SET,
        readme_body: str = ShapeBase.NOT_SET,
        readme_url: str = ShapeBase.NOT_SET,
        semantic_version: str = ShapeBase.NOT_SET,
        source_code_url: str = ShapeBase.NOT_SET,
        spdx_license_id: str = ShapeBase.NOT_SET,
        template_body: str = ShapeBase.NOT_SET,
        template_url: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateApplicationResponse:
        """
        Creates an application, optionally including an AWS SAM file to create the first
        application version in the same call.
        """
        if _request is None:
            _params = {}
            if author is not ShapeBase.NOT_SET:
                _params['author'] = author
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if home_page_url is not ShapeBase.NOT_SET:
                _params['home_page_url'] = home_page_url
            if labels is not ShapeBase.NOT_SET:
                _params['labels'] = labels
            if license_body is not ShapeBase.NOT_SET:
                _params['license_body'] = license_body
            if license_url is not ShapeBase.NOT_SET:
                _params['license_url'] = license_url
            if readme_body is not ShapeBase.NOT_SET:
                _params['readme_body'] = readme_body
            if readme_url is not ShapeBase.NOT_SET:
                _params['readme_url'] = readme_url
            if semantic_version is not ShapeBase.NOT_SET:
                _params['semantic_version'] = semantic_version
            if source_code_url is not ShapeBase.NOT_SET:
                _params['source_code_url'] = source_code_url
            if spdx_license_id is not ShapeBase.NOT_SET:
                _params['spdx_license_id'] = spdx_license_id
            if template_body is not ShapeBase.NOT_SET:
                _params['template_body'] = template_body
            if template_url is not ShapeBase.NOT_SET:
                _params['template_url'] = template_url
            _request = shapes.CreateApplicationRequest(**_params)
        response = self._boto_client.create_application(**_request.to_boto())

        return shapes.CreateApplicationResponse.from_boto(response)

    def create_application_version(
        self,
        _request: shapes.CreateApplicationVersionRequest = None,
        *,
        application_id: str,
        semantic_version: str,
        source_code_url: str = ShapeBase.NOT_SET,
        template_body: str = ShapeBase.NOT_SET,
        template_url: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateApplicationVersionResponse:
        """
        Creates an application version.
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            if semantic_version is not ShapeBase.NOT_SET:
                _params['semantic_version'] = semantic_version
            if source_code_url is not ShapeBase.NOT_SET:
                _params['source_code_url'] = source_code_url
            if template_body is not ShapeBase.NOT_SET:
                _params['template_body'] = template_body
            if template_url is not ShapeBase.NOT_SET:
                _params['template_url'] = template_url
            _request = shapes.CreateApplicationVersionRequest(**_params)
        response = self._boto_client.create_application_version(
            **_request.to_boto()
        )

        return shapes.CreateApplicationVersionResponse.from_boto(response)

    def create_cloud_formation_change_set(
        self,
        _request: shapes.CreateCloudFormationChangeSetRequest = None,
        *,
        application_id: str,
        stack_name: str,
        parameter_overrides: typing.List[shapes.ParameterValue
                                        ] = ShapeBase.NOT_SET,
        semantic_version: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateCloudFormationChangeSetResponse:
        """
        Creates an AWS CloudFormation change set for the given application.
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            if stack_name is not ShapeBase.NOT_SET:
                _params['stack_name'] = stack_name
            if parameter_overrides is not ShapeBase.NOT_SET:
                _params['parameter_overrides'] = parameter_overrides
            if semantic_version is not ShapeBase.NOT_SET:
                _params['semantic_version'] = semantic_version
            _request = shapes.CreateCloudFormationChangeSetRequest(**_params)
        response = self._boto_client.create_cloud_formation_change_set(
            **_request.to_boto()
        )

        return shapes.CreateCloudFormationChangeSetResponse.from_boto(response)

    def delete_application(
        self,
        _request: shapes.DeleteApplicationRequest = None,
        *,
        application_id: str,
    ) -> None:
        """
        Deletes the specified application.
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            _request = shapes.DeleteApplicationRequest(**_params)
        response = self._boto_client.delete_application(**_request.to_boto())

    def get_application(
        self,
        _request: shapes.GetApplicationRequest = None,
        *,
        application_id: str,
        semantic_version: str = ShapeBase.NOT_SET,
    ) -> shapes.GetApplicationResponse:
        """
        Gets the specified application.
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            if semantic_version is not ShapeBase.NOT_SET:
                _params['semantic_version'] = semantic_version
            _request = shapes.GetApplicationRequest(**_params)
        response = self._boto_client.get_application(**_request.to_boto())

        return shapes.GetApplicationResponse.from_boto(response)

    def get_application_policy(
        self,
        _request: shapes.GetApplicationPolicyRequest = None,
        *,
        application_id: str,
    ) -> shapes.GetApplicationPolicyResponse:
        """
        Retrieves the policy for the application.
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            _request = shapes.GetApplicationPolicyRequest(**_params)
        response = self._boto_client.get_application_policy(
            **_request.to_boto()
        )

        return shapes.GetApplicationPolicyResponse.from_boto(response)

    def list_application_versions(
        self,
        _request: shapes.ListApplicationVersionsRequest = None,
        *,
        application_id: str,
        max_items: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListApplicationVersionsResponse:
        """
        Lists versions for the specified application.
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            if max_items is not ShapeBase.NOT_SET:
                _params['max_items'] = max_items
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListApplicationVersionsRequest(**_params)
        response = self._boto_client.list_application_versions(
            **_request.to_boto()
        )

        return shapes.ListApplicationVersionsResponse.from_boto(response)

    def list_applications(
        self,
        _request: shapes.ListApplicationsRequest = None,
        *,
        max_items: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListApplicationsResponse:
        """
        Lists applications owned by the requester.
        """
        if _request is None:
            _params = {}
            if max_items is not ShapeBase.NOT_SET:
                _params['max_items'] = max_items
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListApplicationsRequest(**_params)
        response = self._boto_client.list_applications(**_request.to_boto())

        return shapes.ListApplicationsResponse.from_boto(response)

    def put_application_policy(
        self,
        _request: shapes.PutApplicationPolicyRequest = None,
        *,
        application_id: str,
        statements: typing.List[shapes.ApplicationPolicyStatement],
    ) -> shapes.PutApplicationPolicyResponse:
        """
        Sets the permission policy for an application. See [Application
        Permissions](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/access-
        control-resource-based.html#application-permissions) for the list of supported
        actions that can be used with this operation.
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            if statements is not ShapeBase.NOT_SET:
                _params['statements'] = statements
            _request = shapes.PutApplicationPolicyRequest(**_params)
        response = self._boto_client.put_application_policy(
            **_request.to_boto()
        )

        return shapes.PutApplicationPolicyResponse.from_boto(response)

    def update_application(
        self,
        _request: shapes.UpdateApplicationRequest = None,
        *,
        application_id: str,
        author: str = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
        home_page_url: str = ShapeBase.NOT_SET,
        labels: typing.List[str] = ShapeBase.NOT_SET,
        readme_body: str = ShapeBase.NOT_SET,
        readme_url: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateApplicationResponse:
        """
        Updates the specified application.
        """
        if _request is None:
            _params = {}
            if application_id is not ShapeBase.NOT_SET:
                _params['application_id'] = application_id
            if author is not ShapeBase.NOT_SET:
                _params['author'] = author
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if home_page_url is not ShapeBase.NOT_SET:
                _params['home_page_url'] = home_page_url
            if labels is not ShapeBase.NOT_SET:
                _params['labels'] = labels
            if readme_body is not ShapeBase.NOT_SET:
                _params['readme_body'] = readme_body
            if readme_url is not ShapeBase.NOT_SET:
                _params['readme_url'] = readme_url
            _request = shapes.UpdateApplicationRequest(**_params)
        response = self._boto_client.update_application(**_request.to_boto())

        return shapes.UpdateApplicationResponse.from_boto(response)
