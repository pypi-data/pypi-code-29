import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("iot1click-projects", *args, **kwargs)

    def associate_device_with_placement(
        self,
        _request: shapes.AssociateDeviceWithPlacementRequest = None,
        *,
        project_name: str,
        placement_name: str,
        device_id: str,
        device_template_name: str,
    ) -> shapes.AssociateDeviceWithPlacementResponse:
        """
        Associates a physical device with a placement.
        """
        if _request is None:
            _params = {}
            if project_name is not ShapeBase.NOT_SET:
                _params['project_name'] = project_name
            if placement_name is not ShapeBase.NOT_SET:
                _params['placement_name'] = placement_name
            if device_id is not ShapeBase.NOT_SET:
                _params['device_id'] = device_id
            if device_template_name is not ShapeBase.NOT_SET:
                _params['device_template_name'] = device_template_name
            _request = shapes.AssociateDeviceWithPlacementRequest(**_params)
        response = self._boto_client.associate_device_with_placement(
            **_request.to_boto()
        )

        return shapes.AssociateDeviceWithPlacementResponse.from_boto(response)

    def create_placement(
        self,
        _request: shapes.CreatePlacementRequest = None,
        *,
        placement_name: str,
        project_name: str,
        attributes: typing.Dict[str, str] = ShapeBase.NOT_SET,
    ) -> shapes.CreatePlacementResponse:
        """
        Creates an empty placement.
        """
        if _request is None:
            _params = {}
            if placement_name is not ShapeBase.NOT_SET:
                _params['placement_name'] = placement_name
            if project_name is not ShapeBase.NOT_SET:
                _params['project_name'] = project_name
            if attributes is not ShapeBase.NOT_SET:
                _params['attributes'] = attributes
            _request = shapes.CreatePlacementRequest(**_params)
        response = self._boto_client.create_placement(**_request.to_boto())

        return shapes.CreatePlacementResponse.from_boto(response)

    def create_project(
        self,
        _request: shapes.CreateProjectRequest = None,
        *,
        project_name: str,
        description: str = ShapeBase.NOT_SET,
        placement_template: shapes.PlacementTemplate = ShapeBase.NOT_SET,
    ) -> shapes.CreateProjectResponse:
        """
        Creates an empty project with a placement template. A project contains zero or
        more placements that adhere to the placement template defined in the project.
        """
        if _request is None:
            _params = {}
            if project_name is not ShapeBase.NOT_SET:
                _params['project_name'] = project_name
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if placement_template is not ShapeBase.NOT_SET:
                _params['placement_template'] = placement_template
            _request = shapes.CreateProjectRequest(**_params)
        response = self._boto_client.create_project(**_request.to_boto())

        return shapes.CreateProjectResponse.from_boto(response)

    def delete_placement(
        self,
        _request: shapes.DeletePlacementRequest = None,
        *,
        placement_name: str,
        project_name: str,
    ) -> shapes.DeletePlacementResponse:
        """
        Deletes a placement. To delete a placement, it must not have any devices
        associated with it.

        When you delete a placement, all associated data becomes irretrievable.
        """
        if _request is None:
            _params = {}
            if placement_name is not ShapeBase.NOT_SET:
                _params['placement_name'] = placement_name
            if project_name is not ShapeBase.NOT_SET:
                _params['project_name'] = project_name
            _request = shapes.DeletePlacementRequest(**_params)
        response = self._boto_client.delete_placement(**_request.to_boto())

        return shapes.DeletePlacementResponse.from_boto(response)

    def delete_project(
        self,
        _request: shapes.DeleteProjectRequest = None,
        *,
        project_name: str,
    ) -> shapes.DeleteProjectResponse:
        """
        Deletes a project. To delete a project, it must not have any placements
        associated with it.

        When you delete a project, all associated data becomes irretrievable.
        """
        if _request is None:
            _params = {}
            if project_name is not ShapeBase.NOT_SET:
                _params['project_name'] = project_name
            _request = shapes.DeleteProjectRequest(**_params)
        response = self._boto_client.delete_project(**_request.to_boto())

        return shapes.DeleteProjectResponse.from_boto(response)

    def describe_placement(
        self,
        _request: shapes.DescribePlacementRequest = None,
        *,
        placement_name: str,
        project_name: str,
    ) -> shapes.DescribePlacementResponse:
        """
        Describes a placement in a project.
        """
        if _request is None:
            _params = {}
            if placement_name is not ShapeBase.NOT_SET:
                _params['placement_name'] = placement_name
            if project_name is not ShapeBase.NOT_SET:
                _params['project_name'] = project_name
            _request = shapes.DescribePlacementRequest(**_params)
        response = self._boto_client.describe_placement(**_request.to_boto())

        return shapes.DescribePlacementResponse.from_boto(response)

    def describe_project(
        self,
        _request: shapes.DescribeProjectRequest = None,
        *,
        project_name: str,
    ) -> shapes.DescribeProjectResponse:
        """
        Returns an object describing a project.
        """
        if _request is None:
            _params = {}
            if project_name is not ShapeBase.NOT_SET:
                _params['project_name'] = project_name
            _request = shapes.DescribeProjectRequest(**_params)
        response = self._boto_client.describe_project(**_request.to_boto())

        return shapes.DescribeProjectResponse.from_boto(response)

    def disassociate_device_from_placement(
        self,
        _request: shapes.DisassociateDeviceFromPlacementRequest = None,
        *,
        project_name: str,
        placement_name: str,
        device_template_name: str,
    ) -> shapes.DisassociateDeviceFromPlacementResponse:
        """
        Removes a physical device from a placement.
        """
        if _request is None:
            _params = {}
            if project_name is not ShapeBase.NOT_SET:
                _params['project_name'] = project_name
            if placement_name is not ShapeBase.NOT_SET:
                _params['placement_name'] = placement_name
            if device_template_name is not ShapeBase.NOT_SET:
                _params['device_template_name'] = device_template_name
            _request = shapes.DisassociateDeviceFromPlacementRequest(**_params)
        response = self._boto_client.disassociate_device_from_placement(
            **_request.to_boto()
        )

        return shapes.DisassociateDeviceFromPlacementResponse.from_boto(
            response
        )

    def get_devices_in_placement(
        self,
        _request: shapes.GetDevicesInPlacementRequest = None,
        *,
        project_name: str,
        placement_name: str,
    ) -> shapes.GetDevicesInPlacementResponse:
        """
        Returns an object enumerating the devices in a placement.
        """
        if _request is None:
            _params = {}
            if project_name is not ShapeBase.NOT_SET:
                _params['project_name'] = project_name
            if placement_name is not ShapeBase.NOT_SET:
                _params['placement_name'] = placement_name
            _request = shapes.GetDevicesInPlacementRequest(**_params)
        response = self._boto_client.get_devices_in_placement(
            **_request.to_boto()
        )

        return shapes.GetDevicesInPlacementResponse.from_boto(response)

    def list_placements(
        self,
        _request: shapes.ListPlacementsRequest = None,
        *,
        project_name: str,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListPlacementsResponse:
        """
        Lists the placement(s) of a project.
        """
        if _request is None:
            _params = {}
            if project_name is not ShapeBase.NOT_SET:
                _params['project_name'] = project_name
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListPlacementsRequest(**_params)
        response = self._boto_client.list_placements(**_request.to_boto())

        return shapes.ListPlacementsResponse.from_boto(response)

    def list_projects(
        self,
        _request: shapes.ListProjectsRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListProjectsResponse:
        """
        Lists the AWS IoT 1-Click project(s) associated with your AWS account and
        region.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListProjectsRequest(**_params)
        response = self._boto_client.list_projects(**_request.to_boto())

        return shapes.ListProjectsResponse.from_boto(response)

    def update_placement(
        self,
        _request: shapes.UpdatePlacementRequest = None,
        *,
        placement_name: str,
        project_name: str,
        attributes: typing.Dict[str, str] = ShapeBase.NOT_SET,
    ) -> shapes.UpdatePlacementResponse:
        """
        Updates a placement with the given attributes. To clear an attribute, pass an
        empty value (i.e., "").
        """
        if _request is None:
            _params = {}
            if placement_name is not ShapeBase.NOT_SET:
                _params['placement_name'] = placement_name
            if project_name is not ShapeBase.NOT_SET:
                _params['project_name'] = project_name
            if attributes is not ShapeBase.NOT_SET:
                _params['attributes'] = attributes
            _request = shapes.UpdatePlacementRequest(**_params)
        response = self._boto_client.update_placement(**_request.to_boto())

        return shapes.UpdatePlacementResponse.from_boto(response)

    def update_project(
        self,
        _request: shapes.UpdateProjectRequest = None,
        *,
        project_name: str,
        description: str = ShapeBase.NOT_SET,
        placement_template: shapes.PlacementTemplate = ShapeBase.NOT_SET,
    ) -> shapes.UpdateProjectResponse:
        """
        Updates a project associated with your AWS account and region. With the
        exception of device template names, you can pass just the values that need to be
        updated because the update request will change only the values that are
        provided. To clear a value, pass the empty string (i.e., `""`).
        """
        if _request is None:
            _params = {}
            if project_name is not ShapeBase.NOT_SET:
                _params['project_name'] = project_name
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if placement_template is not ShapeBase.NOT_SET:
                _params['placement_template'] = placement_template
            _request = shapes.UpdateProjectRequest(**_params)
        response = self._boto_client.update_project(**_request.to_boto())

        return shapes.UpdateProjectResponse.from_boto(response)
