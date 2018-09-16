import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


@dataclasses.dataclass
class AccountSettings(ShapeBase):
    """
    A container for account-level settings within AWS Device Farm.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "aws_account_number",
                "awsAccountNumber",
                TypeInfo(str),
            ),
            (
                "unmetered_devices",
                "unmeteredDevices",
                TypeInfo(typing.Dict[typing.Union[str, DevicePlatform], int]),
            ),
            (
                "unmetered_remote_access_devices",
                "unmeteredRemoteAccessDevices",
                TypeInfo(typing.Dict[typing.Union[str, DevicePlatform], int]),
            ),
            (
                "max_job_timeout_minutes",
                "maxJobTimeoutMinutes",
                TypeInfo(int),
            ),
            (
                "trial_minutes",
                "trialMinutes",
                TypeInfo(TrialMinutes),
            ),
            (
                "max_slots",
                "maxSlots",
                TypeInfo(typing.Dict[str, int]),
            ),
            (
                "default_job_timeout_minutes",
                "defaultJobTimeoutMinutes",
                TypeInfo(int),
            ),
            (
                "skip_app_resign",
                "skipAppResign",
                TypeInfo(bool),
            ),
        ]

    # The AWS account number specified in the `AccountSettings` container.
    aws_account_number: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Returns the unmetered devices you have purchased or want to purchase.
    unmetered_devices: typing.Dict[typing.Union[str, "DevicePlatform"], int
                                  ] = dataclasses.field(
                                      default=ShapeBase.NOT_SET,
                                  )

    # Returns the unmetered remote access devices you have purchased or want to
    # purchase.
    unmetered_remote_access_devices: typing.Dict[
        typing.Union[str, "DevicePlatform"], int] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # The maximum number of minutes a test run will execute before it times out.
    max_job_timeout_minutes: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about an AWS account's usage of free trial device minutes.
    trial_minutes: "TrialMinutes" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of device slots that the AWS account can purchase. Each
    # maximum is expressed as an `offering-id:number` pair, where the `offering-
    # id` represents one of the IDs returned by the `ListOfferings` command.
    max_slots: typing.Dict[str, int] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The default number of minutes (at the account level) a test run will
    # execute before it times out. Default value is 60 minutes.
    default_job_timeout_minutes: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When set to `true`, for private devices, Device Farm will not sign your app
    # again. For public devices, Device Farm always signs your apps again and
    # this parameter has no effect.

    # For more information about how Device Farm re-signs your app(s), see [Do
    # you modify my app?](https://aws.amazon.com/device-farm/faq/) in the _AWS
    # Device Farm FAQs_.
    skip_app_resign: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ArgumentException(ShapeBase):
    """
    An invalid argument was specified.
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

    # Any additional information about the exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Artifact(ShapeBase):
    """
    Represents the output of a test. Examples of artifacts include logs and
    screenshots.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "type",
                "type",
                TypeInfo(typing.Union[str, ArtifactType]),
            ),
            (
                "extension",
                "extension",
                TypeInfo(str),
            ),
            (
                "url",
                "url",
                TypeInfo(str),
            ),
        ]

    # The artifact's ARN.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The artifact's name.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The artifact's type.

    # Allowed values include the following:

    #   * UNKNOWN: An unknown type.

    #   * SCREENSHOT: The screenshot type.

    #   * DEVICE_LOG: The device log type.

    #   * MESSAGE_LOG: The message log type.

    #   * RESULT_LOG: The result log type.

    #   * SERVICE_LOG: The service log type.

    #   * WEBKIT_LOG: The web kit log type.

    #   * INSTRUMENTATION_OUTPUT: The instrumentation type.

    #   * EXERCISER_MONKEY_OUTPUT: For Android, the artifact (log) generated by an Android fuzz test.

    #   * CALABASH_JSON_OUTPUT: The Calabash JSON output type.

    #   * CALABASH_PRETTY_OUTPUT: The Calabash pretty output type.

    #   * CALABASH_STANDARD_OUTPUT: The Calabash standard output type.

    #   * CALABASH_JAVA_XML_OUTPUT: The Calabash Java XML output type.

    #   * AUTOMATION_OUTPUT: The automation output type.

    #   * APPIUM_SERVER_OUTPUT: The Appium server output type.

    #   * APPIUM_JAVA_OUTPUT: The Appium Java output type.

    #   * APPIUM_JAVA_XML_OUTPUT: The Appium Java XML output type.

    #   * APPIUM_PYTHON_OUTPUT: The Appium Python output type.

    #   * APPIUM_PYTHON_XML_OUTPUT: The Appium Python XML output type.

    #   * EXPLORER_EVENT_LOG: The Explorer event log output type.

    #   * EXPLORER_SUMMARY_LOG: The Explorer summary log output type.

    #   * APPLICATION_CRASH_REPORT: The application crash report output type.

    #   * XCTEST_LOG: The XCode test output type.
    type: typing.Union[str, "ArtifactType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The artifact's file extension.
    extension: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The pre-signed Amazon S3 URL that can be used with a corresponding GET
    # request to download the artifact's file.
    url: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class ArtifactCategory(str):
    SCREENSHOT = "SCREENSHOT"
    FILE = "FILE"
    LOG = "LOG"


class ArtifactType(str):
    UNKNOWN = "UNKNOWN"
    SCREENSHOT = "SCREENSHOT"
    DEVICE_LOG = "DEVICE_LOG"
    MESSAGE_LOG = "MESSAGE_LOG"
    VIDEO_LOG = "VIDEO_LOG"
    RESULT_LOG = "RESULT_LOG"
    SERVICE_LOG = "SERVICE_LOG"
    WEBKIT_LOG = "WEBKIT_LOG"
    INSTRUMENTATION_OUTPUT = "INSTRUMENTATION_OUTPUT"
    EXERCISER_MONKEY_OUTPUT = "EXERCISER_MONKEY_OUTPUT"
    CALABASH_JSON_OUTPUT = "CALABASH_JSON_OUTPUT"
    CALABASH_PRETTY_OUTPUT = "CALABASH_PRETTY_OUTPUT"
    CALABASH_STANDARD_OUTPUT = "CALABASH_STANDARD_OUTPUT"
    CALABASH_JAVA_XML_OUTPUT = "CALABASH_JAVA_XML_OUTPUT"
    AUTOMATION_OUTPUT = "AUTOMATION_OUTPUT"
    APPIUM_SERVER_OUTPUT = "APPIUM_SERVER_OUTPUT"
    APPIUM_JAVA_OUTPUT = "APPIUM_JAVA_OUTPUT"
    APPIUM_JAVA_XML_OUTPUT = "APPIUM_JAVA_XML_OUTPUT"
    APPIUM_PYTHON_OUTPUT = "APPIUM_PYTHON_OUTPUT"
    APPIUM_PYTHON_XML_OUTPUT = "APPIUM_PYTHON_XML_OUTPUT"
    EXPLORER_EVENT_LOG = "EXPLORER_EVENT_LOG"
    EXPLORER_SUMMARY_LOG = "EXPLORER_SUMMARY_LOG"
    APPLICATION_CRASH_REPORT = "APPLICATION_CRASH_REPORT"
    XCTEST_LOG = "XCTEST_LOG"
    VIDEO = "VIDEO"
    CUSTOMER_ARTIFACT = "CUSTOMER_ARTIFACT"
    CUSTOMER_ARTIFACT_LOG = "CUSTOMER_ARTIFACT_LOG"
    TESTSPEC_OUTPUT = "TESTSPEC_OUTPUT"


class BillingMethod(str):
    METERED = "METERED"
    UNMETERED = "UNMETERED"


@dataclasses.dataclass
class CPU(ShapeBase):
    """
    Represents the amount of CPU that an app is using on a physical device.

    Note that this does not represent system-wide CPU usage.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "frequency",
                "frequency",
                TypeInfo(str),
            ),
            (
                "architecture",
                "architecture",
                TypeInfo(str),
            ),
            (
                "clock",
                "clock",
                TypeInfo(float),
            ),
        ]

    # The CPU's frequency.
    frequency: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The CPU's architecture, for example x86 or ARM.
    architecture: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The clock speed of the device's CPU, expressed in hertz (Hz). For example,
    # a 1.2 GHz CPU is expressed as 1200000000.
    clock: float = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Counters(ShapeBase):
    """
    Represents entity counters.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "total",
                "total",
                TypeInfo(int),
            ),
            (
                "passed",
                "passed",
                TypeInfo(int),
            ),
            (
                "failed",
                "failed",
                TypeInfo(int),
            ),
            (
                "warned",
                "warned",
                TypeInfo(int),
            ),
            (
                "errored",
                "errored",
                TypeInfo(int),
            ),
            (
                "stopped",
                "stopped",
                TypeInfo(int),
            ),
            (
                "skipped",
                "skipped",
                TypeInfo(int),
            ),
        ]

    # The total number of entities.
    total: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of passed entities.
    passed: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of failed entities.
    failed: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of warned entities.
    warned: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of errored entities.
    errored: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of stopped entities.
    stopped: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of skipped entities.
    skipped: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateDevicePoolRequest(ShapeBase):
    """
    Represents a request to the create device pool operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "project_arn",
                "projectArn",
                TypeInfo(str),
            ),
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "rules",
                "rules",
                TypeInfo(typing.List[Rule]),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
        ]

    # The ARN of the project for the device pool.
    project_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The device pool's name.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The device pool's rules.
    rules: typing.List["Rule"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The device pool's description.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateDevicePoolResult(OutputShapeBase):
    """
    Represents the result of a create device pool request.
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
                "device_pool",
                "devicePool",
                TypeInfo(DevicePool),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The newly created device pool.
    device_pool: "DevicePool" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateInstanceProfileRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
            (
                "package_cleanup",
                "packageCleanup",
                TypeInfo(bool),
            ),
            (
                "exclude_app_packages_from_cleanup",
                "excludeAppPackagesFromCleanup",
                TypeInfo(typing.List[str]),
            ),
            (
                "reboot_after_use",
                "rebootAfterUse",
                TypeInfo(bool),
            ),
        ]

    # The name of your instance profile.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of your instance profile.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When set to `true`, Device Farm will remove app packages after a test run.
    # The default value is `false` for private devices.
    package_cleanup: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of strings specifying the list of app packages that should not be
    # cleaned up from the device after a test run is over.

    # The list of packages is only considered if you set `packageCleanup` to
    # `true`.
    exclude_app_packages_from_cleanup: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When set to `true`, Device Farm will reboot the instance after a test run.
    # The default value is `true`.
    reboot_after_use: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateInstanceProfileResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "instance_profile",
                "instanceProfile",
                TypeInfo(InstanceProfile),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An object containing information about your instance profile.
    instance_profile: "InstanceProfile" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateNetworkProfileRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "project_arn",
                "projectArn",
                TypeInfo(str),
            ),
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
            (
                "type",
                "type",
                TypeInfo(typing.Union[str, NetworkProfileType]),
            ),
            (
                "uplink_bandwidth_bits",
                "uplinkBandwidthBits",
                TypeInfo(int),
            ),
            (
                "downlink_bandwidth_bits",
                "downlinkBandwidthBits",
                TypeInfo(int),
            ),
            (
                "uplink_delay_ms",
                "uplinkDelayMs",
                TypeInfo(int),
            ),
            (
                "downlink_delay_ms",
                "downlinkDelayMs",
                TypeInfo(int),
            ),
            (
                "uplink_jitter_ms",
                "uplinkJitterMs",
                TypeInfo(int),
            ),
            (
                "downlink_jitter_ms",
                "downlinkJitterMs",
                TypeInfo(int),
            ),
            (
                "uplink_loss_percent",
                "uplinkLossPercent",
                TypeInfo(int),
            ),
            (
                "downlink_loss_percent",
                "downlinkLossPercent",
                TypeInfo(int),
            ),
        ]

    # The Amazon Resource Name (ARN) of the project for which you want to create
    # a network profile.
    project_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name you wish to specify for the new network profile.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the network profile.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of network profile you wish to create. Valid values are listed
    # below.
    type: typing.Union[str, "NetworkProfileType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The data throughput rate in bits per second, as an integer from 0 to
    # 104857600.
    uplink_bandwidth_bits: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The data throughput rate in bits per second, as an integer from 0 to
    # 104857600.
    downlink_bandwidth_bits: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Delay time for all packets to destination in milliseconds as an integer
    # from 0 to 2000.
    uplink_delay_ms: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Delay time for all packets to destination in milliseconds as an integer
    # from 0 to 2000.
    downlink_delay_ms: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Time variation in the delay of received packets in milliseconds as an
    # integer from 0 to 2000.
    uplink_jitter_ms: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Time variation in the delay of received packets in milliseconds as an
    # integer from 0 to 2000.
    downlink_jitter_ms: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Proportion of transmitted packets that fail to arrive from 0 to 100
    # percent.
    uplink_loss_percent: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Proportion of received packets that fail to arrive from 0 to 100 percent.
    downlink_loss_percent: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateNetworkProfileResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "network_profile",
                "networkProfile",
                TypeInfo(NetworkProfile),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The network profile that is returned by the create network profile request.
    network_profile: "NetworkProfile" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateProjectRequest(ShapeBase):
    """
    Represents a request to the create project operation.
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
                "default_job_timeout_minutes",
                "defaultJobTimeoutMinutes",
                TypeInfo(int),
            ),
        ]

    # The project's name.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Sets the execution timeout value (in minutes) for a project. All test runs
    # in this project will use the specified execution timeout value unless
    # overridden when scheduling a run.
    default_job_timeout_minutes: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateProjectResult(OutputShapeBase):
    """
    Represents the result of a create project request.
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
                "project",
                "project",
                TypeInfo(Project),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The newly created project.
    project: "Project" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateRemoteAccessSessionConfiguration(ShapeBase):
    """
    Configuration settings for a remote access session, including billing method.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "billing_method",
                "billingMethod",
                TypeInfo(typing.Union[str, BillingMethod]),
            ),
            (
                "vpce_configuration_arns",
                "vpceConfigurationArns",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The billing method for the remote access session.
    billing_method: typing.Union[str, "BillingMethod"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of Amazon Resource Names (ARNs) included in the VPC endpoint
    # configuration.
    vpce_configuration_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateRemoteAccessSessionRequest(ShapeBase):
    """
    Creates and submits a request to start a remote access session.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "project_arn",
                "projectArn",
                TypeInfo(str),
            ),
            (
                "device_arn",
                "deviceArn",
                TypeInfo(str),
            ),
            (
                "instance_arn",
                "instanceArn",
                TypeInfo(str),
            ),
            (
                "ssh_public_key",
                "sshPublicKey",
                TypeInfo(str),
            ),
            (
                "remote_debug_enabled",
                "remoteDebugEnabled",
                TypeInfo(bool),
            ),
            (
                "remote_record_enabled",
                "remoteRecordEnabled",
                TypeInfo(bool),
            ),
            (
                "remote_record_app_arn",
                "remoteRecordAppArn",
                TypeInfo(str),
            ),
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "client_id",
                "clientId",
                TypeInfo(str),
            ),
            (
                "configuration",
                "configuration",
                TypeInfo(CreateRemoteAccessSessionConfiguration),
            ),
            (
                "interaction_mode",
                "interactionMode",
                TypeInfo(typing.Union[str, InteractionMode]),
            ),
            (
                "skip_app_resign",
                "skipAppResign",
                TypeInfo(bool),
            ),
        ]

    # The Amazon Resource Name (ARN) of the project for which you want to create
    # a remote access session.
    project_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the device for which you want to create a
    # remote access session.
    device_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the device instance for which you want to
    # create a remote access session.
    instance_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The public key of the `ssh` key pair you want to use for connecting to
    # remote devices in your remote debugging session. This is only required if
    # `remoteDebugEnabled` is set to `true`.
    ssh_public_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Set to `true` if you want to access devices remotely for debugging in your
    # remote access session.
    remote_debug_enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Set to `true` to enable remote recording for the remote access session.
    remote_record_enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) for the app to be recorded in the remote
    # access session.
    remote_record_app_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the remote access session that you wish to create.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique identifier for the client. If you want access to multiple devices on
    # the same client, you should pass the same `clientId` value in each call to
    # `CreateRemoteAccessSession`. This is required only if `remoteDebugEnabled`
    # is set to `true`.
    client_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The configuration information for the remote access session request.
    configuration: "CreateRemoteAccessSessionConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The interaction mode of the remote access session. Valid values are:

    #   * INTERACTIVE: You can interact with the iOS device by viewing, touching, and rotating the screen. You **cannot** run XCUITest framework-based tests in this mode.

    #   * NO_VIDEO: You are connected to the device but cannot interact with it or view the screen. This mode has the fastest test execution speed. You **can** run XCUITest framework-based tests in this mode.

    #   * VIDEO_ONLY: You can view the screen but cannot touch or rotate it. You **can** run XCUITest framework-based tests and watch the screen in this mode.
    interaction_mode: typing.Union[str, "InteractionMode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When set to `true`, for private devices, Device Farm will not sign your app
    # again. For public devices, Device Farm always signs your apps again and
    # this parameter has no effect.

    # For more information about how Device Farm re-signs your app(s), see [Do
    # you modify my app?](https://aws.amazon.com/device-farm/faq/) in the _AWS
    # Device Farm FAQs_.
    skip_app_resign: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateRemoteAccessSessionResult(OutputShapeBase):
    """
    Represents the server response from a request to create a remote access session.
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
                "remote_access_session",
                "remoteAccessSession",
                TypeInfo(RemoteAccessSession),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A container that describes the remote access session when the request to
    # create a remote access session is sent.
    remote_access_session: "RemoteAccessSession" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateUploadRequest(ShapeBase):
    """
    Represents a request to the create upload operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "project_arn",
                "projectArn",
                TypeInfo(str),
            ),
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "type",
                "type",
                TypeInfo(typing.Union[str, UploadType]),
            ),
            (
                "content_type",
                "contentType",
                TypeInfo(str),
            ),
        ]

    # The ARN of the project for the upload.
    project_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The upload's file name. The name should not contain the '/' character. If
    # uploading an iOS app, the file name needs to end with the `.ipa` extension.
    # If uploading an Android app, the file name needs to end with the `.apk`
    # extension. For all others, the file name must end with the `.zip` file
    # extension.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The upload's upload type.

    # Must be one of the following values:

    #   * ANDROID_APP: An Android upload.

    #   * IOS_APP: An iOS upload.

    #   * WEB_APP: A web application upload.

    #   * EXTERNAL_DATA: An external data upload.

    #   * APPIUM_JAVA_JUNIT_TEST_PACKAGE: An Appium Java JUnit test package upload.

    #   * APPIUM_JAVA_TESTNG_TEST_PACKAGE: An Appium Java TestNG test package upload.

    #   * APPIUM_PYTHON_TEST_PACKAGE: An Appium Python test package upload.

    #   * APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE: An Appium Java JUnit test package upload.

    #   * APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE: An Appium Java TestNG test package upload.

    #   * APPIUM_WEB_PYTHON_TEST_PACKAGE: An Appium Python test package upload.

    #   * CALABASH_TEST_PACKAGE: A Calabash test package upload.

    #   * INSTRUMENTATION_TEST_PACKAGE: An instrumentation upload.

    #   * UIAUTOMATION_TEST_PACKAGE: A uiautomation test package upload.

    #   * UIAUTOMATOR_TEST_PACKAGE: A uiautomator test package upload.

    #   * XCTEST_TEST_PACKAGE: An XCode test package upload.

    #   * XCTEST_UI_TEST_PACKAGE: An XCode UI test package upload.

    # **Note** If you call `CreateUpload` with `WEB_APP` specified, AWS Device
    # Farm throws an `ArgumentException` error.
    type: typing.Union[str, "UploadType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The upload's content type (for example, "application/octet-stream").
    content_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateUploadResult(OutputShapeBase):
    """
    Represents the result of a create upload request.
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
                "upload",
                "upload",
                TypeInfo(Upload),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The newly created upload.
    upload: "Upload" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateVPCEConfigurationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "vpce_configuration_name",
                "vpceConfigurationName",
                TypeInfo(str),
            ),
            (
                "vpce_service_name",
                "vpceServiceName",
                TypeInfo(str),
            ),
            (
                "service_dns_name",
                "serviceDnsName",
                TypeInfo(str),
            ),
            (
                "vpce_configuration_description",
                "vpceConfigurationDescription",
                TypeInfo(str),
            ),
        ]

    # The friendly name you give to your VPC endpoint configuration, to manage
    # your configurations more easily.
    vpce_configuration_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the VPC endpoint service running inside your AWS account that
    # you want Device Farm to test.
    vpce_service_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The DNS name of the service running in your VPC that you want Device Farm
    # to test.
    service_dns_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional description, providing more details about your VPC endpoint
    # configuration.
    vpce_configuration_description: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateVPCEConfigurationResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "vpce_configuration",
                "vpceConfiguration",
                TypeInfo(VPCEConfiguration),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An object containing information about your VPC endpoint configuration.
    vpce_configuration: "VPCEConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class CurrencyCode(str):
    USD = "USD"


@dataclasses.dataclass
class CustomerArtifactPaths(ShapeBase):
    """
    A JSON object specifying the paths where the artifacts generated by the
    customer's tests, on the device or in the test environment, will be pulled from.

    Specify `deviceHostPaths` and optionally specify either `iosPaths` or
    `androidPaths`.

    For web app tests, you can specify both `iosPaths` and `androidPaths`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ios_paths",
                "iosPaths",
                TypeInfo(typing.List[str]),
            ),
            (
                "android_paths",
                "androidPaths",
                TypeInfo(typing.List[str]),
            ),
            (
                "device_host_paths",
                "deviceHostPaths",
                TypeInfo(typing.List[str]),
            ),
        ]

    # Comma-separated list of paths on the iOS device where the artifacts
    # generated by the customer's tests will be pulled from.
    ios_paths: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Comma-separated list of paths on the Android device where the artifacts
    # generated by the customer's tests will be pulled from.
    android_paths: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Comma-separated list of paths in the test execution environment where the
    # artifacts generated by the customer's tests will be pulled from.
    device_host_paths: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteDevicePoolRequest(ShapeBase):
    """
    Represents a request to the delete device pool operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
        ]

    # Represents the Amazon Resource Name (ARN) of the Device Farm device pool
    # you wish to delete.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteDevicePoolResult(OutputShapeBase):
    """
    Represents the result of a delete device pool request.
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
class DeleteInstanceProfileRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the instance profile you are requesting
    # to delete.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteInstanceProfileResult(OutputShapeBase):
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
class DeleteNetworkProfileRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the network profile you want to delete.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteNetworkProfileResult(OutputShapeBase):
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
    """
    Represents a request to the delete project operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
        ]

    # Represents the Amazon Resource Name (ARN) of the Device Farm project you
    # wish to delete.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteProjectResult(OutputShapeBase):
    """
    Represents the result of a delete project request.
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
class DeleteRemoteAccessSessionRequest(ShapeBase):
    """
    Represents the request to delete the specified remote access session.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the sesssion for which you want to delete
    # remote access.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteRemoteAccessSessionResult(OutputShapeBase):
    """
    The response from the server when a request is made to delete the remote access
    session.
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
class DeleteRunRequest(ShapeBase):
    """
    Represents a request to the delete run operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) for the run you wish to delete.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteRunResult(OutputShapeBase):
    """
    Represents the result of a delete run request.
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
class DeleteUploadRequest(ShapeBase):
    """
    Represents a request to the delete upload operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
        ]

    # Represents the Amazon Resource Name (ARN) of the Device Farm upload you
    # wish to delete.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteUploadResult(OutputShapeBase):
    """
    Represents the result of a delete upload request.
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
class DeleteVPCEConfigurationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the VPC endpoint configuration you want
    # to delete.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteVPCEConfigurationResult(OutputShapeBase):
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
class Device(ShapeBase):
    """
    Represents a device type that an app is tested against.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "manufacturer",
                "manufacturer",
                TypeInfo(str),
            ),
            (
                "model",
                "model",
                TypeInfo(str),
            ),
            (
                "model_id",
                "modelId",
                TypeInfo(str),
            ),
            (
                "form_factor",
                "formFactor",
                TypeInfo(typing.Union[str, DeviceFormFactor]),
            ),
            (
                "platform",
                "platform",
                TypeInfo(typing.Union[str, DevicePlatform]),
            ),
            (
                "os",
                "os",
                TypeInfo(str),
            ),
            (
                "cpu",
                "cpu",
                TypeInfo(CPU),
            ),
            (
                "resolution",
                "resolution",
                TypeInfo(Resolution),
            ),
            (
                "heap_size",
                "heapSize",
                TypeInfo(int),
            ),
            (
                "memory",
                "memory",
                TypeInfo(int),
            ),
            (
                "image",
                "image",
                TypeInfo(str),
            ),
            (
                "carrier",
                "carrier",
                TypeInfo(str),
            ),
            (
                "radio",
                "radio",
                TypeInfo(str),
            ),
            (
                "remote_access_enabled",
                "remoteAccessEnabled",
                TypeInfo(bool),
            ),
            (
                "remote_debug_enabled",
                "remoteDebugEnabled",
                TypeInfo(bool),
            ),
            (
                "fleet_type",
                "fleetType",
                TypeInfo(str),
            ),
            (
                "fleet_name",
                "fleetName",
                TypeInfo(str),
            ),
            (
                "instances",
                "instances",
                TypeInfo(typing.List[DeviceInstance]),
            ),
        ]

    # The device's ARN.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The device's display name.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The device's manufacturer name.
    manufacturer: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The device's model name.
    model: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The device's model ID.
    model_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The device's form factor.

    # Allowed values include:

    #   * PHONE: The phone form factor.

    #   * TABLET: The tablet form factor.
    form_factor: typing.Union[str, "DeviceFormFactor"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The device's platform.

    # Allowed values include:

    #   * ANDROID: The Android platform.

    #   * IOS: The iOS platform.
    platform: typing.Union[str, "DevicePlatform"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The device's operating system type.
    os: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the device's CPU.
    cpu: "CPU" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The resolution of the device.
    resolution: "Resolution" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The device's heap size, expressed in bytes.
    heap_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The device's total memory size, expressed in bytes.
    memory: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The device's image name.
    image: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The device's carrier.
    carrier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The device's radio.
    radio: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies whether remote access has been enabled for the specified device.
    remote_access_enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This flag is set to `true` if remote debugging is enabled for the device.
    remote_debug_enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of fleet to which this device belongs. Possible values for fleet
    # type are PRIVATE and PUBLIC.
    fleet_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the fleet to which this device belongs.
    fleet_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The instances belonging to this device.
    instances: typing.List["DeviceInstance"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class DeviceAttribute(str):
    ARN = "ARN"
    PLATFORM = "PLATFORM"
    FORM_FACTOR = "FORM_FACTOR"
    MANUFACTURER = "MANUFACTURER"
    REMOTE_ACCESS_ENABLED = "REMOTE_ACCESS_ENABLED"
    REMOTE_DEBUG_ENABLED = "REMOTE_DEBUG_ENABLED"
    APPIUM_VERSION = "APPIUM_VERSION"
    INSTANCE_ARN = "INSTANCE_ARN"
    INSTANCE_LABELS = "INSTANCE_LABELS"
    FLEET_TYPE = "FLEET_TYPE"


class DeviceFormFactor(str):
    PHONE = "PHONE"
    TABLET = "TABLET"


@dataclasses.dataclass
class DeviceInstance(ShapeBase):
    """
    Represents the device instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
            (
                "device_arn",
                "deviceArn",
                TypeInfo(str),
            ),
            (
                "labels",
                "labels",
                TypeInfo(typing.List[str]),
            ),
            (
                "status",
                "status",
                TypeInfo(typing.Union[str, InstanceStatus]),
            ),
            (
                "udid",
                "udid",
                TypeInfo(str),
            ),
            (
                "instance_profile",
                "instanceProfile",
                TypeInfo(InstanceProfile),
            ),
        ]

    # The Amazon Resource Name (ARN) of the device instance.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the device.
    device_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of strings describing the device instance.
    labels: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the device instance. Valid values are listed below.
    status: typing.Union[str, "InstanceStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Unique device identifier for the device instance.
    udid: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A object containing information about the instance profile.
    instance_profile: "InstanceProfile" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeviceMinutes(ShapeBase):
    """
    Represents the total (metered or unmetered) minutes used by the resource to run
    tests. Contains the sum of minutes consumed by all children.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "total",
                "total",
                TypeInfo(float),
            ),
            (
                "metered",
                "metered",
                TypeInfo(float),
            ),
            (
                "unmetered",
                "unmetered",
                TypeInfo(float),
            ),
        ]

    # When specified, represents the total minutes used by the resource to run
    # tests.
    total: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When specified, represents only the sum of metered minutes used by the
    # resource to run tests.
    metered: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When specified, represents only the sum of unmetered minutes used by the
    # resource to run tests.
    unmetered: float = dataclasses.field(default=ShapeBase.NOT_SET, )


class DevicePlatform(str):
    ANDROID = "ANDROID"
    IOS = "IOS"


@dataclasses.dataclass
class DevicePool(ShapeBase):
    """
    Represents a collection of device types.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
            (
                "type",
                "type",
                TypeInfo(typing.Union[str, DevicePoolType]),
            ),
            (
                "rules",
                "rules",
                TypeInfo(typing.List[Rule]),
            ),
        ]

    # The device pool's ARN.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The device pool's name.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The device pool's description.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The device pool's type.

    # Allowed values include:

    #   * CURATED: A device pool that is created and managed by AWS Device Farm.

    #   * PRIVATE: A device pool that is created and managed by the device pool developer.
    type: typing.Union[str, "DevicePoolType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the device pool's rules.
    rules: typing.List["Rule"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DevicePoolCompatibilityResult(ShapeBase):
    """
    Represents a device pool compatibility result.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "device",
                "device",
                TypeInfo(Device),
            ),
            (
                "compatible",
                "compatible",
                TypeInfo(bool),
            ),
            (
                "incompatibility_messages",
                "incompatibilityMessages",
                TypeInfo(typing.List[IncompatibilityMessage]),
            ),
        ]

    # The device (phone or tablet) that you wish to return information about.
    device: "Device" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Whether the result was compatible with the device pool.
    compatible: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the compatibility.
    incompatibility_messages: typing.List["IncompatibilityMessage"
                                         ] = dataclasses.field(
                                             default=ShapeBase.NOT_SET,
                                         )


class DevicePoolType(str):
    CURATED = "CURATED"
    PRIVATE = "PRIVATE"


@dataclasses.dataclass
class ExecutionConfiguration(ShapeBase):
    """
    Represents configuration information about a test run, such as the execution
    timeout (in minutes).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_timeout_minutes",
                "jobTimeoutMinutes",
                TypeInfo(int),
            ),
            (
                "accounts_cleanup",
                "accountsCleanup",
                TypeInfo(bool),
            ),
            (
                "app_packages_cleanup",
                "appPackagesCleanup",
                TypeInfo(bool),
            ),
            (
                "video_capture",
                "videoCapture",
                TypeInfo(bool),
            ),
            (
                "skip_app_resign",
                "skipAppResign",
                TypeInfo(bool),
            ),
        ]

    # The number of minutes a test run will execute before it times out.
    job_timeout_minutes: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # True if account cleanup is enabled at the beginning of the test; otherwise,
    # false.
    accounts_cleanup: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # True if app package cleanup is enabled at the beginning of the test;
    # otherwise, false.
    app_packages_cleanup: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Set to true to enable video capture; otherwise, set to false. The default
    # is true.
    video_capture: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When set to `true`, for private devices, Device Farm will not sign your app
    # again. For public devices, Device Farm always signs your apps again and
    # this parameter has no effect.

    # For more information about how Device Farm re-signs your app(s), see [Do
    # you modify my app?](https://aws.amazon.com/device-farm/faq/) in the _AWS
    # Device Farm FAQs_.
    skip_app_resign: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


class ExecutionResult(str):
    PENDING = "PENDING"
    PASSED = "PASSED"
    WARNED = "WARNED"
    FAILED = "FAILED"
    SKIPPED = "SKIPPED"
    ERRORED = "ERRORED"
    STOPPED = "STOPPED"


class ExecutionResultCode(str):
    PARSING_FAILED = "PARSING_FAILED"
    VPC_ENDPOINT_SETUP_FAILED = "VPC_ENDPOINT_SETUP_FAILED"


class ExecutionStatus(str):
    PENDING = "PENDING"
    PENDING_CONCURRENCY = "PENDING_CONCURRENCY"
    PENDING_DEVICE = "PENDING_DEVICE"
    PROCESSING = "PROCESSING"
    SCHEDULING = "SCHEDULING"
    PREPARING = "PREPARING"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    STOPPING = "STOPPING"


@dataclasses.dataclass
class GetAccountSettingsRequest(ShapeBase):
    """
    Represents the request sent to retrieve the account settings.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class GetAccountSettingsResult(OutputShapeBase):
    """
    Represents the account settings return values from the `GetAccountSettings`
    request.
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
                "account_settings",
                "accountSettings",
                TypeInfo(AccountSettings),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The account settings.
    account_settings: "AccountSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetDeviceInstanceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the instance you're requesting
    # information about.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDeviceInstanceResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "device_instance",
                "deviceInstance",
                TypeInfo(DeviceInstance),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An object containing information about your device instance.
    device_instance: "DeviceInstance" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetDevicePoolCompatibilityRequest(ShapeBase):
    """
    Represents a request to the get device pool compatibility operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "device_pool_arn",
                "devicePoolArn",
                TypeInfo(str),
            ),
            (
                "app_arn",
                "appArn",
                TypeInfo(str),
            ),
            (
                "test_type",
                "testType",
                TypeInfo(typing.Union[str, TestType]),
            ),
            (
                "test",
                "test",
                TypeInfo(ScheduleRunTest),
            ),
            (
                "configuration",
                "configuration",
                TypeInfo(ScheduleRunConfiguration),
            ),
        ]

    # The device pool's ARN.
    device_pool_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the app that is associated with the specified device pool.
    app_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The test type for the specified device pool.

    # Allowed values include the following:

    #   * BUILTIN_FUZZ: The built-in fuzz type.

    #   * BUILTIN_EXPLORER: For Android, an app explorer that will traverse an Android app, interacting with it and capturing screenshots at the same time.

    #   * APPIUM_JAVA_JUNIT: The Appium Java JUnit type.

    #   * APPIUM_JAVA_TESTNG: The Appium Java TestNG type.

    #   * APPIUM_PYTHON: The Appium Python type.

    #   * APPIUM_WEB_JAVA_JUNIT: The Appium Java JUnit type for Web apps.

    #   * APPIUM_WEB_JAVA_TESTNG: The Appium Java TestNG type for Web apps.

    #   * APPIUM_WEB_PYTHON: The Appium Python type for Web apps.

    #   * CALABASH: The Calabash type.

    #   * INSTRUMENTATION: The Instrumentation type.

    #   * UIAUTOMATION: The uiautomation type.

    #   * UIAUTOMATOR: The uiautomator type.

    #   * XCTEST: The XCode test type.

    #   * XCTEST_UI: The XCode UI test type.
    test_type: typing.Union[str, "TestType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the uploaded test to be run against the device pool.
    test: "ScheduleRunTest" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An object containing information about the settings for a run.
    configuration: "ScheduleRunConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetDevicePoolCompatibilityResult(OutputShapeBase):
    """
    Represents the result of describe device pool compatibility request.
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
                "compatible_devices",
                "compatibleDevices",
                TypeInfo(typing.List[DevicePoolCompatibilityResult]),
            ),
            (
                "incompatible_devices",
                "incompatibleDevices",
                TypeInfo(typing.List[DevicePoolCompatibilityResult]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about compatible devices.
    compatible_devices: typing.List["DevicePoolCompatibilityResult"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # Information about incompatible devices.
    incompatible_devices: typing.List["DevicePoolCompatibilityResult"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )


@dataclasses.dataclass
class GetDevicePoolRequest(ShapeBase):
    """
    Represents a request to the get device pool operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
        ]

    # The device pool's ARN.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDevicePoolResult(OutputShapeBase):
    """
    Represents the result of a get device pool request.
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
                "device_pool",
                "devicePool",
                TypeInfo(DevicePool),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An object containing information about the requested device pool.
    device_pool: "DevicePool" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDeviceRequest(ShapeBase):
    """
    Represents a request to the get device request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
        ]

    # The device type's ARN.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDeviceResult(OutputShapeBase):
    """
    Represents the result of a get device request.
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
                "device",
                "device",
                TypeInfo(Device),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An object containing information about the requested device.
    device: "Device" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetInstanceProfileRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of your instance profile.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetInstanceProfileResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "instance_profile",
                "instanceProfile",
                TypeInfo(InstanceProfile),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An object containing information about your instance profile.
    instance_profile: "InstanceProfile" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetJobRequest(ShapeBase):
    """
    Represents a request to the get job operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
        ]

    # The job's ARN.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetJobResult(OutputShapeBase):
    """
    Represents the result of a get job request.
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
                "job",
                "job",
                TypeInfo(Job),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An object containing information about the requested job.
    job: "Job" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetNetworkProfileRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the network profile you want to return
    # information about.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetNetworkProfileResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "network_profile",
                "networkProfile",
                TypeInfo(NetworkProfile),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The network profile.
    network_profile: "NetworkProfile" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetOfferingStatusRequest(ShapeBase):
    """
    Represents the request to retrieve the offering status for the specified
    customer or account.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    # An identifier that was returned from the previous call to this operation,
    # which can be used to return the next set of items in the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetOfferingStatusResult(OutputShapeBase):
    """
    Returns the status result for a device offering.
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
                "current",
                "current",
                TypeInfo(typing.Dict[str, OfferingStatus]),
            ),
            (
                "next_period",
                "nextPeriod",
                TypeInfo(typing.Dict[str, OfferingStatus]),
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

    # When specified, gets the offering status for the current period.
    current: typing.Dict[str, "OfferingStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When specified, gets the offering status for the next period.
    next_period: typing.Dict[str, "OfferingStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An identifier that was returned from the previous call to this operation,
    # which can be used to return the next set of items in the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["GetOfferingStatusResult", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class GetProjectRequest(ShapeBase):
    """
    Represents a request to the get project operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
        ]

    # The project's ARN.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetProjectResult(OutputShapeBase):
    """
    Represents the result of a get project request.
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
                "project",
                "project",
                TypeInfo(Project),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The project you wish to get information about.
    project: "Project" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetRemoteAccessSessionRequest(ShapeBase):
    """
    Represents the request to get information about the specified remote access
    session.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the remote access session about which you
    # want to get session information.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetRemoteAccessSessionResult(OutputShapeBase):
    """
    Represents the response from the server that lists detailed information about
    the remote access session.
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
                "remote_access_session",
                "remoteAccessSession",
                TypeInfo(RemoteAccessSession),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A container that lists detailed information about the remote access
    # session.
    remote_access_session: "RemoteAccessSession" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetRunRequest(ShapeBase):
    """
    Represents a request to the get run operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
        ]

    # The run's ARN.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetRunResult(OutputShapeBase):
    """
    Represents the result of a get run request.
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
                "run",
                "run",
                TypeInfo(Run),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The run you wish to get results from.
    run: "Run" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetSuiteRequest(ShapeBase):
    """
    Represents a request to the get suite operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
        ]

    # The suite's ARN.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetSuiteResult(OutputShapeBase):
    """
    Represents the result of a get suite request.
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
                "suite",
                "suite",
                TypeInfo(Suite),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A collection of one or more tests.
    suite: "Suite" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetTestRequest(ShapeBase):
    """
    Represents a request to the get test operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
        ]

    # The test's ARN.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetTestResult(OutputShapeBase):
    """
    Represents the result of a get test request.
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
                "test",
                "test",
                TypeInfo(Test),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A test condition that is evaluated.
    test: "Test" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetUploadRequest(ShapeBase):
    """
    Represents a request to the get upload operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
        ]

    # The upload's ARN.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetUploadResult(OutputShapeBase):
    """
    Represents the result of a get upload request.
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
                "upload",
                "upload",
                TypeInfo(Upload),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An app or a set of one or more tests to upload or that have been uploaded.
    upload: "Upload" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetVPCEConfigurationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the VPC endpoint configuration you want
    # to describe.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetVPCEConfigurationResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "vpce_configuration",
                "vpceConfiguration",
                TypeInfo(VPCEConfiguration),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An object containing information about your VPC endpoint configuration.
    vpce_configuration: "VPCEConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class IdempotencyException(ShapeBase):
    """
    An entity with the same name already exists.
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

    # Any additional information about the exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class IncompatibilityMessage(ShapeBase):
    """
    Represents information about incompatibility.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
            (
                "type",
                "type",
                TypeInfo(typing.Union[str, DeviceAttribute]),
            ),
        ]

    # A message about the incompatibility.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of incompatibility.

    # Allowed values include:

    #   * ARN: The ARN.

    #   * FORM_FACTOR: The form factor (for example, phone or tablet).

    #   * MANUFACTURER: The manufacturer.

    #   * PLATFORM: The platform (for example, Android or iOS).

    #   * REMOTE_ACCESS_ENABLED: Whether the device is enabled for remote access.

    #   * APPIUM_VERSION: The Appium version for the test.
    type: typing.Union[str, "DeviceAttribute"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InstallToRemoteAccessSessionRequest(ShapeBase):
    """
    Represents the request to install an Android application (in .apk format) or an
    iOS application (in .ipa format) as part of a remote access session.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "remote_access_session_arn",
                "remoteAccessSessionArn",
                TypeInfo(str),
            ),
            (
                "app_arn",
                "appArn",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the remote access session about which you
    # are requesting information.
    remote_access_session_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the app about which you are requesting
    # information.
    app_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InstallToRemoteAccessSessionResult(OutputShapeBase):
    """
    Represents the response from the server after AWS Device Farm makes a request to
    install to a remote access session.
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
                "app_upload",
                "appUpload",
                TypeInfo(Upload),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An app to upload or that has been uploaded.
    app_upload: "Upload" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InstanceProfile(ShapeBase):
    """
    Represents the instance profile.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
            (
                "package_cleanup",
                "packageCleanup",
                TypeInfo(bool),
            ),
            (
                "exclude_app_packages_from_cleanup",
                "excludeAppPackagesFromCleanup",
                TypeInfo(typing.List[str]),
            ),
            (
                "reboot_after_use",
                "rebootAfterUse",
                TypeInfo(bool),
            ),
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the instance profile.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When set to `true`, Device Farm will remove app packages after a test run.
    # The default value is `false` for private devices.
    package_cleanup: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of strings specifying the list of app packages that should not be
    # cleaned up from the device after a test run is over.

    # The list of packages is only considered if you set `packageCleanup` to
    # `true`.
    exclude_app_packages_from_cleanup: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When set to `true`, Device Farm will reboot the instance after a test run.
    # The default value is `true`.
    reboot_after_use: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the instance profile.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the instance profile.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class InstanceStatus(str):
    IN_USE = "IN_USE"
    PREPARING = "PREPARING"
    AVAILABLE = "AVAILABLE"
    NOT_AVAILABLE = "NOT_AVAILABLE"


class InteractionMode(str):
    INTERACTIVE = "INTERACTIVE"
    NO_VIDEO = "NO_VIDEO"
    VIDEO_ONLY = "VIDEO_ONLY"


@dataclasses.dataclass
class InvalidOperationException(ShapeBase):
    """
    There was an error with the update request, or you do not have sufficient
    permissions to update this VPC endpoint configuration.
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

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Job(ShapeBase):
    """
    Represents a device.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "type",
                "type",
                TypeInfo(typing.Union[str, TestType]),
            ),
            (
                "created",
                "created",
                TypeInfo(datetime.datetime),
            ),
            (
                "status",
                "status",
                TypeInfo(typing.Union[str, ExecutionStatus]),
            ),
            (
                "result",
                "result",
                TypeInfo(typing.Union[str, ExecutionResult]),
            ),
            (
                "started",
                "started",
                TypeInfo(datetime.datetime),
            ),
            (
                "stopped",
                "stopped",
                TypeInfo(datetime.datetime),
            ),
            (
                "counters",
                "counters",
                TypeInfo(Counters),
            ),
            (
                "message",
                "message",
                TypeInfo(str),
            ),
            (
                "device",
                "device",
                TypeInfo(Device),
            ),
            (
                "instance_arn",
                "instanceArn",
                TypeInfo(str),
            ),
            (
                "device_minutes",
                "deviceMinutes",
                TypeInfo(DeviceMinutes),
            ),
            (
                "video_endpoint",
                "videoEndpoint",
                TypeInfo(str),
            ),
            (
                "video_capture",
                "videoCapture",
                TypeInfo(bool),
            ),
        ]

    # The job's ARN.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The job's name.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The job's type.

    # Allowed values include the following:

    #   * BUILTIN_FUZZ: The built-in fuzz type.

    #   * BUILTIN_EXPLORER: For Android, an app explorer that will traverse an Android app, interacting with it and capturing screenshots at the same time.

    #   * APPIUM_JAVA_JUNIT: The Appium Java JUnit type.

    #   * APPIUM_JAVA_TESTNG: The Appium Java TestNG type.

    #   * APPIUM_PYTHON: The Appium Python type.

    #   * APPIUM_WEB_JAVA_JUNIT: The Appium Java JUnit type for Web apps.

    #   * APPIUM_WEB_JAVA_TESTNG: The Appium Java TestNG type for Web apps.

    #   * APPIUM_WEB_PYTHON: The Appium Python type for Web apps.

    #   * CALABASH: The Calabash type.

    #   * INSTRUMENTATION: The Instrumentation type.

    #   * UIAUTOMATION: The uiautomation type.

    #   * UIAUTOMATOR: The uiautomator type.

    #   * XCTEST: The XCode test type.

    #   * XCTEST_UI: The XCode UI test type.
    type: typing.Union[str, "TestType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When the job was created.
    created: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The job's status.

    # Allowed values include:

    #   * PENDING: A pending status.

    #   * PENDING_CONCURRENCY: A pending concurrency status.

    #   * PENDING_DEVICE: A pending device status.

    #   * PROCESSING: A processing status.

    #   * SCHEDULING: A scheduling status.

    #   * PREPARING: A preparing status.

    #   * RUNNING: A running status.

    #   * COMPLETED: A completed status.

    #   * STOPPING: A stopping status.
    status: typing.Union[str, "ExecutionStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The job's result.

    # Allowed values include:

    #   * PENDING: A pending condition.

    #   * PASSED: A passing condition.

    #   * WARNED: A warning condition.

    #   * FAILED: A failed condition.

    #   * SKIPPED: A skipped condition.

    #   * ERRORED: An error condition.

    #   * STOPPED: A stopped condition.
    result: typing.Union[str, "ExecutionResult"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The job's start time.
    started: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The job's stop time.
    stopped: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The job's result counters.
    counters: "Counters" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A message about the job's result.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The device (phone or tablet).
    device: "Device" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the instance.
    instance_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Represents the total (metered or unmetered) minutes used by the job.
    device_minutes: "DeviceMinutes" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The endpoint for streaming device video.
    video_endpoint: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This value is set to true if video capture is enabled; otherwise, it is set
    # to false.
    video_capture: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LimitExceededException(ShapeBase):
    """
    A limit was exceeded.
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

    # Any additional information about the exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListArtifactsRequest(ShapeBase):
    """
    Represents a request to the list artifacts operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
            (
                "type",
                "type",
                TypeInfo(typing.Union[str, ArtifactCategory]),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    # The Run, Job, Suite, or Test ARN.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The artifacts' type.

    # Allowed values include:

    #   * FILE: The artifacts are files.

    #   * LOG: The artifacts are logs.

    #   * SCREENSHOT: The artifacts are screenshots.
    type: typing.Union[str, "ArtifactCategory"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An identifier that was returned from the previous call to this operation,
    # which can be used to return the next set of items in the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListArtifactsResult(OutputShapeBase):
    """
    Represents the result of a list artifacts operation.
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
                "artifacts",
                "artifacts",
                TypeInfo(typing.List[Artifact]),
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

    # Information about the artifacts.
    artifacts: typing.List["Artifact"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the number of items that are returned is significantly large, this is an
    # identifier that is also returned, which can be used in a subsequent call to
    # this operation to return the next set of items in the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["ListArtifactsResult", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListDeviceInstancesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "max_results",
                "maxResults",
                TypeInfo(int),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    # An integer specifying the maximum number of items you want to return in the
    # API response.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An identifier that was returned from the previous call to this operation,
    # which can be used to return the next set of items in the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListDeviceInstancesResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "device_instances",
                "deviceInstances",
                TypeInfo(typing.List[DeviceInstance]),
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

    # An object containing information about your device instances.
    device_instances: typing.List["DeviceInstance"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An identifier that can be used in the next call to this operation to return
    # the next set of items in the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListDevicePoolsRequest(ShapeBase):
    """
    Represents the result of a list device pools request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
            (
                "type",
                "type",
                TypeInfo(typing.Union[str, DevicePoolType]),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    # The project ARN.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The device pools' type.

    # Allowed values include:

    #   * CURATED: A device pool that is created and managed by AWS Device Farm.

    #   * PRIVATE: A device pool that is created and managed by the device pool developer.
    type: typing.Union[str, "DevicePoolType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An identifier that was returned from the previous call to this operation,
    # which can be used to return the next set of items in the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListDevicePoolsResult(OutputShapeBase):
    """
    Represents the result of a list device pools request.
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
                "device_pools",
                "devicePools",
                TypeInfo(typing.List[DevicePool]),
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

    # Information about the device pools.
    device_pools: typing.List["DevicePool"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the number of items that are returned is significantly large, this is an
    # identifier that is also returned, which can be used in a subsequent call to
    # this operation to return the next set of items in the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ListDevicePoolsResult", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListDevicesRequest(ShapeBase):
    """
    Represents the result of a list devices request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the project.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An identifier that was returned from the previous call to this operation,
    # which can be used to return the next set of items in the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListDevicesResult(OutputShapeBase):
    """
    Represents the result of a list devices operation.
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
                "devices",
                "devices",
                TypeInfo(typing.List[Device]),
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

    # Information about the devices.
    devices: typing.List["Device"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the number of items that are returned is significantly large, this is an
    # identifier that is also returned, which can be used in a subsequent call to
    # this operation to return the next set of items in the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["ListDevicesResult", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListInstanceProfilesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "max_results",
                "maxResults",
                TypeInfo(int),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    # An integer specifying the maximum number of items you want to return in the
    # API response.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An identifier that was returned from the previous call to this operation,
    # which can be used to return the next set of items in the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListInstanceProfilesResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "instance_profiles",
                "instanceProfiles",
                TypeInfo(typing.List[InstanceProfile]),
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

    # An object containing information about your instance profiles.
    instance_profiles: typing.List["InstanceProfile"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An identifier that can be used in the next call to this operation to return
    # the next set of items in the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListJobsRequest(ShapeBase):
    """
    Represents a request to the list jobs operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    # The run's Amazon Resource Name (ARN).
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An identifier that was returned from the previous call to this operation,
    # which can be used to return the next set of items in the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListJobsResult(OutputShapeBase):
    """
    Represents the result of a list jobs request.
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
                "jobs",
                "jobs",
                TypeInfo(typing.List[Job]),
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

    # Information about the jobs.
    jobs: typing.List["Job"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If the number of items that are returned is significantly large, this is an
    # identifier that is also returned, which can be used in a subsequent call to
    # this operation to return the next set of items in the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["ListJobsResult", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListNetworkProfilesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
            (
                "type",
                "type",
                TypeInfo(typing.Union[str, NetworkProfileType]),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the project for which you want to list
    # network profiles.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of network profile you wish to return information about. Valid
    # values are listed below.
    type: typing.Union[str, "NetworkProfileType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An identifier that was returned from the previous call to this operation,
    # which can be used to return the next set of items in the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListNetworkProfilesResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "network_profiles",
                "networkProfiles",
                TypeInfo(typing.List[NetworkProfile]),
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

    # A list of the available network profiles.
    network_profiles: typing.List["NetworkProfile"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An identifier that was returned from the previous call to this operation,
    # which can be used to return the next set of items in the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListOfferingPromotionsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    # An identifier that was returned from the previous call to this operation,
    # which can be used to return the next set of items in the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListOfferingPromotionsResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "offering_promotions",
                "offeringPromotions",
                TypeInfo(typing.List[OfferingPromotion]),
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

    # Information about the offering promotions.
    offering_promotions: typing.List["OfferingPromotion"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An identifier to be used in the next call to this operation, to return the
    # next set of items in the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListOfferingTransactionsRequest(ShapeBase):
    """
    Represents the request to list the offering transaction history.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    # An identifier that was returned from the previous call to this operation,
    # which can be used to return the next set of items in the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListOfferingTransactionsResult(OutputShapeBase):
    """
    Returns the transaction log of the specified offerings.
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
                "offering_transactions",
                "offeringTransactions",
                TypeInfo(typing.List[OfferingTransaction]),
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

    # The audit log of subscriptions you have purchased and modified through AWS
    # Device Farm.
    offering_transactions: typing.List["OfferingTransaction"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    # An identifier that was returned from the previous call to this operation,
    # which can be used to return the next set of items in the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["ListOfferingTransactionsResult", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListOfferingsRequest(ShapeBase):
    """
    Represents the request to list all offerings.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    # An identifier that was returned from the previous call to this operation,
    # which can be used to return the next set of items in the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListOfferingsResult(OutputShapeBase):
    """
    Represents the return values of the list of offerings.
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
                "offerings",
                "offerings",
                TypeInfo(typing.List[Offering]),
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

    # A value representing the list offering results.
    offerings: typing.List["Offering"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An identifier that was returned from the previous call to this operation,
    # which can be used to return the next set of items in the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["ListOfferingsResult", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListProjectsRequest(ShapeBase):
    """
    Represents a request to the list projects operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    # Optional. If no Amazon Resource Name (ARN) is specified, then AWS Device
    # Farm returns a list of all projects for the AWS account. You can also
    # specify a project ARN.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An identifier that was returned from the previous call to this operation,
    # which can be used to return the next set of items in the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListProjectsResult(OutputShapeBase):
    """
    Represents the result of a list projects request.
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
                "projects",
                "projects",
                TypeInfo(typing.List[Project]),
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

    # Information about the projects.
    projects: typing.List["Project"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the number of items that are returned is significantly large, this is an
    # identifier that is also returned, which can be used in a subsequent call to
    # this operation to return the next set of items in the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["ListProjectsResult", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListRemoteAccessSessionsRequest(ShapeBase):
    """
    Represents the request to return information about the remote access session.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the remote access session about which you
    # are requesting information.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An identifier that was returned from the previous call to this operation,
    # which can be used to return the next set of items in the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListRemoteAccessSessionsResult(OutputShapeBase):
    """
    Represents the response from the server after AWS Device Farm makes a request to
    return information about the remote access session.
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
                "remote_access_sessions",
                "remoteAccessSessions",
                TypeInfo(typing.List[RemoteAccessSession]),
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

    # A container representing the metadata from the service about each remote
    # access session you are requesting.
    remote_access_sessions: typing.List["RemoteAccessSession"
                                       ] = dataclasses.field(
                                           default=ShapeBase.NOT_SET,
                                       )

    # An identifier that was returned from the previous call to this operation,
    # which can be used to return the next set of items in the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListRunsRequest(ShapeBase):
    """
    Represents a request to the list runs operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the project for which you want to list
    # runs.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An identifier that was returned from the previous call to this operation,
    # which can be used to return the next set of items in the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListRunsResult(OutputShapeBase):
    """
    Represents the result of a list runs request.
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
                "runs",
                "runs",
                TypeInfo(typing.List[Run]),
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

    # Information about the runs.
    runs: typing.List["Run"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If the number of items that are returned is significantly large, this is an
    # identifier that is also returned, which can be used in a subsequent call to
    # this operation to return the next set of items in the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["ListRunsResult", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListSamplesRequest(ShapeBase):
    """
    Represents a request to the list samples operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the project for which you want to list
    # samples.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An identifier that was returned from the previous call to this operation,
    # which can be used to return the next set of items in the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListSamplesResult(OutputShapeBase):
    """
    Represents the result of a list samples request.
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
                "samples",
                "samples",
                TypeInfo(typing.List[Sample]),
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

    # Information about the samples.
    samples: typing.List["Sample"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the number of items that are returned is significantly large, this is an
    # identifier that is also returned, which can be used in a subsequent call to
    # this operation to return the next set of items in the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["ListSamplesResult", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListSuitesRequest(ShapeBase):
    """
    Represents a request to the list suites operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    # The job's Amazon Resource Name (ARN).
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An identifier that was returned from the previous call to this operation,
    # which can be used to return the next set of items in the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListSuitesResult(OutputShapeBase):
    """
    Represents the result of a list suites request.
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
                "suites",
                "suites",
                TypeInfo(typing.List[Suite]),
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

    # Information about the suites.
    suites: typing.List["Suite"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the number of items that are returned is significantly large, this is an
    # identifier that is also returned, which can be used in a subsequent call to
    # this operation to return the next set of items in the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["ListSuitesResult", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListTestsRequest(ShapeBase):
    """
    Represents a request to the list tests operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    # The test suite's Amazon Resource Name (ARN).
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An identifier that was returned from the previous call to this operation,
    # which can be used to return the next set of items in the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTestsResult(OutputShapeBase):
    """
    Represents the result of a list tests request.
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
                "tests",
                "tests",
                TypeInfo(typing.List[Test]),
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

    # Information about the tests.
    tests: typing.List["Test"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If the number of items that are returned is significantly large, this is an
    # identifier that is also returned, which can be used in a subsequent call to
    # this operation to return the next set of items in the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["ListTestsResult", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListUniqueProblemsRequest(ShapeBase):
    """
    Represents a request to the list unique problems operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    # The unique problems' ARNs.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An identifier that was returned from the previous call to this operation,
    # which can be used to return the next set of items in the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListUniqueProblemsResult(OutputShapeBase):
    """
    Represents the result of a list unique problems request.
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
                "unique_problems",
                "uniqueProblems",
                TypeInfo(
                    typing.Dict[typing.Union[str, ExecutionResult], typing.
                                List[UniqueProblem]]
                ),
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

    # Information about the unique problems.

    # Allowed values include:

    #   * PENDING: A pending condition.

    #   * PASSED: A passing condition.

    #   * WARNED: A warning condition.

    #   * FAILED: A failed condition.

    #   * SKIPPED: A skipped condition.

    #   * ERRORED: An error condition.

    #   * STOPPED: A stopped condition.
    unique_problems: typing.Dict[typing.Union[str, "ExecutionResult"], typing.
                                 List["UniqueProblem"]] = dataclasses.field(
                                     default=ShapeBase.NOT_SET,
                                 )

    # If the number of items that are returned is significantly large, this is an
    # identifier that is also returned, which can be used in a subsequent call to
    # this operation to return the next set of items in the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ListUniqueProblemsResult", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListUploadsRequest(ShapeBase):
    """
    Represents a request to the list uploads operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
            (
                "type",
                "type",
                TypeInfo(typing.Union[str, UploadType]),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the project for which you want to list
    # uploads.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of upload.

    # Must be one of the following values:

    #   * ANDROID_APP: An Android upload.

    #   * IOS_APP: An iOS upload.

    #   * WEB_APP: A web appliction upload.

    #   * EXTERNAL_DATA: An external data upload.

    #   * APPIUM_JAVA_JUNIT_TEST_PACKAGE: An Appium Java JUnit test package upload.

    #   * APPIUM_JAVA_TESTNG_TEST_PACKAGE: An Appium Java TestNG test package upload.

    #   * APPIUM_PYTHON_TEST_PACKAGE: An Appium Python test package upload.

    #   * APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE: An Appium Java JUnit test package upload.

    #   * APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE: An Appium Java TestNG test package upload.

    #   * APPIUM_WEB_PYTHON_TEST_PACKAGE: An Appium Python test package upload.

    #   * CALABASH_TEST_PACKAGE: A Calabash test package upload.

    #   * INSTRUMENTATION_TEST_PACKAGE: An instrumentation upload.

    #   * UIAUTOMATION_TEST_PACKAGE: A uiautomation test package upload.

    #   * UIAUTOMATOR_TEST_PACKAGE: A uiautomator test package upload.

    #   * XCTEST_TEST_PACKAGE: An XCode test package upload.

    #   * XCTEST_UI_TEST_PACKAGE: An XCode UI test package upload.

    #   * APPIUM_JAVA_JUNIT_TEST_SPEC: An Appium Java JUnit test spec upload.

    #   * APPIUM_JAVA_TESTNG_TEST_SPEC: An Appium Java TestNG test spec upload.

    #   * APPIUM_PYTHON_TEST_SPEC: An Appium Python test spec upload.

    #   * APPIUM_WEB_JAVA_JUNIT_TEST_SPEC: An Appium Java JUnit test spec upload.

    #   * APPIUM_WEB_JAVA_TESTNG_TEST_SPEC: An Appium Java TestNG test spec upload.

    #   * APPIUM_WEB_PYTHON_TEST_SPEC: An Appium Python test spec upload.

    #   * INSTRUMENTATION_TEST_SPEC: An instrumentation test spec upload.

    #   * XCTEST_UI_TEST_SPEC: An XCode UI test spec upload.
    type: typing.Union[str, "UploadType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An identifier that was returned from the previous call to this operation,
    # which can be used to return the next set of items in the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListUploadsResult(OutputShapeBase):
    """
    Represents the result of a list uploads request.
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
                "uploads",
                "uploads",
                TypeInfo(typing.List[Upload]),
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

    # Information about the uploads.
    uploads: typing.List["Upload"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the number of items that are returned is significantly large, this is an
    # identifier that is also returned, which can be used in a subsequent call to
    # this operation to return the next set of items in the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["ListUploadsResult", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListVPCEConfigurationsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "max_results",
                "maxResults",
                TypeInfo(int),
            ),
            (
                "next_token",
                "nextToken",
                TypeInfo(str),
            ),
        ]

    # An integer specifying the maximum number of items you want to return in the
    # API response.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An identifier that was returned from the previous call to this operation,
    # which can be used to return the next set of items in the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListVPCEConfigurationsResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "vpce_configurations",
                "vpceConfigurations",
                TypeInfo(typing.List[VPCEConfiguration]),
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

    # An array of `VPCEConfiguration` objects containing information about your
    # VPC endpoint configuration.
    vpce_configurations: typing.List["VPCEConfiguration"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An identifier that was returned from the previous call to this operation,
    # which can be used to return the next set of items in the list.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Location(ShapeBase):
    """
    Represents a latitude and longitude pair, expressed in geographic coordinate
    system degrees (for example 47.6204, -122.3491).

    Elevation is currently not supported.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "latitude",
                "latitude",
                TypeInfo(float),
            ),
            (
                "longitude",
                "longitude",
                TypeInfo(float),
            ),
        ]

    # The latitude.
    latitude: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The longitude.
    longitude: float = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MonetaryAmount(ShapeBase):
    """
    A number representing the monetary amount for an offering or transaction.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "amount",
                "amount",
                TypeInfo(float),
            ),
            (
                "currency_code",
                "currencyCode",
                TypeInfo(typing.Union[str, CurrencyCode]),
            ),
        ]

    # The numerical amount of an offering or transaction.
    amount: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The currency code of a monetary amount. For example, `USD` means "U.S.
    # dollars."
    currency_code: typing.Union[str, "CurrencyCode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class NetworkProfile(ShapeBase):
    """
    An array of settings that describes characteristics of a network profile.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
            (
                "type",
                "type",
                TypeInfo(typing.Union[str, NetworkProfileType]),
            ),
            (
                "uplink_bandwidth_bits",
                "uplinkBandwidthBits",
                TypeInfo(int),
            ),
            (
                "downlink_bandwidth_bits",
                "downlinkBandwidthBits",
                TypeInfo(int),
            ),
            (
                "uplink_delay_ms",
                "uplinkDelayMs",
                TypeInfo(int),
            ),
            (
                "downlink_delay_ms",
                "downlinkDelayMs",
                TypeInfo(int),
            ),
            (
                "uplink_jitter_ms",
                "uplinkJitterMs",
                TypeInfo(int),
            ),
            (
                "downlink_jitter_ms",
                "downlinkJitterMs",
                TypeInfo(int),
            ),
            (
                "uplink_loss_percent",
                "uplinkLossPercent",
                TypeInfo(int),
            ),
            (
                "downlink_loss_percent",
                "downlinkLossPercent",
                TypeInfo(int),
            ),
        ]

    # The Amazon Resource Name (ARN) of the network profile.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the network profile.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The description of the network profile.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of network profile. Valid values are listed below.
    type: typing.Union[str, "NetworkProfileType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The data throughput rate in bits per second, as an integer from 0 to
    # 104857600.
    uplink_bandwidth_bits: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The data throughput rate in bits per second, as an integer from 0 to
    # 104857600.
    downlink_bandwidth_bits: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Delay time for all packets to destination in milliseconds as an integer
    # from 0 to 2000.
    uplink_delay_ms: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Delay time for all packets to destination in milliseconds as an integer
    # from 0 to 2000.
    downlink_delay_ms: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Time variation in the delay of received packets in milliseconds as an
    # integer from 0 to 2000.
    uplink_jitter_ms: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Time variation in the delay of received packets in milliseconds as an
    # integer from 0 to 2000.
    downlink_jitter_ms: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Proportion of transmitted packets that fail to arrive from 0 to 100
    # percent.
    uplink_loss_percent: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Proportion of received packets that fail to arrive from 0 to 100 percent.
    downlink_loss_percent: int = dataclasses.field(default=ShapeBase.NOT_SET, )


class NetworkProfileType(str):
    CURATED = "CURATED"
    PRIVATE = "PRIVATE"


@dataclasses.dataclass
class NotEligibleException(ShapeBase):
    """
    Exception gets thrown when a user is not eligible to perform the specified
    transaction.
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

    # The HTTP response code of a Not Eligible exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class NotFoundException(ShapeBase):
    """
    The specified entity was not found.
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

    # Any additional information about the exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Offering(ShapeBase):
    """
    Represents the metadata of a device offering.
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
                "description",
                "description",
                TypeInfo(str),
            ),
            (
                "type",
                "type",
                TypeInfo(typing.Union[str, OfferingType]),
            ),
            (
                "platform",
                "platform",
                TypeInfo(typing.Union[str, DevicePlatform]),
            ),
            (
                "recurring_charges",
                "recurringCharges",
                TypeInfo(typing.List[RecurringCharge]),
            ),
        ]

    # The ID that corresponds to a device offering.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A string describing the offering.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of offering (e.g., "RECURRING") for a device.
    type: typing.Union[str, "OfferingType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The platform of the device (e.g., ANDROID or IOS).
    platform: typing.Union[str, "DevicePlatform"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies whether there are recurring charges for the offering.
    recurring_charges: typing.List["RecurringCharge"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class OfferingPromotion(ShapeBase):
    """
    Represents information about an offering promotion.
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
                "description",
                "description",
                TypeInfo(str),
            ),
        ]

    # The ID of the offering promotion.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A string describing the offering promotion.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class OfferingStatus(ShapeBase):
    """
    The status of the offering.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "type",
                TypeInfo(typing.Union[str, OfferingTransactionType]),
            ),
            (
                "offering",
                "offering",
                TypeInfo(Offering),
            ),
            (
                "quantity",
                "quantity",
                TypeInfo(int),
            ),
            (
                "effective_on",
                "effectiveOn",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The type specified for the offering status.
    type: typing.Union[str, "OfferingTransactionType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Represents the metadata of an offering status.
    offering: "Offering" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of available devices in the offering.
    quantity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date on which the offering is effective.
    effective_on: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class OfferingTransaction(ShapeBase):
    """
    Represents the metadata of an offering transaction.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "offering_status",
                "offeringStatus",
                TypeInfo(OfferingStatus),
            ),
            (
                "transaction_id",
                "transactionId",
                TypeInfo(str),
            ),
            (
                "offering_promotion_id",
                "offeringPromotionId",
                TypeInfo(str),
            ),
            (
                "created_on",
                "createdOn",
                TypeInfo(datetime.datetime),
            ),
            (
                "cost",
                "cost",
                TypeInfo(MonetaryAmount),
            ),
        ]

    # The status of an offering transaction.
    offering_status: "OfferingStatus" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The transaction ID of the offering transaction.
    transaction_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID that corresponds to a device offering promotion.
    offering_promotion_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date on which an offering transaction was created.
    created_on: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The cost of an offering transaction.
    cost: "MonetaryAmount" = dataclasses.field(default=ShapeBase.NOT_SET, )


class OfferingTransactionType(str):
    PURCHASE = "PURCHASE"
    RENEW = "RENEW"
    SYSTEM = "SYSTEM"


class OfferingType(str):
    RECURRING = "RECURRING"


@dataclasses.dataclass
class Problem(ShapeBase):
    """
    Represents a specific warning or failure.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "run",
                "run",
                TypeInfo(ProblemDetail),
            ),
            (
                "job",
                "job",
                TypeInfo(ProblemDetail),
            ),
            (
                "suite",
                "suite",
                TypeInfo(ProblemDetail),
            ),
            (
                "test",
                "test",
                TypeInfo(ProblemDetail),
            ),
            (
                "device",
                "device",
                TypeInfo(Device),
            ),
            (
                "result",
                "result",
                TypeInfo(typing.Union[str, ExecutionResult]),
            ),
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    # Information about the associated run.
    run: "ProblemDetail" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the associated job.
    job: "ProblemDetail" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the associated suite.
    suite: "ProblemDetail" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the associated test.
    test: "ProblemDetail" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the associated device.
    device: "Device" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The problem's result.

    # Allowed values include:

    #   * PENDING: A pending condition.

    #   * PASSED: A passing condition.

    #   * WARNED: A warning condition.

    #   * FAILED: A failed condition.

    #   * SKIPPED: A skipped condition.

    #   * ERRORED: An error condition.

    #   * STOPPED: A stopped condition.
    result: typing.Union[str, "ExecutionResult"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A message about the problem's result.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ProblemDetail(ShapeBase):
    """
    Information about a problem detail.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
            (
                "name",
                "name",
                TypeInfo(str),
            ),
        ]

    # The problem detail's ARN.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The problem detail's name.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Project(ShapeBase):
    """
    Represents an operating-system neutral workspace for running and managing tests.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "default_job_timeout_minutes",
                "defaultJobTimeoutMinutes",
                TypeInfo(int),
            ),
            (
                "created",
                "created",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The project's ARN.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The project's name.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The default number of minutes (at the project level) a test run will
    # execute before it times out. Default value is 60 minutes.
    default_job_timeout_minutes: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When the project was created.
    created: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PurchaseOfferingRequest(ShapeBase):
    """
    Represents a request for a purchase offering.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "offering_id",
                "offeringId",
                TypeInfo(str),
            ),
            (
                "quantity",
                "quantity",
                TypeInfo(int),
            ),
            (
                "offering_promotion_id",
                "offeringPromotionId",
                TypeInfo(str),
            ),
        ]

    # The ID of the offering.
    offering_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of device slots you wish to purchase in an offering request.
    quantity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the offering promotion to be applied to the purchase.
    offering_promotion_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PurchaseOfferingResult(OutputShapeBase):
    """
    The result of the purchase offering (e.g., success or failure).
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
                "offering_transaction",
                "offeringTransaction",
                TypeInfo(OfferingTransaction),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Represents the offering transaction for the purchase result.
    offering_transaction: "OfferingTransaction" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Radios(ShapeBase):
    """
    Represents the set of radios and their states on a device. Examples of radios
    include Wi-Fi, GPS, Bluetooth, and NFC.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "wifi",
                "wifi",
                TypeInfo(bool),
            ),
            (
                "bluetooth",
                "bluetooth",
                TypeInfo(bool),
            ),
            (
                "nfc",
                "nfc",
                TypeInfo(bool),
            ),
            (
                "gps",
                "gps",
                TypeInfo(bool),
            ),
        ]

    # True if Wi-Fi is enabled at the beginning of the test; otherwise, false.
    wifi: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # True if Bluetooth is enabled at the beginning of the test; otherwise,
    # false.
    bluetooth: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # True if NFC is enabled at the beginning of the test; otherwise, false.
    nfc: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # True if GPS is enabled at the beginning of the test; otherwise, false.
    gps: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RecurringCharge(ShapeBase):
    """
    Specifies whether charges for devices will be recurring.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cost",
                "cost",
                TypeInfo(MonetaryAmount),
            ),
            (
                "frequency",
                "frequency",
                TypeInfo(typing.Union[str, RecurringChargeFrequency]),
            ),
        ]

    # The cost of the recurring charge.
    cost: "MonetaryAmount" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The frequency in which charges will recur.
    frequency: typing.Union[str, "RecurringChargeFrequency"
                           ] = dataclasses.field(
                               default=ShapeBase.NOT_SET,
                           )


class RecurringChargeFrequency(str):
    MONTHLY = "MONTHLY"


@dataclasses.dataclass
class RemoteAccessSession(ShapeBase):
    """
    Represents information about the remote access session.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "created",
                "created",
                TypeInfo(datetime.datetime),
            ),
            (
                "status",
                "status",
                TypeInfo(typing.Union[str, ExecutionStatus]),
            ),
            (
                "result",
                "result",
                TypeInfo(typing.Union[str, ExecutionResult]),
            ),
            (
                "message",
                "message",
                TypeInfo(str),
            ),
            (
                "started",
                "started",
                TypeInfo(datetime.datetime),
            ),
            (
                "stopped",
                "stopped",
                TypeInfo(datetime.datetime),
            ),
            (
                "device",
                "device",
                TypeInfo(Device),
            ),
            (
                "instance_arn",
                "instanceArn",
                TypeInfo(str),
            ),
            (
                "remote_debug_enabled",
                "remoteDebugEnabled",
                TypeInfo(bool),
            ),
            (
                "remote_record_enabled",
                "remoteRecordEnabled",
                TypeInfo(bool),
            ),
            (
                "remote_record_app_arn",
                "remoteRecordAppArn",
                TypeInfo(str),
            ),
            (
                "host_address",
                "hostAddress",
                TypeInfo(str),
            ),
            (
                "client_id",
                "clientId",
                TypeInfo(str),
            ),
            (
                "billing_method",
                "billingMethod",
                TypeInfo(typing.Union[str, BillingMethod]),
            ),
            (
                "device_minutes",
                "deviceMinutes",
                TypeInfo(DeviceMinutes),
            ),
            (
                "endpoint",
                "endpoint",
                TypeInfo(str),
            ),
            (
                "device_udid",
                "deviceUdid",
                TypeInfo(str),
            ),
            (
                "interaction_mode",
                "interactionMode",
                TypeInfo(typing.Union[str, InteractionMode]),
            ),
            (
                "skip_app_resign",
                "skipAppResign",
                TypeInfo(bool),
            ),
        ]

    # The Amazon Resource Name (ARN) of the remote access session.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the remote access session.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time the remote access session was created.
    created: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the remote access session. Can be any of the following:

    #   * PENDING: A pending status.

    #   * PENDING_CONCURRENCY: A pending concurrency status.

    #   * PENDING_DEVICE: A pending device status.

    #   * PROCESSING: A processing status.

    #   * SCHEDULING: A scheduling status.

    #   * PREPARING: A preparing status.

    #   * RUNNING: A running status.

    #   * COMPLETED: A completed status.

    #   * STOPPING: A stopping status.
    status: typing.Union[str, "ExecutionStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The result of the remote access session. Can be any of the following:

    #   * PENDING: A pending condition.

    #   * PASSED: A passing condition.

    #   * WARNED: A warning condition.

    #   * FAILED: A failed condition.

    #   * SKIPPED: A skipped condition.

    #   * ERRORED: An error condition.

    #   * STOPPED: A stopped condition.
    result: typing.Union[str, "ExecutionResult"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A message about the remote access session.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time the remote access session was started.
    started: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time the remote access session was stopped.
    stopped: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The device (phone or tablet) used in the remote access session.
    device: "Device" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the instance.
    instance_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This flag is set to `true` if remote debugging is enabled for the remote
    # access session.
    remote_debug_enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This flag is set to `true` if remote recording is enabled for the remote
    # access session.
    remote_record_enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) for the app to be recorded in the remote
    # access session.
    remote_record_app_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # IP address of the EC2 host where you need to connect to remotely debug
    # devices. Only returned if remote debugging is enabled for the remote access
    # session.
    host_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique identifier of your client for the remote access session. Only
    # returned if remote debugging is enabled for the remote access session.
    client_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The billing method of the remote access session. Possible values include
    # `METERED` or `UNMETERED`. For more information about metered devices, see
    # [AWS Device Farm
    # terminology](http://docs.aws.amazon.com/devicefarm/latest/developerguide/welcome.html#welcome-
    # terminology)."
    billing_method: typing.Union[str, "BillingMethod"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of minutes a device is used in a remote access sesssion
    # (including setup and teardown minutes).
    device_minutes: "DeviceMinutes" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The endpoint for the remote access sesssion.
    endpoint: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique device identifier for the remote device. Only returned if remote
    # debugging is enabled for the remote access session.
    device_udid: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The interaction mode of the remote access session. Valid values are:

    #   * INTERACTIVE: You can interact with the iOS device by viewing, touching, and rotating the screen. You **cannot** run XCUITest framework-based tests in this mode.

    #   * NO_VIDEO: You are connected to the device but cannot interact with it or view the screen. This mode has the fastest test execution speed. You **can** run XCUITest framework-based tests in this mode.

    #   * VIDEO_ONLY: You can view the screen but cannot touch or rotate it. You **can** run XCUITest framework-based tests and watch the screen in this mode.
    interaction_mode: typing.Union[str, "InteractionMode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When set to `true`, for private devices, Device Farm will not sign your app
    # again. For public devices, Device Farm always signs your apps again and
    # this parameter has no effect.

    # For more information about how Device Farm re-signs your app(s), see [Do
    # you modify my app?](https://aws.amazon.com/device-farm/faq/) in the _AWS
    # Device Farm FAQs_.
    skip_app_resign: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RenewOfferingRequest(ShapeBase):
    """
    A request representing an offering renewal.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "offering_id",
                "offeringId",
                TypeInfo(str),
            ),
            (
                "quantity",
                "quantity",
                TypeInfo(int),
            ),
        ]

    # The ID of a request to renew an offering.
    offering_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The quantity requested in an offering renewal.
    quantity: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RenewOfferingResult(OutputShapeBase):
    """
    The result of a renewal offering.
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
                "offering_transaction",
                "offeringTransaction",
                TypeInfo(OfferingTransaction),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Represents the status of the offering transaction for the renewal.
    offering_transaction: "OfferingTransaction" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Resolution(ShapeBase):
    """
    Represents the screen resolution of a device in height and width, expressed in
    pixels.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "width",
                "width",
                TypeInfo(int),
            ),
            (
                "height",
                "height",
                TypeInfo(int),
            ),
        ]

    # The screen resolution's width, expressed in pixels.
    width: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The screen resolution's height, expressed in pixels.
    height: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Rule(ShapeBase):
    """
    Represents a condition for a device pool.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attribute",
                "attribute",
                TypeInfo(typing.Union[str, DeviceAttribute]),
            ),
            (
                "operator",
                "operator",
                TypeInfo(typing.Union[str, RuleOperator]),
            ),
            (
                "value",
                "value",
                TypeInfo(str),
            ),
        ]

    # The rule's stringified attribute. For example, specify the value as
    # `"\"abc\""`.

    # Allowed values include:

    #   * ARN: The ARN.

    #   * FORM_FACTOR: The form factor (for example, phone or tablet).

    #   * MANUFACTURER: The manufacturer.

    #   * PLATFORM: The platform (for example, Android or iOS).

    #   * REMOTE_ACCESS_ENABLED: Whether the device is enabled for remote access.

    #   * APPIUM_VERSION: The Appium version for the test.

    #   * INSTANCE_ARN: The Amazon Resource Name (ARN) of the device instance.

    #   * INSTANCE_LABELS: The label of the device instance.
    attribute: typing.Union[str, "DeviceAttribute"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The rule's operator.

    #   * EQUALS: The equals operator.

    #   * GREATER_THAN: The greater-than operator.

    #   * IN: The in operator.

    #   * LESS_THAN: The less-than operator.

    #   * NOT_IN: The not-in operator.

    #   * CONTAINS: The contains operator.
    operator: typing.Union[str, "RuleOperator"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The rule's value.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class RuleOperator(str):
    EQUALS = "EQUALS"
    LESS_THAN = "LESS_THAN"
    GREATER_THAN = "GREATER_THAN"
    IN = "IN"
    NOT_IN = "NOT_IN"
    CONTAINS = "CONTAINS"


@dataclasses.dataclass
class Run(ShapeBase):
    """
    Represents a test run on a set of devices with a given app package, test
    parameters, etc.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "type",
                "type",
                TypeInfo(typing.Union[str, TestType]),
            ),
            (
                "platform",
                "platform",
                TypeInfo(typing.Union[str, DevicePlatform]),
            ),
            (
                "created",
                "created",
                TypeInfo(datetime.datetime),
            ),
            (
                "status",
                "status",
                TypeInfo(typing.Union[str, ExecutionStatus]),
            ),
            (
                "result",
                "result",
                TypeInfo(typing.Union[str, ExecutionResult]),
            ),
            (
                "started",
                "started",
                TypeInfo(datetime.datetime),
            ),
            (
                "stopped",
                "stopped",
                TypeInfo(datetime.datetime),
            ),
            (
                "counters",
                "counters",
                TypeInfo(Counters),
            ),
            (
                "message",
                "message",
                TypeInfo(str),
            ),
            (
                "total_jobs",
                "totalJobs",
                TypeInfo(int),
            ),
            (
                "completed_jobs",
                "completedJobs",
                TypeInfo(int),
            ),
            (
                "billing_method",
                "billingMethod",
                TypeInfo(typing.Union[str, BillingMethod]),
            ),
            (
                "device_minutes",
                "deviceMinutes",
                TypeInfo(DeviceMinutes),
            ),
            (
                "network_profile",
                "networkProfile",
                TypeInfo(NetworkProfile),
            ),
            (
                "parsing_result_url",
                "parsingResultUrl",
                TypeInfo(str),
            ),
            (
                "result_code",
                "resultCode",
                TypeInfo(typing.Union[str, ExecutionResultCode]),
            ),
            (
                "seed",
                "seed",
                TypeInfo(int),
            ),
            (
                "app_upload",
                "appUpload",
                TypeInfo(str),
            ),
            (
                "event_count",
                "eventCount",
                TypeInfo(int),
            ),
            (
                "job_timeout_minutes",
                "jobTimeoutMinutes",
                TypeInfo(int),
            ),
            (
                "device_pool_arn",
                "devicePoolArn",
                TypeInfo(str),
            ),
            (
                "locale",
                "locale",
                TypeInfo(str),
            ),
            (
                "radios",
                "radios",
                TypeInfo(Radios),
            ),
            (
                "location",
                "location",
                TypeInfo(Location),
            ),
            (
                "customer_artifact_paths",
                "customerArtifactPaths",
                TypeInfo(CustomerArtifactPaths),
            ),
            (
                "web_url",
                "webUrl",
                TypeInfo(str),
            ),
            (
                "skip_app_resign",
                "skipAppResign",
                TypeInfo(bool),
            ),
            (
                "test_spec_arn",
                "testSpecArn",
                TypeInfo(str),
            ),
        ]

    # The run's ARN.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The run's name.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The run's type.

    # Must be one of the following values:

    #   * BUILTIN_FUZZ: The built-in fuzz type.

    #   * BUILTIN_EXPLORER: For Android, an app explorer that will traverse an Android app, interacting with it and capturing screenshots at the same time.

    #   * APPIUM_JAVA_JUNIT: The Appium Java JUnit type.

    #   * APPIUM_JAVA_TESTNG: The Appium Java TestNG type.

    #   * APPIUM_PYTHON: The Appium Python type.

    #   * APPIUM_WEB_JAVA_JUNIT: The Appium Java JUnit type for Web apps.

    #   * APPIUM_WEB_JAVA_TESTNG: The Appium Java TestNG type for Web apps.

    #   * APPIUM_WEB_PYTHON: The Appium Python type for Web apps.

    #   * CALABASH: The Calabash type.

    #   * INSTRUMENTATION: The Instrumentation type.

    #   * UIAUTOMATION: The uiautomation type.

    #   * UIAUTOMATOR: The uiautomator type.

    #   * XCTEST: The XCode test type.

    #   * XCTEST_UI: The XCode UI test type.
    type: typing.Union[str, "TestType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The run's platform.

    # Allowed values include:

    #   * ANDROID: The Android platform.

    #   * IOS: The iOS platform.
    platform: typing.Union[str, "DevicePlatform"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When the run was created.
    created: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The run's status.

    # Allowed values include:

    #   * PENDING: A pending status.

    #   * PENDING_CONCURRENCY: A pending concurrency status.

    #   * PENDING_DEVICE: A pending device status.

    #   * PROCESSING: A processing status.

    #   * SCHEDULING: A scheduling status.

    #   * PREPARING: A preparing status.

    #   * RUNNING: A running status.

    #   * COMPLETED: A completed status.

    #   * STOPPING: A stopping status.
    status: typing.Union[str, "ExecutionStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The run's result.

    # Allowed values include:

    #   * PENDING: A pending condition.

    #   * PASSED: A passing condition.

    #   * WARNED: A warning condition.

    #   * FAILED: A failed condition.

    #   * SKIPPED: A skipped condition.

    #   * ERRORED: An error condition.

    #   * STOPPED: A stopped condition.
    result: typing.Union[str, "ExecutionResult"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The run's start time.
    started: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The run's stop time.
    stopped: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The run's result counters.
    counters: "Counters" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A message about the run's result.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The total number of jobs for the run.
    total_jobs: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The total number of completed jobs.
    completed_jobs: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the billing method for a test run: `metered` or `unmetered`. If
    # the parameter is not specified, the default value is `metered`.
    billing_method: typing.Union[str, "BillingMethod"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Represents the total (metered or unmetered) minutes used by the test run.
    device_minutes: "DeviceMinutes" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The network profile being used for a test run.
    network_profile: "NetworkProfile" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Read-only URL for an object in S3 bucket where you can get the parsing
    # results of the test package. If the test package doesn't parse, the reason
    # why it doesn't parse appears in the file that this URL points to.
    parsing_result_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Supporting field for the result field. Set only if `result` is `SKIPPED`.
    # `PARSING_FAILED` if the result is skipped because of test package parsing
    # failure.
    result_code: typing.Union[str, "ExecutionResultCode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # For fuzz tests, this is a seed to use for randomizing the UI fuzz test.
    # Using the same seed value between tests ensures identical event sequences.
    seed: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An app to upload or that has been uploaded.
    app_upload: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # For fuzz tests, this is the number of events, between 1 and 10000, that the
    # UI fuzz test should perform.
    event_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of minutes the job will execute before it times out.
    job_timeout_minutes: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the device pool for the run.
    device_pool_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the locale that is used for the run.
    locale: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the radio states for the run.
    radios: "Radios" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the location that is used for the run.
    location: "Location" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Output `CustomerArtifactPaths` object for the test run.
    customer_artifact_paths: "CustomerArtifactPaths" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Device Farm console URL for the recording of the run.
    web_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When set to `true`, for private devices, Device Farm will not sign your app
    # again. For public devices, Device Farm always signs your apps again and
    # this parameter has no effect.

    # For more information about how Device Farm re-signs your app(s), see [Do
    # you modify my app?](https://aws.amazon.com/device-farm/faq/) in the _AWS
    # Device Farm FAQs_.
    skip_app_resign: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the YAML-formatted test specification for the run.
    test_spec_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Sample(ShapeBase):
    """
    Represents a sample of performance data.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
            (
                "type",
                "type",
                TypeInfo(typing.Union[str, SampleType]),
            ),
            (
                "url",
                "url",
                TypeInfo(str),
            ),
        ]

    # The sample's ARN.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The sample's type.

    # Must be one of the following values:

    #   * CPU: A CPU sample type. This is expressed as the app processing CPU time (including child processes) as reported by process, as a percentage.

    #   * MEMORY: A memory usage sample type. This is expressed as the total proportional set size of an app process, in kilobytes.

    #   * NATIVE_AVG_DRAWTIME

    #   * NATIVE_FPS

    #   * NATIVE_FRAMES

    #   * NATIVE_MAX_DRAWTIME

    #   * NATIVE_MIN_DRAWTIME

    #   * OPENGL_AVG_DRAWTIME

    #   * OPENGL_FPS

    #   * OPENGL_FRAMES

    #   * OPENGL_MAX_DRAWTIME

    #   * OPENGL_MIN_DRAWTIME

    #   * RX

    #   * RX_RATE: The total number of bytes per second (TCP and UDP) that are sent, by app process.

    #   * THREADS: A threads sample type. This is expressed as the total number of threads per app process.

    #   * TX

    #   * TX_RATE: The total number of bytes per second (TCP and UDP) that are received, by app process.
    type: typing.Union[str, "SampleType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pre-signed Amazon S3 URL that can be used with a corresponding GET
    # request to download the sample's file.
    url: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class SampleType(str):
    CPU = "CPU"
    MEMORY = "MEMORY"
    THREADS = "THREADS"
    RX_RATE = "RX_RATE"
    TX_RATE = "TX_RATE"
    RX = "RX"
    TX = "TX"
    NATIVE_FRAMES = "NATIVE_FRAMES"
    NATIVE_FPS = "NATIVE_FPS"
    NATIVE_MIN_DRAWTIME = "NATIVE_MIN_DRAWTIME"
    NATIVE_AVG_DRAWTIME = "NATIVE_AVG_DRAWTIME"
    NATIVE_MAX_DRAWTIME = "NATIVE_MAX_DRAWTIME"
    OPENGL_FRAMES = "OPENGL_FRAMES"
    OPENGL_FPS = "OPENGL_FPS"
    OPENGL_MIN_DRAWTIME = "OPENGL_MIN_DRAWTIME"
    OPENGL_AVG_DRAWTIME = "OPENGL_AVG_DRAWTIME"
    OPENGL_MAX_DRAWTIME = "OPENGL_MAX_DRAWTIME"


@dataclasses.dataclass
class ScheduleRunConfiguration(ShapeBase):
    """
    Represents the settings for a run. Includes things like location, radio states,
    auxiliary apps, and network profiles.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "extra_data_package_arn",
                "extraDataPackageArn",
                TypeInfo(str),
            ),
            (
                "network_profile_arn",
                "networkProfileArn",
                TypeInfo(str),
            ),
            (
                "locale",
                "locale",
                TypeInfo(str),
            ),
            (
                "location",
                "location",
                TypeInfo(Location),
            ),
            (
                "vpce_configuration_arns",
                "vpceConfigurationArns",
                TypeInfo(typing.List[str]),
            ),
            (
                "customer_artifact_paths",
                "customerArtifactPaths",
                TypeInfo(CustomerArtifactPaths),
            ),
            (
                "radios",
                "radios",
                TypeInfo(Radios),
            ),
            (
                "auxiliary_apps",
                "auxiliaryApps",
                TypeInfo(typing.List[str]),
            ),
            (
                "billing_method",
                "billingMethod",
                TypeInfo(typing.Union[str, BillingMethod]),
            ),
        ]

    # The ARN of the extra data for the run. The extra data is a .zip file that
    # AWS Device Farm will extract to external data for Android or the app's
    # sandbox for iOS.
    extra_data_package_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Reserved for internal use.
    network_profile_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the locale that is used for the run.
    locale: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the location that is used for the run.
    location: "Location" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of Amazon Resource Names (ARNs) for your VPC endpoint
    # configurations.
    vpce_configuration_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Input `CustomerArtifactPaths` object for the scheduled run configuration.
    customer_artifact_paths: "CustomerArtifactPaths" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the radio states for the run.
    radios: "Radios" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of auxiliary apps for the run.
    auxiliary_apps: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the billing method for a test run: `metered` or `unmetered`. If
    # the parameter is not specified, the default value is `metered`.
    billing_method: typing.Union[str, "BillingMethod"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ScheduleRunRequest(ShapeBase):
    """
    Represents a request to the schedule run operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "project_arn",
                "projectArn",
                TypeInfo(str),
            ),
            (
                "device_pool_arn",
                "devicePoolArn",
                TypeInfo(str),
            ),
            (
                "test",
                "test",
                TypeInfo(ScheduleRunTest),
            ),
            (
                "app_arn",
                "appArn",
                TypeInfo(str),
            ),
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "configuration",
                "configuration",
                TypeInfo(ScheduleRunConfiguration),
            ),
            (
                "execution_configuration",
                "executionConfiguration",
                TypeInfo(ExecutionConfiguration),
            ),
        ]

    # The ARN of the project for the run to be scheduled.
    project_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the device pool for the run to be scheduled.
    device_pool_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the test for the run to be scheduled.
    test: "ScheduleRunTest" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the app to schedule a run.
    app_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name for the run to be scheduled.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the settings for the run to be scheduled.
    configuration: "ScheduleRunConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies configuration information about a test run, such as the execution
    # timeout (in minutes).
    execution_configuration: "ExecutionConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ScheduleRunResult(OutputShapeBase):
    """
    Represents the result of a schedule run request.
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
                "run",
                "run",
                TypeInfo(Run),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about the scheduled run.
    run: "Run" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ScheduleRunTest(ShapeBase):
    """
    Represents additional test settings.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "type",
                TypeInfo(typing.Union[str, TestType]),
            ),
            (
                "test_package_arn",
                "testPackageArn",
                TypeInfo(str),
            ),
            (
                "test_spec_arn",
                "testSpecArn",
                TypeInfo(str),
            ),
            (
                "filter",
                "filter",
                TypeInfo(str),
            ),
            (
                "parameters",
                "parameters",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The test's type.

    # Must be one of the following values:

    #   * BUILTIN_FUZZ: The built-in fuzz type.

    #   * BUILTIN_EXPLORER: For Android, an app explorer that will traverse an Android app, interacting with it and capturing screenshots at the same time.

    #   * APPIUM_JAVA_JUNIT: The Appium Java JUnit type.

    #   * APPIUM_JAVA_TESTNG: The Appium Java TestNG type.

    #   * APPIUM_PYTHON: The Appium Python type.

    #   * APPIUM_WEB_JAVA_JUNIT: The Appium Java JUnit type for Web apps.

    #   * APPIUM_WEB_JAVA_TESTNG: The Appium Java TestNG type for Web apps.

    #   * APPIUM_WEB_PYTHON: The Appium Python type for Web apps.

    #   * CALABASH: The Calabash type.

    #   * INSTRUMENTATION: The Instrumentation type.

    #   * UIAUTOMATION: The uiautomation type.

    #   * UIAUTOMATOR: The uiautomator type.

    #   * XCTEST: The XCode test type.

    #   * XCTEST_UI: The XCode UI test type.
    type: typing.Union[str, "TestType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the uploaded test that will be run.
    test_package_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the YAML-formatted test specification.
    test_spec_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The test's filter.
    filter: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The test's parameters, such as the following test framework parameters and
    # fixture settings:

    # For Calabash tests:

    #   * profile: A cucumber profile, for example, "my_profile_name".

    #   * tags: You can limit execution to features or scenarios that have (or don't have) certain tags, for example, "@smoke" or "@smoke,~@wip".

    # For Appium tests (all types):

    #   * appium_version: The Appium version. Currently supported values are "1.4.16", "1.6.3", "latest", and "default".

    #     * “latest” will run the latest Appium version supported by Device Farm (1.6.3).

    #     * For “default”, Device Farm will choose a compatible version of Appium for the device. The current behavior is to run 1.4.16 on Android devices and iOS 9 and earlier, 1.6.3 for iOS 10 and later.

    #     * This behavior is subject to change.

    # For Fuzz tests (Android only):

    #   * event_count: The number of events, between 1 and 10000, that the UI fuzz test should perform.

    #   * throttle: The time, in ms, between 0 and 1000, that the UI fuzz test should wait between events.

    #   * seed: A seed to use for randomizing the UI fuzz test. Using the same seed value between tests ensures identical event sequences.

    # For Explorer tests:

    #   * username: A username to use if the Explorer encounters a login form. If not supplied, no username will be inserted.

    #   * password: A password to use if the Explorer encounters a login form. If not supplied, no password will be inserted.

    # For Instrumentation:

    #   * filter: A test filter string. Examples:

    #     * Running a single test case: "com.android.abc.Test1"

    #     * Running a single test: "com.android.abc.Test1#smoke"

    #     * Running multiple tests: "com.android.abc.Test1,com.android.abc.Test2"

    # For XCTest and XCTestUI:

    #   * filter: A test filter string. Examples:

    #     * Running a single test class: "LoginTests"

    #     * Running a multiple test classes: "LoginTests,SmokeTests"

    #     * Running a single test: "LoginTests/testValid"

    #     * Running multiple tests: "LoginTests/testValid,LoginTests/testInvalid"

    # For UIAutomator:

    #   * filter: A test filter string. Examples:

    #     * Running a single test case: "com.android.abc.Test1"

    #     * Running a single test: "com.android.abc.Test1#smoke"

    #     * Running multiple tests: "com.android.abc.Test1,com.android.abc.Test2"
    parameters: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ServiceAccountException(ShapeBase):
    """
    There was a problem with the service account.
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

    # Any additional information about the exception.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StopJobRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
        ]

    # Represents the Amazon Resource Name (ARN) of the Device Farm job you wish
    # to stop.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StopJobResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "job",
                "job",
                TypeInfo(Job),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The job that was stopped.
    job: "Job" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StopRemoteAccessSessionRequest(ShapeBase):
    """
    Represents the request to stop the remote access session.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the remote access session you wish to
    # stop.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StopRemoteAccessSessionResult(OutputShapeBase):
    """
    Represents the response from the server that describes the remote access session
    when AWS Device Farm stops the session.
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
                "remote_access_session",
                "remoteAccessSession",
                TypeInfo(RemoteAccessSession),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A container representing the metadata from the service about the remote
    # access session you are stopping.
    remote_access_session: "RemoteAccessSession" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StopRunRequest(ShapeBase):
    """
    Represents the request to stop a specific run.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
        ]

    # Represents the Amazon Resource Name (ARN) of the Device Farm run you wish
    # to stop.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StopRunResult(OutputShapeBase):
    """
    Represents the results of your stop run attempt.
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
                "run",
                "run",
                TypeInfo(Run),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The run that was stopped.
    run: "Run" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Suite(ShapeBase):
    """
    Represents a collection of one or more tests.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "type",
                "type",
                TypeInfo(typing.Union[str, TestType]),
            ),
            (
                "created",
                "created",
                TypeInfo(datetime.datetime),
            ),
            (
                "status",
                "status",
                TypeInfo(typing.Union[str, ExecutionStatus]),
            ),
            (
                "result",
                "result",
                TypeInfo(typing.Union[str, ExecutionResult]),
            ),
            (
                "started",
                "started",
                TypeInfo(datetime.datetime),
            ),
            (
                "stopped",
                "stopped",
                TypeInfo(datetime.datetime),
            ),
            (
                "counters",
                "counters",
                TypeInfo(Counters),
            ),
            (
                "message",
                "message",
                TypeInfo(str),
            ),
            (
                "device_minutes",
                "deviceMinutes",
                TypeInfo(DeviceMinutes),
            ),
        ]

    # The suite's ARN.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The suite's name.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The suite's type.

    # Must be one of the following values:

    #   * BUILTIN_FUZZ: The built-in fuzz type.

    #   * BUILTIN_EXPLORER: For Android, an app explorer that will traverse an Android app, interacting with it and capturing screenshots at the same time.

    #   * APPIUM_JAVA_JUNIT: The Appium Java JUnit type.

    #   * APPIUM_JAVA_TESTNG: The Appium Java TestNG type.

    #   * APPIUM_PYTHON: The Appium Python type.

    #   * APPIUM_WEB_JAVA_JUNIT: The Appium Java JUnit type for Web apps.

    #   * APPIUM_WEB_JAVA_TESTNG: The Appium Java TestNG type for Web apps.

    #   * APPIUM_WEB_PYTHON: The Appium Python type for Web apps.

    #   * CALABASH: The Calabash type.

    #   * INSTRUMENTATION: The Instrumentation type.

    #   * UIAUTOMATION: The uiautomation type.

    #   * UIAUTOMATOR: The uiautomator type.

    #   * XCTEST: The XCode test type.

    #   * XCTEST_UI: The XCode UI test type.
    type: typing.Union[str, "TestType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When the suite was created.
    created: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The suite's status.

    # Allowed values include:

    #   * PENDING: A pending status.

    #   * PENDING_CONCURRENCY: A pending concurrency status.

    #   * PENDING_DEVICE: A pending device status.

    #   * PROCESSING: A processing status.

    #   * SCHEDULING: A scheduling status.

    #   * PREPARING: A preparing status.

    #   * RUNNING: A running status.

    #   * COMPLETED: A completed status.

    #   * STOPPING: A stopping status.
    status: typing.Union[str, "ExecutionStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The suite's result.

    # Allowed values include:

    #   * PENDING: A pending condition.

    #   * PASSED: A passing condition.

    #   * WARNED: A warning condition.

    #   * FAILED: A failed condition.

    #   * SKIPPED: A skipped condition.

    #   * ERRORED: An error condition.

    #   * STOPPED: A stopped condition.
    result: typing.Union[str, "ExecutionResult"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The suite's start time.
    started: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The suite's stop time.
    stopped: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The suite's result counters.
    counters: "Counters" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A message about the suite's result.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Represents the total (metered or unmetered) minutes used by the test suite.
    device_minutes: "DeviceMinutes" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Test(ShapeBase):
    """
    Represents a condition that is evaluated.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "type",
                "type",
                TypeInfo(typing.Union[str, TestType]),
            ),
            (
                "created",
                "created",
                TypeInfo(datetime.datetime),
            ),
            (
                "status",
                "status",
                TypeInfo(typing.Union[str, ExecutionStatus]),
            ),
            (
                "result",
                "result",
                TypeInfo(typing.Union[str, ExecutionResult]),
            ),
            (
                "started",
                "started",
                TypeInfo(datetime.datetime),
            ),
            (
                "stopped",
                "stopped",
                TypeInfo(datetime.datetime),
            ),
            (
                "counters",
                "counters",
                TypeInfo(Counters),
            ),
            (
                "message",
                "message",
                TypeInfo(str),
            ),
            (
                "device_minutes",
                "deviceMinutes",
                TypeInfo(DeviceMinutes),
            ),
        ]

    # The test's ARN.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The test's name.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The test's type.

    # Must be one of the following values:

    #   * BUILTIN_FUZZ: The built-in fuzz type.

    #   * BUILTIN_EXPLORER: For Android, an app explorer that will traverse an Android app, interacting with it and capturing screenshots at the same time.

    #   * APPIUM_JAVA_JUNIT: The Appium Java JUnit type.

    #   * APPIUM_JAVA_TESTNG: The Appium Java TestNG type.

    #   * APPIUM_PYTHON: The Appium Python type.

    #   * APPIUM_WEB_JAVA_JUNIT: The Appium Java JUnit type for Web apps.

    #   * APPIUM_WEB_JAVA_TESTNG: The Appium Java TestNG type for Web apps.

    #   * APPIUM_WEB_PYTHON: The Appium Python type for Web apps.

    #   * CALABASH: The Calabash type.

    #   * INSTRUMENTATION: The Instrumentation type.

    #   * UIAUTOMATION: The uiautomation type.

    #   * UIAUTOMATOR: The uiautomator type.

    #   * XCTEST: The XCode test type.

    #   * XCTEST_UI: The XCode UI test type.
    type: typing.Union[str, "TestType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When the test was created.
    created: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The test's status.

    # Allowed values include:

    #   * PENDING: A pending status.

    #   * PENDING_CONCURRENCY: A pending concurrency status.

    #   * PENDING_DEVICE: A pending device status.

    #   * PROCESSING: A processing status.

    #   * SCHEDULING: A scheduling status.

    #   * PREPARING: A preparing status.

    #   * RUNNING: A running status.

    #   * COMPLETED: A completed status.

    #   * STOPPING: A stopping status.
    status: typing.Union[str, "ExecutionStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The test's result.

    # Allowed values include:

    #   * PENDING: A pending condition.

    #   * PASSED: A passing condition.

    #   * WARNED: A warning condition.

    #   * FAILED: A failed condition.

    #   * SKIPPED: A skipped condition.

    #   * ERRORED: An error condition.

    #   * STOPPED: A stopped condition.
    result: typing.Union[str, "ExecutionResult"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The test's start time.
    started: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The test's stop time.
    stopped: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The test's result counters.
    counters: "Counters" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A message about the test's result.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Represents the total (metered or unmetered) minutes used by the test.
    device_minutes: "DeviceMinutes" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class TestType(str):
    BUILTIN_FUZZ = "BUILTIN_FUZZ"
    BUILTIN_EXPLORER = "BUILTIN_EXPLORER"
    WEB_PERFORMANCE_PROFILE = "WEB_PERFORMANCE_PROFILE"
    APPIUM_JAVA_JUNIT = "APPIUM_JAVA_JUNIT"
    APPIUM_JAVA_TESTNG = "APPIUM_JAVA_TESTNG"
    APPIUM_PYTHON = "APPIUM_PYTHON"
    APPIUM_WEB_JAVA_JUNIT = "APPIUM_WEB_JAVA_JUNIT"
    APPIUM_WEB_JAVA_TESTNG = "APPIUM_WEB_JAVA_TESTNG"
    APPIUM_WEB_PYTHON = "APPIUM_WEB_PYTHON"
    CALABASH = "CALABASH"
    INSTRUMENTATION = "INSTRUMENTATION"
    UIAUTOMATION = "UIAUTOMATION"
    UIAUTOMATOR = "UIAUTOMATOR"
    XCTEST = "XCTEST"
    XCTEST_UI = "XCTEST_UI"
    REMOTE_ACCESS_RECORD = "REMOTE_ACCESS_RECORD"
    REMOTE_ACCESS_REPLAY = "REMOTE_ACCESS_REPLAY"


@dataclasses.dataclass
class TrialMinutes(ShapeBase):
    """
    Represents information about free trial device minutes for an AWS account.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "total",
                "total",
                TypeInfo(float),
            ),
            (
                "remaining",
                "remaining",
                TypeInfo(float),
            ),
        ]

    # The total number of free trial minutes that the account started with.
    total: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of free trial minutes remaining in the account.
    remaining: float = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UniqueProblem(ShapeBase):
    """
    A collection of one or more problems, grouped by their result.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
            (
                "problems",
                "problems",
                TypeInfo(typing.List[Problem]),
            ),
        ]

    # A message about the unique problems' result.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the problems.
    problems: typing.List["Problem"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateDeviceInstanceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
            (
                "profile_arn",
                "profileArn",
                TypeInfo(str),
            ),
            (
                "labels",
                "labels",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The Amazon Resource Name (ARN) of the device instance.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the profile that you want to associate
    # with the device instance.
    profile_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of strings that you want to associate with the device instance.
    labels: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateDeviceInstanceResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "device_instance",
                "deviceInstance",
                TypeInfo(DeviceInstance),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An object containing information about your device instance.
    device_instance: "DeviceInstance" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateDevicePoolRequest(ShapeBase):
    """
    Represents a request to the update device pool operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
            (
                "rules",
                "rules",
                TypeInfo(typing.List[Rule]),
            ),
        ]

    # The Amazon Resourc Name (ARN) of the Device Farm device pool you wish to
    # update.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A string representing the name of the device pool you wish to update.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description of the device pool you wish to update.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Represents the rules you wish to modify for the device pool. Updating rules
    # is optional; however, if you choose to update rules for your request, the
    # update will replace the existing rules.
    rules: typing.List["Rule"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateDevicePoolResult(OutputShapeBase):
    """
    Represents the result of an update device pool request.
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
                "device_pool",
                "devicePool",
                TypeInfo(DevicePool),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The device pool you just updated.
    device_pool: "DevicePool" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateInstanceProfileRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
            (
                "package_cleanup",
                "packageCleanup",
                TypeInfo(bool),
            ),
            (
                "exclude_app_packages_from_cleanup",
                "excludeAppPackagesFromCleanup",
                TypeInfo(typing.List[str]),
            ),
            (
                "reboot_after_use",
                "rebootAfterUse",
                TypeInfo(bool),
            ),
        ]

    # The Amazon Resource Name (ARN) of the instance profile.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The updated name for your instance profile.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The updated description for your instance profile.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The updated choice for whether you want to specify package cleanup. The
    # default value is `false` for private devices.
    package_cleanup: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of strings specifying the list of app packages that should not be
    # cleaned up from the device after a test run is over.

    # The list of packages is only considered if you set `packageCleanup` to
    # `true`.
    exclude_app_packages_from_cleanup: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The updated choice for whether you want to reboot the device after use. The
    # default value is `true`.
    reboot_after_use: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateInstanceProfileResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "instance_profile",
                "instanceProfile",
                TypeInfo(InstanceProfile),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An object containing information about your instance profile.
    instance_profile: "InstanceProfile" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateNetworkProfileRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "description",
                "description",
                TypeInfo(str),
            ),
            (
                "type",
                "type",
                TypeInfo(typing.Union[str, NetworkProfileType]),
            ),
            (
                "uplink_bandwidth_bits",
                "uplinkBandwidthBits",
                TypeInfo(int),
            ),
            (
                "downlink_bandwidth_bits",
                "downlinkBandwidthBits",
                TypeInfo(int),
            ),
            (
                "uplink_delay_ms",
                "uplinkDelayMs",
                TypeInfo(int),
            ),
            (
                "downlink_delay_ms",
                "downlinkDelayMs",
                TypeInfo(int),
            ),
            (
                "uplink_jitter_ms",
                "uplinkJitterMs",
                TypeInfo(int),
            ),
            (
                "downlink_jitter_ms",
                "downlinkJitterMs",
                TypeInfo(int),
            ),
            (
                "uplink_loss_percent",
                "uplinkLossPercent",
                TypeInfo(int),
            ),
            (
                "downlink_loss_percent",
                "downlinkLossPercent",
                TypeInfo(int),
            ),
        ]

    # The Amazon Resource Name (ARN) of the project for which you want to update
    # network profile settings.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the network profile about which you are returning information.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The descriptoin of the network profile about which you are returning
    # information.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of network profile you wish to return information about. Valid
    # values are listed below.
    type: typing.Union[str, "NetworkProfileType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The data throughput rate in bits per second, as an integer from 0 to
    # 104857600.
    uplink_bandwidth_bits: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The data throughput rate in bits per second, as an integer from 0 to
    # 104857600.
    downlink_bandwidth_bits: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Delay time for all packets to destination in milliseconds as an integer
    # from 0 to 2000.
    uplink_delay_ms: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Delay time for all packets to destination in milliseconds as an integer
    # from 0 to 2000.
    downlink_delay_ms: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Time variation in the delay of received packets in milliseconds as an
    # integer from 0 to 2000.
    uplink_jitter_ms: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Time variation in the delay of received packets in milliseconds as an
    # integer from 0 to 2000.
    downlink_jitter_ms: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Proportion of transmitted packets that fail to arrive from 0 to 100
    # percent.
    uplink_loss_percent: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Proportion of received packets that fail to arrive from 0 to 100 percent.
    downlink_loss_percent: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateNetworkProfileResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "network_profile",
                "networkProfile",
                TypeInfo(NetworkProfile),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of the available network profiles.
    network_profile: "NetworkProfile" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateProjectRequest(ShapeBase):
    """
    Represents a request to the update project operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "default_job_timeout_minutes",
                "defaultJobTimeoutMinutes",
                TypeInfo(int),
            ),
        ]

    # The Amazon Resource Name (ARN) of the project whose name you wish to
    # update.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A string representing the new name of the project that you are updating.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of minutes a test run in the project will execute before it
    # times out.
    default_job_timeout_minutes: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateProjectResult(OutputShapeBase):
    """
    Represents the result of an update project request.
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
                "project",
                "project",
                TypeInfo(Project),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The project you wish to update.
    project: "Project" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateUploadRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "content_type",
                "contentType",
                TypeInfo(str),
            ),
            (
                "edit_content",
                "editContent",
                TypeInfo(bool),
            ),
        ]

    # The Amazon Resource Name (ARN) of the uploaded test spec.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The upload's test spec file name. The name should not contain the '/'
    # character. The test spec file name must end with the `.yaml` or `.yml` file
    # extension.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The upload's content type (for example, "application/x-yaml").
    content_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Set to true if the YAML file has changed and needs to be updated;
    # otherwise, set to false.
    edit_content: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateUploadResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "upload",
                "upload",
                TypeInfo(Upload),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A test spec uploaded to Device Farm.
    upload: "Upload" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateVPCEConfigurationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
            (
                "vpce_configuration_name",
                "vpceConfigurationName",
                TypeInfo(str),
            ),
            (
                "vpce_service_name",
                "vpceServiceName",
                TypeInfo(str),
            ),
            (
                "service_dns_name",
                "serviceDnsName",
                TypeInfo(str),
            ),
            (
                "vpce_configuration_description",
                "vpceConfigurationDescription",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the VPC endpoint configuration you want
    # to update.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The friendly name you give to your VPC endpoint configuration, to manage
    # your configurations more easily.
    vpce_configuration_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the VPC endpoint service running inside your AWS account that
    # you want Device Farm to test.
    vpce_service_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The DNS (domain) name used to connect to your private service in your
    # Amazon VPC. The DNS name must not already be in use on the Internet.
    service_dns_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional description, providing more details about your VPC endpoint
    # configuration.
    vpce_configuration_description: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateVPCEConfigurationResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "vpce_configuration",
                "vpceConfiguration",
                TypeInfo(VPCEConfiguration),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An object containing information about your VPC endpoint configuration.
    vpce_configuration: "VPCEConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Upload(ShapeBase):
    """
    An app or a set of one or more tests to upload or that have been uploaded.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
            (
                "name",
                "name",
                TypeInfo(str),
            ),
            (
                "created",
                "created",
                TypeInfo(datetime.datetime),
            ),
            (
                "type",
                "type",
                TypeInfo(typing.Union[str, UploadType]),
            ),
            (
                "status",
                "status",
                TypeInfo(typing.Union[str, UploadStatus]),
            ),
            (
                "url",
                "url",
                TypeInfo(str),
            ),
            (
                "metadata",
                "metadata",
                TypeInfo(str),
            ),
            (
                "content_type",
                "contentType",
                TypeInfo(str),
            ),
            (
                "message",
                "message",
                TypeInfo(str),
            ),
            (
                "category",
                "category",
                TypeInfo(typing.Union[str, UploadCategory]),
            ),
        ]

    # The upload's ARN.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The upload's file name.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When the upload was created.
    created: datetime.datetime = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The upload's type.

    # Must be one of the following values:

    #   * ANDROID_APP: An Android upload.

    #   * IOS_APP: An iOS upload.

    #   * WEB_APP: A web appliction upload.

    #   * EXTERNAL_DATA: An external data upload.

    #   * APPIUM_JAVA_JUNIT_TEST_PACKAGE: An Appium Java JUnit test package upload.

    #   * APPIUM_JAVA_TESTNG_TEST_PACKAGE: An Appium Java TestNG test package upload.

    #   * APPIUM_PYTHON_TEST_PACKAGE: An Appium Python test package upload.

    #   * APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE: An Appium Java JUnit test package upload.

    #   * APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE: An Appium Java TestNG test package upload.

    #   * APPIUM_WEB_PYTHON_TEST_PACKAGE: An Appium Python test package upload.

    #   * CALABASH_TEST_PACKAGE: A Calabash test package upload.

    #   * INSTRUMENTATION_TEST_PACKAGE: An instrumentation upload.

    #   * UIAUTOMATION_TEST_PACKAGE: A uiautomation test package upload.

    #   * UIAUTOMATOR_TEST_PACKAGE: A uiautomator test package upload.

    #   * XCTEST_TEST_PACKAGE: An XCode test package upload.

    #   * XCTEST_UI_TEST_PACKAGE: An XCode UI test package upload.
    type: typing.Union[str, "UploadType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The upload's status.

    # Must be one of the following values:

    #   * FAILED: A failed status.

    #   * INITIALIZED: An initialized status.

    #   * PROCESSING: A processing status.

    #   * SUCCEEDED: A succeeded status.
    status: typing.Union[str, "UploadStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pre-signed Amazon S3 URL that was used to store a file through a
    # corresponding PUT request.
    url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The upload's metadata. For example, for Android, this contains information
    # that is parsed from the manifest and is displayed in the AWS Device Farm
    # console after the associated app is uploaded.
    metadata: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The upload's content type (for example, "application/octet-stream").
    content_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A message about the upload's result.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The upload's category. Allowed values include:

    #   * CURATED: An upload managed by AWS Device Farm.

    #   * PRIVATE: An upload managed by the AWS Device Farm customer.
    category: typing.Union[str, "UploadCategory"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class UploadCategory(str):
    CURATED = "CURATED"
    PRIVATE = "PRIVATE"


class UploadStatus(str):
    INITIALIZED = "INITIALIZED"
    PROCESSING = "PROCESSING"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"


class UploadType(str):
    ANDROID_APP = "ANDROID_APP"
    IOS_APP = "IOS_APP"
    WEB_APP = "WEB_APP"
    EXTERNAL_DATA = "EXTERNAL_DATA"
    APPIUM_JAVA_JUNIT_TEST_PACKAGE = "APPIUM_JAVA_JUNIT_TEST_PACKAGE"
    APPIUM_JAVA_TESTNG_TEST_PACKAGE = "APPIUM_JAVA_TESTNG_TEST_PACKAGE"
    APPIUM_PYTHON_TEST_PACKAGE = "APPIUM_PYTHON_TEST_PACKAGE"
    APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE = "APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE"
    APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE = "APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE"
    APPIUM_WEB_PYTHON_TEST_PACKAGE = "APPIUM_WEB_PYTHON_TEST_PACKAGE"
    CALABASH_TEST_PACKAGE = "CALABASH_TEST_PACKAGE"
    INSTRUMENTATION_TEST_PACKAGE = "INSTRUMENTATION_TEST_PACKAGE"
    UIAUTOMATION_TEST_PACKAGE = "UIAUTOMATION_TEST_PACKAGE"
    UIAUTOMATOR_TEST_PACKAGE = "UIAUTOMATOR_TEST_PACKAGE"
    XCTEST_TEST_PACKAGE = "XCTEST_TEST_PACKAGE"
    XCTEST_UI_TEST_PACKAGE = "XCTEST_UI_TEST_PACKAGE"
    APPIUM_JAVA_JUNIT_TEST_SPEC = "APPIUM_JAVA_JUNIT_TEST_SPEC"
    APPIUM_JAVA_TESTNG_TEST_SPEC = "APPIUM_JAVA_TESTNG_TEST_SPEC"
    APPIUM_PYTHON_TEST_SPEC = "APPIUM_PYTHON_TEST_SPEC"
    APPIUM_WEB_JAVA_JUNIT_TEST_SPEC = "APPIUM_WEB_JAVA_JUNIT_TEST_SPEC"
    APPIUM_WEB_JAVA_TESTNG_TEST_SPEC = "APPIUM_WEB_JAVA_TESTNG_TEST_SPEC"
    APPIUM_WEB_PYTHON_TEST_SPEC = "APPIUM_WEB_PYTHON_TEST_SPEC"
    INSTRUMENTATION_TEST_SPEC = "INSTRUMENTATION_TEST_SPEC"
    XCTEST_UI_TEST_SPEC = "XCTEST_UI_TEST_SPEC"


@dataclasses.dataclass
class VPCEConfiguration(ShapeBase):
    """
    Represents an Amazon Virtual Private Cloud (VPC) endpoint configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                TypeInfo(str),
            ),
            (
                "vpce_configuration_name",
                "vpceConfigurationName",
                TypeInfo(str),
            ),
            (
                "vpce_service_name",
                "vpceServiceName",
                TypeInfo(str),
            ),
            (
                "service_dns_name",
                "serviceDnsName",
                TypeInfo(str),
            ),
            (
                "vpce_configuration_description",
                "vpceConfigurationDescription",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the VPC endpoint configuration.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The friendly name you give to your VPC endpoint configuration, to manage
    # your configurations more easily.
    vpce_configuration_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the VPC endpoint service running inside your AWS account that
    # you want Device Farm to test.
    vpce_service_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The DNS name that maps to the private IP address of the service you want to
    # access.
    service_dns_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional description, providing more details about your VPC endpoint
    # configuration.
    vpce_configuration_description: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
