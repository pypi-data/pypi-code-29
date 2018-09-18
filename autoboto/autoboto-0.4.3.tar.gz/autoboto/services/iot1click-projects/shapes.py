import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


@dataclasses.dataclass
class AssociateDeviceWithPlacementRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "project_name",
                "projectName",
                TypeInfo(str),
            ),
            (
                "placement_name",
                "placementName",
                TypeInfo(str),
            ),
            (
                "device_id",
                "deviceId",
                TypeInfo(str),
            ),
            (
                "device_template_name",
                "deviceTemplateName",
                TypeInfo(str),
            ),
        ]

    # The name of the project containing the placement in which to associate the
    # device.
    project_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the placement in which to associate the device.
    placement_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the physical device to be associated with the given placement in
    # the project. Note that a mandatory 4 character prefix is required for all
    # `deviceId` values.
    device_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The device template name to associate with the device ID.
    device_template_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AssociateDeviceWithPlacementResponse(OutputShapeBase):
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
class CreatePlacementRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "placement_name",
                "placementName",
                TypeInfo(str),
            ),
            (
                "project_name",
                "projectName",
                TypeInfo(str),
            ),
            (
                "attributes",
                "attributes",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The name of the placement to be created.
    placement_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the project in which to create the placement.
    project_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Optional user-defined key/value pairs providing contextual data (such as
    # location or function) for the placement.
    attributes: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreatePlacementResponse(OutputShapeBase):
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
class CreateProjectRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "project_name",
                "projectName",
                TypeInfo(str),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
            (
                "placement_template",
                "placementTemplate",
                TypeInfo(PlacementTemplate),
            ),
        ]

    # The name of the project to create.
    project_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional description for the project.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The schema defining the placement to be created. A placement template
    # defines placement default attributes and device templates. You cannot add
    # or remove device templates after the project has been created. However, you
    # can update `callbackOverrides` for the device templates using the
    # `UpdateProject` API.
    placement_template: "PlacementTemplate" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateProjectResponse(OutputShapeBase):
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
class DeletePlacementRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "placement_name",
                "placementName",
                TypeInfo(str),
            ),
            (
                "project_name",
                "projectName",
                TypeInfo(str),
            ),
        ]

    # The name of the empty placement to delete.
    placement_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The project containing the empty placement to delete.
    project_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeletePlacementResponse(OutputShapeBase):
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
class DeleteProjectRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "project_name",
                "projectName",
                TypeInfo(str),
            ),
        ]

    # The name of the empty project to delete.
    project_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteProjectResponse(OutputShapeBase):
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
class DescribePlacementRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "placement_name",
                "placementName",
                TypeInfo(str),
            ),
            (
                "project_name",
                "projectName",
                TypeInfo(str),
            ),
        ]

    # The name of the placement within a project.
    placement_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The project containing the placement to be described.
    project_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribePlacementResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "placement",
                "placement",
                TypeInfo(PlacementDescription),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An object describing the placement.
    placement: "PlacementDescription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeProjectRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "project_name",
                "projectName",
                TypeInfo(str),
            ),
        ]

    # The name of the project to be described.
    project_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeProjectResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "project",
                "project",
                TypeInfo(ProjectDescription),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An object describing the project.
    project: "ProjectDescription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeviceTemplate(ShapeBase):
    """
    An object representing a device for a placement template (see
    PlacementTemplate).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "device_type",
                "deviceType",
                TypeInfo(str),
            ),
            (
                "callback_overrides",
                "callbackOverrides",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The device type, which currently must be `"button"`.
    device_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional Lambda function to invoke instead of the default Lambda
    # function provided by the placement template.
    callback_overrides: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DisassociateDeviceFromPlacementRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "project_name",
                "projectName",
                TypeInfo(str),
            ),
            (
                "placement_name",
                "placementName",
                TypeInfo(str),
            ),
            (
                "device_template_name",
                "deviceTemplateName",
                TypeInfo(str),
            ),
        ]

    # The name of the project that contains the placement.
    project_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the placement that the device should be removed from.
    placement_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The device ID that should be removed from the placement.
    device_template_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DisassociateDeviceFromPlacementResponse(OutputShapeBase):
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
class GetDevicesInPlacementRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "project_name",
                "projectName",
                TypeInfo(str),
            ),
            (
                "placement_name",
                "placementName",
                TypeInfo(str),
            ),
        ]

    # The name of the project containing the placement.
    project_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the placement to get the devices from.
    placement_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDevicesInPlacementResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "devices",
                "devices",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An object containing the devices (zero or more) within the placement.
    devices: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InternalFailureException(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "code",
                TypeInfo(str),
            ),
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    code: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidRequestException(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "code",
                TypeInfo(str),
            ),
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    code: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListPlacementsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "project_name",
                "projectName",
                TypeInfo(str),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
            (
                "max_results",
                "maxResults",
                TypeInfo(int),
            ),
        ]

    # The project containing the placements to be listed.
    project_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token to retrieve the next set of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to return per request. If not set, a default
    # value of 100 is used.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListPlacementsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "placements",
                "placements",
                TypeInfo(typing.List[PlacementSummary]),
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

    # An object listing the requested placements.
    placements: typing.List["PlacementSummary"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token used to retrieve the next set of results - will be effectively
    # empty if there are no further results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListProjectsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
            (
                "max_results",
                "maxResults",
                TypeInfo(int),
            ),
        ]

    # The token to retrieve the next set of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to return per request. If not set, a default
    # value of 100 is used.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListProjectsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "projects",
                "projects",
                TypeInfo(typing.List[ProjectSummary]),
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

    # An object containing the list of projects.
    projects: typing.List["ProjectSummary"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token used to retrieve the next set of results - will be effectively
    # empty if there are no further results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PlacementDescription(ShapeBase):
    """
    An object describing a project's placement.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "project_name",
                "projectName",
                TypeInfo(str),
            ),
            (
                "placement_name",
                "placementName",
                TypeInfo(str),
            ),
            (
                "attributes",
                "attributes",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "created_date",
                "createdDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "updated_date",
                "updatedDate",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The name of the project containing the placement.
    project_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the placement.
    placement_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The user-defined attributes associated with the placement.
    attributes: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date when the placement was initially created, in UNIX epoch time
    # format.
    created_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date when the placement was last updated, in UNIX epoch time format. If
    # the placement was not updated, then `createdDate` and `updatedDate` are the
    # same.
    updated_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PlacementSummary(ShapeBase):
    """
    An object providing summary information for a particular placement.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "project_name",
                "projectName",
                TypeInfo(str),
            ),
            (
                "placement_name",
                "placementName",
                TypeInfo(str),
            ),
            (
                "created_date",
                "createdDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "updated_date",
                "updatedDate",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The name of the project containing the placement.
    project_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the placement being summarized.
    placement_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date when the placement was originally created, in UNIX epoch time
    # format.
    created_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date when the placement was last updated, in UNIX epoch time format. If
    # the placement was not updated, then `createdDate` and `updatedDate` are the
    # same.
    updated_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PlacementTemplate(ShapeBase):
    """
    An object defining the template for a placement.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "default_attributes",
                "defaultAttributes",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "device_templates",
                "deviceTemplates",
                TypeInfo(typing.Dict[str, DeviceTemplate]),
            ),
        ]

    # The default attributes (key/value pairs) to be applied to all placements
    # using this template.
    default_attributes: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An object specifying the DeviceTemplate for all placements using this
    # (PlacementTemplate) template.
    device_templates: typing.Dict[str, "DeviceTemplate"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ProjectDescription(ShapeBase):
    """
    An object providing detailed information for a particular project associated
    with an AWS account and region.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "project_name",
                "projectName",
                TypeInfo(str),
            ),
            (
                "created_date",
                "createdDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "updated_date",
                "updatedDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
            (
                "placement_template",
                "placementTemplate",
                TypeInfo(PlacementTemplate),
            ),
        ]

    # The name of the project for which to obtain information from.
    project_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date when the project was originally created, in UNIX epoch time
    # format.
    created_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date when the project was last updated, in UNIX epoch time format. If
    # the project was not updated, then `createdDate` and `updatedDate` are the
    # same.
    updated_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The description of the project.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An object describing the project's placement specifications.
    placement_template: "PlacementTemplate" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ProjectSummary(ShapeBase):
    """
    An object providing summary information for a particular project for an
    associated AWS account and region.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "project_name",
                "projectName",
                TypeInfo(str),
            ),
            (
                "created_date",
                "createdDate",
                TypeInfo(datetime.datetime),
            ),
            (
                "updated_date",
                "updatedDate",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The name of the project being summarized.
    project_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date when the project was originally created, in UNIX epoch time
    # format.
    created_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date when the project was last updated, in UNIX epoch time format. If
    # the project was not updated, then `createdDate` and `updatedDate` are the
    # same.
    updated_date: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ResourceConflictException(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "code",
                TypeInfo(str),
            ),
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    code: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceNotFoundException(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "code",
                TypeInfo(str),
            ),
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    code: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TooManyRequestsException(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "code",
                TypeInfo(str),
            ),
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    code: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdatePlacementRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "placement_name",
                "placementName",
                TypeInfo(str),
            ),
            (
                "project_name",
                "projectName",
                TypeInfo(str),
            ),
            (
                "attributes",
                "attributes",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The name of the placement to update.
    placement_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the project containing the placement to be updated.
    project_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The user-defined object of attributes used to update the placement. The
    # maximum number of key/value pairs is 50.
    attributes: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdatePlacementResponse(OutputShapeBase):
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
class UpdateProjectRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "project_name",
                "projectName",
                TypeInfo(str),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
            (
                "placement_template",
                "placementTemplate",
                TypeInfo(PlacementTemplate),
            ),
        ]

    # The name of the project to be updated.
    project_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional user-defined description for the project.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An object defining the project update. Once a project has been created, you
    # cannot add device template names to the project. However, for a given
    # `placementTemplate`, you can update the associated `callbackOverrides` for
    # the device definition using this API.
    placement_template: "PlacementTemplate" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateProjectResponse(OutputShapeBase):
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
