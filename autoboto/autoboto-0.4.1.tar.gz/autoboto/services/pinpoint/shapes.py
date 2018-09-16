import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


@dataclasses.dataclass
class ADMChannelRequest(ShapeBase):
    """
    Amazon Device Messaging channel definition.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "client_id",
                "ClientId",
                TypeInfo(str),
            ),
            (
                "client_secret",
                "ClientSecret",
                TypeInfo(str),
            ),
            (
                "enabled",
                "Enabled",
                TypeInfo(bool),
            ),
        ]

    # The Client ID that you obtained from the Amazon App Distribution Portal.
    client_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Client Secret that you obtained from the Amazon App Distribution
    # Portal.
    client_secret: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether or not the channel is enabled for sending messages.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ADMChannelResponse(ShapeBase):
    """
    Amazon Device Messaging channel definition.
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
                "creation_date",
                "CreationDate",
                TypeInfo(str),
            ),
            (
                "enabled",
                "Enabled",
                TypeInfo(bool),
            ),
            (
                "has_credential",
                "HasCredential",
                TypeInfo(bool),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "is_archived",
                "IsArchived",
                TypeInfo(bool),
            ),
            (
                "last_modified_by",
                "LastModifiedBy",
                TypeInfo(str),
            ),
            (
                "last_modified_date",
                "LastModifiedDate",
                TypeInfo(str),
            ),
            (
                "platform",
                "Platform",
                TypeInfo(str),
            ),
            (
                "version",
                "Version",
                TypeInfo(int),
            ),
        ]

    # The ID of the application to which the channel applies.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time when this channel was created.
    creation_date: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether or not the channel is enabled for sending messages.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Not used. Retained for backwards compatibility.
    has_credential: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Deprecated) An identifier for the channel. Retained for backwards
    # compatibility.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether or not the channel is archived.
    is_archived: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The user who last updated this channel.
    last_modified_by: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time when this channel was last modified.
    last_modified_date: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The platform type. For this channel, the value is always "ADM."
    platform: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The channel version.
    version: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ADMMessage(ShapeBase):
    """
    ADM Message.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "action",
                "Action",
                TypeInfo(typing.Union[str, Action]),
            ),
            (
                "body",
                "Body",
                TypeInfo(str),
            ),
            (
                "consolidation_key",
                "ConsolidationKey",
                TypeInfo(str),
            ),
            (
                "data",
                "Data",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "expires_after",
                "ExpiresAfter",
                TypeInfo(str),
            ),
            (
                "icon_reference",
                "IconReference",
                TypeInfo(str),
            ),
            (
                "image_icon_url",
                "ImageIconUrl",
                TypeInfo(str),
            ),
            (
                "image_url",
                "ImageUrl",
                TypeInfo(str),
            ),
            (
                "md5",
                "MD5",
                TypeInfo(str),
            ),
            (
                "raw_content",
                "RawContent",
                TypeInfo(str),
            ),
            (
                "silent_push",
                "SilentPush",
                TypeInfo(bool),
            ),
            (
                "small_image_icon_url",
                "SmallImageIconUrl",
                TypeInfo(str),
            ),
            (
                "sound",
                "Sound",
                TypeInfo(str),
            ),
            (
                "substitutions",
                "Substitutions",
                TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
            (
                "title",
                "Title",
                TypeInfo(str),
            ),
            (
                "url",
                "Url",
                TypeInfo(str),
            ),
        ]

    # The action that occurs if the user taps a push notification delivered by
    # the campaign: OPEN_APP - Your app launches, or it becomes the foreground
    # app if it has been sent to the background. This is the default action.
    # DEEP_LINK - Uses deep linking features in iOS and Android to open your app
    # and display a designated user interface within the app. URL - The default
    # mobile browser on the user's device launches and opens a web page at the
    # URL you specify. Possible values include: OPEN_APP | DEEP_LINK | URL
    action: typing.Union[str, "Action"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The message body of the notification.
    body: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Optional. Arbitrary string used to indicate multiple messages are logically
    # the same and that ADM is allowed to drop previously enqueued messages in
    # favor of this one.
    consolidation_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The data payload used for a silent push. This payload is added to the
    # notifications' data.pinpoint.jsonBody' object
    data: typing.Dict[str, str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Optional. Number of seconds ADM should retain the message if the device is
    # offline
    expires_after: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The icon image name of the asset saved in your application.
    icon_reference: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The URL that points to an image used as the large icon to the notification
    # content view.
    image_icon_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The URL that points to an image used in the push notification.
    image_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Optional. Base-64-encoded MD5 checksum of the data parameter. Used to
    # verify data integrity
    md5: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Raw JSON formatted string to be used as the payload. This value
    # overrides the message.
    raw_content: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates if the message should display on the users device. Silent pushes
    # can be used for Remote Configuration and Phone Home use cases.
    silent_push: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The URL that points to an image used as the small icon for the notification
    # which will be used to represent the notification in the status bar and
    # content view
    small_image_icon_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates a sound to play when the device receives the notification.
    # Supports default, or the filename of a sound resource bundled in the app.
    # Android sound files must reside in /res/raw/
    sound: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Default message substitutions. Can be overridden by individual address
    # substitutions.
    substitutions: typing.Dict[str, typing.List[str]] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The message title that displays above the message on the user's device.
    title: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The URL to open in the user's mobile browser. Used if the value for Action
    # is URL.
    url: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class APNSChannelRequest(ShapeBase):
    """
    Apple Push Notification Service channel definition.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bundle_id",
                "BundleId",
                TypeInfo(str),
            ),
            (
                "certificate",
                "Certificate",
                TypeInfo(str),
            ),
            (
                "default_authentication_method",
                "DefaultAuthenticationMethod",
                TypeInfo(str),
            ),
            (
                "enabled",
                "Enabled",
                TypeInfo(bool),
            ),
            (
                "private_key",
                "PrivateKey",
                TypeInfo(str),
            ),
            (
                "team_id",
                "TeamId",
                TypeInfo(str),
            ),
            (
                "token_key",
                "TokenKey",
                TypeInfo(str),
            ),
            (
                "token_key_id",
                "TokenKeyId",
                TypeInfo(str),
            ),
        ]

    # The bundle id used for APNs Tokens.
    bundle_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The distribution certificate from Apple.
    certificate: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The default authentication method used for APNs.
    default_authentication_method: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the channel is enabled for sending messages.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The certificate private key.
    private_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The team id used for APNs Tokens.
    team_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token key used for APNs Tokens.
    token_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token key used for APNs Tokens.
    token_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class APNSChannelResponse(ShapeBase):
    """
    Apple Distribution Push Notification Service channel definition.
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
                "creation_date",
                "CreationDate",
                TypeInfo(str),
            ),
            (
                "default_authentication_method",
                "DefaultAuthenticationMethod",
                TypeInfo(str),
            ),
            (
                "enabled",
                "Enabled",
                TypeInfo(bool),
            ),
            (
                "has_credential",
                "HasCredential",
                TypeInfo(bool),
            ),
            (
                "has_token_key",
                "HasTokenKey",
                TypeInfo(bool),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "is_archived",
                "IsArchived",
                TypeInfo(bool),
            ),
            (
                "last_modified_by",
                "LastModifiedBy",
                TypeInfo(str),
            ),
            (
                "last_modified_date",
                "LastModifiedDate",
                TypeInfo(str),
            ),
            (
                "platform",
                "Platform",
                TypeInfo(str),
            ),
            (
                "version",
                "Version",
                TypeInfo(int),
            ),
        ]

    # The ID of the application that the channel applies to.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time when this channel was created.
    creation_date: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The default authentication method used for APNs.
    default_authentication_method: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the channel is enabled for sending messages.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Not used. Retained for backwards compatibility.
    has_credential: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether the channel is configured with a key for APNs token
    # authentication. Provide a token key by setting the TokenKey attribute.
    has_token_key: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Deprecated) An identifier for the channel. Retained for backwards
    # compatibility.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether or not the channel is archived.
    is_archived: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The user who last updated this channel.
    last_modified_by: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time when this channel was last modified.
    last_modified_date: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The platform type. For this channel, the value is always "ADM."
    platform: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The channel version.
    version: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class APNSMessage(ShapeBase):
    """
    APNS Message.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "action",
                "Action",
                TypeInfo(typing.Union[str, Action]),
            ),
            (
                "badge",
                "Badge",
                TypeInfo(int),
            ),
            (
                "body",
                "Body",
                TypeInfo(str),
            ),
            (
                "category",
                "Category",
                TypeInfo(str),
            ),
            (
                "collapse_id",
                "CollapseId",
                TypeInfo(str),
            ),
            (
                "data",
                "Data",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "media_url",
                "MediaUrl",
                TypeInfo(str),
            ),
            (
                "preferred_authentication_method",
                "PreferredAuthenticationMethod",
                TypeInfo(str),
            ),
            (
                "priority",
                "Priority",
                TypeInfo(str),
            ),
            (
                "raw_content",
                "RawContent",
                TypeInfo(str),
            ),
            (
                "silent_push",
                "SilentPush",
                TypeInfo(bool),
            ),
            (
                "sound",
                "Sound",
                TypeInfo(str),
            ),
            (
                "substitutions",
                "Substitutions",
                TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
            (
                "thread_id",
                "ThreadId",
                TypeInfo(str),
            ),
            (
                "time_to_live",
                "TimeToLive",
                TypeInfo(int),
            ),
            (
                "title",
                "Title",
                TypeInfo(str),
            ),
            (
                "url",
                "Url",
                TypeInfo(str),
            ),
        ]

    # The action that occurs if the user taps a push notification delivered by
    # the campaign: OPEN_APP - Your app launches, or it becomes the foreground
    # app if it has been sent to the background. This is the default action.
    # DEEP_LINK - Uses deep linking features in iOS and Android to open your app
    # and display a designated user interface within the app. URL - The default
    # mobile browser on the user's device launches and opens a web page at the
    # URL you specify. Possible values include: OPEN_APP | DEEP_LINK | URL
    action: typing.Union[str, "Action"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Include this key when you want the system to modify the badge of your app
    # icon. If this key is not included in the dictionary, the badge is not
    # changed. To remove the badge, set the value of this key to 0.
    badge: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The message body of the notification.
    body: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Provide this key with a string value that represents the notification's
    # type. This value corresponds to the value in the identifier property of one
    # of your app's registered categories.
    category: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An ID that, if assigned to multiple messages, causes APNs to coalesce the
    # messages into a single push notification instead of delivering each message
    # individually. The value must not exceed 64 bytes. Amazon Pinpoint uses this
    # value to set the apns-collapse-id request header when it sends the message
    # to APNs.
    collapse_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The data payload used for a silent push. This payload is added to the
    # notifications' data.pinpoint.jsonBody' object
    data: typing.Dict[str, str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The URL that points to a video used in the push notification.
    media_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The preferred authentication method, either "CERTIFICATE" or "TOKEN"
    preferred_authentication_method: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The message priority. Amazon Pinpoint uses this value to set the apns-
    # priority request header when it sends the message to APNs. Accepts the
    # following values: "5" - Low priority. Messages might be delayed, delivered
    # in groups, and throttled. "10" - High priority. Messages are sent
    # immediately. High priority messages must cause an alert, sound, or badge on
    # the receiving device. The default value is "10". The equivalent values for
    # FCM or GCM messages are "normal" and "high". Amazon Pinpoint accepts these
    # values for APNs messages and converts them. For more information about the
    # apns-priority parameter, see Communicating with APNs in the APNs Local and
    # Remote Notification Programming Guide.
    priority: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Raw JSON formatted string to be used as the payload. This value
    # overrides the message.
    raw_content: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates if the message should display on the users device. Silent pushes
    # can be used for Remote Configuration and Phone Home use cases.
    silent_push: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Include this key when you want the system to play a sound. The value of
    # this key is the name of a sound file in your app's main bundle or in the
    # Library/Sounds folder of your app's data container. If the sound file
    # cannot be found, or if you specify defaultfor the value, the system plays
    # the default alert sound.
    sound: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Default message substitutions. Can be overridden by individual address
    # substitutions.
    substitutions: typing.Dict[str, typing.List[str]] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Provide this key with a string value that represents the app-specific
    # identifier for grouping notifications. If you provide a Notification
    # Content app extension, you can use this value to group your notifications
    # together.
    thread_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The length of time (in seconds) that APNs stores and attempts to deliver
    # the message. If the value is 0, APNs does not store the message or attempt
    # to deliver it more than once. Amazon Pinpoint uses this value to set the
    # apns-expiration request header when it sends the message to APNs.
    time_to_live: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The message title that displays above the message on the user's device.
    title: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The URL to open in the user's mobile browser. Used if the value for Action
    # is URL.
    url: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class APNSSandboxChannelRequest(ShapeBase):
    """
    Apple Development Push Notification Service channel definition.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bundle_id",
                "BundleId",
                TypeInfo(str),
            ),
            (
                "certificate",
                "Certificate",
                TypeInfo(str),
            ),
            (
                "default_authentication_method",
                "DefaultAuthenticationMethod",
                TypeInfo(str),
            ),
            (
                "enabled",
                "Enabled",
                TypeInfo(bool),
            ),
            (
                "private_key",
                "PrivateKey",
                TypeInfo(str),
            ),
            (
                "team_id",
                "TeamId",
                TypeInfo(str),
            ),
            (
                "token_key",
                "TokenKey",
                TypeInfo(str),
            ),
            (
                "token_key_id",
                "TokenKeyId",
                TypeInfo(str),
            ),
        ]

    # The bundle id used for APNs Tokens.
    bundle_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The distribution certificate from Apple.
    certificate: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The default authentication method used for APNs.
    default_authentication_method: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the channel is enabled for sending messages.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The certificate private key.
    private_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The team id used for APNs Tokens.
    team_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token key used for APNs Tokens.
    token_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token key used for APNs Tokens.
    token_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class APNSSandboxChannelResponse(ShapeBase):
    """
    Apple Development Push Notification Service channel definition.
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
                "creation_date",
                "CreationDate",
                TypeInfo(str),
            ),
            (
                "default_authentication_method",
                "DefaultAuthenticationMethod",
                TypeInfo(str),
            ),
            (
                "enabled",
                "Enabled",
                TypeInfo(bool),
            ),
            (
                "has_credential",
                "HasCredential",
                TypeInfo(bool),
            ),
            (
                "has_token_key",
                "HasTokenKey",
                TypeInfo(bool),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "is_archived",
                "IsArchived",
                TypeInfo(bool),
            ),
            (
                "last_modified_by",
                "LastModifiedBy",
                TypeInfo(str),
            ),
            (
                "last_modified_date",
                "LastModifiedDate",
                TypeInfo(str),
            ),
            (
                "platform",
                "Platform",
                TypeInfo(str),
            ),
            (
                "version",
                "Version",
                TypeInfo(int),
            ),
        ]

    # The ID of the application to which the channel applies.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When was this segment created
    creation_date: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The default authentication method used for APNs.
    default_authentication_method: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the channel is enabled for sending messages.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Not used. Retained for backwards compatibility.
    has_credential: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether the channel is configured with a key for APNs token
    # authentication. Provide a token key by setting the TokenKey attribute.
    has_token_key: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Channel ID. Not used, only for backwards compatibility.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Is this channel archived
    is_archived: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Who last updated this entry
    last_modified_by: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Last date this was updated
    last_modified_date: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The platform type. Will be APNS_SANDBOX.
    platform: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Version of channel
    version: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class APNSVoipChannelRequest(ShapeBase):
    """
    Apple VoIP Push Notification Service channel definition.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bundle_id",
                "BundleId",
                TypeInfo(str),
            ),
            (
                "certificate",
                "Certificate",
                TypeInfo(str),
            ),
            (
                "default_authentication_method",
                "DefaultAuthenticationMethod",
                TypeInfo(str),
            ),
            (
                "enabled",
                "Enabled",
                TypeInfo(bool),
            ),
            (
                "private_key",
                "PrivateKey",
                TypeInfo(str),
            ),
            (
                "team_id",
                "TeamId",
                TypeInfo(str),
            ),
            (
                "token_key",
                "TokenKey",
                TypeInfo(str),
            ),
            (
                "token_key_id",
                "TokenKeyId",
                TypeInfo(str),
            ),
        ]

    # The bundle id used for APNs Tokens.
    bundle_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The distribution certificate from Apple.
    certificate: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The default authentication method used for APNs.
    default_authentication_method: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the channel is enabled for sending messages.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The certificate private key.
    private_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The team id used for APNs Tokens.
    team_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token key used for APNs Tokens.
    token_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token key used for APNs Tokens.
    token_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class APNSVoipChannelResponse(ShapeBase):
    """
    Apple VoIP Push Notification Service channel definition.
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
                "creation_date",
                "CreationDate",
                TypeInfo(str),
            ),
            (
                "default_authentication_method",
                "DefaultAuthenticationMethod",
                TypeInfo(str),
            ),
            (
                "enabled",
                "Enabled",
                TypeInfo(bool),
            ),
            (
                "has_credential",
                "HasCredential",
                TypeInfo(bool),
            ),
            (
                "has_token_key",
                "HasTokenKey",
                TypeInfo(bool),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "is_archived",
                "IsArchived",
                TypeInfo(bool),
            ),
            (
                "last_modified_by",
                "LastModifiedBy",
                TypeInfo(str),
            ),
            (
                "last_modified_date",
                "LastModifiedDate",
                TypeInfo(str),
            ),
            (
                "platform",
                "Platform",
                TypeInfo(str),
            ),
            (
                "version",
                "Version",
                TypeInfo(int),
            ),
        ]

    # Application id
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When was this segment created
    creation_date: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The default authentication method used for APNs.
    default_authentication_method: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the channel is enabled for sending messages.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Not used. Retained for backwards compatibility.
    has_credential: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If the channel is registered with a token key for authentication.
    has_token_key: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Channel ID. Not used, only for backwards compatibility.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Is this channel archived
    is_archived: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Who made the last change
    last_modified_by: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Last date this was updated
    last_modified_date: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The platform type. Will be APNS.
    platform: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Version of channel
    version: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class APNSVoipSandboxChannelRequest(ShapeBase):
    """
    Apple VoIP Developer Push Notification Service channel definition.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bundle_id",
                "BundleId",
                TypeInfo(str),
            ),
            (
                "certificate",
                "Certificate",
                TypeInfo(str),
            ),
            (
                "default_authentication_method",
                "DefaultAuthenticationMethod",
                TypeInfo(str),
            ),
            (
                "enabled",
                "Enabled",
                TypeInfo(bool),
            ),
            (
                "private_key",
                "PrivateKey",
                TypeInfo(str),
            ),
            (
                "team_id",
                "TeamId",
                TypeInfo(str),
            ),
            (
                "token_key",
                "TokenKey",
                TypeInfo(str),
            ),
            (
                "token_key_id",
                "TokenKeyId",
                TypeInfo(str),
            ),
        ]

    # The bundle id used for APNs Tokens.
    bundle_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The distribution certificate from Apple.
    certificate: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The default authentication method used for APNs.
    default_authentication_method: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the channel is enabled for sending messages.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The certificate private key.
    private_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The team id used for APNs Tokens.
    team_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token key used for APNs Tokens.
    token_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token key used for APNs Tokens.
    token_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class APNSVoipSandboxChannelResponse(ShapeBase):
    """
    Apple VoIP Developer Push Notification Service channel definition.
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
                "creation_date",
                "CreationDate",
                TypeInfo(str),
            ),
            (
                "default_authentication_method",
                "DefaultAuthenticationMethod",
                TypeInfo(str),
            ),
            (
                "enabled",
                "Enabled",
                TypeInfo(bool),
            ),
            (
                "has_credential",
                "HasCredential",
                TypeInfo(bool),
            ),
            (
                "has_token_key",
                "HasTokenKey",
                TypeInfo(bool),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "is_archived",
                "IsArchived",
                TypeInfo(bool),
            ),
            (
                "last_modified_by",
                "LastModifiedBy",
                TypeInfo(str),
            ),
            (
                "last_modified_date",
                "LastModifiedDate",
                TypeInfo(str),
            ),
            (
                "platform",
                "Platform",
                TypeInfo(str),
            ),
            (
                "version",
                "Version",
                TypeInfo(int),
            ),
        ]

    # Application id
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When was this segment created
    creation_date: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The default authentication method used for APNs.
    default_authentication_method: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the channel is enabled for sending messages.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Not used. Retained for backwards compatibility.
    has_credential: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If the channel is registered with a token key for authentication.
    has_token_key: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Channel ID. Not used, only for backwards compatibility.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Is this channel archived
    is_archived: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Who made the last change
    last_modified_by: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Last date this was updated
    last_modified_date: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The platform type. Will be APNS.
    platform: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Version of channel
    version: int = dataclasses.field(default=ShapeBase.NOT_SET, )


class Action(str):
    OPEN_APP = "OPEN_APP"
    DEEP_LINK = "DEEP_LINK"
    URL = "URL"


@dataclasses.dataclass
class ActivitiesResponse(ShapeBase):
    """
    Activities for campaign.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "item",
                "Item",
                TypeInfo(typing.List[ActivityResponse]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # List of campaign activities
    item: typing.List["ActivityResponse"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The string that you use in a subsequent request to get the next page of
    # results in a paginated response.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ActivityResponse(ShapeBase):
    """
    Activity definition
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
                "campaign_id",
                "CampaignId",
                TypeInfo(str),
            ),
            (
                "end",
                "End",
                TypeInfo(str),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "result",
                "Result",
                TypeInfo(str),
            ),
            (
                "scheduled_start",
                "ScheduledStart",
                TypeInfo(str),
            ),
            (
                "start",
                "Start",
                TypeInfo(str),
            ),
            (
                "state",
                "State",
                TypeInfo(str),
            ),
            (
                "successful_endpoint_count",
                "SuccessfulEndpointCount",
                TypeInfo(int),
            ),
            (
                "timezones_completed_count",
                "TimezonesCompletedCount",
                TypeInfo(int),
            ),
            (
                "timezones_total_count",
                "TimezonesTotalCount",
                TypeInfo(int),
            ),
            (
                "total_endpoint_count",
                "TotalEndpointCount",
                TypeInfo(int),
            ),
            (
                "treatment_id",
                "TreatmentId",
                TypeInfo(str),
            ),
        ]

    # The ID of the application to which the campaign applies.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the campaign to which the activity applies.
    campaign_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The actual time the activity was marked CANCELLED or COMPLETED. Provided in
    # ISO 8601 format.
    end: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique activity ID.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether the activity succeeded. Valid values: SUCCESS, FAIL
    result: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The scheduled start time for the activity in ISO 8601 format.
    scheduled_start: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The actual start time of the activity in ISO 8601 format.
    start: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The state of the activity. Valid values: PENDING, INITIALIZING, RUNNING,
    # PAUSED, CANCELLED, COMPLETED
    state: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The total number of endpoints to which the campaign successfully delivered
    # messages.
    successful_endpoint_count: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The total number of timezones completed.
    timezones_completed_count: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The total number of unique timezones present in the segment.
    timezones_total_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The total number of endpoints to which the campaign attempts to deliver
    # messages.
    total_endpoint_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of a variation of the campaign used for A/B testing.
    treatment_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AddressConfiguration(ShapeBase):
    """
    Address configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "body_override",
                "BodyOverride",
                TypeInfo(str),
            ),
            (
                "channel_type",
                "ChannelType",
                TypeInfo(typing.Union[str, ChannelType]),
            ),
            (
                "context",
                "Context",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "raw_content",
                "RawContent",
                TypeInfo(str),
            ),
            (
                "substitutions",
                "Substitutions",
                TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
            (
                "title_override",
                "TitleOverride",
                TypeInfo(str),
            ),
        ]

    # Body override. If specified will override default body.
    body_override: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The channel type. Valid values: GCM | APNS | APNS_SANDBOX | APNS_VOIP |
    # APNS_VOIP_SANDBOX | ADM | SMS | EMAIL | BAIDU
    channel_type: typing.Union[str, "ChannelType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A map of custom attributes to attributes to be attached to the message for
    # this address. This payload is added to the push notification's
    # 'data.pinpoint' object or added to the email/sms delivery receipt event
    # attributes.
    context: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Raw JSON formatted string to be used as the payload. This value
    # overrides the message.
    raw_content: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A map of substitution values for the message to be merged with the
    # DefaultMessage's substitutions. Substitutions on this map take precedence
    # over the all other substitutions.
    substitutions: typing.Dict[str, typing.List[str]] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Title override. If specified will override default title if applicable.
    title_override: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ApplicationResponse(ShapeBase):
    """
    Application Response.
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
        ]

    # The unique application ID.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The display name of the application.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ApplicationSettingsResource(ShapeBase):
    """
    Application settings.
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
                "campaign_hook",
                "CampaignHook",
                TypeInfo(CampaignHook),
            ),
            (
                "last_modified_date",
                "LastModifiedDate",
                TypeInfo(str),
            ),
            (
                "limits",
                "Limits",
                TypeInfo(CampaignLimits),
            ),
            (
                "quiet_time",
                "QuietTime",
                TypeInfo(QuietTime),
            ),
        ]

    # The unique ID for the application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Default campaign hook.
    campaign_hook: "CampaignHook" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date that the settings were last updated in ISO 8601 format.
    last_modified_date: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The default campaign limits for the app. These limits apply to each
    # campaign for the app, unless the campaign overrides the default with limits
    # of its own.
    limits: "CampaignLimits" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The default quiet time for the app. Each campaign for this app sends no
    # messages during this time unless the campaign overrides the default with a
    # quiet time of its own.
    quiet_time: "QuietTime" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ApplicationsResponse(ShapeBase):
    """
    Get Applications Result.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "item",
                "Item",
                TypeInfo(typing.List[ApplicationResponse]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # List of applications returned in this page.
    item: typing.List["ApplicationResponse"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The string that you use in a subsequent request to get the next page of
    # results in a paginated response.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AttributeDimension(ShapeBase):
    """
    Custom attibute dimension
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attribute_type",
                "AttributeType",
                TypeInfo(typing.Union[str, AttributeType]),
            ),
            (
                "values",
                "Values",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The type of dimension: INCLUSIVE - Endpoints that match the criteria are
    # included in the segment. EXCLUSIVE - Endpoints that match the criteria are
    # excluded from the segment.
    attribute_type: typing.Union[str, "AttributeType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The criteria values for the segment dimension. Endpoints with matching
    # attribute values are included or excluded from the segment, depending on
    # the setting for Type.
    values: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


class AttributeType(str):
    INCLUSIVE = "INCLUSIVE"
    EXCLUSIVE = "EXCLUSIVE"


@dataclasses.dataclass
class AttributesResource(ShapeBase):
    """
    Attributes.
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
                "attribute_type",
                "AttributeType",
                TypeInfo(str),
            ),
            (
                "attributes",
                "Attributes",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The unique ID for the application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The attribute type for the application.
    attribute_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The attributes for the application.
    attributes: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BadRequestException(ShapeBase):
    """
    Simple message object.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
            (
                "request_id",
                "RequestID",
                TypeInfo(str),
            ),
        ]

    # The error message that's returned from the API.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique message body ID.
    request_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BaiduChannelRequest(ShapeBase):
    """
    Baidu Cloud Push credentials
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "api_key",
                "ApiKey",
                TypeInfo(str),
            ),
            (
                "enabled",
                "Enabled",
                TypeInfo(bool),
            ),
            (
                "secret_key",
                "SecretKey",
                TypeInfo(str),
            ),
        ]

    # Platform credential API key from Baidu.
    api_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If the channel is enabled for sending messages.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Platform credential Secret key from Baidu.
    secret_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BaiduChannelResponse(ShapeBase):
    """
    Baidu Cloud Messaging channel definition
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
                "creation_date",
                "CreationDate",
                TypeInfo(str),
            ),
            (
                "credential",
                "Credential",
                TypeInfo(str),
            ),
            (
                "enabled",
                "Enabled",
                TypeInfo(bool),
            ),
            (
                "has_credential",
                "HasCredential",
                TypeInfo(bool),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "is_archived",
                "IsArchived",
                TypeInfo(bool),
            ),
            (
                "last_modified_by",
                "LastModifiedBy",
                TypeInfo(str),
            ),
            (
                "last_modified_date",
                "LastModifiedDate",
                TypeInfo(str),
            ),
            (
                "platform",
                "Platform",
                TypeInfo(str),
            ),
            (
                "version",
                "Version",
                TypeInfo(int),
            ),
        ]

    # Application id
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When was this segment created
    creation_date: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Baidu API key from Baidu.
    credential: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If the channel is enabled for sending messages.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Not used. Retained for backwards compatibility.
    has_credential: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Channel ID. Not used, only for backwards compatibility.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Is this channel archived
    is_archived: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Who made the last change
    last_modified_by: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Last date this was updated
    last_modified_date: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The platform type. Will be BAIDU
    platform: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Version of channel
    version: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BaiduMessage(ShapeBase):
    """
    Baidu Message.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "action",
                "Action",
                TypeInfo(typing.Union[str, Action]),
            ),
            (
                "body",
                "Body",
                TypeInfo(str),
            ),
            (
                "data",
                "Data",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "icon_reference",
                "IconReference",
                TypeInfo(str),
            ),
            (
                "image_icon_url",
                "ImageIconUrl",
                TypeInfo(str),
            ),
            (
                "image_url",
                "ImageUrl",
                TypeInfo(str),
            ),
            (
                "raw_content",
                "RawContent",
                TypeInfo(str),
            ),
            (
                "silent_push",
                "SilentPush",
                TypeInfo(bool),
            ),
            (
                "small_image_icon_url",
                "SmallImageIconUrl",
                TypeInfo(str),
            ),
            (
                "sound",
                "Sound",
                TypeInfo(str),
            ),
            (
                "substitutions",
                "Substitutions",
                TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
            (
                "time_to_live",
                "TimeToLive",
                TypeInfo(int),
            ),
            (
                "title",
                "Title",
                TypeInfo(str),
            ),
            (
                "url",
                "Url",
                TypeInfo(str),
            ),
        ]

    # The action that occurs if the user taps a push notification delivered by
    # the campaign: OPEN_APP - Your app launches, or it becomes the foreground
    # app if it has been sent to the background. This is the default action.
    # DEEP_LINK - Uses deep linking features in iOS and Android to open your app
    # and display a designated user interface within the app. URL - The default
    # mobile browser on the user's device launches and opens a web page at the
    # URL you specify. Possible values include: OPEN_APP | DEEP_LINK | URL
    action: typing.Union[str, "Action"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The message body of the notification.
    body: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The data payload used for a silent push. This payload is added to the
    # notifications' data.pinpoint.jsonBody' object
    data: typing.Dict[str, str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The icon image name of the asset saved in your application.
    icon_reference: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The URL that points to an image used as the large icon to the notification
    # content view.
    image_icon_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The URL that points to an image used in the push notification.
    image_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Raw JSON formatted string to be used as the payload. This value
    # overrides the message.
    raw_content: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates if the message should display on the users device. Silent pushes
    # can be used for Remote Configuration and Phone Home use cases.
    silent_push: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The URL that points to an image used as the small icon for the notification
    # which will be used to represent the notification in the status bar and
    # content view
    small_image_icon_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates a sound to play when the device receives the notification.
    # Supports default, or the filename of a sound resource bundled in the app.
    # Android sound files must reside in /res/raw/
    sound: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Default message substitutions. Can be overridden by individual address
    # substitutions.
    substitutions: typing.Dict[str, typing.List[str]] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # This parameter specifies how long (in seconds) the message should be kept
    # in Baidu storage if the device is offline. The and the default value and
    # the maximum time to live supported is 7 days (604800 seconds)
    time_to_live: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The message title that displays above the message on the user's device.
    title: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The URL to open in the user's mobile browser. Used if the value for Action
    # is URL.
    url: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CampaignEmailMessage(ShapeBase):
    """
    The email message configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "body",
                "Body",
                TypeInfo(str),
            ),
            (
                "from_address",
                "FromAddress",
                TypeInfo(str),
            ),
            (
                "html_body",
                "HtmlBody",
                TypeInfo(str),
            ),
            (
                "title",
                "Title",
                TypeInfo(str),
            ),
        ]

    # The email text body.
    body: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The email address used to send the email from. Defaults to use FromAddress
    # specified in the Email Channel.
    from_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The email html body.
    html_body: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The email title (Or subject).
    title: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CampaignHook(ShapeBase):
    """
    Campaign hook information.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "lambda_function_name",
                "LambdaFunctionName",
                TypeInfo(str),
            ),
            (
                "mode",
                "Mode",
                TypeInfo(typing.Union[str, Mode]),
            ),
            (
                "web_url",
                "WebUrl",
                TypeInfo(str),
            ),
        ]

    # Lambda function name or arn to be called for delivery
    lambda_function_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # What mode Lambda should be invoked in.
    mode: typing.Union[str, "Mode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Web URL to call for hook. If the URL has authentication specified it will
    # be added as authentication to the request
    web_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CampaignLimits(ShapeBase):
    """
    Campaign Limits are used to limit the number of messages that can be sent to a
    user.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "daily",
                "Daily",
                TypeInfo(int),
            ),
            (
                "maximum_duration",
                "MaximumDuration",
                TypeInfo(int),
            ),
            (
                "messages_per_second",
                "MessagesPerSecond",
                TypeInfo(int),
            ),
            (
                "total",
                "Total",
                TypeInfo(int),
            ),
        ]

    # The maximum number of messages that the campaign can send daily.
    daily: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The length of time (in seconds) that the campaign can run before it ends
    # and message deliveries stop. This duration begins at the scheduled start
    # time for the campaign. The minimum value is 60.
    maximum_duration: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of messages that the campaign can send per second. The minimum
    # value is 50, and the maximum is 20000.
    messages_per_second: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum total number of messages that the campaign can send.
    total: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CampaignResponse(ShapeBase):
    """
    Campaign definition
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "additional_treatments",
                "AdditionalTreatments",
                TypeInfo(typing.List[TreatmentResource]),
            ),
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
            (
                "creation_date",
                "CreationDate",
                TypeInfo(str),
            ),
            (
                "default_state",
                "DefaultState",
                TypeInfo(CampaignState),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "holdout_percent",
                "HoldoutPercent",
                TypeInfo(int),
            ),
            (
                "hook",
                "Hook",
                TypeInfo(CampaignHook),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "is_paused",
                "IsPaused",
                TypeInfo(bool),
            ),
            (
                "last_modified_date",
                "LastModifiedDate",
                TypeInfo(str),
            ),
            (
                "limits",
                "Limits",
                TypeInfo(CampaignLimits),
            ),
            (
                "message_configuration",
                "MessageConfiguration",
                TypeInfo(MessageConfiguration),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "schedule",
                "Schedule",
                TypeInfo(Schedule),
            ),
            (
                "segment_id",
                "SegmentId",
                TypeInfo(str),
            ),
            (
                "segment_version",
                "SegmentVersion",
                TypeInfo(int),
            ),
            (
                "state",
                "State",
                TypeInfo(CampaignState),
            ),
            (
                "treatment_description",
                "TreatmentDescription",
                TypeInfo(str),
            ),
            (
                "treatment_name",
                "TreatmentName",
                TypeInfo(str),
            ),
            (
                "version",
                "Version",
                TypeInfo(int),
            ),
        ]

    # Treatments that are defined in addition to the default treatment.
    additional_treatments: typing.List["TreatmentResource"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the application to which the campaign applies.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date the campaign was created in ISO 8601 format.
    creation_date: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the campaign's default treatment. Only present for A/B test
    # campaigns.
    default_state: "CampaignState" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A description of the campaign.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The allocated percentage of end users who will not receive messages from
    # this campaign.
    holdout_percent: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Campaign hook information.
    hook: "CampaignHook" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique campaign ID.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether the campaign is paused. A paused campaign does not send
    # messages unless you resume it by setting IsPaused to false.
    is_paused: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date the campaign was last updated in ISO 8601 format.
    last_modified_date: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The campaign limits settings.
    limits: "CampaignLimits" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The message configuration settings.
    message_configuration: "MessageConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The custom name of the campaign.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The campaign schedule.
    schedule: "Schedule" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the segment to which the campaign sends messages.
    segment_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version of the segment to which the campaign sends messages.
    segment_version: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The campaign status. An A/B test campaign will have a status of COMPLETED
    # only when all treatments have a status of COMPLETED.
    state: "CampaignState" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A custom description for the treatment.
    treatment_description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The custom name of a variation of the campaign used for A/B testing.
    treatment_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The campaign version number.
    version: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CampaignSmsMessage(ShapeBase):
    """
    SMS message configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "body",
                "Body",
                TypeInfo(str),
            ),
            (
                "message_type",
                "MessageType",
                TypeInfo(typing.Union[str, MessageType]),
            ),
            (
                "sender_id",
                "SenderId",
                TypeInfo(str),
            ),
        ]

    # The SMS text body.
    body: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Is this is a transactional SMS message, otherwise a promotional message.
    message_type: typing.Union[str, "MessageType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Sender ID of sent message.
    sender_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CampaignState(ShapeBase):
    """
    State of the Campaign
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "campaign_status",
                "CampaignStatus",
                TypeInfo(typing.Union[str, CampaignStatus]),
            ),
        ]

    # The status of the campaign, or the status of a treatment that belongs to an
    # A/B test campaign. Valid values: SCHEDULED, EXECUTING, PENDING_NEXT_RUN,
    # COMPLETED, PAUSED
    campaign_status: typing.Union[str, "CampaignStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class CampaignStatus(str):
    SCHEDULED = "SCHEDULED"
    EXECUTING = "EXECUTING"
    PENDING_NEXT_RUN = "PENDING_NEXT_RUN"
    COMPLETED = "COMPLETED"
    PAUSED = "PAUSED"
    DELETED = "DELETED"


@dataclasses.dataclass
class CampaignsResponse(ShapeBase):
    """
    List of available campaigns.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "item",
                "Item",
                TypeInfo(typing.List[CampaignResponse]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # A list of campaigns.
    item: typing.List["CampaignResponse"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The string that you use in a subsequent request to get the next page of
    # results in a paginated response.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ChannelResponse(ShapeBase):
    """
    Base definition for channel response.
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
                "creation_date",
                "CreationDate",
                TypeInfo(str),
            ),
            (
                "enabled",
                "Enabled",
                TypeInfo(bool),
            ),
            (
                "has_credential",
                "HasCredential",
                TypeInfo(bool),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "is_archived",
                "IsArchived",
                TypeInfo(bool),
            ),
            (
                "last_modified_by",
                "LastModifiedBy",
                TypeInfo(str),
            ),
            (
                "last_modified_date",
                "LastModifiedDate",
                TypeInfo(str),
            ),
            (
                "version",
                "Version",
                TypeInfo(int),
            ),
        ]

    # Application id
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When was this segment created
    creation_date: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If the channel is enabled for sending messages.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Not used. Retained for backwards compatibility.
    has_credential: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Channel ID. Not used, only for backwards compatibility.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Is this channel archived
    is_archived: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Who made the last change
    last_modified_by: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Last date this was updated
    last_modified_date: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Version of channel
    version: int = dataclasses.field(default=ShapeBase.NOT_SET, )


