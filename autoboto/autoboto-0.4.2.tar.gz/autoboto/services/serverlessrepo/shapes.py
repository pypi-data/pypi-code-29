import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


@dataclasses.dataclass
class Application(ShapeBase):
    """
    Details about the application.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
            (
                "author",
                "Author",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "creation_time",
                "CreationTime",
                TypeInfo(str),
            ),
            (
                "home_page_url",
                "HomePageUrl",
                TypeInfo(str),
            ),
            (
                "labels",
                "Labels",
                TypeInfo(typing.List[str]),
            ),
            (
                "license_url",
                "LicenseUrl",
                TypeInfo(str),
            ),
            (
                "readme_url",
                "ReadmeUrl",
                TypeInfo(str),
            ),
            (
                "spdx_license_id",
                "SpdxLicenseId",
                TypeInfo(str),
            ),
            (
                "version",
                "Version",
                TypeInfo(Version),
            ),
        ]

    # The application Amazon Resource Name (ARN).
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the author publishing the app.

    # Minimum length=1. Maximum length=127.

    # Pattern "^[a-z0-9](([a-z0-9]|-(?!-))*[a-z0-9])?$";
    author: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the application.

    # Minimum length=1. Maximum length=256
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the application.

    # Minimum length=1. Maximum length=140

    # Pattern: "[a-zA-Z0-9\\\\-]+";
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time this resource was created.
    creation_time: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A URL with more information about the application, for example the location
    # of your GitHub repository for the application.
    home_page_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Labels to improve discovery of apps in search results.

    # Minimum length=1. Maximum length=127. Maximum number of labels: 10

    # Pattern: "^[a-zA-Z0-9+\\\\-_:\\\/@]+$";
    labels: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A link to a license file of the app that matches the spdxLicenseID value of
    # your application.

    # Maximum size 5 MB
    license_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A link to the readme file in Markdown language that contains a more
    # detailed description of the application and how it works.

    # Maximum size 5 MB
    readme_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A valid identifier from https://spdx.org/licenses/.
    spdx_license_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Version information about the application.
    version: "Version" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ApplicationPage(ShapeBase):
    """
    A list of application details.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "applications",
                "Applications",
                TypeInfo(typing.List[ApplicationSummary]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # An array of application summaries.
    applications: typing.List["ApplicationSummary"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token to request the next page of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ApplicationPolicy(ShapeBase):
    """
    Policy statements applied to the application.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "statements",
                "Statements",
                TypeInfo(typing.List[ApplicationPolicyStatement]),
            ),
        ]

    # An array of policy statements applied to the application.
    statements: typing.List["ApplicationPolicyStatement"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ApplicationPolicyStatement(ShapeBase):
    """
    Policy statement applied to the application.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "actions",
                "Actions",
                TypeInfo(typing.List[str]),
            ),
            (
                "principals",
                "Principals",
                TypeInfo(typing.List[str]),
            ),
            (
                "statement_id",
                "StatementId",
                TypeInfo(str),
            ),
        ]

    # See [Application
    # Permissions](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/access-
    # control-resource-based.html#application-permissions) for the list of
    # supported actions.
    actions: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An AWS account ID, or * to make the application public.
    principals: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A unique ID for the statement.
    statement_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ApplicationSummary(ShapeBase):
    """
    Summary of details about the application.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
            (
                "author",
                "Author",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "creation_time",
                "CreationTime",
                TypeInfo(str),
            ),
            (
                "home_page_url",
                "HomePageUrl",
                TypeInfo(str),
            ),
            (
                "labels",
                "Labels",
                TypeInfo(typing.List[str]),
            ),
            (
                "spdx_license_id",
                "SpdxLicenseId",
                TypeInfo(str),
            ),
        ]

    # The application Amazon Resource Name (ARN).
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the author publishing the app.

    # Minimum length=1. Maximum length=127.

    # Pattern "^[a-z0-9](([a-z0-9]|-(?!-))*[a-z0-9])?$";
    author: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the application.

    # Minimum length=1. Maximum length=256
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the application.

    # Minimum length=1. Maximum length=140

    # Pattern: "[a-zA-Z0-9\\\\-]+";
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time this resource was created.
    creation_time: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A URL with more information about the application, for example the location
    # of your GitHub repository for the application.
    home_page_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Labels to improve discovery of apps in search results.

    # Minimum length=1. Maximum length=127. Maximum number of labels: 10

    # Pattern: "^[a-zA-Z0-9+\\\\-_:\\\/@]+$";
    labels: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A valid identifier from <https://spdx.org/licenses/>.
    spdx_license_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ApplicationVersionPage(ShapeBase):
    """
    A list of version summaries for the application.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "versions",
                "Versions",
                TypeInfo(typing.List[VersionSummary]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # An array of version summaries for the application.
    versions: typing.List["VersionSummary"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token to request the next page of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BadRequestException(ShapeBase):
    """
    One of the parameters in the request is invalid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "error_code",
                "ErrorCode",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    # 400
    error_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # One of the parameters in the request is invalid.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ChangeSetDetails(ShapeBase):
    """
    Details of the change set.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
            (
                "change_set_id",
                "ChangeSetId",
                TypeInfo(str),
            ),
            (
                "semantic_version",
                "SemanticVersion",
                TypeInfo(str),
            ),
            (
                "stack_id",
                "StackId",
                TypeInfo(str),
            ),
        ]

    # The application Amazon Resource Name (ARN).
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the change set.

    # Length constraints: Minimum length of 1.

    # Pattern: ARN:[-a-zA-Z0-9:/]*
    change_set_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The semantic version of the application:

    # <https://semver.org/>
    semantic_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique ID of the stack.
    stack_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ConflictException(ShapeBase):
    """
    The resource already exists.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "error_code",
                "ErrorCode",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    # 409
    error_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The resource already exists.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateApplicationInput(ShapeBase):
    """
    Create an application request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "author",
                "Author",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "home_page_url",
                "HomePageUrl",
                TypeInfo(str),
            ),
            (
                "labels",
                "Labels",
                TypeInfo(typing.List[str]),
            ),
            (
                "license_body",
                "LicenseBody",
                TypeInfo(str),
            ),
            (
                "license_url",
                "LicenseUrl",
                TypeInfo(str),
            ),
            (
                "readme_body",
                "ReadmeBody",
                TypeInfo(str),
            ),
            (
                "readme_url",
                "ReadmeUrl",
                TypeInfo(str),
            ),
            (
                "semantic_version",
                "SemanticVersion",
                TypeInfo(str),
            ),
            (
                "source_code_url",
                "SourceCodeUrl",
                TypeInfo(str),
            ),
            (
                "spdx_license_id",
                "SpdxLicenseId",
                TypeInfo(str),
            ),
            (
                "template_body",
                "TemplateBody",
                TypeInfo(str),
            ),
            (
                "template_url",
                "TemplateUrl",
                TypeInfo(str),
            ),
        ]

    # The name of the author publishing the app.

    # Minimum length=1. Maximum length=127.

    # Pattern "^[a-z0-9](([a-z0-9]|-(?!-))*[a-z0-9])?$";
    author: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the application.

    # Minimum length=1. Maximum length=256
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the application that you want to publish.

    # Minimum length=1. Maximum length=140

    # Pattern: "[a-zA-Z0-9\\\\-]+";
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A URL with more information about the application, for example the location
    # of your GitHub repository for the application.
    home_page_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Labels to improve discovery of apps in search results.

    # Minimum length=1. Maximum length=127. Maximum number of labels: 10

    # Pattern: "^[a-zA-Z0-9+\\\\-_:\\\/@]+$";
    labels: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A local text file that contains the license of the app that matches the
    # spdxLicenseID value of your application. The file is of the format
    # file://<path>/<filename>.

    # Maximum size 5 MB

    # Note: Only one of licenseBody and licenseUrl can be specified, otherwise an
    # error will result.
    license_body: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A link to the S3 object that contains the license of the app that matches
    # the spdxLicenseID value of your application.

    # Maximum size 5 MB

    # Note: Only one of licenseBody and licenseUrl can be specified, otherwise an
    # error will result.
    license_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A local text readme file in Markdown language that contains a more detailed
    # description of the application and how it works. The file is of the format
    # file://<path>/<filename>.

    # Maximum size 5 MB

    # Note: Only one of readmeBody and readmeUrl can be specified, otherwise an
    # error will result.
    readme_body: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A link to the S3 object in Markdown language that contains a more detailed
    # description of the application and how it works.

    # Maximum size 5 MB

    # Note: Only one of readmeBody and readmeUrl can be specified, otherwise an
    # error will result.
    readme_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The semantic version of the application:

    # <https://semver.org/>
    semantic_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A link to a public repository for the source code of your application.
    source_code_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A valid identifier from <https://spdx.org/licenses/>.
    spdx_license_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The local raw packaged AWS SAM template file of your application. The file
    # is of the format file://<path>/<filename>.

    # Note: Only one of templateBody and templateUrl can be specified, otherwise
    # an error will result.
    template_body: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A link to the S3 object cotaining the packaged AWS SAM template of your
    # application.

    # Note: Only one of templateBody and templateUrl can be specified, otherwise
    # an error will result.
    template_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateApplicationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "author",
                "Author",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "home_page_url",
                "HomePageUrl",
                TypeInfo(str),
            ),
            (
                "labels",
                "Labels",
                TypeInfo(typing.List[str]),
            ),
            (
                "license_body",
                "LicenseBody",
                TypeInfo(str),
            ),
            (
                "license_url",
                "LicenseUrl",
                TypeInfo(str),
            ),
            (
                "readme_body",
                "ReadmeBody",
                TypeInfo(str),
            ),
            (
                "readme_url",
                "ReadmeUrl",
                TypeInfo(str),
            ),
            (
                "semantic_version",
                "SemanticVersion",
                TypeInfo(str),
            ),
            (
                "source_code_url",
                "SourceCodeUrl",
                TypeInfo(str),
            ),
            (
                "spdx_license_id",
                "SpdxLicenseId",
                TypeInfo(str),
            ),
            (
                "template_body",
                "TemplateBody",
                TypeInfo(str),
            ),
            (
                "template_url",
                "TemplateUrl",
                TypeInfo(str),
            ),
        ]

    # The name of the author publishing the app.

    # Minimum length=1. Maximum length=127.

    # Pattern "^[a-z0-9](([a-z0-9]|-(?!-))*[a-z0-9])?$";
    author: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the application.

    # Minimum length=1. Maximum length=256
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the application that you want to publish.

    # Minimum length=1. Maximum length=140

    # Pattern: "[a-zA-Z0-9\\\\-]+";
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A URL with more information about the application, for example the location
    # of your GitHub repository for the application.
    home_page_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Labels to improve discovery of apps in search results.

    # Minimum length=1. Maximum length=127. Maximum number of labels: 10

    # Pattern: "^[a-zA-Z0-9+\\\\-_:\\\/@]+$";
    labels: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A local text file that contains the license of the app that matches the
    # spdxLicenseID value of your application. The file is of the format
    # file://<path>/<filename>.

    # Maximum size 5 MB

    # Note: Only one of licenseBody and licenseUrl can be specified, otherwise an
    # error will result.
    license_body: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A link to the S3 object that contains the license of the app that matches
    # the spdxLicenseID value of your application.

    # Maximum size 5 MB

    # Note: Only one of licenseBody and licenseUrl can be specified, otherwise an
    # error will result.
    license_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A local text readme file in Markdown language that contains a more detailed
    # description of the application and how it works. The file is of the format
    # file://<path>/<filename>.

    # Maximum size 5 MB

    # Note: Only one of readmeBody and readmeUrl can be specified, otherwise an
    # error will result.
    readme_body: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A link to the S3 object in Markdown language that contains a more detailed
    # description of the application and how it works.

    # Maximum size 5 MB

    # Note: Only one of readmeBody and readmeUrl can be specified, otherwise an
    # error will result.
    readme_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The semantic version of the application:

    # <https://semver.org/>
    semantic_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A link to a public repository for the source code of your application.
    source_code_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A valid identifier from <https://spdx.org/licenses/>.
    spdx_license_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The local raw packaged AWS SAM template file of your application. The file
    # is of the format file://<path>/<filename>.

    # Note: Only one of templateBody and templateUrl can be specified, otherwise
    # an error will result.
    template_body: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A link to the S3 object cotaining the packaged AWS SAM template of your
    # application.

    # Note: Only one of templateBody and templateUrl can be specified, otherwise
    # an error will result.
    template_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateApplicationResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
            (
                "author",
                "Author",
                TypeInfo(str),
            ),
            (
                "creation_time",
                "CreationTime",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "home_page_url",
                "HomePageUrl",
                TypeInfo(str),
            ),
            (
                "labels",
                "Labels",
                TypeInfo(typing.List[str]),
            ),
            (
                "license_url",
                "LicenseUrl",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "readme_url",
                "ReadmeUrl",
                TypeInfo(str),
            ),
            (
                "spdx_license_id",
                "SpdxLicenseId",
                TypeInfo(str),
            ),
            (
                "version",
                "Version",
                TypeInfo(Version),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The application Amazon Resource Name (ARN).
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the author publishing the app.

    # Minimum length=1. Maximum length=127.

    # Pattern "^[a-z0-9](([a-z0-9]|-(?!-))*[a-z0-9])?$";
    author: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time this resource was created.
    creation_time: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the application.

    # Minimum length=1. Maximum length=256
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A URL with more information about the application, for example the location
    # of your GitHub repository for the application.
    home_page_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Labels to improve discovery of apps in search results.

    # Minimum length=1. Maximum length=127. Maximum number of labels: 10

    # Pattern: "^[a-zA-Z0-9+\\\\-_:\\\/@]+$";
    labels: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A link to a license file of the app that matches the spdxLicenseID value of
    # your application.

    # Maximum size 5 MB
    license_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the application.

    # Minimum length=1. Maximum length=140

    # Pattern: "[a-zA-Z0-9\\\\-]+";
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A link to the readme file in Markdown language that contains a more
    # detailed description of the application and how it works.

    # Maximum size 5 MB
    readme_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A valid identifier from https://spdx.org/licenses/.
    spdx_license_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Version information about the application.
    version: "Version" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateApplicationVersionInput(ShapeBase):
    """
    Create a version request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "source_code_url",
                "SourceCodeUrl",
                TypeInfo(str),
            ),
            (
                "template_body",
                "TemplateBody",
                TypeInfo(str),
            ),
            (
                "template_url",
                "TemplateUrl",
                TypeInfo(str),
            ),
        ]

    # A link to a public repository for the source code of your application.
    source_code_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The raw packaged AWS SAM template of your application.
    template_body: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A link to the packaged AWS SAM template of your application.
    template_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateApplicationVersionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
            (
                "semantic_version",
                "SemanticVersion",
                TypeInfo(str),
            ),
            (
                "source_code_url",
                "SourceCodeUrl",
                TypeInfo(str),
            ),
            (
                "template_body",
                "TemplateBody",
                TypeInfo(str),
            ),
            (
                "template_url",
                "TemplateUrl",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The semantic version of the new version.
    semantic_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A link to a public repository for the source code of your application.
    source_code_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The raw packaged AWS SAM template of your application.
    template_body: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A link to the packaged AWS SAM template of your application.
    template_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateApplicationVersionResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
            (
                "creation_time",
                "CreationTime",
                TypeInfo(str),
            ),
            (
                "parameter_definitions",
                "ParameterDefinitions",
                TypeInfo(typing.List[ParameterDefinition]),
            ),
            (
                "semantic_version",
                "SemanticVersion",
                TypeInfo(str),
            ),
            (
                "source_code_url",
                "SourceCodeUrl",
                TypeInfo(str),
            ),
            (
                "template_url",
                "TemplateUrl",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The application Amazon Resource Name (ARN).
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time this resource was created.
    creation_time: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of parameter types supported by the application.
    parameter_definitions: typing.List["ParameterDefinition"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    # The semantic version of the application:

    # <https://semver.org/>
    semantic_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A link to a public repository for the source code of your application.
    source_code_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A link to the packaged AWS SAM template of your application.
    template_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateCloudFormationChangeSetInput(ShapeBase):
    """
    Create an application change set request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stack_name",
                "StackName",
                TypeInfo(str),
            ),
            (
                "parameter_overrides",
                "ParameterOverrides",
                TypeInfo(typing.List[ParameterValue]),
            ),
            (
                "semantic_version",
                "SemanticVersion",
                TypeInfo(str),
            ),
        ]

    # The name or the unique ID of the stack for which you are creating a change
    # set. AWS CloudFormation generates the change set by comparing this stack's
    # information with the information that you submit, such as a modified
    # template or different parameter input values.

    # Constraints: Minimum length of 1.

    # Pattern: ([a-zA-Z][-a-zA-Z0-9]*)|(arn:\b(aws|aws-us-gov|aws-
    # cn)\b:[-a-zA-Z0-9:/._+]*)
    stack_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of parameter values for the parameters of the application.
    parameter_overrides: typing.List["ParameterValue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The semantic version of the application:

    # <https://semver.org/>
    semantic_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateCloudFormationChangeSetRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
            (
                "stack_name",
                "StackName",
                TypeInfo(str),
            ),
            (
                "parameter_overrides",
                "ParameterOverrides",
                TypeInfo(typing.List[ParameterValue]),
            ),
            (
                "semantic_version",
                "SemanticVersion",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name or the unique ID of the stack for which you are creating a change
    # set. AWS CloudFormation generates the change set by comparing this stack's
    # information with the information that you submit, such as a modified
    # template or different parameter input values.

    # Constraints: Minimum length of 1.

    # Pattern: ([a-zA-Z][-a-zA-Z0-9]*)|(arn:\b(aws|aws-us-gov|aws-
    # cn)\b:[-a-zA-Z0-9:/._+]*)
    stack_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of parameter values for the parameters of the application.
    parameter_overrides: typing.List["ParameterValue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The semantic version of the application:

    # <https://semver.org/>
    semantic_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateCloudFormationChangeSetResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
            (
                "change_set_id",
                "ChangeSetId",
                TypeInfo(str),
            ),
            (
                "semantic_version",
                "SemanticVersion",
                TypeInfo(str),
            ),
            (
                "stack_id",
                "StackId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The application Amazon Resource Name (ARN).
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the change set.

    # Length constraints: Minimum length of 1.

    # Pattern: ARN:[-a-zA-Z0-9:/]*
    change_set_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The semantic version of the application:

    # <https://semver.org/>
    semantic_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique ID of the stack.
    stack_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteApplicationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ForbiddenException(ShapeBase):
    """
    The client is not authenticated.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "error_code",
                "ErrorCode",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    # 403
    error_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The client is not authenticated.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetApplicationPolicyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetApplicationPolicyResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "statements",
                "Statements",
                TypeInfo(typing.List[ApplicationPolicyStatement]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of policy statements applied to the application.
    statements: typing.List["ApplicationPolicyStatement"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetApplicationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
            (
                "semantic_version",
                "SemanticVersion",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The semantic version of the application to get.
    semantic_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetApplicationResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
            (
                "author",
                "Author",
                TypeInfo(str),
            ),
            (
                "creation_time",
                "CreationTime",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "home_page_url",
                "HomePageUrl",
                TypeInfo(str),
            ),
            (
                "labels",
                "Labels",
                TypeInfo(typing.List[str]),
            ),
            (
                "license_url",
                "LicenseUrl",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "readme_url",
                "ReadmeUrl",
                TypeInfo(str),
            ),
            (
                "spdx_license_id",
                "SpdxLicenseId",
                TypeInfo(str),
            ),
            (
                "version",
                "Version",
                TypeInfo(Version),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The application Amazon Resource Name (ARN).
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the author publishing the app.

    # Minimum length=1. Maximum length=127.

    # Pattern "^[a-z0-9](([a-z0-9]|-(?!-))*[a-z0-9])?$";
    author: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time this resource was created.
    creation_time: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the application.

    # Minimum length=1. Maximum length=256
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A URL with more information about the application, for example the location
    # of your GitHub repository for the application.
    home_page_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Labels to improve discovery of apps in search results.

    # Minimum length=1. Maximum length=127. Maximum number of labels: 10

    # Pattern: "^[a-zA-Z0-9+\\\\-_:\\\/@]+$";
    labels: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A link to a license file of the app that matches the spdxLicenseID value of
    # your application.

    # Maximum size 5 MB
    license_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the application.

    # Minimum length=1. Maximum length=140

    # Pattern: "[a-zA-Z0-9\\\\-]+";
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A link to the readme file in Markdown language that contains a more
    # detailed description of the application and how it works.

    # Maximum size 5 MB
    readme_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A valid identifier from https://spdx.org/licenses/.
    spdx_license_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Version information about the application.
    version: "Version" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InternalServerErrorException(ShapeBase):
    """
    The AWS Serverless Application Repository service encountered an internal error.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "error_code",
                "ErrorCode",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    # 500
    error_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS Serverless Application Repository service encountered an internal
    # error.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListApplicationVersionsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
            (
                "max_items",
                "MaxItems",
                TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The total number of items to return.
    max_items: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A token to specify where to start paginating.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListApplicationVersionsResponse(OutputShapeBase):
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
                TypeInfo(typing.List[VersionSummary]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token to request the next page of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of version summaries for the application.
    versions: typing.List["VersionSummary"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListApplicationsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "max_items",
                "MaxItems",
                TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The total number of items to return.
    max_items: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A token to specify where to start paginating.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListApplicationsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "applications",
                "Applications",
                TypeInfo(typing.List[ApplicationSummary]),
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

    # An array of application summaries.
    applications: typing.List["ApplicationSummary"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token to request the next page of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class NotFoundException(ShapeBase):
    """
    The resource (for example, an access policy statement) specified in the request
    doesn't exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "error_code",
                "ErrorCode",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    # 404
    error_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The resource (for example, an access policy statement) specified in the
    # request doesn't exist.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ParameterDefinition(ShapeBase):
    """
    Parameters supported by the application.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "referenced_by_resources",
                "ReferencedByResources",
                TypeInfo(typing.List[str]),
            ),
            (
                "allowed_pattern",
                "AllowedPattern",
                TypeInfo(str),
            ),
            (
                "allowed_values",
                "AllowedValues",
                TypeInfo(typing.List[str]),
            ),
            (
                "constraint_description",
                "ConstraintDescription",
                TypeInfo(str),
            ),
            (
                "default_value",
                "DefaultValue",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "max_length",
                "MaxLength",
                TypeInfo(int),
            ),
            (
                "max_value",
                "MaxValue",
                TypeInfo(int),
            ),
            (
                "min_length",
                "MinLength",
                TypeInfo(int),
            ),
            (
                "min_value",
                "MinValue",
                TypeInfo(int),
            ),
            (
                "no_echo",
                "NoEcho",
                TypeInfo(bool),
            ),
            (
                "type",
                "Type",
                TypeInfo(str),
            ),
        ]

    # The name of the parameter.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of AWS SAM resources that use this parameter.
    referenced_by_resources: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A regular expression that represents the patterns to allow for String
    # types.
    allowed_pattern: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array containing the list of values allowed for the parameter.
    allowed_values: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A string that explains a constraint when the constraint is violated. For
    # example, without a constraint description, a parameter that has an allowed
    # pattern of [A-Za-z0-9]+ displays the following error message when the user
    # specifies an invalid value:

    # Malformed input-Parameter MyParameter must match pattern [A-Za-z0-9]+

    # By adding a constraint description, such as "must contain only uppercase
    # and lowercase letters and numbers," you can display the following
    # customized error message:

    # Malformed input-Parameter MyParameter must contain only uppercase and
    # lowercase letters and numbers.
    constraint_description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A value of the appropriate type for the template to use if no value is
    # specified when a stack is created. If you define constraints for the
    # parameter, you must specify a value that adheres to those constraints.
    default_value: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A string of up to 4,000 characters that describes the parameter.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An integer value that determines the largest number of characters that you
    # want to allow for String types.
    max_length: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A numeric value that determines the largest numeric value that you want to
    # allow for Number types.
    max_value: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An integer value that determines the smallest number of characters that you
    # want to allow for String types.
    min_length: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A numeric value that determines the smallest numeric value that you want to
    # allow for Number types.
    min_value: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Whether to mask the parameter value whenever anyone makes a call that
    # describes the stack. If you set the value to true, the parameter value is
    # masked with asterisks (*****).
    no_echo: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of the parameter.

    # Valid values: String | Number | List<Number> | CommaDelimitedList

    # String: A literal string.

    # For example, users can specify "MyUserName".

    # Number: An integer or float. AWS CloudFormation validates the parameter
    # value as a number. However, when you use the parameter elsewhere in your
    # template (for example, by using the Ref intrinsic function), the parameter
    # value becomes a string.

    # For example, users might specify "8888".

    # List<Number>: An array of integers or floats that are separated by commas.
    # AWS CloudFormation validates the parameter value as numbers. However, when
    # you use the parameter elsewhere in your template (for example, by using the
    # Ref intrinsic function), the parameter value becomes a list of strings.

    # For example, users might specify "80,20", and then Ref results in
    # ["80","20"].

    # CommaDelimitedList: An array of literal strings that are separated by
    # commas. The total number of strings should be one more than the total
    # number of commas. Also, each member string is space-trimmed.

    # For example, users might specify "test,dev,prod", and then Ref results in
    # ["test","dev","prod"].
    type: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ParameterValue(ShapeBase):
    """
    Parameter value of the application.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "value",
                "Value",
                TypeInfo(str),
            ),
        ]

    # The key associated with the parameter. If you don't specify a key and value
    # for a particular parameter, AWS CloudFormation uses the default value that
    # is specified in your template.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The input value associated with the parameter.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutApplicationPolicyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
            (
                "statements",
                "Statements",
                TypeInfo(typing.List[ApplicationPolicyStatement]),
            ),
        ]

    # The Amazon Resource Name (ARN) of the application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of policy statements applied to the application.
    statements: typing.List["ApplicationPolicyStatement"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutApplicationPolicyResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "statements",
                "Statements",
                TypeInfo(typing.List[ApplicationPolicyStatement]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of policy statements applied to the application.
    statements: typing.List["ApplicationPolicyStatement"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class TooManyRequestsException(ShapeBase):
    """
    The client is sending more than the allowed number of requests per unit of time.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "error_code",
                "ErrorCode",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    # 429
    error_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The client is sending more than the allowed number of requests per unit of
    # time.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateApplicationInput(ShapeBase):
    """
    Update the application request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "author",
                "Author",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "home_page_url",
                "HomePageUrl",
                TypeInfo(str),
            ),
            (
                "labels",
                "Labels",
                TypeInfo(typing.List[str]),
            ),
            (
                "readme_body",
                "ReadmeBody",
                TypeInfo(str),
            ),
            (
                "readme_url",
                "ReadmeUrl",
                TypeInfo(str),
            ),
        ]

    # The name of the author publishing the app.

    # Minimum length=1. Maximum length=127.

    # Pattern "^[a-z0-9](([a-z0-9]|-(?!-))*[a-z0-9])?$";
    author: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the application.

    # Minimum length=1. Maximum length=256
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A URL with more information about the application, for example the location
    # of your GitHub repository for the application.
    home_page_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Labels to improve discovery of apps in search results.

    # Minimum length=1. Maximum length=127. Maximum number of labels: 10

    # Pattern: "^[a-zA-Z0-9+\\\\-_:\\\/@]+$";
    labels: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A text readme file in Markdown language that contains a more detailed
    # description of the application and how it works.

    # Maximum size 5 MB
    readme_body: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A link to the readme file in Markdown language that contains a more
    # detailed description of the application and how it works.

    # Maximum size 5 MB
    readme_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateApplicationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
            (
                "author",
                "Author",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "home_page_url",
                "HomePageUrl",
                TypeInfo(str),
            ),
            (
                "labels",
                "Labels",
                TypeInfo(typing.List[str]),
            ),
            (
                "readme_body",
                "ReadmeBody",
                TypeInfo(str),
            ),
            (
                "readme_url",
                "ReadmeUrl",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the author publishing the app.

    # Minimum length=1. Maximum length=127.

    # Pattern "^[a-z0-9](([a-z0-9]|-(?!-))*[a-z0-9])?$";
    author: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the application.

    # Minimum length=1. Maximum length=256
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A URL with more information about the application, for example the location
    # of your GitHub repository for the application.
    home_page_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Labels to improve discovery of apps in search results.

    # Minimum length=1. Maximum length=127. Maximum number of labels: 10

    # Pattern: "^[a-zA-Z0-9+\\\\-_:\\\/@]+$";
    labels: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A text readme file in Markdown language that contains a more detailed
    # description of the application and how it works.

    # Maximum size 5 MB
    readme_body: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A link to the readme file in Markdown language that contains a more
    # detailed description of the application and how it works.

    # Maximum size 5 MB
    readme_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateApplicationResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
            (
                "author",
                "Author",
                TypeInfo(str),
            ),
            (
                "creation_time",
                "CreationTime",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "home_page_url",
                "HomePageUrl",
                TypeInfo(str),
            ),
            (
                "labels",
                "Labels",
                TypeInfo(typing.List[str]),
            ),
            (
                "license_url",
                "LicenseUrl",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "readme_url",
                "ReadmeUrl",
                TypeInfo(str),
            ),
            (
                "spdx_license_id",
                "SpdxLicenseId",
                TypeInfo(str),
            ),
            (
                "version",
                "Version",
                TypeInfo(Version),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The application Amazon Resource Name (ARN).
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the author publishing the app.

    # Minimum length=1. Maximum length=127.

    # Pattern "^[a-z0-9](([a-z0-9]|-(?!-))*[a-z0-9])?$";
    author: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time this resource was created.
    creation_time: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the application.

    # Minimum length=1. Maximum length=256
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A URL with more information about the application, for example the location
    # of your GitHub repository for the application.
    home_page_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Labels to improve discovery of apps in search results.

    # Minimum length=1. Maximum length=127. Maximum number of labels: 10

    # Pattern: "^[a-zA-Z0-9+\\\\-_:\\\/@]+$";
    labels: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A link to a license file of the app that matches the spdxLicenseID value of
    # your application.

    # Maximum size 5 MB
    license_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the application.

    # Minimum length=1. Maximum length=140

    # Pattern: "[a-zA-Z0-9\\\\-]+";
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A link to the readme file in Markdown language that contains a more
    # detailed description of the application and how it works.

    # Maximum size 5 MB
    readme_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A valid identifier from https://spdx.org/licenses/.
    spdx_license_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Version information about the application.
    version: "Version" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Version(ShapeBase):
    """
    Application version details.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
            (
                "creation_time",
                "CreationTime",
                TypeInfo(str),
            ),
            (
                "parameter_definitions",
                "ParameterDefinitions",
                TypeInfo(typing.List[ParameterDefinition]),
            ),
            (
                "semantic_version",
                "SemanticVersion",
                TypeInfo(str),
            ),
            (
                "template_url",
                "TemplateUrl",
                TypeInfo(str),
            ),
            (
                "source_code_url",
                "SourceCodeUrl",
                TypeInfo(str),
            ),
        ]

    # The application Amazon Resource Name (ARN).
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time this resource was created.
    creation_time: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of parameter types supported by the application.
    parameter_definitions: typing.List["ParameterDefinition"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    # The semantic version of the application:

    # <https://semver.org/>
    semantic_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A link to the packaged AWS SAM template of your application.
    template_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A link to a public repository for the source code of your application.
    source_code_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class VersionSummary(ShapeBase):
    """
    An application version summary.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
            (
                "creation_time",
                "CreationTime",
                TypeInfo(str),
            ),
            (
                "semantic_version",
                "SemanticVersion",
                TypeInfo(str),
            ),
            (
                "source_code_url",
                "SourceCodeUrl",
                TypeInfo(str),
            ),
        ]

    # The application Amazon Resource Name (ARN).
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time this resource was created.
    creation_time: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The semantic version of the application:

    # <https://semver.org/>
    semantic_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A link to a public repository for the source code of your application.
    source_code_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )
