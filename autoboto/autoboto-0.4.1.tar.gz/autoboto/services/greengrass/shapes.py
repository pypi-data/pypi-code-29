import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


@dataclasses.dataclass
class AssociateRoleToGroupRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_id",
                "GroupId",
                TypeInfo(str),
            ),
            (
                "role_arn",
                "RoleArn",
                TypeInfo(str),
            ),
        ]

    # The ID of the AWS Greengrass group.
    group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the role you wish to associate with this group.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AssociateRoleToGroupResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "associated_at",
                "AssociatedAt",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time, in milliseconds since the epoch, when the role ARN was associated
    # with the group.
    associated_at: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AssociateServiceRoleToAccountRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_arn",
                "RoleArn",
                TypeInfo(str),
            ),
        ]

    # The ARN of the service role you wish to associate with your account.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AssociateServiceRoleToAccountResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "associated_at",
                "AssociatedAt",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time when the service role was associated with the account.
    associated_at: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BadRequestException(ShapeBase):
    """
    General error information.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "error_details",
                "ErrorDetails",
                TypeInfo(typing.List[ErrorDetail]),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    # Details about the error.
    error_details: typing.List["ErrorDetail"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A message containing information about the error.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ConnectivityInfo(ShapeBase):
    """
    Information about a Greengrass core's connectivity.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "host_address",
                "HostAddress",
                TypeInfo(str),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "metadata",
                "Metadata",
                TypeInfo(str),
            ),
            (
                "port_number",
                "PortNumber",
                TypeInfo(int),
            ),
        ]

    # The endpoint for the Greengrass core. Can be an IP address or DNS.
    host_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the connectivity information.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Metadata for this endpoint.
    metadata: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The port of the Greengrass core. Usually 8883.
    port_number: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Core(ShapeBase):
    """
    Information about a core.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_arn",
                "CertificateArn",
                TypeInfo(str),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "sync_shadow",
                "SyncShadow",
                TypeInfo(bool),
            ),
            (
                "thing_arn",
                "ThingArn",
                TypeInfo(str),
            ),
        ]

    # The ARN of the certificate associated with the core.
    certificate_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the core.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If true, the core's local shadow is automatically synced with the cloud.
    sync_shadow: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the thing which is the core.
    thing_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CoreDefinitionVersion(ShapeBase):
    """
    Information about a core definition version.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cores",
                "Cores",
                TypeInfo(typing.List[Core]),
            ),
        ]

    # A list of cores in the core definition version.
    cores: typing.List["Core"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateCoreDefinitionRequest(ShapeBase):
    """
    Information needed to create a core definition.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "amzn_client_token",
                "AmznClientToken",
                TypeInfo(str),
            ),
            (
                "initial_version",
                "InitialVersion",
                TypeInfo(CoreDefinitionVersion),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # A client token used to correlate requests and responses.
    amzn_client_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the initial version of the core definition.
    initial_version: "CoreDefinitionVersion" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the core definition.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateCoreDefinitionResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "creation_timestamp",
                "CreationTimestamp",
                TypeInfo(str),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "last_updated_timestamp",
                "LastUpdatedTimestamp",
                TypeInfo(str),
            ),
            (
                "latest_version",
                "LatestVersion",
                TypeInfo(str),
            ),
            (
                "latest_version_arn",
                "LatestVersionArn",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the definition.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time, in milliseconds since the epoch, when the definition was created.
    creation_timestamp: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the definition.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time, in milliseconds since the epoch, when the definition was last
    # updated.
    last_updated_timestamp: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The latest version of the definition.
    latest_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the latest version of the definition.
    latest_version_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the definition.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateCoreDefinitionVersionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "core_definition_id",
                "CoreDefinitionId",
                TypeInfo(str),
            ),
            (
                "amzn_client_token",
                "AmznClientToken",
                TypeInfo(str),
            ),
            (
                "cores",
                "Cores",
                TypeInfo(typing.List[Core]),
            ),
        ]

    # The ID of the core definition.
    core_definition_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A client token used to correlate requests and responses.
    amzn_client_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of cores in the core definition version.
    cores: typing.List["Core"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateCoreDefinitionVersionResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "creation_timestamp",
                "CreationTimestamp",
                TypeInfo(str),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "version",
                "Version",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the version.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time, in milliseconds since the epoch, when the version was created.
    creation_timestamp: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the version.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique ID of the version.
    version: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateDeploymentRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_id",
                "GroupId",
                TypeInfo(str),
            ),
            (
                "amzn_client_token",
                "AmznClientToken",
                TypeInfo(str),
            ),
            (
                "deployment_id",
                "DeploymentId",
                TypeInfo(str),
            ),
            (
                "deployment_type",
                "DeploymentType",
                TypeInfo(typing.Union[str, DeploymentType]),
            ),
            (
                "group_version_id",
                "GroupVersionId",
                TypeInfo(str),
            ),
        ]

    # The ID of the AWS Greengrass group.
    group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A client token used to correlate requests and responses.
    amzn_client_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the deployment if you wish to redeploy a previous deployment.
    deployment_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of deployment. When used in ''CreateDeployment'', only
    # ''NewDeployment'' and ''Redeployment'' are valid.
    deployment_type: typing.Union[str, "DeploymentType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the group version to be deployed.
    group_version_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateDeploymentResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "deployment_arn",
                "DeploymentArn",
                TypeInfo(str),
            ),
            (
                "deployment_id",
                "DeploymentId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the deployment.
    deployment_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the deployment.
    deployment_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateDeviceDefinitionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "amzn_client_token",
                "AmznClientToken",
                TypeInfo(str),
            ),
            (
                "initial_version",
                "InitialVersion",
                TypeInfo(DeviceDefinitionVersion),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # A client token used to correlate requests and responses.
    amzn_client_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the initial version of the device definition.
    initial_version: "DeviceDefinitionVersion" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the device definition.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateDeviceDefinitionResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "creation_timestamp",
                "CreationTimestamp",
                TypeInfo(str),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "last_updated_timestamp",
                "LastUpdatedTimestamp",
                TypeInfo(str),
            ),
            (
                "latest_version",
                "LatestVersion",
                TypeInfo(str),
            ),
            (
                "latest_version_arn",
                "LatestVersionArn",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the definition.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time, in milliseconds since the epoch, when the definition was created.
    creation_timestamp: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the definition.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time, in milliseconds since the epoch, when the definition was last
    # updated.
    last_updated_timestamp: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The latest version of the definition.
    latest_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the latest version of the definition.
    latest_version_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the definition.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateDeviceDefinitionVersionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "device_definition_id",
                "DeviceDefinitionId",
                TypeInfo(str),
            ),
            (
                "amzn_client_token",
                "AmznClientToken",
                TypeInfo(str),
            ),
            (
                "devices",
                "Devices",
                TypeInfo(typing.List[Device]),
            ),
        ]

    # The ID of the device definition.
    device_definition_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A client token used to correlate requests and responses.
    amzn_client_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of devices in the definition version.
    devices: typing.List["Device"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateDeviceDefinitionVersionResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "creation_timestamp",
                "CreationTimestamp",
                TypeInfo(str),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "version",
                "Version",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the version.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time, in milliseconds since the epoch, when the version was created.
    creation_timestamp: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the version.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique ID of the version.
    version: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateFunctionDefinitionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "amzn_client_token",
                "AmznClientToken",
                TypeInfo(str),
            ),
            (
                "initial_version",
                "InitialVersion",
                TypeInfo(FunctionDefinitionVersion),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # A client token used to correlate requests and responses.
    amzn_client_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the initial version of the function definition.
    initial_version: "FunctionDefinitionVersion" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the function definition.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateFunctionDefinitionResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "creation_timestamp",
                "CreationTimestamp",
                TypeInfo(str),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "last_updated_timestamp",
                "LastUpdatedTimestamp",
                TypeInfo(str),
            ),
            (
                "latest_version",
                "LatestVersion",
                TypeInfo(str),
            ),
            (
                "latest_version_arn",
                "LatestVersionArn",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the definition.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time, in milliseconds since the epoch, when the definition was created.
    creation_timestamp: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the definition.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time, in milliseconds since the epoch, when the definition was last
    # updated.
    last_updated_timestamp: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The latest version of the definition.
    latest_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the latest version of the definition.
    latest_version_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the definition.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateFunctionDefinitionVersionRequest(ShapeBase):
    """
    Information needed to create a function definition version.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "function_definition_id",
                "FunctionDefinitionId",
                TypeInfo(str),
            ),
            (
                "amzn_client_token",
                "AmznClientToken",
                TypeInfo(str),
            ),
            (
                "functions",
                "Functions",
                TypeInfo(typing.List[Function]),
            ),
        ]

    # The ID of the Lambda function definition.
    function_definition_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A client token used to correlate requests and responses.
    amzn_client_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of Lambda functions in this function definition version.
    functions: typing.List["Function"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateFunctionDefinitionVersionResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "creation_timestamp",
                "CreationTimestamp",
                TypeInfo(str),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "version",
                "Version",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the version.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time, in milliseconds since the epoch, when the version was created.
    creation_timestamp: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the version.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique ID of the version.
    version: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateGroupCertificateAuthorityRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_id",
                "GroupId",
                TypeInfo(str),
            ),
            (
                "amzn_client_token",
                "AmznClientToken",
                TypeInfo(str),
            ),
        ]

    # The ID of the AWS Greengrass group.
    group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A client token used to correlate requests and responses.
    amzn_client_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateGroupCertificateAuthorityResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "group_certificate_authority_arn",
                "GroupCertificateAuthorityArn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the group certificate authority.
    group_certificate_authority_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateGroupRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "amzn_client_token",
                "AmznClientToken",
                TypeInfo(str),
            ),
            (
                "initial_version",
                "InitialVersion",
                TypeInfo(GroupVersion),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # A client token used to correlate requests and responses.
    amzn_client_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the initial version of the group.
    initial_version: "GroupVersion" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the group.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateGroupResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "creation_timestamp",
                "CreationTimestamp",
                TypeInfo(str),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "last_updated_timestamp",
                "LastUpdatedTimestamp",
                TypeInfo(str),
            ),
            (
                "latest_version",
                "LatestVersion",
                TypeInfo(str),
            ),
            (
                "latest_version_arn",
                "LatestVersionArn",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the definition.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time, in milliseconds since the epoch, when the definition was created.
    creation_timestamp: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the definition.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time, in milliseconds since the epoch, when the definition was last
    # updated.
    last_updated_timestamp: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The latest version of the definition.
    latest_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the latest version of the definition.
    latest_version_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the definition.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateGroupVersionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_id",
                "GroupId",
                TypeInfo(str),
            ),
            (
                "amzn_client_token",
                "AmznClientToken",
                TypeInfo(str),
            ),
            (
                "core_definition_version_arn",
                "CoreDefinitionVersionArn",
                TypeInfo(str),
            ),
            (
                "device_definition_version_arn",
                "DeviceDefinitionVersionArn",
                TypeInfo(str),
            ),
            (
                "function_definition_version_arn",
                "FunctionDefinitionVersionArn",
                TypeInfo(str),
            ),
            (
                "logger_definition_version_arn",
                "LoggerDefinitionVersionArn",
                TypeInfo(str),
            ),
            (
                "resource_definition_version_arn",
                "ResourceDefinitionVersionArn",
                TypeInfo(str),
            ),
            (
                "subscription_definition_version_arn",
                "SubscriptionDefinitionVersionArn",
                TypeInfo(str),
            ),
        ]

    # The ID of the AWS Greengrass group.
    group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A client token used to correlate requests and responses.
    amzn_client_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the core definition version for this group.
    core_definition_version_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the device definition version for this group.
    device_definition_version_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the function definition version for this group.
    function_definition_version_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the logger definition version for this group.
    logger_definition_version_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The resource definition version ARN for this group.
    resource_definition_version_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the subscription definition version for this group.
    subscription_definition_version_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateGroupVersionResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "creation_timestamp",
                "CreationTimestamp",
                TypeInfo(str),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "version",
                "Version",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the version.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time, in milliseconds since the epoch, when the version was created.
    creation_timestamp: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the version.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique ID of the version.
    version: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateLoggerDefinitionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "amzn_client_token",
                "AmznClientToken",
                TypeInfo(str),
            ),
            (
                "initial_version",
                "InitialVersion",
                TypeInfo(LoggerDefinitionVersion),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # A client token used to correlate requests and responses.
    amzn_client_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the initial version of the logger definition.
    initial_version: "LoggerDefinitionVersion" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the logger definition.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateLoggerDefinitionResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "creation_timestamp",
                "CreationTimestamp",
                TypeInfo(str),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "last_updated_timestamp",
                "LastUpdatedTimestamp",
                TypeInfo(str),
            ),
            (
                "latest_version",
                "LatestVersion",
                TypeInfo(str),
            ),
            (
                "latest_version_arn",
                "LatestVersionArn",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the definition.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time, in milliseconds since the epoch, when the definition was created.
    creation_timestamp: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the definition.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time, in milliseconds since the epoch, when the definition was last
    # updated.
    last_updated_timestamp: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The latest version of the definition.
    latest_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the latest version of the definition.
    latest_version_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the definition.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateLoggerDefinitionVersionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "logger_definition_id",
                "LoggerDefinitionId",
                TypeInfo(str),
            ),
            (
                "amzn_client_token",
                "AmznClientToken",
                TypeInfo(str),
            ),
            (
                "loggers",
                "Loggers",
                TypeInfo(typing.List[Logger]),
            ),
        ]

    # The ID of the logger definition.
    logger_definition_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A client token used to correlate requests and responses.
    amzn_client_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of loggers.
    loggers: typing.List["Logger"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateLoggerDefinitionVersionResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "creation_timestamp",
                "CreationTimestamp",
                TypeInfo(str),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "version",
                "Version",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the version.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time, in milliseconds since the epoch, when the version was created.
    creation_timestamp: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the version.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique ID of the version.
    version: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateResourceDefinitionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "amzn_client_token",
                "AmznClientToken",
                TypeInfo(str),
            ),
            (
                "initial_version",
                "InitialVersion",
                TypeInfo(ResourceDefinitionVersion),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # A client token used to correlate requests and responses.
    amzn_client_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the initial version of the resource definition.
    initial_version: "ResourceDefinitionVersion" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the resource definition.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateResourceDefinitionResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "creation_timestamp",
                "CreationTimestamp",
                TypeInfo(str),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "last_updated_timestamp",
                "LastUpdatedTimestamp",
                TypeInfo(str),
            ),
            (
                "latest_version",
                "LatestVersion",
                TypeInfo(str),
            ),
            (
                "latest_version_arn",
                "LatestVersionArn",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the definition.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time, in milliseconds since the epoch, when the definition was created.
    creation_timestamp: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the definition.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time, in milliseconds since the epoch, when the definition was last
    # updated.
    last_updated_timestamp: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The latest version of the definition.
    latest_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the latest version of the definition.
    latest_version_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the definition.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateResourceDefinitionVersionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_definition_id",
                "ResourceDefinitionId",
                TypeInfo(str),
            ),
            (
                "amzn_client_token",
                "AmznClientToken",
                TypeInfo(str),
            ),
            (
                "resources",
                "Resources",
                TypeInfo(typing.List[Resource]),
            ),
        ]

    # The ID of the resource definition.
    resource_definition_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A client token used to correlate requests and responses.
    amzn_client_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of resources.
    resources: typing.List["Resource"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateResourceDefinitionVersionResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "creation_timestamp",
                "CreationTimestamp",
                TypeInfo(str),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "version",
                "Version",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the version.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time, in milliseconds since the epoch, when the version was created.
    creation_timestamp: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the version.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique ID of the version.
    version: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateSoftwareUpdateJobRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "amzn_client_token",
                "AmznClientToken",
                TypeInfo(str),
            ),
            (
                "s3_url_signer_role",
                "S3UrlSignerRole",
                TypeInfo(str),
            ),
            (
                "software_to_update",
                "SoftwareToUpdate",
                TypeInfo(typing.Union[str, SoftwareToUpdate]),
            ),
            (
                "update_agent_log_level",
                "UpdateAgentLogLevel",
                TypeInfo(typing.Union[str, UpdateAgentLogLevel]),
            ),
            (
                "update_targets",
                "UpdateTargets",
                TypeInfo(typing.List[str]),
            ),
            (
                "update_targets_architecture",
                "UpdateTargetsArchitecture",
                TypeInfo(typing.Union[str, UpdateTargetsArchitecture]),
            ),
            (
                "update_targets_operating_system",
                "UpdateTargetsOperatingSystem",
                TypeInfo(typing.Union[str, UpdateTargetsOperatingSystem]),
            ),
        ]

    # A client token used to correlate requests and responses.
    amzn_client_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The IAM Role that Greengrass will use to create pre-signed URLs pointing
    # towards the update artifact.
    s3_url_signer_role: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The piece of software on the Greengrass core that will be updated.
    software_to_update: typing.Union[str, "SoftwareToUpdate"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )

    # The minimum level of log statements that should be logged by the OTA Agent
    # during an update.
    update_agent_log_level: typing.Union[str, "UpdateAgentLogLevel"
                                        ] = dataclasses.field(
                                            default=ShapeBase.NOT_SET,
                                        )

    # The ARNs of the targets (IoT things or IoT thing groups) that this update
    # will be applied to.
    update_targets: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The architecture of the cores which are the targets of an update.
    update_targets_architecture: typing.Union[str, "UpdateTargetsArchitecture"
                                             ] = dataclasses.field(
                                                 default=ShapeBase.NOT_SET,
                                             )

    # The operating system of the cores which are the targets of an update.
    update_targets_operating_system: typing.Union[
        str, "UpdateTargetsOperatingSystem"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )


@dataclasses.dataclass
class CreateSoftwareUpdateJobResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "iot_job_arn",
                "IotJobArn",
                TypeInfo(str),
            ),
            (
                "iot_job_id",
                "IotJobId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The IoT Job ARN corresponding to this update.
    iot_job_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The IoT Job Id corresponding to this update.
    iot_job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateSubscriptionDefinitionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "amzn_client_token",
                "AmznClientToken",
                TypeInfo(str),
            ),
            (
                "initial_version",
                "InitialVersion",
                TypeInfo(SubscriptionDefinitionVersion),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # A client token used to correlate requests and responses.
    amzn_client_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the initial version of the subscription definition.
    initial_version: "SubscriptionDefinitionVersion" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the subscription definition.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateSubscriptionDefinitionResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "creation_timestamp",
                "CreationTimestamp",
                TypeInfo(str),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "last_updated_timestamp",
                "LastUpdatedTimestamp",
                TypeInfo(str),
            ),
            (
                "latest_version",
                "LatestVersion",
                TypeInfo(str),
            ),
            (
                "latest_version_arn",
                "LatestVersionArn",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the definition.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time, in milliseconds since the epoch, when the definition was created.
    creation_timestamp: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the definition.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time, in milliseconds since the epoch, when the definition was last
    # updated.
    last_updated_timestamp: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The latest version of the definition.
    latest_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the latest version of the definition.
    latest_version_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the definition.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateSubscriptionDefinitionVersionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subscription_definition_id",
                "SubscriptionDefinitionId",
                TypeInfo(str),
            ),
            (
                "amzn_client_token",
                "AmznClientToken",
                TypeInfo(str),
            ),
            (
                "subscriptions",
                "Subscriptions",
                TypeInfo(typing.List[Subscription]),
            ),
        ]

    # The ID of the subscription definition.
    subscription_definition_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A client token used to correlate requests and responses.
    amzn_client_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of subscriptions.
    subscriptions: typing.List["Subscription"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateSubscriptionDefinitionVersionResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "creation_timestamp",
                "CreationTimestamp",
                TypeInfo(str),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "version",
                "Version",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the version.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time, in milliseconds since the epoch, when the version was created.
    creation_timestamp: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the version.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique ID of the version.
    version: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DefinitionInformation(ShapeBase):
    """
    Information about a definition.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "creation_timestamp",
                "CreationTimestamp",
                TypeInfo(str),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "last_updated_timestamp",
                "LastUpdatedTimestamp",
                TypeInfo(str),
            ),
            (
                "latest_version",
                "LatestVersion",
                TypeInfo(str),
            ),
            (
                "latest_version_arn",
                "LatestVersionArn",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The ARN of the definition.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time, in milliseconds since the epoch, when the definition was created.
    creation_timestamp: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the definition.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time, in milliseconds since the epoch, when the definition was last
    # updated.
    last_updated_timestamp: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The latest version of the definition.
    latest_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the latest version of the definition.
    latest_version_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the definition.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteCoreDefinitionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "core_definition_id",
                "CoreDefinitionId",
                TypeInfo(str),
            ),
        ]

    # The ID of the core definition.
    core_definition_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteCoreDefinitionResponse(OutputShapeBase):
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
class DeleteDeviceDefinitionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "device_definition_id",
                "DeviceDefinitionId",
                TypeInfo(str),
            ),
        ]

    # The ID of the device definition.
    device_definition_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteDeviceDefinitionResponse(OutputShapeBase):
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
class DeleteFunctionDefinitionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "function_definition_id",
                "FunctionDefinitionId",
                TypeInfo(str),
            ),
        ]

    # The ID of the Lambda function definition.
    function_definition_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteFunctionDefinitionResponse(OutputShapeBase):
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
class DeleteGroupRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_id",
                "GroupId",
                TypeInfo(str),
            ),
        ]

    # The ID of the AWS Greengrass group.
    group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteGroupResponse(OutputShapeBase):
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
class DeleteLoggerDefinitionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "logger_definition_id",
                "LoggerDefinitionId",
                TypeInfo(str),
            ),
        ]

    # The ID of the logger definition.
    logger_definition_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteLoggerDefinitionResponse(OutputShapeBase):
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
class DeleteResourceDefinitionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_definition_id",
                "ResourceDefinitionId",
                TypeInfo(str),
            ),
        ]

    # The ID of the resource definition.
    resource_definition_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteResourceDefinitionResponse(OutputShapeBase):
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
class DeleteSubscriptionDefinitionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subscription_definition_id",
                "SubscriptionDefinitionId",
                TypeInfo(str),
            ),
        ]

    # The ID of the subscription definition.
    subscription_definition_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteSubscriptionDefinitionResponse(OutputShapeBase):
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
class Deployment(ShapeBase):
    """
    Information about a deployment.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "created_at",
                "CreatedAt",
                TypeInfo(str),
            ),
            (
                "deployment_arn",
                "DeploymentArn",
                TypeInfo(str),
            ),
            (
                "deployment_id",
                "DeploymentId",
                TypeInfo(str),
            ),
            (
                "deployment_type",
                "DeploymentType",
                TypeInfo(typing.Union[str, DeploymentType]),
            ),
            (
                "group_arn",
                "GroupArn",
                TypeInfo(str),
            ),
        ]

    # The time, in milliseconds since the epoch, when the deployment was created.
    created_at: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the deployment.
    deployment_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the deployment.
    deployment_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of the deployment.
    deployment_type: typing.Union[str, "DeploymentType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the group for this deployment.
    group_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class DeploymentType(str):
    NewDeployment = "NewDeployment"
    Redeployment = "Redeployment"
    ResetDeployment = "ResetDeployment"
    ForceResetDeployment = "ForceResetDeployment"


@dataclasses.dataclass
class Device(ShapeBase):
    """
    Information about a device.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_arn",
                "CertificateArn",
                TypeInfo(str),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "sync_shadow",
                "SyncShadow",
                TypeInfo(bool),
            ),
            (
                "thing_arn",
                "ThingArn",
                TypeInfo(str),
            ),
        ]

    # The ARN of the certificate associated with the device.
    certificate_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the device.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If true, the device's local shadow will be automatically synced with the
    # cloud.
    sync_shadow: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The thing ARN of the device.
    thing_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeviceDefinitionVersion(ShapeBase):
    """
    Information about a device definition version.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "devices",
                "Devices",
                TypeInfo(typing.List[Device]),
            ),
        ]

    # A list of devices in the definition version.
    devices: typing.List["Device"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DisassociateRoleFromGroupRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_id",
                "GroupId",
                TypeInfo(str),
            ),
        ]

    # The ID of the AWS Greengrass group.
    group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DisassociateRoleFromGroupResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "disassociated_at",
                "DisassociatedAt",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time, in milliseconds since the epoch, when the role was disassociated
    # from the group.
    disassociated_at: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DisassociateServiceRoleFromAccountRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DisassociateServiceRoleFromAccountResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "disassociated_at",
                "DisassociatedAt",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time when the service role was disassociated from the account.
    disassociated_at: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Empty(ShapeBase):
    """
    Empty
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class EncodingType(str):
    binary = "binary"
    json = "json"


@dataclasses.dataclass
class ErrorDetail(ShapeBase):
    """
    Details about the error.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detailed_error_code",
                "DetailedErrorCode",
                TypeInfo(str),
            ),
            (
                "detailed_error_message",
                "DetailedErrorMessage",
                TypeInfo(str),
            ),
        ]

    # A detailed error code.
    detailed_error_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A detailed error message.
    detailed_error_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Function(ShapeBase):
    """
    Information about a Lambda function.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "function_arn",
                "FunctionArn",
                TypeInfo(str),
            ),
            (
                "function_configuration",
                "FunctionConfiguration",
                TypeInfo(FunctionConfiguration),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
        ]

    # The ARN of the Lambda function.
    function_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The configuration of the Lambda function.
    function_configuration: "FunctionConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the Lambda function.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class FunctionConfiguration(ShapeBase):
    """
    The configuration of the Lambda function.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "encoding_type",
                "EncodingType",
                TypeInfo(typing.Union[str, EncodingType]),
            ),
            (
                "environment",
                "Environment",
                TypeInfo(FunctionConfigurationEnvironment),
            ),
            (
                "exec_args",
                "ExecArgs",
                TypeInfo(str),
            ),
            (
                "executable",
                "Executable",
                TypeInfo(str),
            ),
            (
                "memory_size",
                "MemorySize",
                TypeInfo(int),
            ),
            (
                "pinned",
                "Pinned",
                TypeInfo(bool),
            ),
            (
                "timeout",
                "Timeout",
                TypeInfo(int),
            ),
        ]

    # The expected encoding type of the input payload for the function. The
    # default is ''json''.
    encoding_type: typing.Union[str, "EncodingType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The environment configuration of the function.
    environment: "FunctionConfigurationEnvironment" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The execution arguments.
    exec_args: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the function executable.
    executable: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The memory size, in KB, which the function requires.
    memory_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # True if the function is pinned. Pinned means the function is long-lived and
    # starts when the core starts.
    pinned: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The allowed function execution time, after which Lambda should terminate
    # the function. This timeout still applies to pinned lambdas for each
    # request.
    timeout: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class FunctionConfigurationEnvironment(ShapeBase):
    """
    The environment configuration of the function.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "access_sysfs",
                "AccessSysfs",
                TypeInfo(bool),
            ),
            (
                "resource_access_policies",
                "ResourceAccessPolicies",
                TypeInfo(typing.List[ResourceAccessPolicy]),
            ),
            (
                "variables",
                "Variables",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # If true, the Lambda function is allowed to access the host's /sys folder.
    # Use this when the Lambda function needs to read device information from
    # /sys.
    access_sysfs: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of the resources, with their permissions, to which the Lambda
    # function will be granted access. A Lambda function can have at most 10
    # resources.
    resource_access_policies: typing.List["ResourceAccessPolicy"
                                         ] = dataclasses.field(
                                             default=ShapeBase.NOT_SET,
                                         )

    # Environment variables for the Lambda function's configuration.
    variables: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class FunctionDefinitionVersion(ShapeBase):
    """
    Information about a function definition version.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "functions",
                "Functions",
                TypeInfo(typing.List[Function]),
            ),
        ]

    # A list of Lambda functions in this function definition version.
    functions: typing.List["Function"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GeneralError(ShapeBase):
    """
    General error information.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "error_details",
                "ErrorDetails",
                TypeInfo(typing.List[ErrorDetail]),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    # Details about the error.
    error_details: typing.List["ErrorDetail"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A message containing information about the error.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetAssociatedRoleRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_id",
                "GroupId",
                TypeInfo(str),
            ),
        ]

    # The ID of the AWS Greengrass group.
    group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetAssociatedRoleResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "associated_at",
                "AssociatedAt",
                TypeInfo(str),
            ),
            (
                "role_arn",
                "RoleArn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time when the role was associated with the group.
    associated_at: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the role that is associated with the group.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetConnectivityInfoRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "thing_name",
                "ThingName",
                TypeInfo(str),
            ),
        ]

    # The thing name.
    thing_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetConnectivityInfoResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "connectivity_info",
                "ConnectivityInfo",
                TypeInfo(typing.List[ConnectivityInfo]),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Connectivity info list.
    connectivity_info: typing.List["ConnectivityInfo"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A message about the connectivity info request.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetCoreDefinitionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "core_definition_id",
                "CoreDefinitionId",
                TypeInfo(str),
            ),
        ]

    # The ID of the core definition.
    core_definition_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetCoreDefinitionResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "creation_timestamp",
                "CreationTimestamp",
                TypeInfo(str),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "last_updated_timestamp",
                "LastUpdatedTimestamp",
                TypeInfo(str),
            ),
            (
                "latest_version",
                "LatestVersion",
                TypeInfo(str),
            ),
            (
                "latest_version_arn",
                "LatestVersionArn",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the definition.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time, in milliseconds since the epoch, when the definition was created.
    creation_timestamp: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the definition.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time, in milliseconds since the epoch, when the definition was last
    # updated.
    last_updated_timestamp: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The latest version of the definition.
    latest_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the latest version of the definition.
    latest_version_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the definition.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetCoreDefinitionVersionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "core_definition_id",
                "CoreDefinitionId",
                TypeInfo(str),
            ),
            (
                "core_definition_version_id",
                "CoreDefinitionVersionId",
                TypeInfo(str),
            ),
        ]

    # The ID of the core definition.
    core_definition_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the core definition version.
    core_definition_version_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetCoreDefinitionVersionResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "creation_timestamp",
                "CreationTimestamp",
                TypeInfo(str),
            ),
            (
                "definition",
                "Definition",
                TypeInfo(CoreDefinitionVersion),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "version",
                "Version",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the core definition version.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time, in milliseconds since the epoch, when the core definition version
    # was created.
    creation_timestamp: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the core definition version.
    definition: "CoreDefinitionVersion" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the core definition version.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version of the core definition version.
    version: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDeploymentStatusRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "deployment_id",
                "DeploymentId",
                TypeInfo(str),
            ),
            (
                "group_id",
                "GroupId",
                TypeInfo(str),
            ),
        ]

    # The ID of the deployment.
    deployment_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the AWS Greengrass group.
    group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDeploymentStatusResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "deployment_status",
                "DeploymentStatus",
                TypeInfo(str),
            ),
            (
                "deployment_type",
                "DeploymentType",
                TypeInfo(typing.Union[str, DeploymentType]),
            ),
            (
                "error_details",
                "ErrorDetails",
                TypeInfo(typing.List[ErrorDetail]),
            ),
            (
                "error_message",
                "ErrorMessage",
                TypeInfo(str),
            ),
            (
                "updated_at",
                "UpdatedAt",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of the deployment.
    deployment_status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of the deployment.
    deployment_type: typing.Union[str, "DeploymentType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Error details
    error_details: typing.List["ErrorDetail"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Error message
    error_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time, in milliseconds since the epoch, when the deployment status was
    # updated.
    updated_at: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDeviceDefinitionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "device_definition_id",
                "DeviceDefinitionId",
                TypeInfo(str),
            ),
        ]

    # The ID of the device definition.
    device_definition_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDeviceDefinitionResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "creation_timestamp",
                "CreationTimestamp",
                TypeInfo(str),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "last_updated_timestamp",
                "LastUpdatedTimestamp",
                TypeInfo(str),
            ),
            (
                "latest_version",
                "LatestVersion",
                TypeInfo(str),
            ),
            (
                "latest_version_arn",
                "LatestVersionArn",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the definition.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time, in milliseconds since the epoch, when the definition was created.
    creation_timestamp: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the definition.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time, in milliseconds since the epoch, when the definition was last
    # updated.
    last_updated_timestamp: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The latest version of the definition.
    latest_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the latest version of the definition.
    latest_version_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the definition.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDeviceDefinitionVersionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "device_definition_id",
                "DeviceDefinitionId",
                TypeInfo(str),
            ),
            (
                "device_definition_version_id",
                "DeviceDefinitionVersionId",
                TypeInfo(str),
            ),
        ]

    # The ID of the device definition.
    device_definition_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the device definition version.
    device_definition_version_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetDeviceDefinitionVersionResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "creation_timestamp",
                "CreationTimestamp",
                TypeInfo(str),
            ),
            (
                "definition",
                "Definition",
                TypeInfo(DeviceDefinitionVersion),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "version",
                "Version",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the device definition version.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time, in milliseconds since the epoch, when the device definition
    # version was created.
    creation_timestamp: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the device definition version.
    definition: "DeviceDefinitionVersion" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the device definition version.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version of the device definition version.
    version: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetFunctionDefinitionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "function_definition_id",
                "FunctionDefinitionId",
                TypeInfo(str),
            ),
        ]

    # The ID of the Lambda function definition.
    function_definition_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetFunctionDefinitionResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "creation_timestamp",
                "CreationTimestamp",
                TypeInfo(str),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "last_updated_timestamp",
                "LastUpdatedTimestamp",
                TypeInfo(str),
            ),
            (
                "latest_version",
                "LatestVersion",
                TypeInfo(str),
            ),
            (
                "latest_version_arn",
                "LatestVersionArn",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the definition.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time, in milliseconds since the epoch, when the definition was created.
    creation_timestamp: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the definition.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time, in milliseconds since the epoch, when the definition was last
    # updated.
    last_updated_timestamp: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The latest version of the definition.
    latest_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the latest version of the definition.
    latest_version_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the definition.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetFunctionDefinitionVersionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "function_definition_id",
                "FunctionDefinitionId",
                TypeInfo(str),
            ),
            (
                "function_definition_version_id",
                "FunctionDefinitionVersionId",
                TypeInfo(str),
            ),
        ]

    # The ID of the Lambda function definition.
    function_definition_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the function definition version.
    function_definition_version_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetFunctionDefinitionVersionResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "creation_timestamp",
                "CreationTimestamp",
                TypeInfo(str),
            ),
            (
                "definition",
                "Definition",
                TypeInfo(FunctionDefinitionVersion),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "version",
                "Version",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the function definition version.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time, in milliseconds since the epoch, when the function definition
    # version was created.
    creation_timestamp: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information on the definition.
    definition: "FunctionDefinitionVersion" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the function definition version.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version of the function definition version.
    version: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetGroupCertificateAuthorityRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_authority_id",
                "CertificateAuthorityId",
                TypeInfo(str),
            ),
            (
                "group_id",
                "GroupId",
                TypeInfo(str),
            ),
        ]

    # The ID of the certificate authority.
    certificate_authority_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the AWS Greengrass group.
    group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetGroupCertificateAuthorityResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "group_certificate_authority_arn",
                "GroupCertificateAuthorityArn",
                TypeInfo(str),
            ),
            (
                "group_certificate_authority_id",
                "GroupCertificateAuthorityId",
                TypeInfo(str),
            ),
            (
                "pem_encoded_certificate",
                "PemEncodedCertificate",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the certificate authority for the group.
    group_certificate_authority_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the certificate authority for the group.
    group_certificate_authority_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The PEM encoded certificate for the group.
    pem_encoded_certificate: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetGroupCertificateConfigurationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_id",
                "GroupId",
                TypeInfo(str),
            ),
        ]

    # The ID of the AWS Greengrass group.
    group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetGroupCertificateConfigurationResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "certificate_authority_expiry_in_milliseconds",
                "CertificateAuthorityExpiryInMilliseconds",
                TypeInfo(str),
            ),
            (
                "certificate_expiry_in_milliseconds",
                "CertificateExpiryInMilliseconds",
                TypeInfo(str),
            ),
            (
                "group_id",
                "GroupId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The amount of time remaining before the certificate authority expires, in
    # milliseconds.
    certificate_authority_expiry_in_milliseconds: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The amount of time remaining before the certificate expires, in
    # milliseconds.
    certificate_expiry_in_milliseconds: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the group certificate configuration.
    group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetGroupRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_id",
                "GroupId",
                TypeInfo(str),
            ),
        ]

    # The ID of the AWS Greengrass group.
    group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetGroupResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "creation_timestamp",
                "CreationTimestamp",
                TypeInfo(str),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "last_updated_timestamp",
                "LastUpdatedTimestamp",
                TypeInfo(str),
            ),
            (
                "latest_version",
                "LatestVersion",
                TypeInfo(str),
            ),
            (
                "latest_version_arn",
                "LatestVersionArn",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the definition.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time, in milliseconds since the epoch, when the definition was created.
    creation_timestamp: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the definition.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time, in milliseconds since the epoch, when the definition was last
    # updated.
    last_updated_timestamp: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The latest version of the definition.
    latest_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the latest version of the definition.
    latest_version_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the definition.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetGroupVersionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_id",
                "GroupId",
                TypeInfo(str),
            ),
            (
                "group_version_id",
                "GroupVersionId",
                TypeInfo(str),
            ),
        ]

    # The ID of the AWS Greengrass group.
    group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the group version.
    group_version_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetGroupVersionResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "creation_timestamp",
                "CreationTimestamp",
                TypeInfo(str),
            ),
            (
                "definition",
                "Definition",
                TypeInfo(GroupVersion),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "version",
                "Version",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the group version.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time, in milliseconds since the epoch, when the group version was
    # created.
    creation_timestamp: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the group version definition.
    definition: "GroupVersion" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the group version.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique ID for the version of the group.
    version: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetLoggerDefinitionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "logger_definition_id",
                "LoggerDefinitionId",
                TypeInfo(str),
            ),
        ]

    # The ID of the logger definition.
    logger_definition_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetLoggerDefinitionResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "creation_timestamp",
                "CreationTimestamp",
                TypeInfo(str),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "last_updated_timestamp",
                "LastUpdatedTimestamp",
                TypeInfo(str),
            ),
            (
                "latest_version",
                "LatestVersion",
                TypeInfo(str),
            ),
            (
                "latest_version_arn",
                "LatestVersionArn",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the definition.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time, in milliseconds since the epoch, when the definition was created.
    creation_timestamp: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the definition.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time, in milliseconds since the epoch, when the definition was last
    # updated.
    last_updated_timestamp: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The latest version of the definition.
    latest_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the latest version of the definition.
    latest_version_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the definition.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetLoggerDefinitionVersionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "logger_definition_id",
                "LoggerDefinitionId",
                TypeInfo(str),
            ),
            (
                "logger_definition_version_id",
                "LoggerDefinitionVersionId",
                TypeInfo(str),
            ),
        ]

    # The ID of the logger definition.
    logger_definition_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the logger definition version.
    logger_definition_version_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetLoggerDefinitionVersionResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "creation_timestamp",
                "CreationTimestamp",
                TypeInfo(str),
            ),
            (
                "definition",
                "Definition",
                TypeInfo(LoggerDefinitionVersion),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "version",
                "Version",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the logger definition version.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time, in milliseconds since the epoch, when the logger definition
    # version was created.
    creation_timestamp: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the logger definition version.
    definition: "LoggerDefinitionVersion" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the logger definition version.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version of the logger definition version.
    version: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetResourceDefinitionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_definition_id",
                "ResourceDefinitionId",
                TypeInfo(str),
            ),
        ]

    # The ID of the resource definition.
    resource_definition_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetResourceDefinitionResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "creation_timestamp",
                "CreationTimestamp",
                TypeInfo(str),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "last_updated_timestamp",
                "LastUpdatedTimestamp",
                TypeInfo(str),
            ),
            (
                "latest_version",
                "LatestVersion",
                TypeInfo(str),
            ),
            (
                "latest_version_arn",
                "LatestVersionArn",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the definition.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time, in milliseconds since the epoch, when the definition was created.
    creation_timestamp: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the definition.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time, in milliseconds since the epoch, when the definition was last
    # updated.
    last_updated_timestamp: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The latest version of the definition.
    latest_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the latest version of the definition.
    latest_version_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the definition.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetResourceDefinitionVersionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_definition_id",
                "ResourceDefinitionId",
                TypeInfo(str),
            ),
            (
                "resource_definition_version_id",
                "ResourceDefinitionVersionId",
                TypeInfo(str),
            ),
        ]

    # The ID of the resource definition.
    resource_definition_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the resource definition version.
    resource_definition_version_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetResourceDefinitionVersionResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "creation_timestamp",
                "CreationTimestamp",
                TypeInfo(str),
            ),
            (
                "definition",
                "Definition",
                TypeInfo(ResourceDefinitionVersion),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "version",
                "Version",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Arn of the resource definition version.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time, in milliseconds since the epoch, when the resource definition
    # version was created.
    creation_timestamp: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the definition.
    definition: "ResourceDefinitionVersion" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the resource definition version.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version of the resource definition version.
    version: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetServiceRoleForAccountRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class GetServiceRoleForAccountResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "associated_at",
                "AssociatedAt",
                TypeInfo(str),
            ),
            (
                "role_arn",
                "RoleArn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time when the service role was associated with the account.
    associated_at: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the role which is associated with the account.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetSubscriptionDefinitionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subscription_definition_id",
                "SubscriptionDefinitionId",
                TypeInfo(str),
            ),
        ]

    # The ID of the subscription definition.
    subscription_definition_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetSubscriptionDefinitionResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "creation_timestamp",
                "CreationTimestamp",
                TypeInfo(str),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "last_updated_timestamp",
                "LastUpdatedTimestamp",
                TypeInfo(str),
            ),
            (
                "latest_version",
                "LatestVersion",
                TypeInfo(str),
            ),
            (
                "latest_version_arn",
                "LatestVersionArn",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the definition.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time, in milliseconds since the epoch, when the definition was created.
    creation_timestamp: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the definition.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time, in milliseconds since the epoch, when the definition was last
    # updated.
    last_updated_timestamp: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The latest version of the definition.
    latest_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the latest version of the definition.
    latest_version_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the definition.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetSubscriptionDefinitionVersionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subscription_definition_id",
                "SubscriptionDefinitionId",
                TypeInfo(str),
            ),
            (
                "subscription_definition_version_id",
                "SubscriptionDefinitionVersionId",
                TypeInfo(str),
            ),
        ]

    # The ID of the subscription definition.
    subscription_definition_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the subscription definition version.
    subscription_definition_version_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetSubscriptionDefinitionVersionResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "creation_timestamp",
                "CreationTimestamp",
                TypeInfo(str),
            ),
            (
                "definition",
                "Definition",
                TypeInfo(SubscriptionDefinitionVersion),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "version",
                "Version",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the subscription definition version.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time, in milliseconds since the epoch, when the subscription definition
    # version was created.
    creation_timestamp: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the subscription definition version.
    definition: "SubscriptionDefinitionVersion" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the subscription definition version.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version of the subscription definition version.
    version: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GroupCertificateAuthorityProperties(ShapeBase):
    """
    Information about a certificate authority for a group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_certificate_authority_arn",
                "GroupCertificateAuthorityArn",
                TypeInfo(str),
            ),
            (
                "group_certificate_authority_id",
                "GroupCertificateAuthorityId",
                TypeInfo(str),
            ),
        ]

    # The ARN of the certificate authority for the group.
    group_certificate_authority_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the certificate authority for the group.
    group_certificate_authority_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GroupCertificateConfiguration(ShapeBase):
    """
    Information about a group certificate configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "certificate_authority_expiry_in_milliseconds",
                "CertificateAuthorityExpiryInMilliseconds",
                TypeInfo(str),
            ),
            (
                "certificate_expiry_in_milliseconds",
                "CertificateExpiryInMilliseconds",
                TypeInfo(str),
            ),
            (
                "group_id",
                "GroupId",
                TypeInfo(str),
            ),
        ]

    # The amount of time remaining before the certificate authority expires, in
    # milliseconds.
    certificate_authority_expiry_in_milliseconds: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The amount of time remaining before the certificate expires, in
    # milliseconds.
    certificate_expiry_in_milliseconds: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the group certificate configuration.
    group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GroupInformation(ShapeBase):
    """
    Information about a group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "creation_timestamp",
                "CreationTimestamp",
                TypeInfo(str),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "last_updated_timestamp",
                "LastUpdatedTimestamp",
                TypeInfo(str),
            ),
            (
                "latest_version",
                "LatestVersion",
                TypeInfo(str),
            ),
            (
                "latest_version_arn",
                "LatestVersionArn",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The ARN of the group.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time, in milliseconds since the epoch, when the group was created.
    creation_timestamp: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the group.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time, in milliseconds since the epoch, when the group was last updated.
    last_updated_timestamp: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The latest version of the group.
    latest_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the latest version of the group.
    latest_version_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the group.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GroupOwnerSetting(ShapeBase):
    """
    Group owner related settings for local resources.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "auto_add_group_owner",
                "AutoAddGroupOwner",
                TypeInfo(bool),
            ),
            (
                "group_owner",
                "GroupOwner",
                TypeInfo(str),
            ),
        ]

    # If true, GreenGrass automatically adds the specified Linux OS group owner
    # of the resource to the Lambda process privileges. Thus the Lambda process
    # will have the file access permissions of the added Linux group.
    auto_add_group_owner: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the Linux OS group whose privileges will be added to the Lambda
    # process. This field is optional.
    group_owner: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GroupVersion(ShapeBase):
    """
    Information about a group version.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "core_definition_version_arn",
                "CoreDefinitionVersionArn",
                TypeInfo(str),
            ),
            (
                "device_definition_version_arn",
                "DeviceDefinitionVersionArn",
                TypeInfo(str),
            ),
            (
                "function_definition_version_arn",
                "FunctionDefinitionVersionArn",
                TypeInfo(str),
            ),
            (
                "logger_definition_version_arn",
                "LoggerDefinitionVersionArn",
                TypeInfo(str),
            ),
            (
                "resource_definition_version_arn",
                "ResourceDefinitionVersionArn",
                TypeInfo(str),
            ),
            (
                "subscription_definition_version_arn",
                "SubscriptionDefinitionVersionArn",
                TypeInfo(str),
            ),
        ]

    # The ARN of the core definition version for this group.
    core_definition_version_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the device definition version for this group.
    device_definition_version_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the function definition version for this group.
    function_definition_version_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the logger definition version for this group.
    logger_definition_version_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The resource definition version ARN for this group.
    resource_definition_version_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the subscription definition version for this group.
    subscription_definition_version_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InternalServerErrorException(ShapeBase):
    """
    General error information.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "error_details",
                "ErrorDetails",
                TypeInfo(typing.List[ErrorDetail]),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    # Details about the error.
    error_details: typing.List["ErrorDetail"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A message containing information about the error.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListCoreDefinitionVersionsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "core_definition_id",
                "CoreDefinitionId",
                TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The ID of the core definition.
    core_definition_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to be returned per request.
    max_results: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token for the next set of results, or ''null'' if there are no
    # additional results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListCoreDefinitionVersionsResponse(OutputShapeBase):
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
                "versions",
                "Versions",
                TypeInfo(typing.List[VersionInformation]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token for the next set of results, or ''null'' if there are no
    # additional results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about a version.
    versions: typing.List["VersionInformation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListCoreDefinitionsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "max_results",
                "MaxResults",
                TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The maximum number of results to be returned per request.
    max_results: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token for the next set of results, or ''null'' if there are no
    # additional results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListCoreDefinitionsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "definitions",
                "Definitions",
                TypeInfo(typing.List[DefinitionInformation]),
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

    # Information about a definition.
    definitions: typing.List["DefinitionInformation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token for the next set of results, or ''null'' if there are no
    # additional results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListDefinitionsResponse(ShapeBase):
    """
    A list of definitions.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "definitions",
                "Definitions",
                TypeInfo(typing.List[DefinitionInformation]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # Information about a definition.
    definitions: typing.List["DefinitionInformation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token for the next set of results, or ''null'' if there are no
    # additional results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListDeploymentsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_id",
                "GroupId",
                TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The ID of the AWS Greengrass group.
    group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to be returned per request.
    max_results: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token for the next set of results, or ''null'' if there are no
    # additional results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListDeploymentsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "deployments",
                "Deployments",
                TypeInfo(typing.List[Deployment]),
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

    # A list of deployments for the requested groups.
    deployments: typing.List["Deployment"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token for the next set of results, or ''null'' if there are no
    # additional results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListDeviceDefinitionVersionsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "device_definition_id",
                "DeviceDefinitionId",
                TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The ID of the device definition.
    device_definition_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to be returned per request.
    max_results: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token for the next set of results, or ''null'' if there are no
    # additional results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListDeviceDefinitionVersionsResponse(OutputShapeBase):
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
                "versions",
                "Versions",
                TypeInfo(typing.List[VersionInformation]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token for the next set of results, or ''null'' if there are no
    # additional results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about a version.
    versions: typing.List["VersionInformation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListDeviceDefinitionsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "max_results",
                "MaxResults",
                TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The maximum number of results to be returned per request.
    max_results: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token for the next set of results, or ''null'' if there are no
    # additional results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListDeviceDefinitionsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "definitions",
                "Definitions",
                TypeInfo(typing.List[DefinitionInformation]),
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

    # Information about a definition.
    definitions: typing.List["DefinitionInformation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token for the next set of results, or ''null'' if there are no
    # additional results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListFunctionDefinitionVersionsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "function_definition_id",
                "FunctionDefinitionId",
                TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The ID of the Lambda function definition.
    function_definition_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to be returned per request.
    max_results: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token for the next set of results, or ''null'' if there are no
    # additional results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListFunctionDefinitionVersionsResponse(OutputShapeBase):
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
                "versions",
                "Versions",
                TypeInfo(typing.List[VersionInformation]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token for the next set of results, or ''null'' if there are no
    # additional results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about a version.
    versions: typing.List["VersionInformation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListFunctionDefinitionsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "max_results",
                "MaxResults",
                TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The maximum number of results to be returned per request.
    max_results: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token for the next set of results, or ''null'' if there are no
    # additional results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListFunctionDefinitionsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "definitions",
                "Definitions",
                TypeInfo(typing.List[DefinitionInformation]),
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

    # Information about a definition.
    definitions: typing.List["DefinitionInformation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token for the next set of results, or ''null'' if there are no
    # additional results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListGroupCertificateAuthoritiesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_id",
                "GroupId",
                TypeInfo(str),
            ),
        ]

    # The ID of the AWS Greengrass group.
    group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListGroupCertificateAuthoritiesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "group_certificate_authorities",
                "GroupCertificateAuthorities",
                TypeInfo(typing.List[GroupCertificateAuthorityProperties]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of certificate authorities associated with the group.
    group_certificate_authorities: typing.List[
        "GroupCertificateAuthorityProperties"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )


@dataclasses.dataclass
class ListGroupVersionsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_id",
                "GroupId",
                TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The ID of the AWS Greengrass group.
    group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to be returned per request.
    max_results: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token for the next set of results, or ''null'' if there are no
    # additional results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListGroupVersionsResponse(OutputShapeBase):
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
                "versions",
                "Versions",
                TypeInfo(typing.List[VersionInformation]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token for the next set of results, or ''null'' if there are no
    # additional results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about a version.
    versions: typing.List["VersionInformation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListGroupsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "max_results",
                "MaxResults",
                TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The maximum number of results to be returned per request.
    max_results: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token for the next set of results, or ''null'' if there are no
    # additional results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListGroupsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "groups",
                "Groups",
                TypeInfo(typing.List[GroupInformation]),
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

    # Information about a group.
    groups: typing.List["GroupInformation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token for the next set of results, or ''null'' if there are no
    # additional results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListLoggerDefinitionVersionsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "logger_definition_id",
                "LoggerDefinitionId",
                TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The ID of the logger definition.
    logger_definition_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to be returned per request.
    max_results: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token for the next set of results, or ''null'' if there are no
    # additional results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListLoggerDefinitionVersionsResponse(OutputShapeBase):
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
                "versions",
                "Versions",
                TypeInfo(typing.List[VersionInformation]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token for the next set of results, or ''null'' if there are no
    # additional results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about a version.
    versions: typing.List["VersionInformation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListLoggerDefinitionsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "max_results",
                "MaxResults",
                TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The maximum number of results to be returned per request.
    max_results: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token for the next set of results, or ''null'' if there are no
    # additional results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListLoggerDefinitionsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "definitions",
                "Definitions",
                TypeInfo(typing.List[DefinitionInformation]),
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

    # Information about a definition.
    definitions: typing.List["DefinitionInformation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token for the next set of results, or ''null'' if there are no
    # additional results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListResourceDefinitionVersionsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_definition_id",
                "ResourceDefinitionId",
                TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The ID of the resource definition.
    resource_definition_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to be returned per request.
    max_results: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token for the next set of results, or ''null'' if there are no
    # additional results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListResourceDefinitionVersionsResponse(OutputShapeBase):
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
                "versions",
                "Versions",
                TypeInfo(typing.List[VersionInformation]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token for the next set of results, or ''null'' if there are no
    # additional results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about a version.
    versions: typing.List["VersionInformation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListResourceDefinitionsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "max_results",
                "MaxResults",
                TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The maximum number of results to be returned per request.
    max_results: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token for the next set of results, or ''null'' if there are no
    # additional results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListResourceDefinitionsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "definitions",
                "Definitions",
                TypeInfo(typing.List[DefinitionInformation]),
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

    # Information about a definition.
    definitions: typing.List["DefinitionInformation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token for the next set of results, or ''null'' if there are no
    # additional results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListSubscriptionDefinitionVersionsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subscription_definition_id",
                "SubscriptionDefinitionId",
                TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The ID of the subscription definition.
    subscription_definition_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of results to be returned per request.
    max_results: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token for the next set of results, or ''null'' if there are no
    # additional results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListSubscriptionDefinitionVersionsResponse(OutputShapeBase):
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
                "versions",
                "Versions",
                TypeInfo(typing.List[VersionInformation]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token for the next set of results, or ''null'' if there are no
    # additional results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about a version.
    versions: typing.List["VersionInformation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListSubscriptionDefinitionsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "max_results",
                "MaxResults",
                TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The maximum number of results to be returned per request.
    max_results: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token for the next set of results, or ''null'' if there are no
    # additional results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListSubscriptionDefinitionsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "definitions",
                "Definitions",
                TypeInfo(typing.List[DefinitionInformation]),
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

    # Information about a definition.
    definitions: typing.List["DefinitionInformation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token for the next set of results, or ''null'' if there are no
    # additional results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListVersionsResponse(ShapeBase):
    """
    A list of versions.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "versions",
                "Versions",
                TypeInfo(typing.List[VersionInformation]),
            ),
        ]

    # The token for the next set of results, or ''null'' if there are no
    # additional results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about a version.
    versions: typing.List["VersionInformation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class LocalDeviceResourceData(ShapeBase):
    """
    Attributes that define a local device resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_owner_setting",
                "GroupOwnerSetting",
                TypeInfo(GroupOwnerSetting),
            ),
            (
                "source_path",
                "SourcePath",
                TypeInfo(str),
            ),
        ]

    # Group/owner related settings for local resources.
    group_owner_setting: "GroupOwnerSetting" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The local absolute path of the device resource. The source path for a
    # device resource can refer only to a character device or block device under
    # ''/dev''.
    source_path: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LocalVolumeResourceData(ShapeBase):
    """
    Attributes that define a local volume resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "destination_path",
                "DestinationPath",
                TypeInfo(str),
            ),
            (
                "group_owner_setting",
                "GroupOwnerSetting",
                TypeInfo(GroupOwnerSetting),
            ),
            (
                "source_path",
                "SourcePath",
                TypeInfo(str),
            ),
        ]

    # The absolute local path of the resource inside the lambda environment.
    destination_path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Allows you to configure additional group privileges for the Lambda process.
    # This field is optional.
    group_owner_setting: "GroupOwnerSetting" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The local absolute path of the volume resource on the host. The source path
    # for a volume resource type cannot start with ''/sys''.
    source_path: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Logger(ShapeBase):
    """
    Information about a logger
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "component",
                "Component",
                TypeInfo(typing.Union[str, LoggerComponent]),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "level",
                "Level",
                TypeInfo(typing.Union[str, LoggerLevel]),
            ),
            (
                "space",
                "Space",
                TypeInfo(int),
            ),
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, LoggerType]),
            ),
        ]

    # The component that will be subject to logging.
    component: typing.Union[str, "LoggerComponent"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The id of the logger.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The level of the logs.
    level: typing.Union[str, "LoggerLevel"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The amount of file space, in KB, to use if the local file system is used
    # for logging purposes.
    space: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of log output which will be used.
    type: typing.Union[str, "LoggerType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class LoggerComponent(str):
    GreengrassSystem = "GreengrassSystem"
    Lambda = "Lambda"


@dataclasses.dataclass
class LoggerDefinitionVersion(ShapeBase):
    """
    Information about a logger definition version.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "loggers",
                "Loggers",
                TypeInfo(typing.List[Logger]),
            ),
        ]

    # A list of loggers.
    loggers: typing.List["Logger"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class LoggerLevel(str):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARN = "WARN"
    ERROR = "ERROR"
    FATAL = "FATAL"


class LoggerType(str):
    FileSystem = "FileSystem"
    AWSCloudWatch = "AWSCloudWatch"


class Permission(str):
    """
    The type of permission a function has to access a resource.
    """
    ro = "ro"
    rw = "rw"


@dataclasses.dataclass
class ResetDeploymentsRequest(ShapeBase):
    """
    Information needed to reset deployments.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_id",
                "GroupId",
                TypeInfo(str),
            ),
            (
                "amzn_client_token",
                "AmznClientToken",
                TypeInfo(str),
            ),
            (
                "force",
                "Force",
                TypeInfo(bool),
            ),
        ]

    # The ID of the AWS Greengrass group.
    group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A client token used to correlate requests and responses.
    amzn_client_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If true, performs a best-effort only core reset.
    force: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResetDeploymentsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "deployment_arn",
                "DeploymentArn",
                TypeInfo(str),
            ),
            (
                "deployment_id",
                "DeploymentId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the deployment.
    deployment_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the deployment.
    deployment_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Resource(ShapeBase):
    """
    Information about a resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "resource_data_container",
                "ResourceDataContainer",
                TypeInfo(ResourceDataContainer),
            ),
        ]

    # The resource ID, used to refer to a resource in the Lambda function
    # configuration. Max length is 128 characters with pattern
    # ''[a-zA-Z0-9:_-]+''. This must be unique within a Greengrass group.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The descriptive resource name, which is displayed on the Greengrass
    # console. Max length 128 characters with pattern ''[a-zA-Z0-9:_-]+''. This
    # must be unique within a Greengrass group.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A container of data for all resource types.
    resource_data_container: "ResourceDataContainer" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ResourceAccessPolicy(ShapeBase):
    """
    A policy used by the function to access a resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "permission",
                "Permission",
                TypeInfo(typing.Union[str, Permission]),
            ),
            (
                "resource_id",
                "ResourceId",
                TypeInfo(str),
            ),
        ]

    # The permissions that the Lambda function has to the resource. Can be one of
    # ''rw'' (read/write) or ''ro'' (read-only).
    permission: typing.Union[str, "Permission"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the resource. (This ID is assigned to the resource when you
    # create the resource definiton.)
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceDataContainer(ShapeBase):
    """
    A container for resource data. The container takes only one of the following
    supported resource data types: ''LocalDeviceResourceData'',
    ''LocalVolumeResourceData'', ''SageMakerMachineLearningModelResourceData'',
    ''S3MachineLearningModelResourceData''.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "local_device_resource_data",
                "LocalDeviceResourceData",
                TypeInfo(LocalDeviceResourceData),
            ),
            (
                "local_volume_resource_data",
                "LocalVolumeResourceData",
                TypeInfo(LocalVolumeResourceData),
            ),
            (
                "s3_machine_learning_model_resource_data",
                "S3MachineLearningModelResourceData",
                TypeInfo(S3MachineLearningModelResourceData),
            ),
            (
                "sage_maker_machine_learning_model_resource_data",
                "SageMakerMachineLearningModelResourceData",
                TypeInfo(SageMakerMachineLearningModelResourceData),
            ),
        ]

    # Attributes that define the local device resource.
    local_device_resource_data: "LocalDeviceResourceData" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Attributes that define the local volume resource.
    local_volume_resource_data: "LocalVolumeResourceData" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Attributes that define an S3 machine learning resource.
    s3_machine_learning_model_resource_data: "S3MachineLearningModelResourceData" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Attributes that define an SageMaker machine learning resource.
    sage_maker_machine_learning_model_resource_data: "SageMakerMachineLearningModelResourceData" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ResourceDefinitionVersion(ShapeBase):
    """
    Information about a resource definition version.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resources",
                "Resources",
                TypeInfo(typing.List[Resource]),
            ),
        ]

    # A list of resources.
    resources: typing.List["Resource"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class S3MachineLearningModelResourceData(ShapeBase):
    """
    Attributes that define an S3 machine learning resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "destination_path",
                "DestinationPath",
                TypeInfo(str),
            ),
            (
                "s3_uri",
                "S3Uri",
                TypeInfo(str),
            ),
        ]

    # The absolute local path of the resource inside the Lambda environment.
    destination_path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The URI of the source model in an S3 bucket. The model package must be in
    # tar.gz or .zip format.
    s3_uri: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SageMakerMachineLearningModelResourceData(ShapeBase):
    """
    Attributes that define an SageMaker machine learning resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "destination_path",
                "DestinationPath",
                TypeInfo(str),
            ),
            (
                "sage_maker_job_arn",
                "SageMakerJobArn",
                TypeInfo(str),
            ),
        ]

    # The absolute local path of the resource inside the Lambda environment.
    destination_path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the SageMaker training job that represents the source model.
    sage_maker_job_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class SoftwareToUpdate(str):
    """
    The piece of software on the Greengrass core that will be updated.
    """
    core = "core"
    ota_agent = "ota_agent"


@dataclasses.dataclass
class Subscription(ShapeBase):
    """
    Information about a subscription.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "source",
                "Source",
                TypeInfo(str),
            ),
            (
                "subject",
                "Subject",
                TypeInfo(str),
            ),
            (
                "target",
                "Target",
                TypeInfo(str),
            ),
        ]

    # The id of the subscription.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The source of the subscription. Can be a thing ARN, a Lambda function ARN,
    # 'cloud' (which represents the IoT cloud), or 'GGShadowService'.
    source: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The subject of the message.
    subject: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Where the message is sent to. Can be a thing ARN, a Lambda function ARN,
    # 'cloud' (which represents the IoT cloud), or 'GGShadowService'.
    target: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SubscriptionDefinitionVersion(ShapeBase):
    """
    Information about a subscription definition version.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subscriptions",
                "Subscriptions",
                TypeInfo(typing.List[Subscription]),
            ),
        ]

    # A list of subscriptions.
    subscriptions: typing.List["Subscription"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class UpdateAgentLogLevel(str):
    """
    The minimum level of log statements that should be logged by the OTA Agent
    during an update.
    """
    NONE = "NONE"
    TRACE = "TRACE"
    DEBUG = "DEBUG"
    VERBOSE = "VERBOSE"
    INFO = "INFO"
    WARN = "WARN"
    ERROR = "ERROR"
    FATAL = "FATAL"


@dataclasses.dataclass
class UpdateConnectivityInfoRequest(ShapeBase):
    """
    Connectivity information.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "thing_name",
                "ThingName",
                TypeInfo(str),
            ),
            (
                "connectivity_info",
                "ConnectivityInfo",
                TypeInfo(typing.List[ConnectivityInfo]),
            ),
        ]

    # The thing name.
    thing_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of connectivity info.
    connectivity_info: typing.List["ConnectivityInfo"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateConnectivityInfoResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
            (
                "version",
                "Version",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A message about the connectivity info update request.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new version of the connectivity info.
    version: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateCoreDefinitionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "core_definition_id",
                "CoreDefinitionId",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The ID of the core definition.
    core_definition_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the definition.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateCoreDefinitionResponse(OutputShapeBase):
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
class UpdateDeviceDefinitionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "device_definition_id",
                "DeviceDefinitionId",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The ID of the device definition.
    device_definition_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the definition.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateDeviceDefinitionResponse(OutputShapeBase):
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
class UpdateFunctionDefinitionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "function_definition_id",
                "FunctionDefinitionId",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The ID of the Lambda function definition.
    function_definition_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the definition.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateFunctionDefinitionResponse(OutputShapeBase):
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
class UpdateGroupCertificateConfigurationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_id",
                "GroupId",
                TypeInfo(str),
            ),
            (
                "certificate_expiry_in_milliseconds",
                "CertificateExpiryInMilliseconds",
                TypeInfo(str),
            ),
        ]

    # The ID of the AWS Greengrass group.
    group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The amount of time remaining before the certificate expires, in
    # milliseconds.
    certificate_expiry_in_milliseconds: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateGroupCertificateConfigurationResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "certificate_authority_expiry_in_milliseconds",
                "CertificateAuthorityExpiryInMilliseconds",
                TypeInfo(str),
            ),
            (
                "certificate_expiry_in_milliseconds",
                "CertificateExpiryInMilliseconds",
                TypeInfo(str),
            ),
            (
                "group_id",
                "GroupId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The amount of time remaining before the certificate authority expires, in
    # milliseconds.
    certificate_authority_expiry_in_milliseconds: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The amount of time remaining before the certificate expires, in
    # milliseconds.
    certificate_expiry_in_milliseconds: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the group certificate configuration.
    group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateGroupRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "group_id",
                "GroupId",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The ID of the AWS Greengrass group.
    group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the definition.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateGroupResponse(OutputShapeBase):
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
class UpdateLoggerDefinitionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "logger_definition_id",
                "LoggerDefinitionId",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The ID of the logger definition.
    logger_definition_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the definition.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateLoggerDefinitionResponse(OutputShapeBase):
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
class UpdateResourceDefinitionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_definition_id",
                "ResourceDefinitionId",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The ID of the resource definition.
    resource_definition_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the definition.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateResourceDefinitionResponse(OutputShapeBase):
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
class UpdateSubscriptionDefinitionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subscription_definition_id",
                "SubscriptionDefinitionId",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The ID of the subscription definition.
    subscription_definition_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the definition.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateSubscriptionDefinitionResponse(OutputShapeBase):
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


class UpdateTargetsArchitecture(str):
    """
    The architecture of the cores which are the targets of an update.
    """
    armv7l = "armv7l"
    x86_64 = "x86_64"
    aarch64 = "aarch64"


class UpdateTargetsOperatingSystem(str):
    """
    The operating system of the cores which are the targets of an update.
    """
    ubuntu = "ubuntu"
    raspbian = "raspbian"
    amazon_linux = "amazon_linux"


@dataclasses.dataclass
class VersionInformation(ShapeBase):
    """
    Information about a version.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "creation_timestamp",
                "CreationTimestamp",
                TypeInfo(str),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "version",
                "Version",
                TypeInfo(str),
            ),
        ]

    # The ARN of the version.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time, in milliseconds since the epoch, when the version was created.
    creation_timestamp: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the version.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique ID of the version.
    version: str = dataclasses.field(default=ShapeBase.NOT_SET, )