class ChannelType(str):
    GCM = "GCM"
    APNS = "APNS"
    APNS_SANDBOX = "APNS_SANDBOX"
    APNS_VOIP = "APNS_VOIP"
    APNS_VOIP_SANDBOX = "APNS_VOIP_SANDBOX"
    ADM = "ADM"
    SMS = "SMS"
    EMAIL = "EMAIL"
    BAIDU = "BAIDU"
    CUSTOM = "CUSTOM"


@dataclasses.dataclass
class ChannelsResponse(ShapeBase):
    """
    Get channels definition
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "channels",
                "Channels",
                TypeInfo(typing.Dict[str, ChannelResponse]),
            ),
        ]

    # A map of channels, with the ChannelType as the key and the Channel as the
    # value.
    channels: typing.Dict[str, "ChannelResponse"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateAppRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "create_application_request",
                "CreateApplicationRequest",
                TypeInfo(CreateApplicationRequest),
            ),
        ]

    # Application Request.
    create_application_request: "CreateApplicationRequest" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateAppResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "application_response",
                "ApplicationResponse",
                TypeInfo(ApplicationResponse),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Application Response.
    application_response: "ApplicationResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateApplicationRequest(ShapeBase):
    """
    Application Request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The display name of the application. Used in the Amazon Pinpoint console.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateCampaignRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
            (
                "write_campaign_request",
                "WriteCampaignRequest",
                TypeInfo(WriteCampaignRequest),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Used to create a campaign.
    write_campaign_request: "WriteCampaignRequest" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateCampaignResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "campaign_response",
                "CampaignResponse",
                TypeInfo(CampaignResponse),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Campaign definition
    campaign_response: "CampaignResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateExportJobRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
            (
                "export_job_request",
                "ExportJobRequest",
                TypeInfo(ExportJobRequest),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Export job request.
    export_job_request: "ExportJobRequest" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateExportJobResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "export_job_response",
                "ExportJobResponse",
                TypeInfo(ExportJobResponse),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Export job response.
    export_job_response: "ExportJobResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateImportJobRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
            (
                "import_job_request",
                "ImportJobRequest",
                TypeInfo(ImportJobRequest),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Import job request.
    import_job_request: "ImportJobRequest" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateImportJobResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "import_job_response",
                "ImportJobResponse",
                TypeInfo(ImportJobResponse),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Import job response.
    import_job_response: "ImportJobResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateSegmentRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
            (
                "write_segment_request",
                "WriteSegmentRequest",
                TypeInfo(WriteSegmentRequest),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Segment definition.
    write_segment_request: "WriteSegmentRequest" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateSegmentResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "segment_response",
                "SegmentResponse",
                TypeInfo(SegmentResponse),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Segment definition.
    segment_response: "SegmentResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DefaultMessage(ShapeBase):
    """
    The default message to use across all channels.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "body",
                "Body",
                TypeInfo(str),
            ),
            (
                "substitutions",
                "Substitutions",
                TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
        ]

    # The message body of the notification, the email body or the text message.
    body: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Default message substitutions. Can be overridden by individual address
    # substitutions.
    substitutions: typing.Dict[str, typing.List[str]] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DefaultPushNotificationMessage(ShapeBase):
    """
    Default Push Notification Message.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "action",
                "Action",
                TypeInfo(typing.Union[str, Action]),
            ),
            (
                "body",
                "Body",
                TypeInfo(str),
            ),
            (
                "data",
                "Data",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "silent_push",
                "SilentPush",
                TypeInfo(bool),
            ),
            (
                "substitutions",
                "Substitutions",
                TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
            (
                "title",
                "Title",
                TypeInfo(str),
            ),
            (
                "url",
                "Url",
                TypeInfo(str),
            ),
        ]

    # The action that occurs if the user taps a push notification delivered by
    # the campaign: OPEN_APP - Your app launches, or it becomes the foreground
    # app if it has been sent to the background. This is the default action.
    # DEEP_LINK - Uses deep linking features in iOS and Android to open your app
    # and display a designated user interface within the app. URL - The default
    # mobile browser on the user's device launches and opens a web page at the
    # URL you specify. Possible values include: OPEN_APP | DEEP_LINK | URL
    action: typing.Union[str, "Action"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The message body of the notification.
    body: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The data payload used for a silent push. This payload is added to the
    # notifications' data.pinpoint.jsonBody' object
    data: typing.Dict[str, str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates if the message should display on the users device. Silent pushes
    # can be used for Remote Configuration and Phone Home use cases.
    silent_push: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Default message substitutions. Can be overridden by individual address
    # substitutions.
    substitutions: typing.Dict[str, typing.List[str]] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The message title that displays above the message on the user's device.
    title: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The URL to open in the user's mobile browser. Used if the value for Action
    # is URL.
    url: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteAdmChannelRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteAdmChannelResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "adm_channel_response",
                "ADMChannelResponse",
                TypeInfo(ADMChannelResponse),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Amazon Device Messaging channel definition.
    adm_channel_response: "ADMChannelResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteApnsChannelRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteApnsChannelResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "apns_channel_response",
                "APNSChannelResponse",
                TypeInfo(APNSChannelResponse),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Apple Distribution Push Notification Service channel definition.
    apns_channel_response: "APNSChannelResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteApnsSandboxChannelRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteApnsSandboxChannelResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "apns_sandbox_channel_response",
                "APNSSandboxChannelResponse",
                TypeInfo(APNSSandboxChannelResponse),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Apple Development Push Notification Service channel definition.
    apns_sandbox_channel_response: "APNSSandboxChannelResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteApnsVoipChannelRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteApnsVoipChannelResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "apns_voip_channel_response",
                "APNSVoipChannelResponse",
                TypeInfo(APNSVoipChannelResponse),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Apple VoIP Push Notification Service channel definition.
    apns_voip_channel_response: "APNSVoipChannelResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteApnsVoipSandboxChannelRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteApnsVoipSandboxChannelResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "apns_voip_sandbox_channel_response",
                "APNSVoipSandboxChannelResponse",
                TypeInfo(APNSVoipSandboxChannelResponse),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Apple VoIP Developer Push Notification Service channel definition.
    apns_voip_sandbox_channel_response: "APNSVoipSandboxChannelResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteAppRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteAppResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "application_response",
                "ApplicationResponse",
                TypeInfo(ApplicationResponse),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Application Response.
    application_response: "ApplicationResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteBaiduChannelRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteBaiduChannelResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "baidu_channel_response",
                "BaiduChannelResponse",
                TypeInfo(BaiduChannelResponse),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Baidu Cloud Messaging channel definition
    baidu_channel_response: "BaiduChannelResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteCampaignRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
            (
                "campaign_id",
                "CampaignId",
                TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique ID of the campaign.
    campaign_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteCampaignResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "campaign_response",
                "CampaignResponse",
                TypeInfo(CampaignResponse),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Campaign definition
    campaign_response: "CampaignResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteEmailChannelRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteEmailChannelResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "email_channel_response",
                "EmailChannelResponse",
                TypeInfo(EmailChannelResponse),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Email Channel Response.
    email_channel_response: "EmailChannelResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteEndpointRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
            (
                "endpoint_id",
                "EndpointId",
                TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique ID of the endpoint.
    endpoint_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteEndpointResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "endpoint_response",
                "EndpointResponse",
                TypeInfo(EndpointResponse),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Endpoint response
    endpoint_response: "EndpointResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteEventStreamRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteEventStreamResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "event_stream",
                "EventStream",
                TypeInfo(EventStream),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Model for an event publishing subscription export.
    event_stream: "EventStream" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteGcmChannelRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteGcmChannelResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "gcm_channel_response",
                "GCMChannelResponse",
                TypeInfo(GCMChannelResponse),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Google Cloud Messaging channel definition
    gcm_channel_response: "GCMChannelResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteSegmentRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
            (
                "segment_id",
                "SegmentId",
                TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique ID of the segment.
    segment_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteSegmentResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "segment_response",
                "SegmentResponse",
                TypeInfo(SegmentResponse),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Segment definition.
    segment_response: "SegmentResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteSmsChannelRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteSmsChannelResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "sms_channel_response",
                "SMSChannelResponse",
                TypeInfo(SMSChannelResponse),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # SMS Channel Response.
    sms_channel_response: "SMSChannelResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteUserEndpointsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
            (
                "user_id",
                "UserId",
                TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique ID of the user.
    user_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteUserEndpointsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "endpoints_response",
                "EndpointsResponse",
                TypeInfo(EndpointsResponse),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # List of endpoints
    endpoints_response: "EndpointsResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class DeliveryStatus(str):
    SUCCESSFUL = "SUCCESSFUL"
    THROTTLED = "THROTTLED"
    TEMPORARY_FAILURE = "TEMPORARY_FAILURE"
    PERMANENT_FAILURE = "PERMANENT_FAILURE"
    UNKNOWN_FAILURE = "UNKNOWN_FAILURE"
    OPT_OUT = "OPT_OUT"
    DUPLICATE = "DUPLICATE"


class DimensionType(str):
    INCLUSIVE = "INCLUSIVE"
    EXCLUSIVE = "EXCLUSIVE"


@dataclasses.dataclass
class DirectMessageConfiguration(ShapeBase):
    """
    Message definitions for the default message and any messages that are tailored
    for specific channels.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "adm_message",
                "ADMMessage",
                TypeInfo(ADMMessage),
            ),
            (
                "apns_message",
                "APNSMessage",
                TypeInfo(APNSMessage),
            ),
            (
                "baidu_message",
                "BaiduMessage",
                TypeInfo(BaiduMessage),
            ),
            (
                "default_message",
                "DefaultMessage",
                TypeInfo(DefaultMessage),
            ),
            (
                "default_push_notification_message",
                "DefaultPushNotificationMessage",
                TypeInfo(DefaultPushNotificationMessage),
            ),
            (
                "gcm_message",
                "GCMMessage",
                TypeInfo(GCMMessage),
            ),
            (
                "sms_message",
                "SMSMessage",
                TypeInfo(SMSMessage),
            ),
        ]

    # The message to ADM channels. Overrides the default push notification
    # message.
    adm_message: "ADMMessage" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The message to APNS channels. Overrides the default push notification
    # message.
    apns_message: "APNSMessage" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The message to Baidu GCM channels. Overrides the default push notification
    # message.
    baidu_message: "BaiduMessage" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The default message for all channels.
    default_message: "DefaultMessage" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The default push notification message for all push channels.
    default_push_notification_message: "DefaultPushNotificationMessage" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The message to GCM channels. Overrides the default push notification
    # message.
    gcm_message: "GCMMessage" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The message to SMS channels. Overrides the default message.
    sms_message: "SMSMessage" = dataclasses.field(default=ShapeBase.NOT_SET, )


class Duration(str):
    HR_24 = "HR_24"
    DAY_7 = "DAY_7"
    DAY_14 = "DAY_14"
    DAY_30 = "DAY_30"


@dataclasses.dataclass
class EmailChannelRequest(ShapeBase):
    """
    Email Channel Request
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "enabled",
                "Enabled",
                TypeInfo(bool),
            ),
            (
                "from_address",
                "FromAddress",
                TypeInfo(str),
            ),
            (
                "identity",
                "Identity",
                TypeInfo(str),
            ),
            (
                "role_arn",
                "RoleArn",
                TypeInfo(str),
            ),
        ]

    # If the channel is enabled for sending messages.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The email address used to send emails from.
    from_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of an identity verified with SES.
    identity: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of an IAM Role used to submit events to Mobile Analytics' event
    # ingestion service
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EmailChannelResponse(ShapeBase):
    """
    Email Channel Response.
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
                "creation_date",
                "CreationDate",
                TypeInfo(str),
            ),
            (
                "enabled",
                "Enabled",
                TypeInfo(bool),
            ),
            (
                "from_address",
                "FromAddress",
                TypeInfo(str),
            ),
            (
                "has_credential",
                "HasCredential",
                TypeInfo(bool),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "identity",
                "Identity",
                TypeInfo(str),
            ),
            (
                "is_archived",
                "IsArchived",
                TypeInfo(bool),
            ),
            (
                "last_modified_by",
                "LastModifiedBy",
                TypeInfo(str),
            ),
            (
                "last_modified_date",
                "LastModifiedDate",
                TypeInfo(str),
            ),
            (
                "messages_per_second",
                "MessagesPerSecond",
                TypeInfo(int),
            ),
            (
                "platform",
                "Platform",
                TypeInfo(str),
            ),
            (
                "role_arn",
                "RoleArn",
                TypeInfo(str),
            ),
            (
                "version",
                "Version",
                TypeInfo(int),
            ),
        ]

    # The unique ID of the application to which the email channel belongs.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date that the settings were last updated in ISO 8601 format.
    creation_date: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If the channel is enabled for sending messages.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The email address used to send emails from.
    from_address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Not used. Retained for backwards compatibility.
    has_credential: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Channel ID. Not used, only for backwards compatibility.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of an identity verified with SES.
    identity: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Is this channel archived
    is_archived: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Who last updated this entry
    last_modified_by: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Last date this was updated
    last_modified_date: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Messages per second that can be sent
    messages_per_second: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Platform type. Will be "EMAIL"
    platform: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of an IAM Role used to submit events to Mobile Analytics' event
    # ingestion service
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Version of channel
    version: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EndpointBatchItem(ShapeBase):
    """
    Endpoint update request
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "address",
                "Address",
                TypeInfo(str),
            ),
            (
                "attributes",
                "Attributes",
                TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
            (
                "channel_type",
                "ChannelType",
                TypeInfo(typing.Union[str, ChannelType]),
            ),
            (
                "demographic",
                "Demographic",
                TypeInfo(EndpointDemographic),
            ),
            (
                "effective_date",
                "EffectiveDate",
                TypeInfo(str),
            ),
            (
                "endpoint_status",
                "EndpointStatus",
                TypeInfo(str),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "location",
                "Location",
                TypeInfo(EndpointLocation),
            ),
            (
                "metrics",
                "Metrics",
                TypeInfo(typing.Dict[str, float]),
            ),
            (
                "opt_out",
                "OptOut",
                TypeInfo(str),
            ),
            (
                "request_id",
                "RequestId",
                TypeInfo(str),
            ),
            (
                "user",
                "User",
                TypeInfo(EndpointUser),
            ),
        ]

    # The destination for messages that you send to this endpoint. The address
    # varies by channel. For mobile push channels, use the token provided by the
    # push notification service, such as the APNs device token or the FCM
    # registration token. For the SMS channel, use a phone number in E.164
    # format, such as +12065550100. For the email channel, use an email address.
    address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Custom attributes that describe the endpoint by associating a name with an
    # array of values. For example, an attribute named "interests" might have the
    # values ["science", "politics", "travel"]. You can use these attributes as
    # selection criteria when you create a segment of users to engage with a
    # messaging campaign. The following characters are not recommended in
    # attribute names: # : ? \ /. The Amazon Pinpoint console does not display
    # attributes that include these characters in the name. This limitation does
    # not apply to attribute values.
    attributes: typing.Dict[str, typing.List[str]] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The channel type. Valid values: GCM | APNS | APNS_SANDBOX | APNS_VOIP |
    # APNS_VOIP_SANDBOX | ADM | SMS | EMAIL | BAIDU
    channel_type: typing.Union[str, "ChannelType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The endpoint demographic attributes.
    demographic: "EndpointDemographic" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The last time the endpoint was updated. Provided in ISO 8601 format.
    effective_date: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unused.
    endpoint_status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique Id for the Endpoint in the batch.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The endpoint location attributes.
    location: "EndpointLocation" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Custom metrics that your app reports to Amazon Pinpoint.
    metrics: typing.Dict[str, float] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates whether a user has opted out of receiving messages with one of
    # the following values: ALL - User has opted out of all messages. NONE -
    # Users has not opted out and receives all messages.
    opt_out: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique ID for the most recent request to update the endpoint.
    request_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Custom user-specific attributes that your app reports to Amazon Pinpoint.
    user: "EndpointUser" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EndpointBatchRequest(ShapeBase):
    """
    Endpoint batch update request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "item",
                "Item",
                TypeInfo(typing.List[EndpointBatchItem]),
            ),
        ]

    # List of items to update. Maximum 100 items
    item: typing.List["EndpointBatchItem"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class EndpointDemographic(ShapeBase):
    """
    Demographic information about the endpoint.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "app_version",
                "AppVersion",
                TypeInfo(str),
            ),
            (
                "locale",
                "Locale",
                TypeInfo(str),
            ),
            (
                "make",
                "Make",
                TypeInfo(str),
            ),
            (
                "model",
                "Model",
                TypeInfo(str),
            ),
            (
                "model_version",
                "ModelVersion",
                TypeInfo(str),
            ),
            (
                "platform",
                "Platform",
                TypeInfo(str),
            ),
            (
                "platform_version",
                "PlatformVersion",
                TypeInfo(str),
            ),
            (
                "timezone",
                "Timezone",
                TypeInfo(str),
            ),
        ]

    # The version of the application associated with the endpoint.
    app_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The endpoint locale in the following format: The ISO 639-1 alpha-2 code,
    # followed by an underscore, followed by an ISO 3166-1 alpha-2 value.
    locale: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The manufacturer of the endpoint device, such as Apple or Samsung.
    make: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The model name or number of the endpoint device, such as iPhone.
    model: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The model version of the endpoint device.
    model_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The platform of the endpoint device, such as iOS or Android.
    platform: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The platform version of the endpoint device.
    platform_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The timezone of the endpoint. Specified as a tz database value, such as
    # Americas/Los_Angeles.
    timezone: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EndpointItemResponse(ShapeBase):
    """
    The responses that are returned after you create or update an endpoint and
    record an event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
            (
                "status_code",
                "StatusCode",
                TypeInfo(int),
            ),
        ]

    # A custom message associated with the registration of an endpoint when
    # issuing a response.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status code to respond with for a particular endpoint id after endpoint
    # registration
    status_code: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EndpointLocation(ShapeBase):
    """
    Location data for the endpoint.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "city",
                "City",
                TypeInfo(str),
            ),
            (
                "country",
                "Country",
                TypeInfo(str),
            ),
            (
                "latitude",
                "Latitude",
                TypeInfo(float),
            ),
            (
                "longitude",
                "Longitude",
                TypeInfo(float),
            ),
            (
                "postal_code",
                "PostalCode",
                TypeInfo(str),
            ),
            (
                "region",
                "Region",
                TypeInfo(str),
            ),
        ]

    # The city where the endpoint is located.
    city: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The two-letter code for the country or region of the endpoint. Specified as
    # an ISO 3166-1 Alpha-2 code, such as "US" for the United States.
    country: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The latitude of the endpoint location, rounded to one decimal place.
    latitude: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The longitude of the endpoint location, rounded to one decimal place.
    longitude: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The postal code or zip code of the endpoint.
    postal_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The region of the endpoint location. For example, in the United States,
    # this corresponds to a state.
    region: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EndpointMessageResult(ShapeBase):
    """
    The result from sending a message to an endpoint.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "address",
                "Address",
                TypeInfo(str),
            ),
            (
                "delivery_status",
                "DeliveryStatus",
                TypeInfo(typing.Union[str, DeliveryStatus]),
            ),
            (
                "message_id",
                "MessageId",
                TypeInfo(str),
            ),
            (
                "status_code",
                "StatusCode",
                TypeInfo(int),
            ),
            (
                "status_message",
                "StatusMessage",
                TypeInfo(str),
            ),
            (
                "updated_token",
                "UpdatedToken",
                TypeInfo(str),
            ),
        ]

    # Address that endpoint message was delivered to.
    address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The delivery status of the message. Possible values: SUCCESS - The message
    # was successfully delivered to the endpoint. TRANSIENT_FAILURE - A temporary
    # error occurred. Amazon Pinpoint will attempt to deliver the message again
    # later. FAILURE_PERMANENT - An error occurred when delivering the message to
    # the endpoint. Amazon Pinpoint won't attempt to send the message again.
    # TIMEOUT - The message couldn't be sent within the timeout period.
    # QUIET_TIME - The local time for the endpoint was within the Quiet Hours for
    # the campaign. DAILY_CAP - The endpoint has received the maximum number of
    # messages it can receive within a 24-hour period. HOLDOUT - The endpoint was
    # in a hold out treatment for the campaign. THROTTLED - Amazon Pinpoint
    # throttled sending to this endpoint. EXPIRED - The endpoint address is
    # expired. CAMPAIGN_CAP - The endpoint received the maximum number of
    # messages allowed by the campaign. SERVICE_FAILURE - A service-level failure
    # prevented Amazon Pinpoint from delivering the message. UNKNOWN - An unknown
    # error occurred.
    delivery_status: typing.Union[str, "DeliveryStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Unique message identifier associated with the message that was sent.
    message_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Downstream service status code.
    status_code: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Status message for message delivery.
    status_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If token was updated as part of delivery. (This is GCM Specific)
    updated_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EndpointRequest(ShapeBase):
    """
    Endpoint update request
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "address",
                "Address",
                TypeInfo(str),
            ),
            (
                "attributes",
                "Attributes",
                TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
            (
                "channel_type",
                "ChannelType",
                TypeInfo(typing.Union[str, ChannelType]),
            ),
            (
                "demographic",
                "Demographic",
                TypeInfo(EndpointDemographic),
            ),
            (
                "effective_date",
                "EffectiveDate",
                TypeInfo(str),
            ),
            (
                "endpoint_status",
                "EndpointStatus",
                TypeInfo(str),
            ),
            (
                "location",
                "Location",
                TypeInfo(EndpointLocation),
            ),
            (
                "metrics",
                "Metrics",
                TypeInfo(typing.Dict[str, float]),
            ),
            (
                "opt_out",
                "OptOut",
                TypeInfo(str),
            ),
            (
                "request_id",
                "RequestId",
                TypeInfo(str),
            ),
            (
                "user",
                "User",
                TypeInfo(EndpointUser),
            ),
        ]

    # The destination for messages that you send to this endpoint. The address
    # varies by channel. For mobile push channels, use the token provided by the
    # push notification service, such as the APNs device token or the FCM
    # registration token. For the SMS channel, use a phone number in E.164
    # format, such as +12065550100. For the email channel, use an email address.
    address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Custom attributes that describe the endpoint by associating a name with an
    # array of values. For example, an attribute named "interests" might have the
    # values ["science", "politics", "travel"]. You can use these attributes as
    # selection criteria when you create a segment of users to engage with a
    # messaging campaign. The following characters are not recommended in
    # attribute names: # : ? \ /. The Amazon Pinpoint console does not display
    # attributes that include these characters in the name. This limitation does
    # not apply to attribute values.
    attributes: typing.Dict[str, typing.List[str]] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The channel type. Valid values: GCM | APNS | APNS_SANDBOX | APNS_VOIP |
    # APNS_VOIP_SANDBOX | ADM | SMS | EMAIL | BAIDU
    channel_type: typing.Union[str, "ChannelType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Demographic attributes for the endpoint.
    demographic: "EndpointDemographic" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time when the endpoint was updated, shown in ISO 8601 format.
    effective_date: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unused.
    endpoint_status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The endpoint location attributes.
    location: "EndpointLocation" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Custom metrics that your app reports to Amazon Pinpoint.
    metrics: typing.Dict[str, float] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates whether a user has opted out of receiving messages with one of
    # the following values: ALL - User has opted out of all messages. NONE -
    # Users has not opted out and receives all messages.
    opt_out: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique ID for the most recent request to update the endpoint.
    request_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Custom user-specific attributes that your app reports to Amazon Pinpoint.
    user: "EndpointUser" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EndpointResponse(ShapeBase):
    """
    Endpoint response
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "address",
                "Address",
                TypeInfo(str),
            ),
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
            (
                "attributes",
                "Attributes",
                TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
            (
                "channel_type",
                "ChannelType",
                TypeInfo(typing.Union[str, ChannelType]),
            ),
            (
                "cohort_id",
                "CohortId",
                TypeInfo(str),
            ),
            (
                "creation_date",
                "CreationDate",
                TypeInfo(str),
            ),
            (
                "demographic",
                "Demographic",
                TypeInfo(EndpointDemographic),
            ),
            (
                "effective_date",
                "EffectiveDate",
                TypeInfo(str),
            ),
            (
                "endpoint_status",
                "EndpointStatus",
                TypeInfo(str),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "location",
                "Location",
                TypeInfo(EndpointLocation),
            ),
            (
                "metrics",
                "Metrics",
                TypeInfo(typing.Dict[str, float]),
            ),
            (
                "opt_out",
                "OptOut",
                TypeInfo(str),
            ),
            (
                "request_id",
                "RequestId",
                TypeInfo(str),
            ),
            (
                "user",
                "User",
                TypeInfo(EndpointUser),
            ),
        ]

    # The address of the endpoint as provided by your push provider. For example,
    # the DeviceToken or RegistrationId.
    address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the application that is associated with the endpoint.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Custom attributes that describe the endpoint by associating a name with an
    # array of values. For example, an attribute named "interests" might have the
    # following values: ["science", "politics", "travel"]. You can use these
    # attributes as selection criteria when you create segments. The Amazon
    # Pinpoint console can't display attribute names that include the following
    # characters: hash/pound sign (#), colon (:), question mark (?), backslash
    # (\\), and forward slash (/). For this reason, you should avoid using these
    # characters in the names of custom attributes.
    attributes: typing.Dict[str, typing.List[str]] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The channel type. Valid values: GCM | APNS | APNS_SANDBOX | APNS_VOIP |
    # APNS_VOIP_SANDBOX | ADM | SMS | EMAIL | BAIDU
    channel_type: typing.Union[str, "ChannelType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A number from 0-99 that represents the cohort the endpoint is assigned to.
    # Endpoints are grouped into cohorts randomly, and each cohort contains
    # approximately 1 percent of the endpoints for an app. Amazon Pinpoint
    # assigns cohorts to the holdout or treatment allocations for a campaign.
    cohort_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time when the endpoint was created, shown in ISO 8601 format.
    creation_date: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The endpoint demographic attributes.
    demographic: "EndpointDemographic" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time when the endpoint was last updated, shown in ISO 8601
    # format.
    effective_date: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unused.
    endpoint_status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique ID that you assigned to the endpoint. The ID should be a
    # globally unique identifier (GUID) to ensure that it doesn't conflict with
    # other endpoint IDs associated with the application.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The endpoint location attributes.
    location: "EndpointLocation" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Custom metrics that your app reports to Amazon Pinpoint.
    metrics: typing.Dict[str, float] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates whether a user has opted out of receiving messages with one of
    # the following values: ALL - User has opted out of all messages. NONE -
    # Users has not opted out and receives all messages.
    opt_out: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique ID for the most recent request to update the endpoint.
    request_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Custom user-specific attributes that your app reports to Amazon Pinpoint.
    user: "EndpointUser" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EndpointSendConfiguration(ShapeBase):
    """
    Endpoint send configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "body_override",
                "BodyOverride",
                TypeInfo(str),
            ),
            (
                "context",
                "Context",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "raw_content",
                "RawContent",
                TypeInfo(str),
            ),
            (
                "substitutions",
                "Substitutions",
                TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
            (
                "title_override",
                "TitleOverride",
                TypeInfo(str),
            ),
        ]

    # Body override. If specified will override default body.
    body_override: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A map of custom attributes to attributes to be attached to the message for
    # this address. This payload is added to the push notification's
    # 'data.pinpoint' object or added to the email/sms delivery receipt event
    # attributes.
    context: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Raw JSON formatted string to be used as the payload. This value
    # overrides the message.
    raw_content: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A map of substitution values for the message to be merged with the
    # DefaultMessage's substitutions. Substitutions on this map take precedence
    # over the all other substitutions.
    substitutions: typing.Dict[str, typing.List[str]] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Title override. If specified will override default title if applicable.
    title_override: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EndpointUser(ShapeBase):
    """
    Endpoint user specific custom userAttributes
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "user_attributes",
                "UserAttributes",
                TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
            (
                "user_id",
                "UserId",
                TypeInfo(str),
            ),
        ]

    # Custom attributes that describe the user by associating a name with an
    # array of values. For example, an attribute named "interests" might have the
    # following values: ["science", "politics", "travel"]. You can use these
    # attributes as selection criteria when you create segments. The Amazon
    # Pinpoint console can't display attribute names that include the following
    # characters: hash/pound sign (#), colon (:), question mark (?), backslash
    # (\\), and forward slash (/). For this reason, you should avoid using these
    # characters in the names of custom attributes.
    user_attributes: typing.Dict[str, typing.List[str]] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unique ID of the user.
    user_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EndpointsResponse(ShapeBase):
    """
    List of endpoints
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "item",
                "Item",
                TypeInfo(typing.List[EndpointResponse]),
            ),
        ]

    # The list of endpoints.
    item: typing.List["EndpointResponse"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Event(ShapeBase):
    """
    Model for creating or updating events.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attributes",
                "Attributes",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "client_sdk_version",
                "ClientSdkVersion",
                TypeInfo(str),
            ),
            (
                "event_type",
                "EventType",
                TypeInfo(str),
            ),
            (
                "metrics",
                "Metrics",
                TypeInfo(typing.Dict[str, float]),
            ),
            (
                "session",
                "Session",
                TypeInfo(Session),
            ),
            (
                "timestamp",
                "Timestamp",
                TypeInfo(str),
            ),
        ]

    # Custom attributes that are associated with the event you're adding or
    # updating.
    attributes: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The version of the SDK that's running on the client device.
    client_sdk_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the custom event that you're recording.
    event_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Event metrics
    metrics: typing.Dict[str, float] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The session
    session: "Session" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time when the event occurred, in ISO 8601 format.
    timestamp: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EventItemResponse(ShapeBase):
    """
    The responses that are returned after you record an event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
            (
                "status_code",
                "StatusCode",
                TypeInfo(int),
            ),
        ]

    # A custom message that is associated with the processing of an event.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status code to respond with for a particular event id
    status_code: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EventStream(ShapeBase):
    """
    Model for an event publishing subscription export.
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
                "destination_stream_arn",
                "DestinationStreamArn",
                TypeInfo(str),
            ),
            (
                "external_id",
                "ExternalId",
                TypeInfo(str),
            ),
            (
                "last_modified_date",
                "LastModifiedDate",
                TypeInfo(str),
            ),
            (
                "last_updated_by",
                "LastUpdatedBy",
                TypeInfo(str),
            ),
            (
                "role_arn",
                "RoleArn",
                TypeInfo(str),
            ),
        ]

    # The ID of the application from which events should be published.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the Amazon Kinesis stream or Firehose
    # delivery stream to which you want to publish events. Firehose ARN:
    # arn:aws:firehose:REGION:ACCOUNT_ID:deliverystream/STREAM_NAME Kinesis ARN:
    # arn:aws:kinesis:REGION:ACCOUNT_ID:stream/STREAM_NAME
    destination_stream_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Deprecated) Your AWS account ID, which you assigned to the ExternalID key
    # in an IAM trust policy. Used by Amazon Pinpoint to assume an IAM role. This
    # requirement is removed, and external IDs are not recommended for IAM roles
    # assumed by Amazon Pinpoint.
    external_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date the event stream was last updated in ISO 8601 format.
    last_modified_date: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The IAM user who last modified the event stream.
    last_updated_by: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The IAM role that authorizes Amazon Pinpoint to publish events to the
    # stream in your account.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EventsBatch(ShapeBase):
    """
    Events batch definition
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "endpoint",
                "Endpoint",
                TypeInfo(PublicEndpoint),
            ),
            (
                "events",
                "Events",
                TypeInfo(typing.Dict[str, Event]),
            ),
        ]

    # Endpoint information
    endpoint: "PublicEndpoint" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Events
    events: typing.Dict[str, "Event"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class EventsRequest(ShapeBase):
    """
    Put Events request
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "batch_item",
                "BatchItem",
                TypeInfo(typing.Dict[str, EventsBatch]),
            ),
        ]

    # Batch of events with endpoint id as the key and an object of EventsBatch as
    # value. The EventsBatch object has the PublicEndpoint and a map of event
    # Id's to events
    batch_item: typing.Dict[str, "EventsBatch"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class EventsResponse(ShapeBase):
    """
    The results from processing a put events request
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "results",
                "Results",
                TypeInfo(typing.Dict[str, ItemResponse]),
            ),
        ]

    # A map containing a multi part response for each endpoint, with the endpoint
    # id as the key and item response as the value
    results: typing.Dict[str, "ItemResponse"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ExportJobRequest(ShapeBase):
    """
    Export job request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_arn",
                "RoleArn",
                TypeInfo(str),
            ),
            (
                "s3_url_prefix",
                "S3UrlPrefix",
                TypeInfo(str),
            ),
            (
                "segment_id",
                "SegmentId",
                TypeInfo(str),
            ),
            (
                "segment_version",
                "SegmentVersion",
                TypeInfo(int),
            ),
        ]

    # The Amazon Resource Name (ARN) of an IAM role that grants Amazon Pinpoint
    # access to the Amazon S3 location that endpoints will be exported to.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A URL that points to the location within an Amazon S3 bucket that will
    # receive the export. The location is typically a folder with multiple files.
    # The URL should follow this format: s3://bucket-name/folder-name/ Amazon
    # Pinpoint will export endpoints to this location.
    s3_url_prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the segment to export endpoints from. If not present, Amazon
    # Pinpoint exports all of the endpoints that belong to the application.
    segment_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version of the segment to export if specified.
    segment_version: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ExportJobResource(ShapeBase):
    """
    Export job resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role_arn",
                "RoleArn",
                TypeInfo(str),
            ),
            (
                "s3_url_prefix",
                "S3UrlPrefix",
                TypeInfo(str),
            ),
            (
                "segment_id",
                "SegmentId",
                TypeInfo(str),
            ),
            (
                "segment_version",
                "SegmentVersion",
                TypeInfo(int),
            ),
        ]

    # The Amazon Resource Name (ARN) of an IAM role that grants Amazon Pinpoint
    # access to the Amazon S3 location that endpoints will be exported to.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A URL that points to the location within an Amazon S3 bucket that will
    # receive the export. The location is typically a folder with multiple files.
    # The URL should follow this format: s3://bucket-name/folder-name/ Amazon
    # Pinpoint will export endpoints to this location.
    s3_url_prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the segment to export endpoints from. If not present, Amazon
    # Pinpoint exports all of the endpoints that belong to the application.
    segment_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version of the segment to export if specified.
    segment_version: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ExportJobResponse(ShapeBase):
    """
    Export job response.
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
                "completed_pieces",
                "CompletedPieces",
                TypeInfo(int),
            ),
            (
                "completion_date",
                "CompletionDate",
                TypeInfo(str),
            ),
            (
                "creation_date",
                "CreationDate",
                TypeInfo(str),
            ),
            (
                "definition",
                "Definition",
                TypeInfo(ExportJobResource),
            ),
            (
                "failed_pieces",
                "FailedPieces",
                TypeInfo(int),
            ),
            (
                "failures",
                "Failures",
                TypeInfo(typing.List[str]),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "job_status",
                "JobStatus",
                TypeInfo(typing.Union[str, JobStatus]),
            ),
            (
                "total_failures",
                "TotalFailures",
                TypeInfo(int),
            ),
            (
                "total_pieces",
                "TotalPieces",
                TypeInfo(int),
            ),
            (
                "total_processed",
                "TotalProcessed",
                TypeInfo(int),
            ),
            (
                "type",
                "Type",
                TypeInfo(str),
            ),
        ]

    # The unique ID of the application associated with the export job.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of pieces that have successfully completed as of the time of the
    # request.
    completed_pieces: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date the job completed in ISO 8601 format.
    completion_date: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date the job was created in ISO 8601 format.
    creation_date: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The export job settings.
    definition: "ExportJobResource" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of pieces that failed to be processed as of the time of the
    # request.
    failed_pieces: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Provides up to 100 of the first failed entries for the job, if any exist.
    failures: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique ID of the job.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the job. Valid values: CREATED, INITIALIZING, PROCESSING,
    # COMPLETING, COMPLETED, FAILING, FAILED The job status is FAILED if one or
    # more pieces failed.
    job_status: typing.Union[str, "JobStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of endpoints that were not processed; for example, because of
    # syntax errors.
    total_failures: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The total number of pieces that must be processed to finish the job. Each
    # piece is an approximately equal portion of the endpoints.
    total_pieces: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of endpoints that were processed by the job.
    total_processed: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The job type. Will be 'EXPORT'.
    type: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ExportJobsResponse(ShapeBase):
    """
    Export job list.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "item",
                "Item",
                TypeInfo(typing.List[ExportJobResponse]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # A list of export jobs for the application.
    item: typing.List["ExportJobResponse"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The string that you use in a subsequent request to get the next page of
    # results in a paginated response.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ForbiddenException(ShapeBase):
    """
    Simple message object.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
            (
                "request_id",
                "RequestID",
                TypeInfo(str),
            ),
        ]

    # The error message that's returned from the API.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique message body ID.
    request_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class Format(str):
    CSV = "CSV"
    JSON = "JSON"


class Frequency(str):
    ONCE = "ONCE"
    HOURLY = "HOURLY"
    DAILY = "DAILY"
    WEEKLY = "WEEKLY"
    MONTHLY = "MONTHLY"


@dataclasses.dataclass
class GCMChannelRequest(ShapeBase):
    """
    Google Cloud Messaging credentials
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "api_key",
                "ApiKey",
                TypeInfo(str),
            ),
            (
                "enabled",
                "Enabled",
                TypeInfo(bool),
            ),
        ]

    # Platform credential API key from Google.
    api_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If the channel is enabled for sending messages.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GCMChannelResponse(ShapeBase):
    """
    Google Cloud Messaging channel definition
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
                "creation_date",
                "CreationDate",
                TypeInfo(str),
            ),
            (
                "credential",
                "Credential",
                TypeInfo(str),
            ),
            (
                "enabled",
                "Enabled",
                TypeInfo(bool),
            ),
            (
                "has_credential",
                "HasCredential",
                TypeInfo(bool),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "is_archived",
                "IsArchived",
                TypeInfo(bool),
            ),
            (
                "last_modified_by",
                "LastModifiedBy",
                TypeInfo(str),
            ),
            (
                "last_modified_date",
                "LastModifiedDate",
                TypeInfo(str),
            ),
            (
                "platform",
                "Platform",
                TypeInfo(str),
            ),
            (
                "version",
                "Version",
                TypeInfo(int),
            ),
        ]

    # The ID of the application to which the channel applies.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When was this segment created
    creation_date: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The GCM API key from Google.
    credential: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If the channel is enabled for sending messages.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Not used. Retained for backwards compatibility.
    has_credential: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Channel ID. Not used. Present only for backwards compatibility.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Is this channel archived
    is_archived: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Who last updated this entry
    last_modified_by: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Last date this was updated
    last_modified_date: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The platform type. Will be GCM
    platform: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Version of channel
    version: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GCMMessage(ShapeBase):
    """
    GCM Message.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "action",
                "Action",
                TypeInfo(typing.Union[str, Action]),
            ),
            (
                "body",
                "Body",
                TypeInfo(str),
            ),
            (
                "collapse_key",
                "CollapseKey",
                TypeInfo(str),
            ),
            (
                "data",
                "Data",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "icon_reference",
                "IconReference",
                TypeInfo(str),
            ),
            (
                "image_icon_url",
                "ImageIconUrl",
                TypeInfo(str),
            ),
            (
                "image_url",
                "ImageUrl",
                TypeInfo(str),
            ),
            (
                "priority",
                "Priority",
                TypeInfo(str),
            ),
            (
                "raw_content",
                "RawContent",
                TypeInfo(str),
            ),
            (
                "restricted_package_name",
                "RestrictedPackageName",
                TypeInfo(str),
            ),
            (
                "silent_push",
                "SilentPush",
                TypeInfo(bool),
            ),
            (
                "small_image_icon_url",
                "SmallImageIconUrl",
                TypeInfo(str),
            ),
            (
                "sound",
                "Sound",
                TypeInfo(str),
            ),
            (
                "substitutions",
                "Substitutions",
                TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
            (
                "time_to_live",
                "TimeToLive",
                TypeInfo(int),
            ),
            (
                "title",
                "Title",
                TypeInfo(str),
            ),
            (
                "url",
                "Url",
                TypeInfo(str),
            ),
        ]

    # The action that occurs if the user taps a push notification delivered by
    # the campaign: OPEN_APP - Your app launches, or it becomes the foreground
    # app if it has been sent to the background. This is the default action.
    # DEEP_LINK - Uses deep linking features in iOS and Android to open your app
    # and display a designated user interface within the app. URL - The default
    # mobile browser on the user's device launches and opens a web page at the
    # URL you specify. Possible values include: OPEN_APP | DEEP_LINK | URL
    action: typing.Union[str, "Action"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The message body of the notification.
    body: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This parameter identifies a group of messages (e.g., with collapse_key:
    # "Updates Available") that can be collapsed, so that only the last message
    # gets sent when delivery can be resumed. This is intended to avoid sending
    # too many of the same messages when the device comes back online or becomes
    # active.
    collapse_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The data payload used for a silent push. This payload is added to the
    # notifications' data.pinpoint.jsonBody' object
    data: typing.Dict[str, str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The icon image name of the asset saved in your application.
    icon_reference: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The URL that points to an image used as the large icon to the notification
    # content view.
    image_icon_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The URL that points to an image used in the push notification.
    image_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The message priority. Amazon Pinpoint uses this value to set the FCM or GCM
    # priority parameter when it sends the message. Accepts the following values:
    # "Normal" - Messages might be delayed. Delivery is optimized for battery
    # usage on the receiving device. Use normal priority unless immediate
    # delivery is required. "High" - Messages are sent immediately and might wake
    # a sleeping device. The equivalent values for APNs messages are "5" and
    # "10". Amazon Pinpoint accepts these values here and converts them. For more
    # information, see About FCM Messages in the Firebase documentation.
    priority: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Raw JSON formatted string to be used as the payload. This value
    # overrides the message.
    raw_content: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This parameter specifies the package name of the application where the
    # registration tokens must match in order to receive the message.
    restricted_package_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates if the message should display on the users device. Silent pushes
    # can be used for Remote Configuration and Phone Home use cases.
    silent_push: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The URL that points to an image used as the small icon for the notification
    # which will be used to represent the notification in the status bar and
    # content view
    small_image_icon_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates a sound to play when the device receives the notification.
    # Supports default, or the filename of a sound resource bundled in the app.
    # Android sound files must reside in /res/raw/
    sound: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Default message substitutions. Can be overridden by individual address
    # substitutions.
    substitutions: typing.Dict[str, typing.List[str]] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The length of time (in seconds) that FCM or GCM stores and attempts to
    # deliver the message. If unspecified, the value defaults to the maximum,
    # which is 2,419,200 seconds (28 days). Amazon Pinpoint uses this value to
    # set the FCM or GCM time_to_live parameter.
    time_to_live: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The message title that displays above the message on the user's device.
    title: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The URL to open in the user's mobile browser. Used if the value for Action
    # is URL.
    url: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GPSCoordinates(ShapeBase):
    """
    GPS coordinates
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "latitude",
                "Latitude",
                TypeInfo(float),
            ),
            (
                "longitude",
                "Longitude",
                TypeInfo(float),
            ),
        ]

    # Latitude
    latitude: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Longitude
    longitude: float = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GPSPointDimension(ShapeBase):
    """
    GPS point location dimension
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "coordinates",
                "Coordinates",
                TypeInfo(GPSCoordinates),
            ),
            (
                "range_in_kilometers",
                "RangeInKilometers",
                TypeInfo(float),
            ),
        ]

    # Coordinate to measure distance from.
    coordinates: "GPSCoordinates" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Range in kilometers from the coordinate.
    range_in_kilometers: float = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetAdmChannelRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetAdmChannelResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "adm_channel_response",
                "ADMChannelResponse",
                TypeInfo(ADMChannelResponse),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Amazon Device Messaging channel definition.
    adm_channel_response: "ADMChannelResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetApnsChannelRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetApnsChannelResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "apns_channel_response",
                "APNSChannelResponse",
                TypeInfo(APNSChannelResponse),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Apple Distribution Push Notification Service channel definition.
    apns_channel_response: "APNSChannelResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetApnsSandboxChannelRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetApnsSandboxChannelResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "apns_sandbox_channel_response",
                "APNSSandboxChannelResponse",
                TypeInfo(APNSSandboxChannelResponse),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Apple Development Push Notification Service channel definition.
    apns_sandbox_channel_response: "APNSSandboxChannelResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetApnsVoipChannelRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetApnsVoipChannelResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "apns_voip_channel_response",
                "APNSVoipChannelResponse",
                TypeInfo(APNSVoipChannelResponse),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Apple VoIP Push Notification Service channel definition.
    apns_voip_channel_response: "APNSVoipChannelResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetApnsVoipSandboxChannelRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetApnsVoipSandboxChannelResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "apns_voip_sandbox_channel_response",
                "APNSVoipSandboxChannelResponse",
                TypeInfo(APNSVoipSandboxChannelResponse),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Apple VoIP Developer Push Notification Service channel definition.
    apns_voip_sandbox_channel_response: "APNSVoipSandboxChannelResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetAppRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetAppResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "application_response",
                "ApplicationResponse",
                TypeInfo(ApplicationResponse),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Application Response.
    application_response: "ApplicationResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetApplicationSettingsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetApplicationSettingsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "application_settings_resource",
                "ApplicationSettingsResource",
                TypeInfo(ApplicationSettingsResource),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Application settings.
    application_settings_resource: "ApplicationSettingsResource" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetAppsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "page_size",
                "PageSize",
                TypeInfo(str),
            ),
            (
                "token",
                "Token",
                TypeInfo(str),
            ),
        ]

    # The number of entries you want on each page in the response.
    page_size: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The NextToken string returned on a previous page that you use to get the
    # next page of results in a paginated response.
    token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetAppsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "applications_response",
                "ApplicationsResponse",
                TypeInfo(ApplicationsResponse),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Get Applications Result.
    applications_response: "ApplicationsResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetBaiduChannelRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetBaiduChannelResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "baidu_channel_response",
                "BaiduChannelResponse",
                TypeInfo(BaiduChannelResponse),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Baidu Cloud Messaging channel definition
    baidu_channel_response: "BaiduChannelResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetCampaignActivitiesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
            (
                "campaign_id",
                "CampaignId",
                TypeInfo(str),
            ),
            (
                "page_size",
                "PageSize",
                TypeInfo(str),
            ),
            (
                "token",
                "Token",
                TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique ID of the campaign.
    campaign_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of entries you want on each page in the response.
    page_size: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The NextToken string returned on a previous page that you use to get the
    # next page of results in a paginated response.
    token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetCampaignActivitiesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "activities_response",
                "ActivitiesResponse",
                TypeInfo(ActivitiesResponse),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Activities for campaign.
    activities_response: "ActivitiesResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetCampaignRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
            (
                "campaign_id",
                "CampaignId",
                TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique ID of the campaign.
    campaign_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetCampaignResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "campaign_response",
                "CampaignResponse",
                TypeInfo(CampaignResponse),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Campaign definition
    campaign_response: "CampaignResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetCampaignVersionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
            (
                "campaign_id",
                "CampaignId",
                TypeInfo(str),
            ),
            (
                "version",
                "Version",
                TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique ID of the campaign.
    campaign_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version of the campaign.
    version: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetCampaignVersionResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "campaign_response",
                "CampaignResponse",
                TypeInfo(CampaignResponse),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Campaign definition
    campaign_response: "CampaignResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetCampaignVersionsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
            (
                "campaign_id",
                "CampaignId",
                TypeInfo(str),
            ),
            (
                "page_size",
                "PageSize",
                TypeInfo(str),
            ),
            (
                "token",
                "Token",
                TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique ID of the campaign.
    campaign_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of entries you want on each page in the response.
    page_size: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The NextToken string returned on a previous page that you use to get the
    # next page of results in a paginated response.
    token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetCampaignVersionsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "campaigns_response",
                "CampaignsResponse",
                TypeInfo(CampaignsResponse),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # List of available campaigns.
    campaigns_response: "CampaignsResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetCampaignsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
            (
                "page_size",
                "PageSize",
                TypeInfo(str),
            ),
            (
                "token",
                "Token",
                TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of entries you want on each page in the response.
    page_size: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The NextToken string returned on a previous page that you use to get the
    # next page of results in a paginated response.
    token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetCampaignsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "campaigns_response",
                "CampaignsResponse",
                TypeInfo(CampaignsResponse),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # List of available campaigns.
    campaigns_response: "CampaignsResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetChannelsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetChannelsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "channels_response",
                "ChannelsResponse",
                TypeInfo(ChannelsResponse),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Get channels definition
    channels_response: "ChannelsResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetEmailChannelRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetEmailChannelResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "email_channel_response",
                "EmailChannelResponse",
                TypeInfo(EmailChannelResponse),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Email Channel Response.
    email_channel_response: "EmailChannelResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetEndpointRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
            (
                "endpoint_id",
                "EndpointId",
                TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique ID of the endpoint.
    endpoint_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetEndpointResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "endpoint_response",
                "EndpointResponse",
                TypeInfo(EndpointResponse),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Endpoint response
    endpoint_response: "EndpointResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetEventStreamRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetEventStreamResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "event_stream",
                "EventStream",
                TypeInfo(EventStream),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Model for an event publishing subscription export.
    event_stream: "EventStream" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetExportJobRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
            (
                "job_id",
                "JobId",
                TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique ID of the job.
    job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetExportJobResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "export_job_response",
                "ExportJobResponse",
                TypeInfo(ExportJobResponse),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Export job response.
    export_job_response: "ExportJobResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetExportJobsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
            (
                "page_size",
                "PageSize",
                TypeInfo(str),
            ),
            (
                "token",
                "Token",
                TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of entries you want on each page in the response.
    page_size: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The NextToken string returned on a previous page that you use to get the
    # next page of results in a paginated response.
    token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetExportJobsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "export_jobs_response",
                "ExportJobsResponse",
                TypeInfo(ExportJobsResponse),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Export job list.
    export_jobs_response: "ExportJobsResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetGcmChannelRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetGcmChannelResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "gcm_channel_response",
                "GCMChannelResponse",
                TypeInfo(GCMChannelResponse),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Google Cloud Messaging channel definition
    gcm_channel_response: "GCMChannelResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetImportJobRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
            (
                "job_id",
                "JobId",
                TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique ID of the job.
    job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetImportJobResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "import_job_response",
                "ImportJobResponse",
                TypeInfo(ImportJobResponse),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Import job response.
    import_job_response: "ImportJobResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetImportJobsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
            (
                "page_size",
                "PageSize",
                TypeInfo(str),
            ),
            (
                "token",
                "Token",
                TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of entries you want on each page in the response.
    page_size: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The NextToken string returned on a previous page that you use to get the
    # next page of results in a paginated response.
    token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetImportJobsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "import_jobs_response",
                "ImportJobsResponse",
                TypeInfo(ImportJobsResponse),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Import job list.
    import_jobs_response: "ImportJobsResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetSegmentExportJobsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
            (
                "segment_id",
                "SegmentId",
                TypeInfo(str),
            ),
            (
                "page_size",
                "PageSize",
                TypeInfo(str),
            ),
            (
                "token",
                "Token",
                TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique ID of the segment.
    segment_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of entries you want on each page in the response.
    page_size: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The NextToken string returned on a previous page that you use to get the
    # next page of results in a paginated response.
    token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetSegmentExportJobsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "export_jobs_response",
                "ExportJobsResponse",
                TypeInfo(ExportJobsResponse),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Export job list.
    export_jobs_response: "ExportJobsResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetSegmentImportJobsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
            (
                "segment_id",
                "SegmentId",
                TypeInfo(str),
            ),
            (
                "page_size",
                "PageSize",
                TypeInfo(str),
            ),
            (
                "token",
                "Token",
                TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique ID of the segment.
    segment_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of entries you want on each page in the response.
    page_size: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The NextToken string returned on a previous page that you use to get the
    # next page of results in a paginated response.
    token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetSegmentImportJobsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "import_jobs_response",
                "ImportJobsResponse",
                TypeInfo(ImportJobsResponse),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Import job list.
    import_jobs_response: "ImportJobsResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetSegmentRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
            (
                "segment_id",
                "SegmentId",
                TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique ID of the segment.
    segment_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetSegmentResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "segment_response",
                "SegmentResponse",
                TypeInfo(SegmentResponse),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Segment definition.
    segment_response: "SegmentResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetSegmentVersionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
            (
                "segment_id",
                "SegmentId",
                TypeInfo(str),
            ),
            (
                "version",
                "Version",
                TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique ID of the segment.
    segment_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The segment version.
    version: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetSegmentVersionResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "segment_response",
                "SegmentResponse",
                TypeInfo(SegmentResponse),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Segment definition.
    segment_response: "SegmentResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetSegmentVersionsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
            (
                "segment_id",
                "SegmentId",
                TypeInfo(str),
            ),
            (
                "page_size",
                "PageSize",
                TypeInfo(str),
            ),
            (
                "token",
                "Token",
                TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique ID of the segment.
    segment_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of entries you want on each page in the response.
    page_size: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The NextToken string returned on a previous page that you use to get the
    # next page of results in a paginated response.
    token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetSegmentVersionsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "segments_response",
                "SegmentsResponse",
                TypeInfo(SegmentsResponse),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Segments in your account.
    segments_response: "SegmentsResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetSegmentsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
            (
                "page_size",
                "PageSize",
                TypeInfo(str),
            ),
            (
                "token",
                "Token",
                TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of entries you want on each page in the response.
    page_size: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The NextToken string returned on a previous page that you use to get the
    # next page of results in a paginated response.
    token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetSegmentsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "segments_response",
                "SegmentsResponse",
                TypeInfo(SegmentsResponse),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Segments in your account.
    segments_response: "SegmentsResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetSmsChannelRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetSmsChannelResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "sms_channel_response",
                "SMSChannelResponse",
                TypeInfo(SMSChannelResponse),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # SMS Channel Response.
    sms_channel_response: "SMSChannelResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetUserEndpointsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
            (
                "user_id",
                "UserId",
                TypeInfo(str),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique ID of the user.
    user_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetUserEndpointsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "endpoints_response",
                "EndpointsResponse",
                TypeInfo(EndpointsResponse),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # List of endpoints
    endpoints_response: "EndpointsResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ImportJobRequest(ShapeBase):
    """
    Import job request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "define_segment",
                "DefineSegment",
                TypeInfo(bool),
            ),
            (
                "external_id",
                "ExternalId",
                TypeInfo(str),
            ),
            (
                "format",
                "Format",
                TypeInfo(typing.Union[str, Format]),
            ),
            (
                "register_endpoints",
                "RegisterEndpoints",
                TypeInfo(bool),
            ),
            (
                "role_arn",
                "RoleArn",
                TypeInfo(str),
            ),
            (
                "s3_url",
                "S3Url",
                TypeInfo(str),
            ),
            (
                "segment_id",
                "SegmentId",
                TypeInfo(str),
            ),
            (
                "segment_name",
                "SegmentName",
                TypeInfo(str),
            ),
        ]

    # Sets whether the endpoints create a segment when they are imported.
    define_segment: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Deprecated) Your AWS account ID, which you assigned to the ExternalID key
    # in an IAM trust policy. Used by Amazon Pinpoint to assume an IAM role. This
    # requirement is removed, and external IDs are not recommended for IAM roles
    # assumed by Amazon Pinpoint.
    external_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The format of the files that contain the endpoint definitions. Valid
    # values: CSV, JSON
    format: typing.Union[str, "Format"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Sets whether the endpoints are registered with Amazon Pinpoint when they
    # are imported.
    register_endpoints: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of an IAM role that grants Amazon Pinpoint
    # access to the Amazon S3 location that contains the endpoints to import.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The URL of the S3 bucket that contains the segment information to import.
    # The location can be a folder or a single file. The URL should use the
    # following format: s3://bucket-name/folder-name/file-name Amazon Pinpoint
    # imports endpoints from this location and any subfolders it contains.
    s3_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the segment to update if the import job is meant to update an
    # existing segment.
    segment_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A custom name for the segment created by the import job. Use if
    # DefineSegment is true.
    segment_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ImportJobResource(ShapeBase):
    """
    Import job resource
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "define_segment",
                "DefineSegment",
                TypeInfo(bool),
            ),
            (
                "external_id",
                "ExternalId",
                TypeInfo(str),
            ),
            (
                "format",
                "Format",
                TypeInfo(typing.Union[str, Format]),
            ),
            (
                "register_endpoints",
                "RegisterEndpoints",
                TypeInfo(bool),
            ),
            (
                "role_arn",
                "RoleArn",
                TypeInfo(str),
            ),
            (
                "s3_url",
                "S3Url",
                TypeInfo(str),
            ),
            (
                "segment_id",
                "SegmentId",
                TypeInfo(str),
            ),
            (
                "segment_name",
                "SegmentName",
                TypeInfo(str),
            ),
        ]

    # Sets whether the endpoints create a segment when they are imported.
    define_segment: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Deprecated) Your AWS account ID, which you assigned to the ExternalID key
    # in an IAM trust policy. Used by Amazon Pinpoint to assume an IAM role. This
    # requirement is removed, and external IDs are not recommended for IAM roles
    # assumed by Amazon Pinpoint.
    external_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The format of the files that contain the endpoint definitions. Valid
    # values: CSV, JSON
    format: typing.Union[str, "Format"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Sets whether the endpoints are registered with Amazon Pinpoint when they
    # are imported.
    register_endpoints: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of an IAM role that grants Amazon Pinpoint
    # access to the Amazon S3 location that contains the endpoints to import.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The URL of the S3 bucket that contains the segment information to import.
    # The location can be a folder or a single file. The URL should use the
    # following format: s3://bucket-name/folder-name/file-name Amazon Pinpoint
    # imports endpoints from this location and any subfolders it contains.
    s3_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the segment to update if the import job is meant to update an
    # existing segment.
    segment_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A custom name for the segment created by the import job. Use if
    # DefineSegment is true.
    segment_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ImportJobResponse(ShapeBase):
    """
    Import job response.
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
                "completed_pieces",
                "CompletedPieces",
                TypeInfo(int),
            ),
            (
                "completion_date",
                "CompletionDate",
                TypeInfo(str),
            ),
            (
                "creation_date",
                "CreationDate",
                TypeInfo(str),
            ),
            (
                "definition",
                "Definition",
                TypeInfo(ImportJobResource),
            ),
            (
                "failed_pieces",
                "FailedPieces",
                TypeInfo(int),
            ),
            (
                "failures",
                "Failures",
                TypeInfo(typing.List[str]),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "job_status",
                "JobStatus",
                TypeInfo(typing.Union[str, JobStatus]),
            ),
            (
                "total_failures",
                "TotalFailures",
                TypeInfo(int),
            ),
            (
                "total_pieces",
                "TotalPieces",
                TypeInfo(int),
            ),
            (
                "total_processed",
                "TotalProcessed",
                TypeInfo(int),
            ),
            (
                "type",
                "Type",
                TypeInfo(str),
            ),
        ]

    # The unique ID of the application to which the import job applies.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of pieces that have successfully imported as of the time of the
    # request.
    completed_pieces: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date the import job completed in ISO 8601 format.
    completion_date: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date the import job was created in ISO 8601 format.
    creation_date: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The import job settings.
    definition: "ImportJobResource" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of pieces that have failed to import as of the time of the
    # request.
    failed_pieces: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Provides up to 100 of the first failed entries for the job, if any exist.
    failures: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique ID of the import job.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the import job. Valid values: CREATED, INITIALIZING,
    # PROCESSING, COMPLETING, COMPLETED, FAILING, FAILED The job status is FAILED
    # if one or more pieces failed to import.
    job_status: typing.Union[str, "JobStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of endpoints that failed to import; for example, because of
    # syntax errors.
    total_failures: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The total number of pieces that must be imported to finish the job. Each
    # piece is an approximately equal portion of the endpoints to import.
    total_pieces: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of endpoints that were processed by the import job.
    total_processed: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The job type. Will be Import.
    type: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ImportJobsResponse(ShapeBase):
    """
    Import job list.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "item",
                "Item",
                TypeInfo(typing.List[ImportJobResponse]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # A list of import jobs for the application.
    item: typing.List["ImportJobResponse"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The string that you use in a subsequent request to get the next page of
    # results in a paginated response.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class Include(str):
    ALL = "ALL"
    ANY = "ANY"
    NONE = "NONE"


@dataclasses.dataclass
class InternalServerErrorException(ShapeBase):
    """
    Simple message object.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
            (
                "request_id",
                "RequestID",
                TypeInfo(str),
            ),
        ]

    # The error message that's returned from the API.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique message body ID.
    request_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ItemResponse(ShapeBase):
    """
    The endpoint and events combined response definition
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "endpoint_item_response",
                "EndpointItemResponse",
                TypeInfo(EndpointItemResponse),
            ),
            (
                "events_item_response",
                "EventsItemResponse",
                TypeInfo(typing.Dict[str, EventItemResponse]),
            ),
        ]

    # Endpoint item response after endpoint registration
    endpoint_item_response: "EndpointItemResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Events item response is a multipart response object per event Id, with
    # eventId as the key and EventItemResponse object as the value
    events_item_response: typing.Dict[str, "EventItemResponse"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )


class JobStatus(str):
    CREATED = "CREATED"
    INITIALIZING = "INITIALIZING"
    PROCESSING = "PROCESSING"
    COMPLETING = "COMPLETING"
    COMPLETED = "COMPLETED"
    FAILING = "FAILING"
    FAILED = "FAILED"


@dataclasses.dataclass
class Message(ShapeBase):
    """
    Message to send
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "action",
                "Action",
                TypeInfo(typing.Union[str, Action]),
            ),
            (
                "body",
                "Body",
                TypeInfo(str),
            ),
            (
                "image_icon_url",
                "ImageIconUrl",
                TypeInfo(str),
            ),
            (
                "image_small_icon_url",
                "ImageSmallIconUrl",
                TypeInfo(str),
            ),
            (
                "image_url",
                "ImageUrl",
                TypeInfo(str),
            ),
            (
                "json_body",
                "JsonBody",
                TypeInfo(str),
            ),
            (
                "media_url",
                "MediaUrl",
                TypeInfo(str),
            ),
            (
                "raw_content",
                "RawContent",
                TypeInfo(str),
            ),
            (
                "silent_push",
                "SilentPush",
                TypeInfo(bool),
            ),
            (
                "time_to_live",
                "TimeToLive",
                TypeInfo(int),
            ),
            (
                "title",
                "Title",
                TypeInfo(str),
            ),
            (
                "url",
                "Url",
                TypeInfo(str),
            ),
        ]

    # The action that occurs if the user taps a push notification delivered by
    # the campaign: OPEN_APP - Your app launches, or it becomes the foreground
    # app if it has been sent to the background. This is the default action.
    # DEEP_LINK - Uses deep linking features in iOS and Android to open your app
    # and display a designated user interface within the app. URL - The default
    # mobile browser on the user's device launches and opens a web page at the
    # URL you specify.
    action: typing.Union[str, "Action"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The message body. Can include up to 140 characters.
    body: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The URL that points to the icon image for the push notification icon, for
    # example, the app icon.
    image_icon_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The URL that points to the small icon image for the push notification icon,
    # for example, the app icon.
    image_small_icon_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The URL that points to an image used in the push notification.
    image_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The JSON payload used for a silent push.
    json_body: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The URL that points to the media resource, for example a .mp4 or .gif file.
    media_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Raw JSON formatted string to be used as the payload. This value
    # overrides the message.
    raw_content: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates if the message should display on the users device. Silent pushes
    # can be used for Remote Configuration and Phone Home use cases.
    silent_push: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This parameter specifies how long (in seconds) the message should be kept
    # if the service is unable to deliver the notification the first time. If the
    # value is 0, it treats the notification as if it expires immediately and
    # does not store the notification or attempt to redeliver it. This value is
    # converted to the expiration field when sent to the service. It only applies
    # to APNs and GCM
    time_to_live: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The message title that displays above the message on the user's device.
    title: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The URL to open in the user's mobile browser. Used if the value for Action
    # is URL.
    url: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MessageBody(ShapeBase):
    """
    Simple message object.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
            (
                "request_id",
                "RequestID",
                TypeInfo(str),
            ),
        ]

    # The error message that's returned from the API.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique message body ID.
    request_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MessageConfiguration(ShapeBase):
    """
    Message configuration for a campaign.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "adm_message",
                "ADMMessage",
                TypeInfo(Message),
            ),
            (
                "apns_message",
                "APNSMessage",
                TypeInfo(Message),
            ),
            (
                "baidu_message",
                "BaiduMessage",
                TypeInfo(Message),
            ),
            (
                "default_message",
                "DefaultMessage",
                TypeInfo(Message),
            ),
            (
                "email_message",
                "EmailMessage",
                TypeInfo(CampaignEmailMessage),
            ),
            (
                "gcm_message",
                "GCMMessage",
                TypeInfo(Message),
            ),
            (
                "sms_message",
                "SMSMessage",
                TypeInfo(CampaignSmsMessage),
            ),
        ]

    # The message that the campaign delivers to ADM channels. Overrides the
    # default message.
    adm_message: "Message" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The message that the campaign delivers to APNS channels. Overrides the
    # default message.
    apns_message: "Message" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The message that the campaign delivers to Baidu channels. Overrides the
    # default message.
    baidu_message: "Message" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The default message for all channels.
    default_message: "Message" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The email message configuration.
    email_message: "CampaignEmailMessage" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The message that the campaign delivers to GCM channels. Overrides the
    # default message.
    gcm_message: "Message" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The SMS message configuration.
    sms_message: "CampaignSmsMessage" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class MessageRequest(ShapeBase):
    """
    Send message request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "addresses",
                "Addresses",
                TypeInfo(typing.Dict[str, AddressConfiguration]),
            ),
            (
                "context",
                "Context",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "endpoints",
                "Endpoints",
                TypeInfo(typing.Dict[str, EndpointSendConfiguration]),
            ),
            (
                "message_configuration",
                "MessageConfiguration",
                TypeInfo(DirectMessageConfiguration),
            ),
            (
                "trace_id",
                "TraceId",
                TypeInfo(str),
            ),
        ]

    # A map of key-value pairs, where each key is an address and each value is an
    # AddressConfiguration object. An address can be a push notification token, a
    # phone number, or an email address.
    addresses: typing.Dict[str, "AddressConfiguration"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A map of custom attributes to attributes to be attached to the message.
    # This payload is added to the push notification's 'data.pinpoint' object or
    # added to the email/sms delivery receipt event attributes.
    context: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A map of key-value pairs, where each key is an endpoint ID and each value
    # is an EndpointSendConfiguration object. Within an EndpointSendConfiguration
    # object, you can tailor the message for an endpoint by specifying message
    # overrides or substitutions.
    endpoints: typing.Dict[str, "EndpointSendConfiguration"
                          ] = dataclasses.field(
                              default=ShapeBase.NOT_SET,
                          )

    # Message configuration.
    message_configuration: "DirectMessageConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A unique ID that you can use to trace a message. This ID is visible to
    # recipients.
    trace_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MessageResponse(ShapeBase):
    """
    Send message response.
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
                "endpoint_result",
                "EndpointResult",
                TypeInfo(typing.Dict[str, EndpointMessageResult]),
            ),
            (
                "request_id",
                "RequestId",
                TypeInfo(str),
            ),
            (
                "result",
                "Result",
                TypeInfo(typing.Dict[str, MessageResult]),
            ),
        ]

    # Application id of the message.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A map containing a multi part response for each address, with the
    # endpointId as the key and the result as the value.
    endpoint_result: typing.Dict[str, "EndpointMessageResult"
                                ] = dataclasses.field(
                                    default=ShapeBase.NOT_SET,
                                )

    # Original request Id for which this message was delivered.
    request_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A map containing a multi part response for each address, with the address
    # as the key(Email address, phone number or push token) and the result as the
    # value.
    result: typing.Dict[str, "MessageResult"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class MessageResult(ShapeBase):
    """
    The result from sending a message to an address.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "delivery_status",
                "DeliveryStatus",
                TypeInfo(typing.Union[str, DeliveryStatus]),
            ),
            (
                "message_id",
                "MessageId",
                TypeInfo(str),
            ),
            (
                "status_code",
                "StatusCode",
                TypeInfo(int),
            ),
            (
                "status_message",
                "StatusMessage",
                TypeInfo(str),
            ),
            (
                "updated_token",
                "UpdatedToken",
                TypeInfo(str),
            ),
        ]

    # The delivery status of the message. Possible values: SUCCESS - The message
    # was successfully delivered to the endpoint. TRANSIENT_FAILURE - A temporary
    # error occurred. Amazon Pinpoint will attempt to deliver the message again
    # later. FAILURE_PERMANENT - An error occurred when delivering the message to
    # the endpoint. Amazon Pinpoint won't attempt to send the message again.
    # TIMEOUT - The message couldn't be sent within the timeout period.
    # QUIET_TIME - The local time for the endpoint was within the Quiet Hours for
    # the campaign. DAILY_CAP - The endpoint has received the maximum number of
    # messages it can receive within a 24-hour period. HOLDOUT - The endpoint was
    # in a hold out treatment for the campaign. THROTTLED - Amazon Pinpoint
    # throttled sending to this endpoint. EXPIRED - The endpoint address is
    # expired. CAMPAIGN_CAP - The endpoint received the maximum number of
    # messages allowed by the campaign. SERVICE_FAILURE - A service-level failure
    # prevented Amazon Pinpoint from delivering the message. UNKNOWN - An unknown
    # error occurred.
    delivery_status: typing.Union[str, "DeliveryStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Unique message identifier associated with the message that was sent.
    message_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Downstream service status code.
    status_code: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Status message for message delivery.
    status_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If token was updated as part of delivery. (This is GCM Specific)
    updated_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class MessageType(str):
    TRANSACTIONAL = "TRANSACTIONAL"
    PROMOTIONAL = "PROMOTIONAL"


@dataclasses.dataclass
class MethodNotAllowedException(ShapeBase):
    """
    Simple message object.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
            (
                "request_id",
                "RequestID",
                TypeInfo(str),
            ),
        ]

    # The error message that's returned from the API.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique message body ID.
    request_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MetricDimension(ShapeBase):
    """
    Custom metric dimension
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "comparison_operator",
                "ComparisonOperator",
                TypeInfo(str),
            ),
            (
                "value",
                "Value",
                TypeInfo(float),
            ),
        ]

    # GREATER_THAN | LESS_THAN | GREATER_THAN_OR_EQUAL | LESS_THAN_OR_EQUAL |
    # EQUAL
    comparison_operator: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Value to be compared.
    value: float = dataclasses.field(default=ShapeBase.NOT_SET, )


class Mode(str):
    DELIVERY = "DELIVERY"
    FILTER = "FILTER"


@dataclasses.dataclass
class NotFoundException(ShapeBase):
    """
    Simple message object.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
            (
                "request_id",
                "RequestID",
                TypeInfo(str),
            ),
        ]

    # The error message that's returned from the API.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique message body ID.
    request_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class NumberValidateRequest(ShapeBase):
    """
    Phone Number Information request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "iso_country_code",
                "IsoCountryCode",
                TypeInfo(str),
            ),
            (
                "phone_number",
                "PhoneNumber",
                TypeInfo(str),
            ),
        ]

    # (Optional) The two-character ISO country code for the country or region
    # where the phone number was originally registered.
    iso_country_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The phone number to get information about. The phone number that you
    # provide should include a country code. If the number doesn't include a
    # valid country code, the operation might result in an error.
    phone_number: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class NumberValidateResponse(ShapeBase):
    """
    Phone Number Information response.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "carrier",
                "Carrier",
                TypeInfo(str),
            ),
            (
                "city",
                "City",
                TypeInfo(str),
            ),
            (
                "cleansed_phone_number_e164",
                "CleansedPhoneNumberE164",
                TypeInfo(str),
            ),
            (
                "cleansed_phone_number_national",
                "CleansedPhoneNumberNational",
                TypeInfo(str),
            ),
            (
                "country",
                "Country",
                TypeInfo(str),
            ),
            (
                "country_code_iso2",
                "CountryCodeIso2",
                TypeInfo(str),
            ),
            (
                "country_code_numeric",
                "CountryCodeNumeric",
                TypeInfo(str),
            ),
            (
                "county",
                "County",
                TypeInfo(str),
            ),
            (
                "original_country_code_iso2",
                "OriginalCountryCodeIso2",
                TypeInfo(str),
            ),
            (
                "original_phone_number",
                "OriginalPhoneNumber",
                TypeInfo(str),
            ),
            (
                "phone_type",
                "PhoneType",
                TypeInfo(str),
            ),
            (
                "phone_type_code",
                "PhoneTypeCode",
                TypeInfo(int),
            ),
            (
                "timezone",
                "Timezone",
                TypeInfo(str),
            ),
            (
                "zip_code",
                "ZipCode",
                TypeInfo(str),
            ),
        ]

    # The carrier or servive provider that the phone number is currently
    # registered with.
    carrier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The city where the phone number was originally registered.
    city: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The cleansed phone number, shown in E.164 format.
    cleansed_phone_number_e164: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The cleansed phone number, shown in the local phone number format.
    cleansed_phone_number_national: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The country or region where the phone number was originally registered.
    country: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The two-character ISO code for the country or region where the phone number
    # was originally registered.
    country_code_iso2: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The numeric code for the country or region where the phone number was
    # originally registered.
    country_code_numeric: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The county where the phone number was originally registered.
    county: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The two-character ISO code for the country or region that you included in
    # the request body.
    original_country_code_iso2: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The phone number that you included in the request body.
    original_phone_number: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A description of the phone type. Possible values are MOBILE, LANDLINE,
    # VOIP, INVALID, PREPAID, and OTHER.
    phone_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The phone type, represented by an integer. Possible values include 0
    # (MOBILE), 1 (LANDLINE), 2 (VOIP), 3 (INVALID), 4 (OTHER), and 5 (PREPAID).
    phone_type_code: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time zone for the location where the phone number was originally
    # registered.
    timezone: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The postal code for the location where the phone number was originally
    # registered.
    zip_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PhoneNumberValidateRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "number_validate_request",
                "NumberValidateRequest",
                TypeInfo(NumberValidateRequest),
            ),
        ]

    # Phone Number Information request.
    number_validate_request: "NumberValidateRequest" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PhoneNumberValidateResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "number_validate_response",
                "NumberValidateResponse",
                TypeInfo(NumberValidateResponse),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Phone Number Information response.
    number_validate_response: "NumberValidateResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PublicEndpoint(ShapeBase):
    """
    Public endpoint attributes.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "address",
                "Address",
                TypeInfo(str),
            ),
            (
                "attributes",
                "Attributes",
                TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
            (
                "channel_type",
                "ChannelType",
                TypeInfo(typing.Union[str, ChannelType]),
            ),
            (
                "demographic",
                "Demographic",
                TypeInfo(EndpointDemographic),
            ),
            (
                "effective_date",
                "EffectiveDate",
                TypeInfo(str),
            ),
            (
                "endpoint_status",
                "EndpointStatus",
                TypeInfo(str),
            ),
            (
                "location",
                "Location",
                TypeInfo(EndpointLocation),
            ),
            (
                "metrics",
                "Metrics",
                TypeInfo(typing.Dict[str, float]),
            ),
            (
                "opt_out",
                "OptOut",
                TypeInfo(str),
            ),
            (
                "request_id",
                "RequestId",
                TypeInfo(str),
            ),
            (
                "user",
                "User",
                TypeInfo(EndpointUser),
            ),
        ]

    # The unique identifier for the recipient. For example, an address could be a
    # device token or an endpoint ID.
    address: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Custom attributes that your app reports to Amazon Pinpoint. You can use
    # these attributes as selection criteria when you create a segment.
    attributes: typing.Dict[str, typing.List[str]] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The channel type. Valid values: APNS, GCM
    channel_type: typing.Union[str, "ChannelType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The endpoint demographic attributes.
    demographic: "EndpointDemographic" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time when the endpoint was last updated.
    effective_date: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the endpoint. If the update fails, the value is INACTIVE. If
    # the endpoint is updated successfully, the value is ACTIVE.
    endpoint_status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The endpoint location attributes.
    location: "EndpointLocation" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Custom metrics that your app reports to Amazon Pinpoint.
    metrics: typing.Dict[str, float] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates whether a user has opted out of receiving messages with one of
    # the following values: ALL - User has opted out of all messages. NONE -
    # Users has not opted out and receives all messages.
    opt_out: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A unique identifier that is generated each time the endpoint is updated.
    request_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Custom user-specific attributes that your app reports to Amazon Pinpoint.
    user: "EndpointUser" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutEventStreamRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
            (
                "write_event_stream",
                "WriteEventStream",
                TypeInfo(WriteEventStream),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Request to save an EventStream.
    write_event_stream: "WriteEventStream" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutEventStreamResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "event_stream",
                "EventStream",
                TypeInfo(EventStream),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Model for an event publishing subscription export.
    event_stream: "EventStream" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutEventsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
            (
                "events_request",
                "EventsRequest",
                TypeInfo(EventsRequest),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Put Events request
    events_request: "EventsRequest" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutEventsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "events_response",
                "EventsResponse",
                TypeInfo(EventsResponse),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The results from processing a put events request
    events_response: "EventsResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class QuietTime(ShapeBase):
    """
    Quiet Time
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "end",
                "End",
                TypeInfo(str),
            ),
            (
                "start",
                "Start",
                TypeInfo(str),
            ),
        ]

    # The default end time for quiet time in ISO 8601 format.
    end: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The default start time for quiet time in ISO 8601 format.
    start: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RecencyDimension(ShapeBase):
    """
    Define how a segment based on recency of use.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "duration",
                "Duration",
                TypeInfo(typing.Union[str, Duration]),
            ),
            (
                "recency_type",
                "RecencyType",
                TypeInfo(typing.Union[str, RecencyType]),
            ),
        ]

    # The length of time during which users have been active or inactive with
    # your app. Valid values: HR_24, DAY_7, DAY_14, DAY_30
    duration: typing.Union[str, "Duration"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The recency dimension type: ACTIVE - Users who have used your app within
    # the specified duration are included in the segment. INACTIVE - Users who
    # have not used your app within the specified duration are included in the
    # segment.
    recency_type: typing.Union[str, "RecencyType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class RecencyType(str):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


@dataclasses.dataclass
class RemoveAttributesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
            (
                "attribute_type",
                "AttributeType",
                TypeInfo(str),
            ),
            (
                "update_attributes_request",
                "UpdateAttributesRequest",
                TypeInfo(UpdateAttributesRequest),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Type of attribute. Can be endpoint-custom-attributes, endpoint-custom-
    # metrics, endpoint-user-attributes.
    attribute_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Update attributes request
    update_attributes_request: "UpdateAttributesRequest" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RemoveAttributesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "attributes_resource",
                "AttributesResource",
                TypeInfo(AttributesResource),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Attributes.
    attributes_resource: "AttributesResource" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SMSChannelRequest(ShapeBase):
    """
    SMS Channel Request
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "enabled",
                "Enabled",
                TypeInfo(bool),
            ),
            (
                "sender_id",
                "SenderId",
                TypeInfo(str),
            ),
            (
                "short_code",
                "ShortCode",
                TypeInfo(str),
            ),
        ]

    # If the channel is enabled for sending messages.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Sender identifier of your messages.
    sender_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # ShortCode registered with phone provider.
    short_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SMSChannelResponse(ShapeBase):
    """
    SMS Channel Response.
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
                "creation_date",
                "CreationDate",
                TypeInfo(str),
            ),
            (
                "enabled",
                "Enabled",
                TypeInfo(bool),
            ),
            (
                "has_credential",
                "HasCredential",
                TypeInfo(bool),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "is_archived",
                "IsArchived",
                TypeInfo(bool),
            ),
            (
                "last_modified_by",
                "LastModifiedBy",
                TypeInfo(str),
            ),
            (
                "last_modified_date",
                "LastModifiedDate",
                TypeInfo(str),
            ),
            (
                "platform",
                "Platform",
                TypeInfo(str),
            ),
            (
                "promotional_messages_per_second",
                "PromotionalMessagesPerSecond",
                TypeInfo(int),
            ),
            (
                "sender_id",
                "SenderId",
                TypeInfo(str),
            ),
            (
                "short_code",
                "ShortCode",
                TypeInfo(str),
            ),
            (
                "transactional_messages_per_second",
                "TransactionalMessagesPerSecond",
                TypeInfo(int),
            ),
            (
                "version",
                "Version",
                TypeInfo(int),
            ),
        ]

    # The unique ID of the application to which the SMS channel belongs.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date that the settings were last updated in ISO 8601 format.
    creation_date: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If the channel is enabled for sending messages.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Not used. Retained for backwards compatibility.
    has_credential: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Channel ID. Not used, only for backwards compatibility.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Is this channel archived
    is_archived: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Who last updated this entry
    last_modified_by: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Last date this was updated
    last_modified_date: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Platform type. Will be "SMS"
    platform: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Promotional messages per second that can be sent
    promotional_messages_per_second: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Sender identifier of your messages.
    sender_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The short code registered with the phone provider.
    short_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Transactional messages per second that can be sent
    transactional_messages_per_second: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Version of channel
    version: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SMSMessage(ShapeBase):
    """
    SMS Message.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "body",
                "Body",
                TypeInfo(str),
            ),
            (
                "keyword",
                "Keyword",
                TypeInfo(str),
            ),
            (
                "message_type",
                "MessageType",
                TypeInfo(typing.Union[str, MessageType]),
            ),
            (
                "origination_number",
                "OriginationNumber",
                TypeInfo(str),
            ),
            (
                "sender_id",
                "SenderId",
                TypeInfo(str),
            ),
            (
                "substitutions",
                "Substitutions",
                TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
        ]

    # The body of the SMS message.
    body: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The SMS program name that you provided to AWS Support when you requested
    # your dedicated number.
    keyword: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Is this a transaction priority message or lower priority.
    message_type: typing.Union[str, "MessageType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The phone number that the SMS message originates from. Specify one of the
    # dedicated long codes or short codes that you requested from AWS Support and
    # that is assigned to your account. If this attribute is not specified,
    # Amazon Pinpoint randomly assigns a long code.
    origination_number: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The sender ID that is shown as the message sender on the recipient's
    # device. Support for sender IDs varies by country or region.
    sender_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Default message substitutions. Can be overridden by individual address
    # substitutions.
    substitutions: typing.Dict[str, typing.List[str]] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Schedule(ShapeBase):
    """
    Shcedule that defines when a campaign is run.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "end_time",
                "EndTime",
                TypeInfo(str),
            ),
            (
                "frequency",
                "Frequency",
                TypeInfo(typing.Union[str, Frequency]),
            ),
            (
                "is_local_time",
                "IsLocalTime",
                TypeInfo(bool),
            ),
            (
                "quiet_time",
                "QuietTime",
                TypeInfo(QuietTime),
            ),
            (
                "start_time",
                "StartTime",
                TypeInfo(str),
            ),
            (
                "timezone",
                "Timezone",
                TypeInfo(str),
            ),
        ]

    # The scheduled time that the campaign ends in ISO 8601 format.
    end_time: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # How often the campaign delivers messages. Valid values: ONCE, HOURLY,
    # DAILY, WEEKLY, MONTHLY
    frequency: typing.Union[str, "Frequency"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates whether the campaign schedule takes effect according to each
    # user's local time.
    is_local_time: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time during which the campaign sends no messages.
    quiet_time: "QuietTime" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The scheduled time that the campaign begins in ISO 8601 format.
    start_time: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The starting UTC offset for the schedule if the value for isLocalTime is
    # true Valid values: UTC UTC+01 UTC+02 UTC+03 UTC+03:30 UTC+04 UTC+04:30
    # UTC+05 UTC+05:30 UTC+05:45 UTC+06 UTC+06:30 UTC+07 UTC+08 UTC+09 UTC+09:30
    # UTC+10 UTC+10:30 UTC+11 UTC+12 UTC+13 UTC-02 UTC-03 UTC-04 UTC-05 UTC-06
    # UTC-07 UTC-08 UTC-09 UTC-10 UTC-11
    timezone: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SegmentBehaviors(ShapeBase):
    """
    Segment behavior dimensions
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "recency",
                "Recency",
                TypeInfo(RecencyDimension),
            ),
        ]

    # The recency of use.
    recency: "RecencyDimension" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SegmentDemographics(ShapeBase):
    """
    Segment demographic dimensions
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "app_version",
                "AppVersion",
                TypeInfo(SetDimension),
            ),
            (
                "channel",
                "Channel",
                TypeInfo(SetDimension),
            ),
            (
                "device_type",
                "DeviceType",
                TypeInfo(SetDimension),
            ),
            (
                "make",
                "Make",
                TypeInfo(SetDimension),
            ),
            (
                "model",
                "Model",
                TypeInfo(SetDimension),
            ),
            (
                "platform",
                "Platform",
                TypeInfo(SetDimension),
            ),
        ]

    # The app version criteria for the segment.
    app_version: "SetDimension" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The channel criteria for the segment.
    channel: "SetDimension" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The device type criteria for the segment.
    device_type: "SetDimension" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The device make criteria for the segment.
    make: "SetDimension" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The device model criteria for the segment.
    model: "SetDimension" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The device platform criteria for the segment.
    platform: "SetDimension" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SegmentDimensions(ShapeBase):
    """
    Segment dimensions
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attributes",
                "Attributes",
                TypeInfo(typing.Dict[str, AttributeDimension]),
            ),
            (
                "behavior",
                "Behavior",
                TypeInfo(SegmentBehaviors),
            ),
            (
                "demographic",
                "Demographic",
                TypeInfo(SegmentDemographics),
            ),
            (
                "location",
                "Location",
                TypeInfo(SegmentLocation),
            ),
            (
                "metrics",
                "Metrics",
                TypeInfo(typing.Dict[str, MetricDimension]),
            ),
            (
                "user_attributes",
                "UserAttributes",
                TypeInfo(typing.Dict[str, AttributeDimension]),
            ),
        ]

    # Custom segment attributes.
    attributes: typing.Dict[str, "AttributeDimension"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The segment behaviors attributes.
    behavior: "SegmentBehaviors" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The segment demographics attributes.
    demographic: "SegmentDemographics" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The segment location attributes.
    location: "SegmentLocation" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Custom segment metrics.
    metrics: typing.Dict[str, "MetricDimension"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Custom segment user attributes.
    user_attributes: typing.Dict[str, "AttributeDimension"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SegmentGroup(ShapeBase):
    """
    Segment group definition.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "dimensions",
                "Dimensions",
                TypeInfo(typing.List[SegmentDimensions]),
            ),
            (
                "source_segments",
                "SourceSegments",
                TypeInfo(typing.List[SegmentReference]),
            ),
            (
                "source_type",
                "SourceType",
                TypeInfo(typing.Union[str, SourceType]),
            ),
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, Type]),
            ),
        ]

    # List of dimensions to include or exclude.
    dimensions: typing.List["SegmentDimensions"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The base segment that you build your segment on. The source segment defines
    # the starting "universe" of endpoints. When you add dimensions to the
    # segment, it filters the source segment based on the dimensions that you
    # specify. You can specify more than one dimensional segment. You can only
    # specify one imported segment.
    source_segments: typing.List["SegmentReference"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specify how to handle multiple source segments. For example, if you specify
    # three source segments, should the resulting segment be based on any or all
    # of the segments? Acceptable values: ANY or ALL.
    source_type: typing.Union[str, "SourceType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specify how to handle multiple segment dimensions. For example, if you
    # specify three dimensions, should the resulting segment include endpoints
    # that are matched by all, any, or none of the dimensions? Acceptable values:
    # ALL, ANY, or NONE.
    type: typing.Union[str, "Type"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SegmentGroupList(ShapeBase):
    """
    Segment group definition.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "groups",
                "Groups",
                TypeInfo(typing.List[SegmentGroup]),
            ),
            (
                "include",
                "Include",
                TypeInfo(typing.Union[str, Include]),
            ),
        ]

    # A set of segment criteria to evaluate.
    groups: typing.List["SegmentGroup"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specify how to handle multiple segment groups. For example, if the segment
    # includes three segment groups, should the resulting segment include
    # endpoints that are matched by all, any, or none of the segment groups you
    # created. Acceptable values: ALL, ANY, or NONE.
    include: typing.Union[str, "Include"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SegmentImportResource(ShapeBase):
    """
    Segment import definition.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "channel_counts",
                "ChannelCounts",
                TypeInfo(typing.Dict[str, int]),
            ),
            (
                "external_id",
                "ExternalId",
                TypeInfo(str),
            ),
            (
                "format",
                "Format",
                TypeInfo(typing.Union[str, Format]),
            ),
            (
                "role_arn",
                "RoleArn",
                TypeInfo(str),
            ),
            (
                "s3_url",
                "S3Url",
                TypeInfo(str),
            ),
            (
                "size",
                "Size",
                TypeInfo(int),
            ),
        ]

    # The number of channel types in the imported segment.
    channel_counts: typing.Dict[str, int] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # (Deprecated) Your AWS account ID, which you assigned to the ExternalID key
    # in an IAM trust policy. Used by Amazon Pinpoint to assume an IAM role. This
    # requirement is removed, and external IDs are not recommended for IAM roles
    # assumed by Amazon Pinpoint.
    external_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The format of the endpoint files that were imported to create this segment.
    # Valid values: CSV, JSON
    format: typing.Union[str, "Format"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of an IAM role that grants Amazon Pinpoint
    # access to the endpoints in Amazon S3.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The URL of the S3 bucket that the segment was imported from.
    s3_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of endpoints that were successfully imported to create this
    # segment.
    size: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SegmentLocation(ShapeBase):
    """
    Segment location dimensions
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "country",
                "Country",
                TypeInfo(SetDimension),
            ),
            (
                "gps_point",
                "GPSPoint",
                TypeInfo(GPSPointDimension),
            ),
        ]

    # The country filter according to ISO 3166-1 Alpha-2 codes.
    country: "SetDimension" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The GPS Point dimension.
    gps_point: "GPSPointDimension" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SegmentReference(ShapeBase):
    """
    Segment reference.
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
                "version",
                "Version",
                TypeInfo(int),
            ),
        ]

    # A unique identifier for the segment.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If specified contains a specific version of the segment included.
    version: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SegmentResponse(ShapeBase):
    """
    Segment definition.
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
                "creation_date",
                "CreationDate",
                TypeInfo(str),
            ),
            (
                "dimensions",
                "Dimensions",
                TypeInfo(SegmentDimensions),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "import_definition",
                "ImportDefinition",
                TypeInfo(SegmentImportResource),
            ),
            (
                "last_modified_date",
                "LastModifiedDate",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "segment_groups",
                "SegmentGroups",
                TypeInfo(SegmentGroupList),
            ),
            (
                "segment_type",
                "SegmentType",
                TypeInfo(typing.Union[str, SegmentType]),
            ),
            (
                "version",
                "Version",
                TypeInfo(int),
            ),
        ]

    # The ID of the application that the segment applies to.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time when the segment was created.
    creation_date: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The segment dimensions attributes.
    dimensions: "SegmentDimensions" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unique segment ID.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The import job settings.
    import_definition: "SegmentImportResource" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time when the segment was last modified.
    last_modified_date: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the segment.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A segment group, which consists of zero or more source segments, plus
    # dimensions that are applied to those source segments.
    segment_groups: "SegmentGroupList" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The segment type: DIMENSIONAL - A dynamic segment built from selection
    # criteria based on endpoint data reported by your app. You create this type
    # of segment by using the segment builder in the Amazon Pinpoint console or
    # by making a POST request to the segments resource. IMPORT - A static
    # segment built from an imported set of endpoint definitions. You create this
    # type of segment by importing a segment in the Amazon Pinpoint console or by
    # making a POST request to the jobs/import resource.
    segment_type: typing.Union[str, "SegmentType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The segment version number.
    version: int = dataclasses.field(default=ShapeBase.NOT_SET, )


class SegmentType(str):
    DIMENSIONAL = "DIMENSIONAL"
    IMPORT = "IMPORT"


@dataclasses.dataclass
class SegmentsResponse(ShapeBase):
    """
    Segments in your account.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "item",
                "Item",
                TypeInfo(typing.List[SegmentResponse]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The list of segments.
    item: typing.List["SegmentResponse"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An identifier used to retrieve the next page of results. The token is null
    # if no additional pages exist.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SendMessagesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
            (
                "message_request",
                "MessageRequest",
                TypeInfo(MessageRequest),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Send message request.
    message_request: "MessageRequest" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SendMessagesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "message_response",
                "MessageResponse",
                TypeInfo(MessageResponse),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Send message response.
    message_response: "MessageResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SendUsersMessageRequest(ShapeBase):
    """
    Send message request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "context",
                "Context",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "message_configuration",
                "MessageConfiguration",
                TypeInfo(DirectMessageConfiguration),
            ),
            (
                "trace_id",
                "TraceId",
                TypeInfo(str),
            ),
            (
                "users",
                "Users",
                TypeInfo(typing.Dict[str, EndpointSendConfiguration]),
            ),
        ]

    # A map of custom attribute-value pairs. Amazon Pinpoint adds these
    # attributes to the data.pinpoint object in the body of the push notification
    # payload. Amazon Pinpoint also provides these attributes in the events that
    # it generates for users-messages deliveries.
    context: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Message definitions for the default message and any messages that are
    # tailored for specific channels.
    message_configuration: "DirectMessageConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A unique ID that you can use to trace a message. This ID is visible to
    # recipients.
    trace_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A map that associates user IDs with EndpointSendConfiguration objects.
    # Within an EndpointSendConfiguration object, you can tailor the message for
    # a user by specifying message overrides or substitutions.
    users: typing.Dict[str, "EndpointSendConfiguration"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SendUsersMessageResponse(ShapeBase):
    """
    User send message response.
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
                "request_id",
                "RequestId",
                TypeInfo(str),
            ),
            (
                "result",
                "Result",
                TypeInfo(
                    typing.Dict[str, typing.Dict[str, EndpointMessageResult]]
                ),
            ),
        ]

    # The unique ID of the Amazon Pinpoint project used to send the message.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique ID assigned to the users-messages request.
    request_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An object that shows the endpoints that were messaged for each user. The
    # object provides a list of user IDs. For each user ID, it provides the
    # endpoint IDs that were messaged. For each endpoint ID, it provides an
    # EndpointMessageResult object.
    result: typing.Dict[str, typing.
                        Dict[str, "EndpointMessageResult"]] = dataclasses.field(
                            default=ShapeBase.NOT_SET,
                        )


@dataclasses.dataclass
class SendUsersMessagesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
            (
                "send_users_message_request",
                "SendUsersMessageRequest",
                TypeInfo(SendUsersMessageRequest),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Send message request.
    send_users_message_request: "SendUsersMessageRequest" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SendUsersMessagesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "send_users_message_response",
                "SendUsersMessageResponse",
                TypeInfo(SendUsersMessageResponse),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # User send message response.
    send_users_message_response: "SendUsersMessageResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Session(ShapeBase):
    """
    Information about a session.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "duration",
                "Duration",
                TypeInfo(int),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "start_timestamp",
                "StartTimestamp",
                TypeInfo(str),
            ),
            (
                "stop_timestamp",
                "StopTimestamp",
                TypeInfo(str),
            ),
        ]

    # Session duration in millis
    duration: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A unique identifier for the session.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time when the session began.
    start_timestamp: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time when the session ended.
    stop_timestamp: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SetDimension(ShapeBase):
    """
    Dimension specification of a segment.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "dimension_type",
                "DimensionType",
                TypeInfo(typing.Union[str, DimensionType]),
            ),
            (
                "values",
                "Values",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The type of dimension: INCLUSIVE - Endpoints that match the criteria are
    # included in the segment. EXCLUSIVE - Endpoints that match the criteria are
    # excluded from the segment.
    dimension_type: typing.Union[str, "DimensionType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The criteria values for the segment dimension. Endpoints with matching
    # attribute values are included or excluded from the segment, depending on
    # the setting for Type.
    values: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


class SourceType(str):
    ALL = "ALL"
    ANY = "ANY"
    NONE = "NONE"


@dataclasses.dataclass
class TooManyRequestsException(ShapeBase):
    """
    Simple message object.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
            (
                "request_id",
                "RequestID",
                TypeInfo(str),
            ),
        ]

    # The error message that's returned from the API.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique message body ID.
    request_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TreatmentResource(ShapeBase):
    """
    Treatment resource
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
                "message_configuration",
                "MessageConfiguration",
                TypeInfo(MessageConfiguration),
            ),
            (
                "schedule",
                "Schedule",
                TypeInfo(Schedule),
            ),
            (
                "size_percent",
                "SizePercent",
                TypeInfo(int),
            ),
            (
                "state",
                "State",
                TypeInfo(CampaignState),
            ),
            (
                "treatment_description",
                "TreatmentDescription",
                TypeInfo(str),
            ),
            (
                "treatment_name",
                "TreatmentName",
                TypeInfo(str),
            ),
        ]

    # The unique treatment ID.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The message configuration settings.
    message_configuration: "MessageConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The campaign schedule.
    schedule: "Schedule" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The allocated percentage of users for this treatment.
    size_percent: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The treatment status.
    state: "CampaignState" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A custom description for the treatment.
    treatment_description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The custom name of a variation of the campaign used for A/B testing.
    treatment_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class Type(str):
    ALL = "ALL"
    ANY = "ANY"
    NONE = "NONE"


@dataclasses.dataclass
class UpdateAdmChannelRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "adm_channel_request",
                "ADMChannelRequest",
                TypeInfo(ADMChannelRequest),
            ),
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
        ]

    # Amazon Device Messaging channel definition.
    adm_channel_request: "ADMChannelRequest" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateAdmChannelResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "adm_channel_response",
                "ADMChannelResponse",
                TypeInfo(ADMChannelResponse),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Amazon Device Messaging channel definition.
    adm_channel_response: "ADMChannelResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateApnsChannelRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "apns_channel_request",
                "APNSChannelRequest",
                TypeInfo(APNSChannelRequest),
            ),
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
        ]

    # Apple Push Notification Service channel definition.
    apns_channel_request: "APNSChannelRequest" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateApnsChannelResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "apns_channel_response",
                "APNSChannelResponse",
                TypeInfo(APNSChannelResponse),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Apple Distribution Push Notification Service channel definition.
    apns_channel_response: "APNSChannelResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateApnsSandboxChannelRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "apns_sandbox_channel_request",
                "APNSSandboxChannelRequest",
                TypeInfo(APNSSandboxChannelRequest),
            ),
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
        ]

    # Apple Development Push Notification Service channel definition.
    apns_sandbox_channel_request: "APNSSandboxChannelRequest" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateApnsSandboxChannelResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "apns_sandbox_channel_response",
                "APNSSandboxChannelResponse",
                TypeInfo(APNSSandboxChannelResponse),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Apple Development Push Notification Service channel definition.
    apns_sandbox_channel_response: "APNSSandboxChannelResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateApnsVoipChannelRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "apns_voip_channel_request",
                "APNSVoipChannelRequest",
                TypeInfo(APNSVoipChannelRequest),
            ),
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
        ]

    # Apple VoIP Push Notification Service channel definition.
    apns_voip_channel_request: "APNSVoipChannelRequest" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateApnsVoipChannelResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "apns_voip_channel_response",
                "APNSVoipChannelResponse",
                TypeInfo(APNSVoipChannelResponse),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Apple VoIP Push Notification Service channel definition.
    apns_voip_channel_response: "APNSVoipChannelResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateApnsVoipSandboxChannelRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "apns_voip_sandbox_channel_request",
                "APNSVoipSandboxChannelRequest",
                TypeInfo(APNSVoipSandboxChannelRequest),
            ),
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
        ]

    # Apple VoIP Developer Push Notification Service channel definition.
    apns_voip_sandbox_channel_request: "APNSVoipSandboxChannelRequest" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateApnsVoipSandboxChannelResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "apns_voip_sandbox_channel_response",
                "APNSVoipSandboxChannelResponse",
                TypeInfo(APNSVoipSandboxChannelResponse),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Apple VoIP Developer Push Notification Service channel definition.
    apns_voip_sandbox_channel_response: "APNSVoipSandboxChannelResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateApplicationSettingsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
            (
                "write_application_settings_request",
                "WriteApplicationSettingsRequest",
                TypeInfo(WriteApplicationSettingsRequest),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Creating application setting request
    write_application_settings_request: "WriteApplicationSettingsRequest" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateApplicationSettingsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "application_settings_resource",
                "ApplicationSettingsResource",
                TypeInfo(ApplicationSettingsResource),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Application settings.
    application_settings_resource: "ApplicationSettingsResource" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateAttributesRequest(ShapeBase):
    """
    Update attributes request
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "blacklist",
                "Blacklist",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The GLOB wildcard for removing the attributes in the application
    blacklist: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateBaiduChannelRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
            (
                "baidu_channel_request",
                "BaiduChannelRequest",
                TypeInfo(BaiduChannelRequest),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Baidu Cloud Push credentials
    baidu_channel_request: "BaiduChannelRequest" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateBaiduChannelResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "baidu_channel_response",
                "BaiduChannelResponse",
                TypeInfo(BaiduChannelResponse),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Baidu Cloud Messaging channel definition
    baidu_channel_response: "BaiduChannelResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateCampaignRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
            (
                "campaign_id",
                "CampaignId",
                TypeInfo(str),
            ),
            (
                "write_campaign_request",
                "WriteCampaignRequest",
                TypeInfo(WriteCampaignRequest),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique ID of the campaign.
    campaign_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Used to create a campaign.
    write_campaign_request: "WriteCampaignRequest" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateCampaignResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "campaign_response",
                "CampaignResponse",
                TypeInfo(CampaignResponse),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Campaign definition
    campaign_response: "CampaignResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateEmailChannelRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
            (
                "email_channel_request",
                "EmailChannelRequest",
                TypeInfo(EmailChannelRequest),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Email Channel Request
    email_channel_request: "EmailChannelRequest" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateEmailChannelResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "email_channel_response",
                "EmailChannelResponse",
                TypeInfo(EmailChannelResponse),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Email Channel Response.
    email_channel_response: "EmailChannelResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateEndpointRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
            (
                "endpoint_id",
                "EndpointId",
                TypeInfo(str),
            ),
            (
                "endpoint_request",
                "EndpointRequest",
                TypeInfo(EndpointRequest),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique ID of the endpoint.
    endpoint_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Endpoint update request
    endpoint_request: "EndpointRequest" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateEndpointResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "message_body",
                "MessageBody",
                TypeInfo(MessageBody),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Simple message object.
    message_body: "MessageBody" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateEndpointsBatchRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
            (
                "endpoint_batch_request",
                "EndpointBatchRequest",
                TypeInfo(EndpointBatchRequest),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Endpoint batch update request.
    endpoint_batch_request: "EndpointBatchRequest" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateEndpointsBatchResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "message_body",
                "MessageBody",
                TypeInfo(MessageBody),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Simple message object.
    message_body: "MessageBody" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateGcmChannelRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
            (
                "gcm_channel_request",
                "GCMChannelRequest",
                TypeInfo(GCMChannelRequest),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Google Cloud Messaging credentials
    gcm_channel_request: "GCMChannelRequest" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateGcmChannelResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "gcm_channel_response",
                "GCMChannelResponse",
                TypeInfo(GCMChannelResponse),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Google Cloud Messaging channel definition
    gcm_channel_response: "GCMChannelResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateSegmentRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
            (
                "segment_id",
                "SegmentId",
                TypeInfo(str),
            ),
            (
                "write_segment_request",
                "WriteSegmentRequest",
                TypeInfo(WriteSegmentRequest),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique ID of the segment.
    segment_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Segment definition.
    write_segment_request: "WriteSegmentRequest" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateSegmentResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "segment_response",
                "SegmentResponse",
                TypeInfo(SegmentResponse),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Segment definition.
    segment_response: "SegmentResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateSmsChannelRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "application_id",
                "ApplicationId",
                TypeInfo(str),
            ),
            (
                "sms_channel_request",
                "SMSChannelRequest",
                TypeInfo(SMSChannelRequest),
            ),
        ]

    # The unique ID of your Amazon Pinpoint application.
    application_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # SMS Channel Request
    sms_channel_request: "SMSChannelRequest" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateSmsChannelResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "sms_channel_response",
                "SMSChannelResponse",
                TypeInfo(SMSChannelResponse),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # SMS Channel Response.
    sms_channel_response: "SMSChannelResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class WriteApplicationSettingsRequest(ShapeBase):
    """
    Creating application setting request
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "campaign_hook",
                "CampaignHook",
                TypeInfo(CampaignHook),
            ),
            (
                "cloud_watch_metrics_enabled",
                "CloudWatchMetricsEnabled",
                TypeInfo(bool),
            ),
            (
                "limits",
                "Limits",
                TypeInfo(CampaignLimits),
            ),
            (
                "quiet_time",
                "QuietTime",
                TypeInfo(QuietTime),
            ),
        ]

    # Default campaign hook information.
    campaign_hook: "CampaignHook" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The CloudWatchMetrics settings for the app.
    cloud_watch_metrics_enabled: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The default campaign limits for the app. These limits apply to each
    # campaign for the app, unless the campaign overrides the default with limits
    # of its own.
    limits: "CampaignLimits" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The default quiet time for the app. Each campaign for this app sends no
    # messages during this time unless the campaign overrides the default with a
    # quiet time of its own.
    quiet_time: "QuietTime" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class WriteCampaignRequest(ShapeBase):
    """
    Used to create a campaign.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "additional_treatments",
                "AdditionalTreatments",
                TypeInfo(typing.List[WriteTreatmentResource]),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "holdout_percent",
                "HoldoutPercent",
                TypeInfo(int),
            ),
            (
                "hook",
                "Hook",
                TypeInfo(CampaignHook),
            ),
            (
                "is_paused",
                "IsPaused",
                TypeInfo(bool),
            ),
            (
                "limits",
                "Limits",
                TypeInfo(CampaignLimits),
            ),
            (
                "message_configuration",
                "MessageConfiguration",
                TypeInfo(MessageConfiguration),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "schedule",
                "Schedule",
                TypeInfo(Schedule),
            ),
            (
                "segment_id",
                "SegmentId",
                TypeInfo(str),
            ),
            (
                "segment_version",
                "SegmentVersion",
                TypeInfo(int),
            ),
            (
                "treatment_description",
                "TreatmentDescription",
                TypeInfo(str),
            ),
            (
                "treatment_name",
                "TreatmentName",
                TypeInfo(str),
            ),
        ]

    # Treatments that are defined in addition to the default treatment.
    additional_treatments: typing.List["WriteTreatmentResource"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    # A description of the campaign.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The allocated percentage of end users who will not receive messages from
    # this campaign.
    holdout_percent: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Campaign hook information.
    hook: "CampaignHook" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether the campaign is paused. A paused campaign does not send
    # messages unless you resume it by setting IsPaused to false.
    is_paused: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The campaign limits settings.
    limits: "CampaignLimits" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The message configuration settings.
    message_configuration: "MessageConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The custom name of the campaign.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The campaign schedule.
    schedule: "Schedule" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ID of the segment to which the campaign sends messages.
    segment_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version of the segment to which the campaign sends messages.
    segment_version: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A custom description for the treatment.
    treatment_description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The custom name of a variation of the campaign used for A/B testing.
    treatment_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class WriteEventStream(ShapeBase):
    """
    Request to save an EventStream.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "destination_stream_arn",
                "DestinationStreamArn",
                TypeInfo(str),
            ),
            (
                "role_arn",
                "RoleArn",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the Amazon Kinesis stream or Firehose
    # delivery stream to which you want to publish events. Firehose ARN:
    # arn:aws:firehose:REGION:ACCOUNT_ID:deliverystream/STREAM_NAME Kinesis ARN:
    # arn:aws:kinesis:REGION:ACCOUNT_ID:stream/STREAM_NAME
    destination_stream_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The IAM role that authorizes Amazon Pinpoint to publish events to the
    # stream in your account.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class WriteSegmentRequest(ShapeBase):
    """
    Segment definition.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "dimensions",
                "Dimensions",
                TypeInfo(SegmentDimensions),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "segment_groups",
                "SegmentGroups",
                TypeInfo(SegmentGroupList),
            ),
        ]

    # The segment dimensions attributes.
    dimensions: "SegmentDimensions" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of segment
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A segment group, which consists of zero or more source segments, plus
    # dimensions that are applied to those source segments. Your request can only
    # include one segment group. Your request can include either a SegmentGroups
    # object or a Dimensions object, but not both.
    segment_groups: "SegmentGroupList" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class WriteTreatmentResource(ShapeBase):
    """
    Used to create a campaign treatment.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message_configuration",
                "MessageConfiguration",
                TypeInfo(MessageConfiguration),
            ),
            (
                "schedule",
                "Schedule",
                TypeInfo(Schedule),
            ),
            (
                "size_percent",
                "SizePercent",
                TypeInfo(int),
            ),
            (
                "treatment_description",
                "TreatmentDescription",
                TypeInfo(str),
            ),
            (
                "treatment_name",
                "TreatmentName",
                TypeInfo(str),
            ),
        ]

    # The message configuration settings.
    message_configuration: "MessageConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The campaign schedule.
    schedule: "Schedule" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The allocated percentage of users for this treatment.
    size_percent: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A custom description for the treatment.
    treatment_description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The custom name of a variation of the campaign used for A/B testing.
    treatment_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )
