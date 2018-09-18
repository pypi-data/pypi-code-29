import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


class AacCodingMode(str):
    """
    Placeholder documentation for AacCodingMode
    """
    AD_RECEIVER_MIX = "AD_RECEIVER_MIX"
    CODING_MODE_1_0 = "CODING_MODE_1_0"
    CODING_MODE_1_1 = "CODING_MODE_1_1"
    CODING_MODE_2_0 = "CODING_MODE_2_0"
    CODING_MODE_5_1 = "CODING_MODE_5_1"


class AacInputType(str):
    """
    Placeholder documentation for AacInputType
    """
    BROADCASTER_MIXED_AD = "BROADCASTER_MIXED_AD"
    NORMAL = "NORMAL"


class AacProfile(str):
    """
    Placeholder documentation for AacProfile
    """
    HEV1 = "HEV1"
    HEV2 = "HEV2"
    LC = "LC"


class AacRateControlMode(str):
    """
    Placeholder documentation for AacRateControlMode
    """
    CBR = "CBR"
    VBR = "VBR"


class AacRawFormat(str):
    """
    Placeholder documentation for AacRawFormat
    """
    LATM_LOAS = "LATM_LOAS"
    NONE = "NONE"


@dataclasses.dataclass
class AacSettings(ShapeBase):
    """
    Placeholder documentation for AacSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bitrate",
                "Bitrate",
                TypeInfo(float),
            ),
            (
                "coding_mode",
                "CodingMode",
                TypeInfo(typing.Union[str, AacCodingMode]),
            ),
            (
                "input_type",
                "InputType",
                TypeInfo(typing.Union[str, AacInputType]),
            ),
            (
                "profile",
                "Profile",
                TypeInfo(typing.Union[str, AacProfile]),
            ),
            (
                "rate_control_mode",
                "RateControlMode",
                TypeInfo(typing.Union[str, AacRateControlMode]),
            ),
            (
                "raw_format",
                "RawFormat",
                TypeInfo(typing.Union[str, AacRawFormat]),
            ),
            (
                "sample_rate",
                "SampleRate",
                TypeInfo(float),
            ),
            (
                "spec",
                "Spec",
                TypeInfo(typing.Union[str, AacSpec]),
            ),
            (
                "vbr_quality",
                "VbrQuality",
                TypeInfo(typing.Union[str, AacVbrQuality]),
            ),
        ]

    # Average bitrate in bits/second. Valid values depend on rate control mode
    # and profile.
    bitrate: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Mono, Stereo, or 5.1 channel layout. Valid values depend on rate control
    # mode and profile. The adReceiverMix setting receives a stereo description
    # plus control track and emits a mono AAC encode of the description track,
    # with control data emitted in the PES header as per ETSI TS 101 154 Annex E.
    coding_mode: typing.Union[str, "AacCodingMode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Set to "broadcasterMixedAd" when input contains pre-mixed main audio + AD
    # (narration) as a stereo pair. The Audio Type field (audioType) will be set
    # to 3, which signals to downstream systems that this stream contains
    # "broadcaster mixed AD". Note that the input received by the encoder must
    # contain pre-mixed audio; the encoder does not perform the mixing. The
    # values in audioTypeControl and audioType (in AudioDescription) are ignored
    # when set to broadcasterMixedAd. Leave set to "normal" when input does not
    # contain pre-mixed audio + AD.
    input_type: typing.Union[str, "AacInputType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # AAC Profile.
    profile: typing.Union[str, "AacProfile"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Rate Control Mode.
    rate_control_mode: typing.Union[str, "AacRateControlMode"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # Sets LATM / LOAS AAC output for raw containers.
    raw_format: typing.Union[str, "AacRawFormat"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Sample rate in Hz. Valid values depend on rate control mode and profile.
    sample_rate: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use MPEG-2 AAC audio instead of MPEG-4 AAC audio for raw or MPEG-2
    # Transport Stream containers.
    spec: typing.Union[str, "AacSpec"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # VBR Quality Level - Only used if rateControlMode is VBR.
    vbr_quality: typing.Union[str, "AacVbrQuality"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class AacSpec(str):
    """
    Placeholder documentation for AacSpec
    """
    MPEG2 = "MPEG2"
    MPEG4 = "MPEG4"


class AacVbrQuality(str):
    """
    Placeholder documentation for AacVbrQuality
    """
    HIGH = "HIGH"
    LOW = "LOW"
    MEDIUM_HIGH = "MEDIUM_HIGH"
    MEDIUM_LOW = "MEDIUM_LOW"


class Ac3BitstreamMode(str):
    """
    Placeholder documentation for Ac3BitstreamMode
    """
    COMMENTARY = "COMMENTARY"
    COMPLETE_MAIN = "COMPLETE_MAIN"
    DIALOGUE = "DIALOGUE"
    EMERGENCY = "EMERGENCY"
    HEARING_IMPAIRED = "HEARING_IMPAIRED"
    MUSIC_AND_EFFECTS = "MUSIC_AND_EFFECTS"
    VISUALLY_IMPAIRED = "VISUALLY_IMPAIRED"
    VOICE_OVER = "VOICE_OVER"


class Ac3CodingMode(str):
    """
    Placeholder documentation for Ac3CodingMode
    """
    CODING_MODE_1_0 = "CODING_MODE_1_0"
    CODING_MODE_1_1 = "CODING_MODE_1_1"
    CODING_MODE_2_0 = "CODING_MODE_2_0"
    CODING_MODE_3_2_LFE = "CODING_MODE_3_2_LFE"


class Ac3DrcProfile(str):
    """
    Placeholder documentation for Ac3DrcProfile
    """
    FILM_STANDARD = "FILM_STANDARD"
    NONE = "NONE"


class Ac3LfeFilter(str):
    """
    Placeholder documentation for Ac3LfeFilter
    """
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class Ac3MetadataControl(str):
    """
    Placeholder documentation for Ac3MetadataControl
    """
    FOLLOW_INPUT = "FOLLOW_INPUT"
    USE_CONFIGURED = "USE_CONFIGURED"


@dataclasses.dataclass
class Ac3Settings(ShapeBase):
    """
    Placeholder documentation for Ac3Settings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bitrate",
                "Bitrate",
                TypeInfo(float),
            ),
            (
                "bitstream_mode",
                "BitstreamMode",
                TypeInfo(typing.Union[str, Ac3BitstreamMode]),
            ),
            (
                "coding_mode",
                "CodingMode",
                TypeInfo(typing.Union[str, Ac3CodingMode]),
            ),
            (
                "dialnorm",
                "Dialnorm",
                TypeInfo(int),
            ),
            (
                "drc_profile",
                "DrcProfile",
                TypeInfo(typing.Union[str, Ac3DrcProfile]),
            ),
            (
                "lfe_filter",
                "LfeFilter",
                TypeInfo(typing.Union[str, Ac3LfeFilter]),
            ),
            (
                "metadata_control",
                "MetadataControl",
                TypeInfo(typing.Union[str, Ac3MetadataControl]),
            ),
        ]

    # Average bitrate in bits/second. Valid bitrates depend on the coding mode.
    bitrate: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the bitstream mode (bsmod) for the emitted AC-3 stream. See ATSC
    # A/52-2012 for background on these values.
    bitstream_mode: typing.Union[str, "Ac3BitstreamMode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Dolby Digital coding mode. Determines number of channels.
    coding_mode: typing.Union[str, "Ac3CodingMode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Sets the dialnorm for the output. If excluded and input audio is Dolby
    # Digital, dialnorm will be passed through.
    dialnorm: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If set to filmStandard, adds dynamic range compression signaling to the
    # output bitstream as defined in the Dolby Digital specification.
    drc_profile: typing.Union[str, "Ac3DrcProfile"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When set to enabled, applies a 120Hz lowpass filter to the LFE channel
    # prior to encoding. Only valid in codingMode32Lfe mode.
    lfe_filter: typing.Union[str, "Ac3LfeFilter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When set to "followInput", encoder metadata will be sourced from the DD,
    # DD+, or DolbyE decoder that supplied this audio data. If audio was not
    # supplied from one of these streams, then the static metadata settings will
    # be used.
    metadata_control: typing.Union[str, "Ac3MetadataControl"
                                  ] = dataclasses.field(
                                      default=ShapeBase.NOT_SET,
                                  )


@dataclasses.dataclass
class AccessDenied(ShapeBase):
    """
    Placeholder documentation for AccessDenied
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    # Placeholder documentation for __string
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class AfdSignaling(str):
    """
    Placeholder documentation for AfdSignaling
    """
    AUTO = "AUTO"
    FIXED = "FIXED"
    NONE = "NONE"


@dataclasses.dataclass
class ArchiveContainerSettings(ShapeBase):
    """
    Placeholder documentation for ArchiveContainerSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "m2ts_settings",
                "M2tsSettings",
                TypeInfo(M2tsSettings),
            ),
        ]

    # Placeholder documentation for M2tsSettings
    m2ts_settings: "M2tsSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ArchiveGroupSettings(ShapeBase):
    """
    Placeholder documentation for ArchiveGroupSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "destination",
                "Destination",
                TypeInfo(OutputLocationRef),
            ),
            (
                "rollover_interval",
                "RolloverInterval",
                TypeInfo(int),
            ),
        ]

    # A directory and base filename where archive files should be written. If the
    # base filename portion of the URI is left blank, the base filename of the
    # first input will be automatically inserted.
    destination: "OutputLocationRef" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Number of seconds to write to archive file before closing and starting a
    # new one.
    rollover_interval: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ArchiveOutputSettings(ShapeBase):
    """
    Placeholder documentation for ArchiveOutputSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "container_settings",
                "ContainerSettings",
                TypeInfo(ArchiveContainerSettings),
            ),
            (
                "extension",
                "Extension",
                TypeInfo(str),
            ),
            (
                "name_modifier",
                "NameModifier",
                TypeInfo(str),
            ),
        ]

    # Settings specific to the container type of the file.
    container_settings: "ArchiveContainerSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Output file extension. If excluded, this will be auto-selected from the
    # container type.
    extension: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # String concatenated to the end of the destination filename. Required for
    # multiple outputs of the same type.
    name_modifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AribDestinationSettings(ShapeBase):
    """
    Placeholder documentation for AribDestinationSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class AribSourceSettings(ShapeBase):
    """
    Placeholder documentation for AribSourceSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class AudioChannelMapping(ShapeBase):
    """
    Placeholder documentation for AudioChannelMapping
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "input_channel_levels",
                "InputChannelLevels",
                TypeInfo(typing.List[InputChannelLevel]),
            ),
            (
                "output_channel",
                "OutputChannel",
                TypeInfo(int),
            ),
        ]

    # Indices and gain values for each input channel that should be remixed into
    # this output channel.
    input_channel_levels: typing.List["InputChannelLevel"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The index of the output channel being produced.
    output_channel: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AudioCodecSettings(ShapeBase):
    """
    Placeholder documentation for AudioCodecSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "aac_settings",
                "AacSettings",
                TypeInfo(AacSettings),
            ),
            (
                "ac3_settings",
                "Ac3Settings",
                TypeInfo(Ac3Settings),
            ),
            (
                "eac3_settings",
                "Eac3Settings",
                TypeInfo(Eac3Settings),
            ),
            (
                "mp2_settings",
                "Mp2Settings",
                TypeInfo(Mp2Settings),
            ),
            (
                "pass_through_settings",
                "PassThroughSettings",
                TypeInfo(PassThroughSettings),
            ),
        ]

    # Placeholder documentation for AacSettings
    aac_settings: "AacSettings" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Placeholder documentation for Ac3Settings
    ac3_settings: "Ac3Settings" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Placeholder documentation for Eac3Settings
    eac3_settings: "Eac3Settings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Placeholder documentation for Mp2Settings
    mp2_settings: "Mp2Settings" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Placeholder documentation for PassThroughSettings
    pass_through_settings: "PassThroughSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AudioDescription(ShapeBase):
    """
    Placeholder documentation for AudioDescription
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "audio_selector_name",
                "AudioSelectorName",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "audio_normalization_settings",
                "AudioNormalizationSettings",
                TypeInfo(AudioNormalizationSettings),
            ),
            (
                "audio_type",
                "AudioType",
                TypeInfo(typing.Union[str, AudioType]),
            ),
            (
                "audio_type_control",
                "AudioTypeControl",
                TypeInfo(typing.Union[str, AudioDescriptionAudioTypeControl]),
            ),
            (
                "codec_settings",
                "CodecSettings",
                TypeInfo(AudioCodecSettings),
            ),
            (
                "language_code",
                "LanguageCode",
                TypeInfo(str),
            ),
            (
                "language_code_control",
                "LanguageCodeControl",
                TypeInfo(
                    typing.Union[str, AudioDescriptionLanguageCodeControl]
                ),
            ),
            (
                "remix_settings",
                "RemixSettings",
                TypeInfo(RemixSettings),
            ),
            (
                "stream_name",
                "StreamName",
                TypeInfo(str),
            ),
        ]

    # The name of the AudioSelector used as the source for this AudioDescription.
    audio_selector_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of this AudioDescription. Outputs will use this name to uniquely
    # identify this AudioDescription. Description names should be unique within
    # this Live Event.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Advanced audio normalization settings.
    audio_normalization_settings: "AudioNormalizationSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Applies only if audioTypeControl is useConfigured. The values for audioType
    # are defined in ISO-IEC 13818-1.
    audio_type: typing.Union[str, "AudioType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Determines how audio type is determined. followInput: If the input contains
    # an ISO 639 audioType, then that value is passed through to the output. If
    # the input contains no ISO 639 audioType, the value in Audio Type is
    # included in the output. useConfigured: The value in Audio Type is included
    # in the output. Note that this field and audioType are both ignored if
    # inputType is broadcasterMixedAd.
    audio_type_control: typing.Union[str, "AudioDescriptionAudioTypeControl"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )

    # Audio codec settings.
    codec_settings: "AudioCodecSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates the language of the audio output track. Only used if
    # languageControlMode is useConfigured, or there is no ISO 639 language code
    # specified in the input.
    language_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Choosing followInput will cause the ISO 639 language code of the output to
    # follow the ISO 639 language code of the input. The languageCode will be
    # used when useConfigured is set, or when followInput is selected but there
    # is no ISO 639 language code specified by the input.
    language_code_control: typing.Union[
        str, "AudioDescriptionLanguageCodeControl"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # Settings that control how input audio channels are remixed into the output
    # audio channels.
    remix_settings: "RemixSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Used for MS Smooth and Apple HLS outputs. Indicates the name displayed by
    # the player (eg. English, or Director Commentary).
    stream_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class AudioDescriptionAudioTypeControl(str):
    """
    Placeholder documentation for AudioDescriptionAudioTypeControl
    """
    FOLLOW_INPUT = "FOLLOW_INPUT"
    USE_CONFIGURED = "USE_CONFIGURED"


class AudioDescriptionLanguageCodeControl(str):
    """
    Placeholder documentation for AudioDescriptionLanguageCodeControl
    """
    FOLLOW_INPUT = "FOLLOW_INPUT"
    USE_CONFIGURED = "USE_CONFIGURED"


@dataclasses.dataclass
class AudioLanguageSelection(ShapeBase):
    """
    Placeholder documentation for AudioLanguageSelection
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "language_code",
                "LanguageCode",
                TypeInfo(str),
            ),
            (
                "language_selection_policy",
                "LanguageSelectionPolicy",
                TypeInfo(typing.Union[str, AudioLanguageSelectionPolicy]),
            ),
        ]

    # Selects a specific three-letter language code from within an audio source.
    language_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When set to "strict", the transport stream demux strictly identifies audio
    # streams by their language descriptor. If a PMT update occurs such that an
    # audio stream matching the initially selected language is no longer present
    # then mute will be encoded until the language returns. If "loose", then on a
    # PMT update the demux will choose another audio stream in the program with
    # the same stream type if it can't find one with the same language.
    language_selection_policy: typing.Union[str, "AudioLanguageSelectionPolicy"
                                           ] = dataclasses.field(
                                               default=ShapeBase.NOT_SET,
                                           )


class AudioLanguageSelectionPolicy(str):
    """
    Placeholder documentation for AudioLanguageSelectionPolicy
    """
    LOOSE = "LOOSE"
    STRICT = "STRICT"


class AudioNormalizationAlgorithm(str):
    """
    Placeholder documentation for AudioNormalizationAlgorithm
    """
    ITU_1770_1 = "ITU_1770_1"
    ITU_1770_2 = "ITU_1770_2"


class AudioNormalizationAlgorithmControl(str):
    """
    Placeholder documentation for AudioNormalizationAlgorithmControl
    """
    CORRECT_AUDIO = "CORRECT_AUDIO"


@dataclasses.dataclass
class AudioNormalizationSettings(ShapeBase):
    """
    Placeholder documentation for AudioNormalizationSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "algorithm",
                "Algorithm",
                TypeInfo(typing.Union[str, AudioNormalizationAlgorithm]),
            ),
            (
                "algorithm_control",
                "AlgorithmControl",
                TypeInfo(typing.Union[str, AudioNormalizationAlgorithmControl]),
            ),
            (
                "target_lkfs",
                "TargetLkfs",
                TypeInfo(float),
            ),
        ]

    # Audio normalization algorithm to use. itu17701 conforms to the CALM Act
    # specification, itu17702 conforms to the EBU R-128 specification.
    algorithm: typing.Union[str, "AudioNormalizationAlgorithm"
                           ] = dataclasses.field(
                               default=ShapeBase.NOT_SET,
                           )

    # When set to correctAudio the output audio is corrected using the chosen
    # algorithm. If set to measureOnly, the audio will be measured but not
    # adjusted.
    algorithm_control: typing.Union[str, "AudioNormalizationAlgorithmControl"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # Target LKFS(loudness) to adjust volume to. If no value is entered, a
    # default value will be used according to the chosen algorithm. The CALM Act
    # (1770-1) recommends a target of -24 LKFS. The EBU R-128 specification
    # (1770-2) recommends a target of -23 LKFS.
    target_lkfs: float = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AudioOnlyHlsSettings(ShapeBase):
    """
    Placeholder documentation for AudioOnlyHlsSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "audio_group_id",
                "AudioGroupId",
                TypeInfo(str),
            ),
            (
                "audio_only_image",
                "AudioOnlyImage",
                TypeInfo(InputLocation),
            ),
            (
                "audio_track_type",
                "AudioTrackType",
                TypeInfo(typing.Union[str, AudioOnlyHlsTrackType]),
            ),
        ]

    # Specifies the group to which the audio Rendition belongs.
    audio_group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # For use with an audio only Stream. Must be a .jpg or .png file. If given,
    # this image will be used as the cover-art for the audio only output.
    # Ideally, it should be formatted for an iPhone screen for two reasons. The
    # iPhone does not resize the image, it crops a centered image on the
    # top/bottom and left/right. Additionally, this image file gets saved bit-
    # for-bit into every 10-second segment file, so will increase bandwidth by
    # {image file size} * {segment count} * {user count.}.
    audio_only_image: "InputLocation" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Four types of audio-only tracks are supported: Audio-Only Variant Stream
    # The client can play back this audio-only stream instead of video in low-
    # bandwidth scenarios. Represented as an EXT-X-STREAM-INF in the HLS
    # manifest. Alternate Audio, Auto Select, Default Alternate rendition that
    # the client should try to play back by default. Represented as an EXT-X-
    # MEDIA in the HLS manifest with DEFAULT=YES, AUTOSELECT=YES Alternate Audio,
    # Auto Select, Not Default Alternate rendition that the client may try to
    # play back by default. Represented as an EXT-X-MEDIA in the HLS manifest
    # with DEFAULT=NO, AUTOSELECT=YES Alternate Audio, not Auto Select Alternate
    # rendition that the client will not try to play back by default. Represented
    # as an EXT-X-MEDIA in the HLS manifest with DEFAULT=NO, AUTOSELECT=NO
    audio_track_type: typing.Union[str, "AudioOnlyHlsTrackType"
                                  ] = dataclasses.field(
                                      default=ShapeBase.NOT_SET,
                                  )


class AudioOnlyHlsTrackType(str):
    """
    Placeholder documentation for AudioOnlyHlsTrackType
    """
    ALTERNATE_AUDIO_AUTO_SELECT = "ALTERNATE_AUDIO_AUTO_SELECT"
    ALTERNATE_AUDIO_AUTO_SELECT_DEFAULT = "ALTERNATE_AUDIO_AUTO_SELECT_DEFAULT"
    ALTERNATE_AUDIO_NOT_AUTO_SELECT = "ALTERNATE_AUDIO_NOT_AUTO_SELECT"
    AUDIO_ONLY_VARIANT_STREAM = "AUDIO_ONLY_VARIANT_STREAM"


@dataclasses.dataclass
class AudioPidSelection(ShapeBase):
    """
    Placeholder documentation for AudioPidSelection
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pid",
                "Pid",
                TypeInfo(int),
            ),
        ]

    # Selects a specific PID from within a source.
    pid: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AudioSelector(ShapeBase):
    """
    Placeholder documentation for AudioSelector
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
                "selector_settings",
                "SelectorSettings",
                TypeInfo(AudioSelectorSettings),
            ),
        ]

    # The name of this AudioSelector. AudioDescriptions will use this name to
    # uniquely identify this Selector. Selector names should be unique per input.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The audio selector settings.
    selector_settings: "AudioSelectorSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AudioSelectorSettings(ShapeBase):
    """
    Placeholder documentation for AudioSelectorSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "audio_language_selection",
                "AudioLanguageSelection",
                TypeInfo(AudioLanguageSelection),
            ),
            (
                "audio_pid_selection",
                "AudioPidSelection",
                TypeInfo(AudioPidSelection),
            ),
        ]

    # Placeholder documentation for AudioLanguageSelection
    audio_language_selection: "AudioLanguageSelection" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Placeholder documentation for AudioPidSelection
    audio_pid_selection: "AudioPidSelection" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class AudioType(str):
    """
    Placeholder documentation for AudioType
    """
    CLEAN_EFFECTS = "CLEAN_EFFECTS"
    HEARING_IMPAIRED = "HEARING_IMPAIRED"
    UNDEFINED = "UNDEFINED"
    VISUAL_IMPAIRED_COMMENTARY = "VISUAL_IMPAIRED_COMMENTARY"


class AuthenticationScheme(str):
    """
    Placeholder documentation for AuthenticationScheme
    """
    AKAMAI = "AKAMAI"
    COMMON = "COMMON"


@dataclasses.dataclass
class AvailBlanking(ShapeBase):
    """
    Placeholder documentation for AvailBlanking
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "avail_blanking_image",
                "AvailBlankingImage",
                TypeInfo(InputLocation),
            ),
            (
                "state",
                "State",
                TypeInfo(typing.Union[str, AvailBlankingState]),
            ),
        ]

    # Blanking image to be used. Leave empty for solid black. Only bmp and png
    # images are supported.
    avail_blanking_image: "InputLocation" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When set to enabled, causes video, audio and captions to be blanked when
    # insertion metadata is added.
    state: typing.Union[str, "AvailBlankingState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class AvailBlankingState(str):
    """
    Placeholder documentation for AvailBlankingState
    """
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


@dataclasses.dataclass
class AvailConfiguration(ShapeBase):
    """
    Placeholder documentation for AvailConfiguration
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "avail_settings",
                "AvailSettings",
                TypeInfo(AvailSettings),
            ),
        ]

    # Ad avail settings.
    avail_settings: "AvailSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AvailSettings(ShapeBase):
    """
    Placeholder documentation for AvailSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "scte35_splice_insert",
                "Scte35SpliceInsert",
                TypeInfo(Scte35SpliceInsert),
            ),
            (
                "scte35_time_signal_apos",
                "Scte35TimeSignalApos",
                TypeInfo(Scte35TimeSignalApos),
            ),
        ]

    # Placeholder documentation for Scte35SpliceInsert
    scte35_splice_insert: "Scte35SpliceInsert" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Placeholder documentation for Scte35TimeSignalApos
    scte35_time_signal_apos: "Scte35TimeSignalApos" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BadGatewayException(ShapeBase):
    """
    Placeholder documentation for BadGatewayException
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    # Placeholder documentation for __string
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BadRequestException(ShapeBase):
    """
    Placeholder documentation for BadRequestException
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    # Placeholder documentation for __string
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BatchScheduleActionCreateRequest(ShapeBase):
    """
    A list of schedule actions to create.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "schedule_actions",
                "ScheduleActions",
                TypeInfo(typing.List[ScheduleAction]),
            ),
        ]

    # A list of schedule actions to create.
    schedule_actions: typing.List["ScheduleAction"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchScheduleActionCreateResult(ShapeBase):
    """
    Returned list of created schedule actions.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "schedule_actions",
                "ScheduleActions",
                TypeInfo(typing.List[ScheduleAction]),
            ),
        ]

    # Returned list of created schedule actions.
    schedule_actions: typing.List["ScheduleAction"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchScheduleActionDeleteRequest(ShapeBase):
    """
    A list of schedule actions to delete.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "action_names",
                "ActionNames",
                TypeInfo(typing.List[str]),
            ),
        ]

    # A list of schedule actions to delete, identified by unique name.
    action_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchScheduleActionDeleteResult(ShapeBase):
    """
    Returned list of deleted schedule actions.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "schedule_actions",
                "ScheduleActions",
                TypeInfo(typing.List[ScheduleAction]),
            ),
        ]

    # Returned list of deleted schedule actions.
    schedule_actions: typing.List["ScheduleAction"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchUpdateScheduleRequest(ShapeBase):
    """
    List of actions to create and list of actions to delete.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "channel_id",
                "ChannelId",
                TypeInfo(str),
            ),
            (
                "creates",
                "Creates",
                TypeInfo(BatchScheduleActionCreateRequest),
            ),
            (
                "deletes",
                "Deletes",
                TypeInfo(BatchScheduleActionDeleteRequest),
            ),
        ]

    # Id of the channel whose schedule is being updated.
    channel_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Schedule actions to create in the schedule.
    creates: "BatchScheduleActionCreateRequest" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Schedule actions to delete from the schedule.
    deletes: "BatchScheduleActionDeleteRequest" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchUpdateScheduleResponse(OutputShapeBase):
    """
    Response to a batch update schedule call.
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
                "creates",
                "Creates",
                TypeInfo(BatchScheduleActionCreateResult),
            ),
            (
                "deletes",
                "Deletes",
                TypeInfo(BatchScheduleActionDeleteResult),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Schedule actions created in the schedule.
    creates: "BatchScheduleActionCreateResult" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Schedule actions deleted from the schedule.
    deletes: "BatchScheduleActionDeleteResult" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchUpdateScheduleResult(ShapeBase):
    """
    Results of a batch schedule update.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "creates",
                "Creates",
                TypeInfo(BatchScheduleActionCreateResult),
            ),
            (
                "deletes",
                "Deletes",
                TypeInfo(BatchScheduleActionDeleteResult),
            ),
        ]

    # Schedule actions created in the schedule.
    creates: "BatchScheduleActionCreateResult" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Schedule actions deleted from the schedule.
    deletes: "BatchScheduleActionDeleteResult" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BlackoutSlate(ShapeBase):
    """
    Placeholder documentation for BlackoutSlate
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "blackout_slate_image",
                "BlackoutSlateImage",
                TypeInfo(InputLocation),
            ),
            (
                "network_end_blackout",
                "NetworkEndBlackout",
                TypeInfo(typing.Union[str, BlackoutSlateNetworkEndBlackout]),
            ),
            (
                "network_end_blackout_image",
                "NetworkEndBlackoutImage",
                TypeInfo(InputLocation),
            ),
            (
                "network_id",
                "NetworkId",
                TypeInfo(str),
            ),
            (
                "state",
                "State",
                TypeInfo(typing.Union[str, BlackoutSlateState]),
            ),
        ]

    # Blackout slate image to be used. Leave empty for solid black. Only bmp and
    # png images are supported.
    blackout_slate_image: "InputLocation" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Setting to enabled causes the encoder to blackout the video, audio, and
    # captions, and raise the "Network Blackout Image" slate when an SCTE104/35
    # Network End Segmentation Descriptor is encountered. The blackout will be
    # lifted when the Network Start Segmentation Descriptor is encountered. The
    # Network End and Network Start descriptors must contain a network ID that
    # matches the value entered in "Network ID".
    network_end_blackout: typing.Union[str, "BlackoutSlateNetworkEndBlackout"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    # Path to local file to use as Network End Blackout image. Image will be
    # scaled to fill the entire output raster.
    network_end_blackout_image: "InputLocation" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Provides Network ID that matches EIDR ID format (e.g., "10.XXXX/XXXX-XXXX-
    # XXXX-XXXX-XXXX-C").
    network_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When set to enabled, causes video, audio and captions to be blanked when
    # indicated by program metadata.
    state: typing.Union[str, "BlackoutSlateState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class BlackoutSlateNetworkEndBlackout(str):
    """
    Placeholder documentation for BlackoutSlateNetworkEndBlackout
    """
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class BlackoutSlateState(str):
    """
    Placeholder documentation for BlackoutSlateState
    """
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class BurnInAlignment(str):
    """
    Placeholder documentation for BurnInAlignment
    """
    CENTERED = "CENTERED"
    LEFT = "LEFT"
    SMART = "SMART"


class BurnInBackgroundColor(str):
    """
    Placeholder documentation for BurnInBackgroundColor
    """
    BLACK = "BLACK"
    NONE = "NONE"
    WHITE = "WHITE"


@dataclasses.dataclass
class BurnInDestinationSettings(ShapeBase):
    """
    Placeholder documentation for BurnInDestinationSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "alignment",
                "Alignment",
                TypeInfo(typing.Union[str, BurnInAlignment]),
            ),
            (
                "background_color",
                "BackgroundColor",
                TypeInfo(typing.Union[str, BurnInBackgroundColor]),
            ),
            (
                "background_opacity",
                "BackgroundOpacity",
                TypeInfo(int),
            ),
            (
                "font",
                "Font",
                TypeInfo(InputLocation),
            ),
            (
                "font_color",
                "FontColor",
                TypeInfo(typing.Union[str, BurnInFontColor]),
            ),
            (
                "font_opacity",
                "FontOpacity",
                TypeInfo(int),
            ),
            (
                "font_resolution",
                "FontResolution",
                TypeInfo(int),
            ),
            (
                "font_size",
                "FontSize",
                TypeInfo(str),
            ),
            (
                "outline_color",
                "OutlineColor",
                TypeInfo(typing.Union[str, BurnInOutlineColor]),
            ),
            (
                "outline_size",
                "OutlineSize",
                TypeInfo(int),
            ),
            (
                "shadow_color",
                "ShadowColor",
                TypeInfo(typing.Union[str, BurnInShadowColor]),
            ),
            (
                "shadow_opacity",
                "ShadowOpacity",
                TypeInfo(int),
            ),
            (
                "shadow_x_offset",
                "ShadowXOffset",
                TypeInfo(int),
            ),
            (
                "shadow_y_offset",
                "ShadowYOffset",
                TypeInfo(int),
            ),
            (
                "teletext_grid_control",
                "TeletextGridControl",
                TypeInfo(typing.Union[str, BurnInTeletextGridControl]),
            ),
            (
                "x_position",
                "XPosition",
                TypeInfo(int),
            ),
            (
                "y_position",
                "YPosition",
                TypeInfo(int),
            ),
        ]

    # If no explicit xPosition or yPosition is provided, setting alignment to
    # centered will place the captions at the bottom center of the output.
    # Similarly, setting a left alignment will align captions to the bottom left
    # of the output. If x and y positions are given in conjunction with the
    # alignment parameter, the font will be justified (either left or centered)
    # relative to those coordinates. Selecting "smart" justification will left-
    # justify live subtitles and center-justify pre-recorded subtitles. All burn-
    # in and DVB-Sub font settings must match.
    alignment: typing.Union[str, "BurnInAlignment"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the color of the rectangle behind the captions. All burn-in and
    # DVB-Sub font settings must match.
    background_color: typing.Union[str, "BurnInBackgroundColor"
                                  ] = dataclasses.field(
                                      default=ShapeBase.NOT_SET,
                                  )

    # Specifies the opacity of the background rectangle. 255 is opaque; 0 is
    # transparent. Leaving this parameter out is equivalent to setting it to 0
    # (transparent). All burn-in and DVB-Sub font settings must match.
    background_opacity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # External font file used for caption burn-in. File extension must be 'ttf'
    # or 'tte'. Although the user can select output fonts for many different
    # types of input captions, embedded, STL and teletext sources use a strict
    # grid system. Using external fonts with these caption sources could cause
    # unexpected display of proportional fonts. All burn-in and DVB-Sub font
    # settings must match.
    font: "InputLocation" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the color of the burned-in captions. This option is not valid for
    # source captions that are STL, 608/embedded or teletext. These source
    # settings are already pre-defined by the caption stream. All burn-in and
    # DVB-Sub font settings must match.
    font_color: typing.Union[str, "BurnInFontColor"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the opacity of the burned-in captions. 255 is opaque; 0 is
    # transparent. All burn-in and DVB-Sub font settings must match.
    font_opacity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Font resolution in DPI (dots per inch); default is 96 dpi. All burn-in and
    # DVB-Sub font settings must match.
    font_resolution: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When set to 'auto' fontSize will scale depending on the size of the output.
    # Giving a positive integer will specify the exact font size in points. All
    # burn-in and DVB-Sub font settings must match.
    font_size: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies font outline color. This option is not valid for source captions
    # that are either 608/embedded or teletext. These source settings are already
    # pre-defined by the caption stream. All burn-in and DVB-Sub font settings
    # must match.
    outline_color: typing.Union[str, "BurnInOutlineColor"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies font outline size in pixels. This option is not valid for source
    # captions that are either 608/embedded or teletext. These source settings
    # are already pre-defined by the caption stream. All burn-in and DVB-Sub font
    # settings must match.
    outline_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the color of the shadow cast by the captions. All burn-in and
    # DVB-Sub font settings must match.
    shadow_color: typing.Union[str, "BurnInShadowColor"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the opacity of the shadow. 255 is opaque; 0 is transparent.
    # Leaving this parameter out is equivalent to setting it to 0 (transparent).
    # All burn-in and DVB-Sub font settings must match.
    shadow_opacity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the horizontal offset of the shadow relative to the captions in
    # pixels. A value of -2 would result in a shadow offset 2 pixels to the left.
    # All burn-in and DVB-Sub font settings must match.
    shadow_x_offset: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the vertical offset of the shadow relative to the captions in
    # pixels. A value of -2 would result in a shadow offset 2 pixels above the
    # text. All burn-in and DVB-Sub font settings must match.
    shadow_y_offset: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Controls whether a fixed grid size will be used to generate the output
    # subtitles bitmap. Only applicable for Teletext inputs and DVB-Sub/Burn-in
    # outputs.
    teletext_grid_control: typing.Union[str, "BurnInTeletextGridControl"
                                       ] = dataclasses.field(
                                           default=ShapeBase.NOT_SET,
                                       )

    # Specifies the horizontal position of the caption relative to the left side
    # of the output in pixels. A value of 10 would result in the captions
    # starting 10 pixels from the left of the output. If no explicit xPosition is
    # provided, the horizontal caption position will be determined by the
    # alignment parameter. All burn-in and DVB-Sub font settings must match.
    x_position: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the vertical position of the caption relative to the top of the
    # output in pixels. A value of 10 would result in the captions starting 10
    # pixels from the top of the output. If no explicit yPosition is provided,
    # the caption will be positioned towards the bottom of the output. All burn-
    # in and DVB-Sub font settings must match.
    y_position: int = dataclasses.field(default=ShapeBase.NOT_SET, )


class BurnInFontColor(str):
    """
    Placeholder documentation for BurnInFontColor
    """
    BLACK = "BLACK"
    BLUE = "BLUE"
    GREEN = "GREEN"
    RED = "RED"
    WHITE = "WHITE"
    YELLOW = "YELLOW"


class BurnInOutlineColor(str):
    """
    Placeholder documentation for BurnInOutlineColor
    """
    BLACK = "BLACK"
    BLUE = "BLUE"
    GREEN = "GREEN"
    RED = "RED"
    WHITE = "WHITE"
    YELLOW = "YELLOW"


class BurnInShadowColor(str):
    """
    Placeholder documentation for BurnInShadowColor
    """
    BLACK = "BLACK"
    NONE = "NONE"
    WHITE = "WHITE"


class BurnInTeletextGridControl(str):
    """
    Placeholder documentation for BurnInTeletextGridControl
    """
    FIXED = "FIXED"
    SCALED = "SCALED"


@dataclasses.dataclass
class CaptionDescription(ShapeBase):
    """
    Output groups for this Live Event. Output groups contain information about where
    streams should be distributed.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "caption_selector_name",
                "CaptionSelectorName",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "destination_settings",
                "DestinationSettings",
                TypeInfo(CaptionDestinationSettings),
            ),
            (
                "language_code",
                "LanguageCode",
                TypeInfo(str),
            ),
            (
                "language_description",
                "LanguageDescription",
                TypeInfo(str),
            ),
        ]

    # Specifies which input caption selector to use as a caption source when
    # generating output captions. This field should match a captionSelector name.
    caption_selector_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Name of the caption description. Used to associate a caption description
    # with an output. Names must be unique within an event.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Additional settings for captions destination that depend on the destination
    # type.
    destination_settings: "CaptionDestinationSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # ISO 639-2 three-digit code: http://www.loc.gov/standards/iso639-2/
    language_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Human readable information to indicate captions available for players (eg.
    # English, or Spanish).
    language_description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CaptionDestinationSettings(ShapeBase):
    """
    Placeholder documentation for CaptionDestinationSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arib_destination_settings",
                "AribDestinationSettings",
                TypeInfo(AribDestinationSettings),
            ),
            (
                "burn_in_destination_settings",
                "BurnInDestinationSettings",
                TypeInfo(BurnInDestinationSettings),
            ),
            (
                "dvb_sub_destination_settings",
                "DvbSubDestinationSettings",
                TypeInfo(DvbSubDestinationSettings),
            ),
            (
                "embedded_destination_settings",
                "EmbeddedDestinationSettings",
                TypeInfo(EmbeddedDestinationSettings),
            ),
            (
                "embedded_plus_scte20_destination_settings",
                "EmbeddedPlusScte20DestinationSettings",
                TypeInfo(EmbeddedPlusScte20DestinationSettings),
            ),
            (
                "rtmp_caption_info_destination_settings",
                "RtmpCaptionInfoDestinationSettings",
                TypeInfo(RtmpCaptionInfoDestinationSettings),
            ),
            (
                "scte20_plus_embedded_destination_settings",
                "Scte20PlusEmbeddedDestinationSettings",
                TypeInfo(Scte20PlusEmbeddedDestinationSettings),
            ),
            (
                "scte27_destination_settings",
                "Scte27DestinationSettings",
                TypeInfo(Scte27DestinationSettings),
            ),
            (
                "smpte_tt_destination_settings",
                "SmpteTtDestinationSettings",
                TypeInfo(SmpteTtDestinationSettings),
            ),
            (
                "teletext_destination_settings",
                "TeletextDestinationSettings",
                TypeInfo(TeletextDestinationSettings),
            ),
            (
                "ttml_destination_settings",
                "TtmlDestinationSettings",
                TypeInfo(TtmlDestinationSettings),
            ),
            (
                "webvtt_destination_settings",
                "WebvttDestinationSettings",
                TypeInfo(WebvttDestinationSettings),
            ),
        ]

    # Placeholder documentation for AribDestinationSettings
    arib_destination_settings: "AribDestinationSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Placeholder documentation for BurnInDestinationSettings
    burn_in_destination_settings: "BurnInDestinationSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Placeholder documentation for DvbSubDestinationSettings
    dvb_sub_destination_settings: "DvbSubDestinationSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Placeholder documentation for EmbeddedDestinationSettings
    embedded_destination_settings: "EmbeddedDestinationSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Placeholder documentation for EmbeddedPlusScte20DestinationSettings
    embedded_plus_scte20_destination_settings: "EmbeddedPlusScte20DestinationSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Placeholder documentation for RtmpCaptionInfoDestinationSettings
    rtmp_caption_info_destination_settings: "RtmpCaptionInfoDestinationSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Placeholder documentation for Scte20PlusEmbeddedDestinationSettings
    scte20_plus_embedded_destination_settings: "Scte20PlusEmbeddedDestinationSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Placeholder documentation for Scte27DestinationSettings
    scte27_destination_settings: "Scte27DestinationSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Placeholder documentation for SmpteTtDestinationSettings
    smpte_tt_destination_settings: "SmpteTtDestinationSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Placeholder documentation for TeletextDestinationSettings
    teletext_destination_settings: "TeletextDestinationSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Placeholder documentation for TtmlDestinationSettings
    ttml_destination_settings: "TtmlDestinationSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Placeholder documentation for WebvttDestinationSettings
    webvtt_destination_settings: "WebvttDestinationSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CaptionLanguageMapping(ShapeBase):
    """
    Maps a caption channel to an ISO 693-2 language code
    (http://www.loc.gov/standards/iso639-2), with an optional description.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "caption_channel",
                "CaptionChannel",
                TypeInfo(int),
            ),
            (
                "language_code",
                "LanguageCode",
                TypeInfo(str),
            ),
            (
                "language_description",
                "LanguageDescription",
                TypeInfo(str),
            ),
        ]

    # The closed caption channel being described by this CaptionLanguageMapping.
    # Each channel mapping must have a unique channel number (maximum of 4)
    caption_channel: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Three character ISO 639-2 language code (see
    # http://www.loc.gov/standards/iso639-2)
    language_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Textual description of language
    language_description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CaptionSelector(ShapeBase):
    """
    Output groups for this Live Event. Output groups contain information about where
    streams should be distributed.
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
                "language_code",
                "LanguageCode",
                TypeInfo(str),
            ),
            (
                "selector_settings",
                "SelectorSettings",
                TypeInfo(CaptionSelectorSettings),
            ),
        ]

    # Name identifier for a caption selector. This name is used to associate this
    # caption selector with one or more caption descriptions. Names must be
    # unique within an event.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When specified this field indicates the three letter language code of the
    # caption track to extract from the source.
    language_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Caption selector settings.
    selector_settings: "CaptionSelectorSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CaptionSelectorSettings(ShapeBase):
    """
    Placeholder documentation for CaptionSelectorSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arib_source_settings",
                "AribSourceSettings",
                TypeInfo(AribSourceSettings),
            ),
            (
                "dvb_sub_source_settings",
                "DvbSubSourceSettings",
                TypeInfo(DvbSubSourceSettings),
            ),
            (
                "embedded_source_settings",
                "EmbeddedSourceSettings",
                TypeInfo(EmbeddedSourceSettings),
            ),
            (
                "scte20_source_settings",
                "Scte20SourceSettings",
                TypeInfo(Scte20SourceSettings),
            ),
            (
                "scte27_source_settings",
                "Scte27SourceSettings",
                TypeInfo(Scte27SourceSettings),
            ),
            (
                "teletext_source_settings",
                "TeletextSourceSettings",
                TypeInfo(TeletextSourceSettings),
            ),
        ]

    # Placeholder documentation for AribSourceSettings
    arib_source_settings: "AribSourceSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Placeholder documentation for DvbSubSourceSettings
    dvb_sub_source_settings: "DvbSubSourceSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Placeholder documentation for EmbeddedSourceSettings
    embedded_source_settings: "EmbeddedSourceSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Placeholder documentation for Scte20SourceSettings
    scte20_source_settings: "Scte20SourceSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Placeholder documentation for Scte27SourceSettings
    scte27_source_settings: "Scte27SourceSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Placeholder documentation for TeletextSourceSettings
    teletext_source_settings: "TeletextSourceSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Channel(ShapeBase):
    """
    Placeholder documentation for Channel
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
                "destinations",
                "Destinations",
                TypeInfo(typing.List[OutputDestination]),
            ),
            (
                "egress_endpoints",
                "EgressEndpoints",
                TypeInfo(typing.List[ChannelEgressEndpoint]),
            ),
            (
                "encoder_settings",
                "EncoderSettings",
                TypeInfo(EncoderSettings),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "input_attachments",
                "InputAttachments",
                TypeInfo(typing.List[InputAttachment]),
            ),
            (
                "input_specification",
                "InputSpecification",
                TypeInfo(InputSpecification),
            ),
            (
                "log_level",
                "LogLevel",
                TypeInfo(typing.Union[str, LogLevel]),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "pipelines_running_count",
                "PipelinesRunningCount",
                TypeInfo(int),
            ),
            (
                "role_arn",
                "RoleArn",
                TypeInfo(str),
            ),
            (
                "state",
                "State",
                TypeInfo(typing.Union[str, ChannelState]),
            ),
        ]

    # The unique arn of the channel.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of destinations of the channel. For UDP outputs, there is one
    # destination per output. For other types (HLS, for example), there is one
    # destination per packager.
    destinations: typing.List["OutputDestination"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The endpoints where outgoing connections initiate from
    egress_endpoints: typing.List["ChannelEgressEndpoint"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Placeholder documentation for EncoderSettings
    encoder_settings: "EncoderSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unique id of the channel.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # List of input attachments for channel.
    input_attachments: typing.List["InputAttachment"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Placeholder documentation for InputSpecification
    input_specification: "InputSpecification" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The log level being written to CloudWatch Logs.
    log_level: typing.Union[str, "LogLevel"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the channel. (user-mutable)
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of currently healthy pipelines.
    pipelines_running_count: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the role assumed when running the
    # Channel.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Placeholder documentation for ChannelState
    state: typing.Union[str, "ChannelState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ChannelConfigurationValidationError(ShapeBase):
    """
    Placeholder documentation for ChannelConfigurationValidationError
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
                "validation_errors",
                "ValidationErrors",
                TypeInfo(typing.List[ValidationError]),
            ),
        ]

    # Placeholder documentation for __string
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A collection of validation error responses.
    validation_errors: typing.List["ValidationError"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ChannelEgressEndpoint(ShapeBase):
    """
    Placeholder documentation for ChannelEgressEndpoint
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "source_ip",
                "SourceIp",
                TypeInfo(str),
            ),
        ]

    # Public IP of where a channel's output comes from
    source_ip: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class ChannelState(str):
    """
    Placeholder documentation for ChannelState
    """
    CREATING = "CREATING"
    CREATE_FAILED = "CREATE_FAILED"
    IDLE = "IDLE"
    STARTING = "STARTING"
    RUNNING = "RUNNING"
    RECOVERING = "RECOVERING"
    STOPPING = "STOPPING"
    DELETING = "DELETING"
    DELETED = "DELETED"


@dataclasses.dataclass
class ChannelSummary(ShapeBase):
    """
    Placeholder documentation for ChannelSummary
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
                "destinations",
                "Destinations",
                TypeInfo(typing.List[OutputDestination]),
            ),
            (
                "egress_endpoints",
                "EgressEndpoints",
                TypeInfo(typing.List[ChannelEgressEndpoint]),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "input_attachments",
                "InputAttachments",
                TypeInfo(typing.List[InputAttachment]),
            ),
            (
                "input_specification",
                "InputSpecification",
                TypeInfo(InputSpecification),
            ),
            (
                "log_level",
                "LogLevel",
                TypeInfo(typing.Union[str, LogLevel]),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "pipelines_running_count",
                "PipelinesRunningCount",
                TypeInfo(int),
            ),
            (
                "role_arn",
                "RoleArn",
                TypeInfo(str),
            ),
            (
                "state",
                "State",
                TypeInfo(typing.Union[str, ChannelState]),
            ),
        ]

    # The unique arn of the channel.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of destinations of the channel. For UDP outputs, there is one
    # destination per output. For other types (HLS, for example), there is one
    # destination per packager.
    destinations: typing.List["OutputDestination"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The endpoints where outgoing connections initiate from
    egress_endpoints: typing.List["ChannelEgressEndpoint"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unique id of the channel.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # List of input attachments for channel.
    input_attachments: typing.List["InputAttachment"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Placeholder documentation for InputSpecification
    input_specification: "InputSpecification" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The log level being written to CloudWatch Logs.
    log_level: typing.Union[str, "LogLevel"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the channel. (user-mutable)
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of currently healthy pipelines.
    pipelines_running_count: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the role assumed when running the
    # Channel.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Placeholder documentation for ChannelState
    state: typing.Union[str, "ChannelState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ConflictException(ShapeBase):
    """
    Placeholder documentation for ConflictException
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    # Placeholder documentation for __string
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateChannel(ShapeBase):
    """
    Placeholder documentation for CreateChannel
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "destinations",
                "Destinations",
                TypeInfo(typing.List[OutputDestination]),
            ),
            (
                "encoder_settings",
                "EncoderSettings",
                TypeInfo(EncoderSettings),
            ),
            (
                "input_attachments",
                "InputAttachments",
                TypeInfo(typing.List[InputAttachment]),
            ),
            (
                "input_specification",
                "InputSpecification",
                TypeInfo(InputSpecification),
            ),
            (
                "log_level",
                "LogLevel",
                TypeInfo(typing.Union[str, LogLevel]),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "request_id",
                "RequestId",
                TypeInfo(str),
            ),
            (
                "reserved",
                "Reserved",
                TypeInfo(str),
            ),
            (
                "role_arn",
                "RoleArn",
                TypeInfo(str),
            ),
        ]

    # Placeholder documentation for __listOfOutputDestination
    destinations: typing.List["OutputDestination"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Placeholder documentation for EncoderSettings
    encoder_settings: "EncoderSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # List of input attachments for channel.
    input_attachments: typing.List["InputAttachment"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specification of input for this channel (max. bitrate, resolution, codec,
    # etc.)
    input_specification: "InputSpecification" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The log level to write to CloudWatch Logs.
    log_level: typing.Union[str, "LogLevel"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Name of channel.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique request ID to be specified. This is needed to prevent retries from
    # creating multiple resources.
    request_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Deprecated field that's only usable by whitelisted customers.
    reserved: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional Amazon Resource Name (ARN) of the role to assume when running
    # the Channel.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateChannelRequest(ShapeBase):
    """
    A request to create a channel
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "destinations",
                "Destinations",
                TypeInfo(typing.List[OutputDestination]),
            ),
            (
                "encoder_settings",
                "EncoderSettings",
                TypeInfo(EncoderSettings),
            ),
            (
                "input_attachments",
                "InputAttachments",
                TypeInfo(typing.List[InputAttachment]),
            ),
            (
                "input_specification",
                "InputSpecification",
                TypeInfo(InputSpecification),
            ),
            (
                "log_level",
                "LogLevel",
                TypeInfo(typing.Union[str, LogLevel]),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "request_id",
                "RequestId",
                TypeInfo(str),
            ),
            (
                "reserved",
                "Reserved",
                TypeInfo(str),
            ),
            (
                "role_arn",
                "RoleArn",
                TypeInfo(str),
            ),
        ]

    # Placeholder documentation for __listOfOutputDestination
    destinations: typing.List["OutputDestination"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Placeholder documentation for EncoderSettings
    encoder_settings: "EncoderSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # List of input attachments for channel.
    input_attachments: typing.List["InputAttachment"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specification of input for this channel (max. bitrate, resolution, codec,
    # etc.)
    input_specification: "InputSpecification" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The log level to write to CloudWatch Logs.
    log_level: typing.Union[str, "LogLevel"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Name of channel.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique request ID to be specified. This is needed to prevent retries from
    # creating multiple resources.
    request_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Deprecated field that's only usable by whitelisted customers.
    reserved: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional Amazon Resource Name (ARN) of the role to assume when running
    # the Channel.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateChannelResponse(OutputShapeBase):
    """
    Placeholder documentation for CreateChannelResponse
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
                "channel",
                "Channel",
                TypeInfo(Channel),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Placeholder documentation for Channel
    channel: "Channel" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateChannelResultModel(ShapeBase):
    """
    Placeholder documentation for CreateChannelResultModel
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "channel",
                "Channel",
                TypeInfo(Channel),
            ),
        ]

    # Placeholder documentation for Channel
    channel: "Channel" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateInput(ShapeBase):
    """
    Placeholder documentation for CreateInput
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "destinations",
                "Destinations",
                TypeInfo(typing.List[InputDestinationRequest]),
            ),
            (
                "input_security_groups",
                "InputSecurityGroups",
                TypeInfo(typing.List[str]),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "request_id",
                "RequestId",
                TypeInfo(str),
            ),
            (
                "sources",
                "Sources",
                TypeInfo(typing.List[InputSourceRequest]),
            ),
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, InputType]),
            ),
        ]

    # Destination settings for PUSH type inputs.
    destinations: typing.List["InputDestinationRequest"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of security groups referenced by IDs to attach to the input.
    input_security_groups: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Name of the input.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique identifier of the request to ensure the request is handled exactly
    # once in case of retries.
    request_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The source URLs for a PULL-type input. Every PULL type input needs exactly
    # two source URLs for redundancy. Only specify sources for PULL type Inputs.
    # Leave Destinations empty.
    sources: typing.List["InputSourceRequest"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Placeholder documentation for InputType
    type: typing.Union[str, "InputType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateInputRequest(ShapeBase):
    """
    The name of the input
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "destinations",
                "Destinations",
                TypeInfo(typing.List[InputDestinationRequest]),
            ),
            (
                "input_security_groups",
                "InputSecurityGroups",
                TypeInfo(typing.List[str]),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "request_id",
                "RequestId",
                TypeInfo(str),
            ),
            (
                "sources",
                "Sources",
                TypeInfo(typing.List[InputSourceRequest]),
            ),
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, InputType]),
            ),
        ]

    # Destination settings for PUSH type inputs.
    destinations: typing.List["InputDestinationRequest"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of security groups referenced by IDs to attach to the input.
    input_security_groups: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Name of the input.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique identifier of the request to ensure the request is handled exactly
    # once in case of retries.
    request_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The source URLs for a PULL-type input. Every PULL type input needs exactly
    # two source URLs for redundancy. Only specify sources for PULL type Inputs.
    # Leave Destinations empty.
    sources: typing.List["InputSourceRequest"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Placeholder documentation for InputType
    type: typing.Union[str, "InputType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateInputResponse(OutputShapeBase):
    """
    Placeholder documentation for CreateInputResponse
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
                "input",
                "Input",
                TypeInfo(Input),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Placeholder documentation for Input
    input: "Input" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateInputResultModel(ShapeBase):
    """
    Placeholder documentation for CreateInputResultModel
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "input",
                "Input",
                TypeInfo(Input),
            ),
        ]

    # Placeholder documentation for Input
    input: "Input" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateInputSecurityGroupRequest(ShapeBase):
    """
    The IPv4 CIDRs to whitelist for this Input Security Group
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "whitelist_rules",
                "WhitelistRules",
                TypeInfo(typing.List[InputWhitelistRuleCidr]),
            ),
        ]

    # List of IPv4 CIDR addresses to whitelist
    whitelist_rules: typing.List["InputWhitelistRuleCidr"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateInputSecurityGroupResponse(OutputShapeBase):
    """
    Placeholder documentation for CreateInputSecurityGroupResponse
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
                "security_group",
                "SecurityGroup",
                TypeInfo(InputSecurityGroup),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An Input Security Group
    security_group: "InputSecurityGroup" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateInputSecurityGroupResultModel(ShapeBase):
    """
    Placeholder documentation for CreateInputSecurityGroupResultModel
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "security_group",
                "SecurityGroup",
                TypeInfo(InputSecurityGroup),
            ),
        ]

    # An Input Security Group
    security_group: "InputSecurityGroup" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteChannelRequest(ShapeBase):
    """
    Placeholder documentation for DeleteChannelRequest
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "channel_id",
                "ChannelId",
                TypeInfo(str),
            ),
        ]

    # Unique ID of the channel.
    channel_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteChannelResponse(OutputShapeBase):
    """
    Placeholder documentation for DeleteChannelResponse
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
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "destinations",
                "Destinations",
                TypeInfo(typing.List[OutputDestination]),
            ),
            (
                "egress_endpoints",
                "EgressEndpoints",
                TypeInfo(typing.List[ChannelEgressEndpoint]),
            ),
            (
                "encoder_settings",
                "EncoderSettings",
                TypeInfo(EncoderSettings),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "input_attachments",
                "InputAttachments",
                TypeInfo(typing.List[InputAttachment]),
            ),
            (
                "input_specification",
                "InputSpecification",
                TypeInfo(InputSpecification),
            ),
            (
                "log_level",
                "LogLevel",
                TypeInfo(typing.Union[str, LogLevel]),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "pipelines_running_count",
                "PipelinesRunningCount",
                TypeInfo(int),
            ),
            (
                "role_arn",
                "RoleArn",
                TypeInfo(str),
            ),
            (
                "state",
                "State",
                TypeInfo(typing.Union[str, ChannelState]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unique arn of the channel.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of destinations of the channel. For UDP outputs, there is one
    # destination per output. For other types (HLS, for example), there is one
    # destination per packager.
    destinations: typing.List["OutputDestination"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The endpoints where outgoing connections initiate from
    egress_endpoints: typing.List["ChannelEgressEndpoint"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Placeholder documentation for EncoderSettings
    encoder_settings: "EncoderSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unique id of the channel.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # List of input attachments for channel.
    input_attachments: typing.List["InputAttachment"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Placeholder documentation for InputSpecification
    input_specification: "InputSpecification" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The log level being written to CloudWatch Logs.
    log_level: typing.Union[str, "LogLevel"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the channel. (user-mutable)
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of currently healthy pipelines.
    pipelines_running_count: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the role assumed when running the
    # Channel.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Placeholder documentation for ChannelState
    state: typing.Union[str, "ChannelState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteInputRequest(ShapeBase):
    """
    Placeholder documentation for DeleteInputRequest
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "input_id",
                "InputId",
                TypeInfo(str),
            ),
        ]

    # Unique ID of the input
    input_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteInputResponse(OutputShapeBase):
    """
    Placeholder documentation for DeleteInputResponse
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
class DeleteInputSecurityGroupRequest(ShapeBase):
    """
    Placeholder documentation for DeleteInputSecurityGroupRequest
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "input_security_group_id",
                "InputSecurityGroupId",
                TypeInfo(str),
            ),
        ]

    # The Input Security Group to delete
    input_security_group_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteInputSecurityGroupResponse(OutputShapeBase):
    """
    Placeholder documentation for DeleteInputSecurityGroupResponse
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
class DeleteReservationRequest(ShapeBase):
    """
    Placeholder documentation for DeleteReservationRequest
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "reservation_id",
                "ReservationId",
                TypeInfo(str),
            ),
        ]

    # Unique reservation ID, e.g. '1234567'
    reservation_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteReservationResponse(OutputShapeBase):
    """
    Placeholder documentation for DeleteReservationResponse
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
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "count",
                "Count",
                TypeInfo(int),
            ),
            (
                "currency_code",
                "CurrencyCode",
                TypeInfo(str),
            ),
            (
                "duration",
                "Duration",
                TypeInfo(int),
            ),
            (
                "duration_units",
                "DurationUnits",
                TypeInfo(typing.Union[str, OfferingDurationUnits]),
            ),
            (
                "end",
                "End",
                TypeInfo(str),
            ),
            (
                "fixed_price",
                "FixedPrice",
                TypeInfo(float),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "offering_description",
                "OfferingDescription",
                TypeInfo(str),
            ),
            (
                "offering_id",
                "OfferingId",
                TypeInfo(str),
            ),
            (
                "offering_type",
                "OfferingType",
                TypeInfo(typing.Union[str, OfferingType]),
            ),
            (
                "region",
                "Region",
                TypeInfo(str),
            ),
            (
                "reservation_id",
                "ReservationId",
                TypeInfo(str),
            ),
            (
                "resource_specification",
                "ResourceSpecification",
                TypeInfo(ReservationResourceSpecification),
            ),
            (
                "start",
                "Start",
                TypeInfo(str),
            ),
            (
                "state",
                "State",
                TypeInfo(typing.Union[str, ReservationState]),
            ),
            (
                "usage_price",
                "UsagePrice",
                TypeInfo(float),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Unique reservation ARN, e.g. 'arn:aws:medialive:us-
    # west-2:123456789012:reservation:1234567'
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Number of reserved resources
    count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Currency code for usagePrice and fixedPrice in ISO-4217 format, e.g. 'USD'
    currency_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Lease duration, e.g. '12'
    duration: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Units for duration, e.g. 'MONTHS'
    duration_units: typing.Union[str, "OfferingDurationUnits"
                                ] = dataclasses.field(
                                    default=ShapeBase.NOT_SET,
                                )

    # Reservation UTC end date and time in ISO-8601 format, e.g.
    # '2019-03-01T00:00:00'
    end: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # One-time charge for each reserved resource, e.g. '0.0' for a NO_UPFRONT
    # offering
    fixed_price: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # User specified reservation name
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Offering description, e.g. 'HD AVC output at 10-20 Mbps, 30 fps, and
    # standard VQ in US West (Oregon)'
    offering_description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique offering ID, e.g. '87654321'
    offering_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Offering type, e.g. 'NO_UPFRONT'
    offering_type: typing.Union[str, "OfferingType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # AWS region, e.g. 'us-west-2'
    region: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique reservation ID, e.g. '1234567'
    reservation_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Resource configuration details
    resource_specification: "ReservationResourceSpecification" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Reservation UTC start date and time in ISO-8601 format, e.g.
    # '2018-03-01T00:00:00'
    start: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Current state of reservation, e.g. 'ACTIVE'
    state: typing.Union[str, "ReservationState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Recurring usage charge for each reserved resource, e.g. '157.0'
    usage_price: float = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeChannelRequest(ShapeBase):
    """
    Placeholder documentation for DescribeChannelRequest
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "channel_id",
                "ChannelId",
                TypeInfo(str),
            ),
        ]

    # channel ID
    channel_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeChannelResponse(OutputShapeBase):
    """
    Placeholder documentation for DescribeChannelResponse
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
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "destinations",
                "Destinations",
                TypeInfo(typing.List[OutputDestination]),
            ),
            (
                "egress_endpoints",
                "EgressEndpoints",
                TypeInfo(typing.List[ChannelEgressEndpoint]),
            ),
            (
                "encoder_settings",
                "EncoderSettings",
                TypeInfo(EncoderSettings),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "input_attachments",
                "InputAttachments",
                TypeInfo(typing.List[InputAttachment]),
            ),
            (
                "input_specification",
                "InputSpecification",
                TypeInfo(InputSpecification),
            ),
            (
                "log_level",
                "LogLevel",
                TypeInfo(typing.Union[str, LogLevel]),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "pipelines_running_count",
                "PipelinesRunningCount",
                TypeInfo(int),
            ),
            (
                "role_arn",
                "RoleArn",
                TypeInfo(str),
            ),
            (
                "state",
                "State",
                TypeInfo(typing.Union[str, ChannelState]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unique arn of the channel.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of destinations of the channel. For UDP outputs, there is one
    # destination per output. For other types (HLS, for example), there is one
    # destination per packager.
    destinations: typing.List["OutputDestination"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The endpoints where outgoing connections initiate from
    egress_endpoints: typing.List["ChannelEgressEndpoint"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Placeholder documentation for EncoderSettings
    encoder_settings: "EncoderSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unique id of the channel.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # List of input attachments for channel.
    input_attachments: typing.List["InputAttachment"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Placeholder documentation for InputSpecification
    input_specification: "InputSpecification" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The log level being written to CloudWatch Logs.
    log_level: typing.Union[str, "LogLevel"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the channel. (user-mutable)
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of currently healthy pipelines.
    pipelines_running_count: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the role assumed when running the
    # Channel.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Placeholder documentation for ChannelState
    state: typing.Union[str, "ChannelState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeInputRequest(ShapeBase):
    """
    Placeholder documentation for DescribeInputRequest
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "input_id",
                "InputId",
                TypeInfo(str),
            ),
        ]

    # Unique ID of the input
    input_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeInputResponse(OutputShapeBase):
    """
    Placeholder documentation for DescribeInputResponse
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
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "attached_channels",
                "AttachedChannels",
                TypeInfo(typing.List[str]),
            ),
            (
                "destinations",
                "Destinations",
                TypeInfo(typing.List[InputDestination]),
            ),
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
                "security_groups",
                "SecurityGroups",
                TypeInfo(typing.List[str]),
            ),
            (
                "sources",
                "Sources",
                TypeInfo(typing.List[InputSource]),
            ),
            (
                "state",
                "State",
                TypeInfo(typing.Union[str, InputState]),
            ),
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, InputType]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Unique ARN of the input (generated, immutable).
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of channel IDs that that input is attached to (currently an input
    # can only be attached to one channel).
    attached_channels: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of the destinations of the input (PUSH-type).
    destinations: typing.List["InputDestination"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The generated ID of the input (unique for user account, immutable).
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The user-assigned name (This is a mutable value).
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of IDs for all the security groups attached to the input.
    security_groups: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of the sources of the input (PULL-type).
    sources: typing.List["InputSource"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Placeholder documentation for InputState
    state: typing.Union[str, "InputState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Placeholder documentation for InputType
    type: typing.Union[str, "InputType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeInputSecurityGroupRequest(ShapeBase):
    """
    Placeholder documentation for DescribeInputSecurityGroupRequest
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "input_security_group_id",
                "InputSecurityGroupId",
                TypeInfo(str),
            ),
        ]

    # The id of the Input Security Group to describe
    input_security_group_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeInputSecurityGroupResponse(OutputShapeBase):
    """
    Placeholder documentation for DescribeInputSecurityGroupResponse
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
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "inputs",
                "Inputs",
                TypeInfo(typing.List[str]),
            ),
            (
                "state",
                "State",
                TypeInfo(typing.Union[str, InputSecurityGroupState]),
            ),
            (
                "whitelist_rules",
                "WhitelistRules",
                TypeInfo(typing.List[InputWhitelistRule]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Unique ARN of Input Security Group
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Id of the Input Security Group
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of inputs currently using this Input Security Group.
    inputs: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current state of the Input Security Group.
    state: typing.Union[str, "InputSecurityGroupState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Whitelist rules and their sync status
    whitelist_rules: typing.List["InputWhitelistRule"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeOfferingRequest(ShapeBase):
    """
    Placeholder documentation for DescribeOfferingRequest
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "offering_id",
                "OfferingId",
                TypeInfo(str),
            ),
        ]

    # Unique offering ID, e.g. '87654321'
    offering_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeOfferingResponse(OutputShapeBase):
    """
    Placeholder documentation for DescribeOfferingResponse
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
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "currency_code",
                "CurrencyCode",
                TypeInfo(str),
            ),
            (
                "duration",
                "Duration",
                TypeInfo(int),
            ),
            (
                "duration_units",
                "DurationUnits",
                TypeInfo(typing.Union[str, OfferingDurationUnits]),
            ),
            (
                "fixed_price",
                "FixedPrice",
                TypeInfo(float),
            ),
            (
                "offering_description",
                "OfferingDescription",
                TypeInfo(str),
            ),
            (
                "offering_id",
                "OfferingId",
                TypeInfo(str),
            ),
            (
                "offering_type",
                "OfferingType",
                TypeInfo(typing.Union[str, OfferingType]),
            ),
            (
                "region",
                "Region",
                TypeInfo(str),
            ),
            (
                "resource_specification",
                "ResourceSpecification",
                TypeInfo(ReservationResourceSpecification),
            ),
            (
                "usage_price",
                "UsagePrice",
                TypeInfo(float),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Unique offering ARN, e.g. 'arn:aws:medialive:us-
    # west-2:123456789012:offering:87654321'
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Currency code for usagePrice and fixedPrice in ISO-4217 format, e.g. 'USD'
    currency_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Lease duration, e.g. '12'
    duration: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Units for duration, e.g. 'MONTHS'
    duration_units: typing.Union[str, "OfferingDurationUnits"
                                ] = dataclasses.field(
                                    default=ShapeBase.NOT_SET,
                                )

    # One-time charge for each reserved resource, e.g. '0.0' for a NO_UPFRONT
    # offering
    fixed_price: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Offering description, e.g. 'HD AVC output at 10-20 Mbps, 30 fps, and
    # standard VQ in US West (Oregon)'
    offering_description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique offering ID, e.g. '87654321'
    offering_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Offering type, e.g. 'NO_UPFRONT'
    offering_type: typing.Union[str, "OfferingType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # AWS region, e.g. 'us-west-2'
    region: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Resource configuration details
    resource_specification: "ReservationResourceSpecification" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Recurring usage charge for each reserved resource, e.g. '157.0'
    usage_price: float = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeReservationRequest(ShapeBase):
    """
    Placeholder documentation for DescribeReservationRequest
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "reservation_id",
                "ReservationId",
                TypeInfo(str),
            ),
        ]

    # Unique reservation ID, e.g. '1234567'
    reservation_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeReservationResponse(OutputShapeBase):
    """
    Placeholder documentation for DescribeReservationResponse
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
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "count",
                "Count",
                TypeInfo(int),
            ),
            (
                "currency_code",
                "CurrencyCode",
                TypeInfo(str),
            ),
            (
                "duration",
                "Duration",
                TypeInfo(int),
            ),
            (
                "duration_units",
                "DurationUnits",
                TypeInfo(typing.Union[str, OfferingDurationUnits]),
            ),
            (
                "end",
                "End",
                TypeInfo(str),
            ),
            (
                "fixed_price",
                "FixedPrice",
                TypeInfo(float),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "offering_description",
                "OfferingDescription",
                TypeInfo(str),
            ),
            (
                "offering_id",
                "OfferingId",
                TypeInfo(str),
            ),
            (
                "offering_type",
                "OfferingType",
                TypeInfo(typing.Union[str, OfferingType]),
            ),
            (
                "region",
                "Region",
                TypeInfo(str),
            ),
            (
                "reservation_id",
                "ReservationId",
                TypeInfo(str),
            ),
            (
                "resource_specification",
                "ResourceSpecification",
                TypeInfo(ReservationResourceSpecification),
            ),
            (
                "start",
                "Start",
                TypeInfo(str),
            ),
            (
                "state",
                "State",
                TypeInfo(typing.Union[str, ReservationState]),
            ),
            (
                "usage_price",
                "UsagePrice",
                TypeInfo(float),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Unique reservation ARN, e.g. 'arn:aws:medialive:us-
    # west-2:123456789012:reservation:1234567'
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Number of reserved resources
    count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Currency code for usagePrice and fixedPrice in ISO-4217 format, e.g. 'USD'
    currency_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Lease duration, e.g. '12'
    duration: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Units for duration, e.g. 'MONTHS'
    duration_units: typing.Union[str, "OfferingDurationUnits"
                                ] = dataclasses.field(
                                    default=ShapeBase.NOT_SET,
                                )

    # Reservation UTC end date and time in ISO-8601 format, e.g.
    # '2019-03-01T00:00:00'
    end: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # One-time charge for each reserved resource, e.g. '0.0' for a NO_UPFRONT
    # offering
    fixed_price: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # User specified reservation name
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Offering description, e.g. 'HD AVC output at 10-20 Mbps, 30 fps, and
    # standard VQ in US West (Oregon)'
    offering_description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique offering ID, e.g. '87654321'
    offering_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Offering type, e.g. 'NO_UPFRONT'
    offering_type: typing.Union[str, "OfferingType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # AWS region, e.g. 'us-west-2'
    region: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique reservation ID, e.g. '1234567'
    reservation_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Resource configuration details
    resource_specification: "ReservationResourceSpecification" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Reservation UTC start date and time in ISO-8601 format, e.g.
    # '2018-03-01T00:00:00'
    start: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Current state of reservation, e.g. 'ACTIVE'
    state: typing.Union[str, "ReservationState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Recurring usage charge for each reserved resource, e.g. '157.0'
    usage_price: float = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeScheduleRequest(ShapeBase):
    """
    Request for a describe schedule call.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "channel_id",
                "ChannelId",
                TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # Id of the channel whose schedule is being updated.
    channel_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Placeholder documentation for MaxResults
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Placeholder documentation for __string
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeScheduleResponse(OutputShapeBase):
    """
    Response for a describe schedule call.
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
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "schedule_actions",
                "ScheduleActions",
                TypeInfo(typing.List[ScheduleAction]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The next token; for use in pagination.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of schedule actions.
    schedule_actions: typing.List["ScheduleAction"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(self,
                ) -> typing.Generator["DescribeScheduleResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class DvbNitSettings(ShapeBase):
    """
    DVB Network Information Table (NIT)
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "network_id",
                "NetworkId",
                TypeInfo(int),
            ),
            (
                "network_name",
                "NetworkName",
                TypeInfo(str),
            ),
            (
                "rep_interval",
                "RepInterval",
                TypeInfo(int),
            ),
        ]

    # The numeric value placed in the Network Information Table (NIT).
    network_id: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The network name text placed in the networkNameDescriptor inside the
    # Network Information Table. Maximum length is 256 characters.
    network_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of milliseconds between instances of this table in the output
    # transport stream.
    rep_interval: int = dataclasses.field(default=ShapeBase.NOT_SET, )


class DvbSdtOutputSdt(str):
    """
    Placeholder documentation for DvbSdtOutputSdt
    """
    SDT_FOLLOW = "SDT_FOLLOW"
    SDT_FOLLOW_IF_PRESENT = "SDT_FOLLOW_IF_PRESENT"
    SDT_MANUAL = "SDT_MANUAL"
    SDT_NONE = "SDT_NONE"


@dataclasses.dataclass
class DvbSdtSettings(ShapeBase):
    """
    DVB Service Description Table (SDT)
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "output_sdt",
                "OutputSdt",
                TypeInfo(typing.Union[str, DvbSdtOutputSdt]),
            ),
            (
                "rep_interval",
                "RepInterval",
                TypeInfo(int),
            ),
            (
                "service_name",
                "ServiceName",
                TypeInfo(str),
            ),
            (
                "service_provider_name",
                "ServiceProviderName",
                TypeInfo(str),
            ),
        ]

    # Selects method of inserting SDT information into output stream. The
    # sdtFollow setting copies SDT information from input stream to output
    # stream. The sdtFollowIfPresent setting copies SDT information from input
    # stream to output stream if SDT information is present in the input,
    # otherwise it will fall back on the user-defined values. The sdtManual
    # setting means user will enter the SDT information. The sdtNone setting
    # means output stream will not contain SDT information.
    output_sdt: typing.Union[str, "DvbSdtOutputSdt"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of milliseconds between instances of this table in the output
    # transport stream.
    rep_interval: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The service name placed in the serviceDescriptor in the Service Description
    # Table. Maximum length is 256 characters.
    service_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The service provider name placed in the serviceDescriptor in the Service
    # Description Table. Maximum length is 256 characters.
    service_provider_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class DvbSubDestinationAlignment(str):
    """
    Placeholder documentation for DvbSubDestinationAlignment
    """
    CENTERED = "CENTERED"
    LEFT = "LEFT"
    SMART = "SMART"


class DvbSubDestinationBackgroundColor(str):
    """
    Placeholder documentation for DvbSubDestinationBackgroundColor
    """
    BLACK = "BLACK"
    NONE = "NONE"
    WHITE = "WHITE"


class DvbSubDestinationFontColor(str):
    """
    Placeholder documentation for DvbSubDestinationFontColor
    """
    BLACK = "BLACK"
    BLUE = "BLUE"
    GREEN = "GREEN"
    RED = "RED"
    WHITE = "WHITE"
    YELLOW = "YELLOW"


class DvbSubDestinationOutlineColor(str):
    """
    Placeholder documentation for DvbSubDestinationOutlineColor
    """
    BLACK = "BLACK"
    BLUE = "BLUE"
    GREEN = "GREEN"
    RED = "RED"
    WHITE = "WHITE"
    YELLOW = "YELLOW"


@dataclasses.dataclass
class DvbSubDestinationSettings(ShapeBase):
    """
    Placeholder documentation for DvbSubDestinationSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "alignment",
                "Alignment",
                TypeInfo(typing.Union[str, DvbSubDestinationAlignment]),
            ),
            (
                "background_color",
                "BackgroundColor",
                TypeInfo(typing.Union[str, DvbSubDestinationBackgroundColor]),
            ),
            (
                "background_opacity",
                "BackgroundOpacity",
                TypeInfo(int),
            ),
            (
                "font",
                "Font",
                TypeInfo(InputLocation),
            ),
            (
                "font_color",
                "FontColor",
                TypeInfo(typing.Union[str, DvbSubDestinationFontColor]),
            ),
            (
                "font_opacity",
                "FontOpacity",
                TypeInfo(int),
            ),
            (
                "font_resolution",
                "FontResolution",
                TypeInfo(int),
            ),
            (
                "font_size",
                "FontSize",
                TypeInfo(str),
            ),
            (
                "outline_color",
                "OutlineColor",
                TypeInfo(typing.Union[str, DvbSubDestinationOutlineColor]),
            ),
            (
                "outline_size",
                "OutlineSize",
                TypeInfo(int),
            ),
            (
                "shadow_color",
                "ShadowColor",
                TypeInfo(typing.Union[str, DvbSubDestinationShadowColor]),
            ),
            (
                "shadow_opacity",
                "ShadowOpacity",
                TypeInfo(int),
            ),
            (
                "shadow_x_offset",
                "ShadowXOffset",
                TypeInfo(int),
            ),
            (
                "shadow_y_offset",
                "ShadowYOffset",
                TypeInfo(int),
            ),
            (
                "teletext_grid_control",
                "TeletextGridControl",
                TypeInfo(
                    typing.Union[str, DvbSubDestinationTeletextGridControl]
                ),
            ),
            (
                "x_position",
                "XPosition",
                TypeInfo(int),
            ),
            (
                "y_position",
                "YPosition",
                TypeInfo(int),
            ),
        ]

    # If no explicit xPosition or yPosition is provided, setting alignment to
    # centered will place the captions at the bottom center of the output.
    # Similarly, setting a left alignment will align captions to the bottom left
    # of the output. If x and y positions are given in conjunction with the
    # alignment parameter, the font will be justified (either left or centered)
    # relative to those coordinates. Selecting "smart" justification will left-
    # justify live subtitles and center-justify pre-recorded subtitles. This
    # option is not valid for source captions that are STL or 608/embedded. These
    # source settings are already pre-defined by the caption stream. All burn-in
    # and DVB-Sub font settings must match.
    alignment: typing.Union[str, "DvbSubDestinationAlignment"
                           ] = dataclasses.field(
                               default=ShapeBase.NOT_SET,
                           )

    # Specifies the color of the rectangle behind the captions. All burn-in and
    # DVB-Sub font settings must match.
    background_color: typing.Union[str, "DvbSubDestinationBackgroundColor"
                                  ] = dataclasses.field(
                                      default=ShapeBase.NOT_SET,
                                  )

    # Specifies the opacity of the background rectangle. 255 is opaque; 0 is
    # transparent. Leaving this parameter blank is equivalent to setting it to 0
    # (transparent). All burn-in and DVB-Sub font settings must match.
    background_opacity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # External font file used for caption burn-in. File extension must be 'ttf'
    # or 'tte'. Although the user can select output fonts for many different
    # types of input captions, embedded, STL and teletext sources use a strict
    # grid system. Using external fonts with these caption sources could cause
    # unexpected display of proportional fonts. All burn-in and DVB-Sub font
    # settings must match.
    font: "InputLocation" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the color of the burned-in captions. This option is not valid for
    # source captions that are STL, 608/embedded or teletext. These source
    # settings are already pre-defined by the caption stream. All burn-in and
    # DVB-Sub font settings must match.
    font_color: typing.Union[str, "DvbSubDestinationFontColor"
                            ] = dataclasses.field(
                                default=ShapeBase.NOT_SET,
                            )

    # Specifies the opacity of the burned-in captions. 255 is opaque; 0 is
    # transparent. All burn-in and DVB-Sub font settings must match.
    font_opacity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Font resolution in DPI (dots per inch); default is 96 dpi. All burn-in and
    # DVB-Sub font settings must match.
    font_resolution: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When set to auto fontSize will scale depending on the size of the output.
    # Giving a positive integer will specify the exact font size in points. All
    # burn-in and DVB-Sub font settings must match.
    font_size: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies font outline color. This option is not valid for source captions
    # that are either 608/embedded or teletext. These source settings are already
    # pre-defined by the caption stream. All burn-in and DVB-Sub font settings
    # must match.
    outline_color: typing.Union[str, "DvbSubDestinationOutlineColor"
                               ] = dataclasses.field(
                                   default=ShapeBase.NOT_SET,
                               )

    # Specifies font outline size in pixels. This option is not valid for source
    # captions that are either 608/embedded or teletext. These source settings
    # are already pre-defined by the caption stream. All burn-in and DVB-Sub font
    # settings must match.
    outline_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the color of the shadow cast by the captions. All burn-in and
    # DVB-Sub font settings must match.
    shadow_color: typing.Union[str, "DvbSubDestinationShadowColor"
                              ] = dataclasses.field(
                                  default=ShapeBase.NOT_SET,
                              )

    # Specifies the opacity of the shadow. 255 is opaque; 0 is transparent.
    # Leaving this parameter blank is equivalent to setting it to 0
    # (transparent). All burn-in and DVB-Sub font settings must match.
    shadow_opacity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the horizontal offset of the shadow relative to the captions in
    # pixels. A value of -2 would result in a shadow offset 2 pixels to the left.
    # All burn-in and DVB-Sub font settings must match.
    shadow_x_offset: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the vertical offset of the shadow relative to the captions in
    # pixels. A value of -2 would result in a shadow offset 2 pixels above the
    # text. All burn-in and DVB-Sub font settings must match.
    shadow_y_offset: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Controls whether a fixed grid size will be used to generate the output
    # subtitles bitmap. Only applicable for Teletext inputs and DVB-Sub/Burn-in
    # outputs.
    teletext_grid_control: typing.Union[
        str, "DvbSubDestinationTeletextGridControl"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # Specifies the horizontal position of the caption relative to the left side
    # of the output in pixels. A value of 10 would result in the captions
    # starting 10 pixels from the left of the output. If no explicit xPosition is
    # provided, the horizontal caption position will be determined by the
    # alignment parameter. This option is not valid for source captions that are
    # STL, 608/embedded or teletext. These source settings are already pre-
    # defined by the caption stream. All burn-in and DVB-Sub font settings must
    # match.
    x_position: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the vertical position of the caption relative to the top of the
    # output in pixels. A value of 10 would result in the captions starting 10
    # pixels from the top of the output. If no explicit yPosition is provided,
    # the caption will be positioned towards the bottom of the output. This
    # option is not valid for source captions that are STL, 608/embedded or
    # teletext. These source settings are already pre-defined by the caption
    # stream. All burn-in and DVB-Sub font settings must match.
    y_position: int = dataclasses.field(default=ShapeBase.NOT_SET, )


class DvbSubDestinationShadowColor(str):
    """
    Placeholder documentation for DvbSubDestinationShadowColor
    """
    BLACK = "BLACK"
    NONE = "NONE"
    WHITE = "WHITE"


class DvbSubDestinationTeletextGridControl(str):
    """
    Placeholder documentation for DvbSubDestinationTeletextGridControl
    """
    FIXED = "FIXED"
    SCALED = "SCALED"


@dataclasses.dataclass
class DvbSubSourceSettings(ShapeBase):
    """
    Placeholder documentation for DvbSubSourceSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pid",
                "Pid",
                TypeInfo(int),
            ),
        ]

    # When using DVB-Sub with Burn-In or SMPTE-TT, use this PID for the source
    # content. Unused for DVB-Sub passthrough. All DVB-Sub content is passed
    # through, regardless of selectors.
    pid: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DvbTdtSettings(ShapeBase):
    """
    DVB Time and Date Table (SDT)
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "rep_interval",
                "RepInterval",
                TypeInfo(int),
            ),
        ]

    # The number of milliseconds between instances of this table in the output
    # transport stream.
    rep_interval: int = dataclasses.field(default=ShapeBase.NOT_SET, )


class Eac3AttenuationControl(str):
    """
    Placeholder documentation for Eac3AttenuationControl
    """
    ATTENUATE_3_DB = "ATTENUATE_3_DB"
    NONE = "NONE"


class Eac3BitstreamMode(str):
    """
    Placeholder documentation for Eac3BitstreamMode
    """
    COMMENTARY = "COMMENTARY"
    COMPLETE_MAIN = "COMPLETE_MAIN"
    EMERGENCY = "EMERGENCY"
    HEARING_IMPAIRED = "HEARING_IMPAIRED"
    VISUALLY_IMPAIRED = "VISUALLY_IMPAIRED"


class Eac3CodingMode(str):
    """
    Placeholder documentation for Eac3CodingMode
    """
    CODING_MODE_1_0 = "CODING_MODE_1_0"
    CODING_MODE_2_0 = "CODING_MODE_2_0"
    CODING_MODE_3_2 = "CODING_MODE_3_2"


class Eac3DcFilter(str):
    """
    Placeholder documentation for Eac3DcFilter
    """
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class Eac3DrcLine(str):
    """
    Placeholder documentation for Eac3DrcLine
    """
    FILM_LIGHT = "FILM_LIGHT"
    FILM_STANDARD = "FILM_STANDARD"
    MUSIC_LIGHT = "MUSIC_LIGHT"
    MUSIC_STANDARD = "MUSIC_STANDARD"
    NONE = "NONE"
    SPEECH = "SPEECH"


class Eac3DrcRf(str):
    """
    Placeholder documentation for Eac3DrcRf
    """
    FILM_LIGHT = "FILM_LIGHT"
    FILM_STANDARD = "FILM_STANDARD"
    MUSIC_LIGHT = "MUSIC_LIGHT"
    MUSIC_STANDARD = "MUSIC_STANDARD"
    NONE = "NONE"
    SPEECH = "SPEECH"


class Eac3LfeControl(str):
    """
    Placeholder documentation for Eac3LfeControl
    """
    LFE = "LFE"
    NO_LFE = "NO_LFE"


class Eac3LfeFilter(str):
    """
    Placeholder documentation for Eac3LfeFilter
    """
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class Eac3MetadataControl(str):
    """
    Placeholder documentation for Eac3MetadataControl
    """
    FOLLOW_INPUT = "FOLLOW_INPUT"
    USE_CONFIGURED = "USE_CONFIGURED"


class Eac3PassthroughControl(str):
    """
    Placeholder documentation for Eac3PassthroughControl
    """
    NO_PASSTHROUGH = "NO_PASSTHROUGH"
    WHEN_POSSIBLE = "WHEN_POSSIBLE"


class Eac3PhaseControl(str):
    """
    Placeholder documentation for Eac3PhaseControl
    """
    NO_SHIFT = "NO_SHIFT"
    SHIFT_90_DEGREES = "SHIFT_90_DEGREES"


@dataclasses.dataclass
class Eac3Settings(ShapeBase):
    """
    Placeholder documentation for Eac3Settings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attenuation_control",
                "AttenuationControl",
                TypeInfo(typing.Union[str, Eac3AttenuationControl]),
            ),
            (
                "bitrate",
                "Bitrate",
                TypeInfo(float),
            ),
            (
                "bitstream_mode",
                "BitstreamMode",
                TypeInfo(typing.Union[str, Eac3BitstreamMode]),
            ),
            (
                "coding_mode",
                "CodingMode",
                TypeInfo(typing.Union[str, Eac3CodingMode]),
            ),
            (
                "dc_filter",
                "DcFilter",
                TypeInfo(typing.Union[str, Eac3DcFilter]),
            ),
            (
                "dialnorm",
                "Dialnorm",
                TypeInfo(int),
            ),
            (
                "drc_line",
                "DrcLine",
                TypeInfo(typing.Union[str, Eac3DrcLine]),
            ),
            (
                "drc_rf",
                "DrcRf",
                TypeInfo(typing.Union[str, Eac3DrcRf]),
            ),
            (
                "lfe_control",
                "LfeControl",
                TypeInfo(typing.Union[str, Eac3LfeControl]),
            ),
            (
                "lfe_filter",
                "LfeFilter",
                TypeInfo(typing.Union[str, Eac3LfeFilter]),
            ),
            (
                "lo_ro_center_mix_level",
                "LoRoCenterMixLevel",
                TypeInfo(float),
            ),
            (
                "lo_ro_surround_mix_level",
                "LoRoSurroundMixLevel",
                TypeInfo(float),
            ),
            (
                "lt_rt_center_mix_level",
                "LtRtCenterMixLevel",
                TypeInfo(float),
            ),
            (
                "lt_rt_surround_mix_level",
                "LtRtSurroundMixLevel",
                TypeInfo(float),
            ),
            (
                "metadata_control",
                "MetadataControl",
                TypeInfo(typing.Union[str, Eac3MetadataControl]),
            ),
            (
                "passthrough_control",
                "PassthroughControl",
                TypeInfo(typing.Union[str, Eac3PassthroughControl]),
            ),
            (
                "phase_control",
                "PhaseControl",
                TypeInfo(typing.Union[str, Eac3PhaseControl]),
            ),
            (
                "stereo_downmix",
                "StereoDownmix",
                TypeInfo(typing.Union[str, Eac3StereoDownmix]),
            ),
            (
                "surround_ex_mode",
                "SurroundExMode",
                TypeInfo(typing.Union[str, Eac3SurroundExMode]),
            ),
            (
                "surround_mode",
                "SurroundMode",
                TypeInfo(typing.Union[str, Eac3SurroundMode]),
            ),
        ]

    # When set to attenuate3Db, applies a 3 dB attenuation to the surround
    # channels. Only used for 3/2 coding mode.
    attenuation_control: typing.Union[str, "Eac3AttenuationControl"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # Average bitrate in bits/second. Valid bitrates depend on the coding mode.
    bitrate: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the bitstream mode (bsmod) for the emitted E-AC-3 stream. See
    # ATSC A/52-2012 (Annex E) for background on these values.
    bitstream_mode: typing.Union[str, "Eac3BitstreamMode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Dolby Digital Plus coding mode. Determines number of channels.
    coding_mode: typing.Union[str, "Eac3CodingMode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When set to enabled, activates a DC highpass filter for all input channels.
    dc_filter: typing.Union[str, "Eac3DcFilter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Sets the dialnorm for the output. If blank and input audio is Dolby Digital
    # Plus, dialnorm will be passed through.
    dialnorm: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Sets the Dolby dynamic range compression profile.
    drc_line: typing.Union[str, "Eac3DrcLine"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Sets the profile for heavy Dolby dynamic range compression, ensures that
    # the instantaneous signal peaks do not exceed specified levels.
    drc_rf: typing.Union[str, "Eac3DrcRf"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When encoding 3/2 audio, setting to lfe enables the LFE channel
    lfe_control: typing.Union[str, "Eac3LfeControl"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When set to enabled, applies a 120Hz lowpass filter to the LFE channel
    # prior to encoding. Only valid with codingMode32 coding mode.
    lfe_filter: typing.Union[str, "Eac3LfeFilter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Left only/Right only center mix level. Only used for 3/2 coding mode.
    lo_ro_center_mix_level: float = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Left only/Right only surround mix level. Only used for 3/2 coding mode.
    lo_ro_surround_mix_level: float = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Left total/Right total center mix level. Only used for 3/2 coding mode.
    lt_rt_center_mix_level: float = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Left total/Right total surround mix level. Only used for 3/2 coding mode.
    lt_rt_surround_mix_level: float = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When set to followInput, encoder metadata will be sourced from the DD, DD+,
    # or DolbyE decoder that supplied this audio data. If audio was not supplied
    # from one of these streams, then the static metadata settings will be used.
    metadata_control: typing.Union[str, "Eac3MetadataControl"
                                  ] = dataclasses.field(
                                      default=ShapeBase.NOT_SET,
                                  )

    # When set to whenPossible, input DD+ audio will be passed through if it is
    # present on the input. This detection is dynamic over the life of the
    # transcode. Inputs that alternate between DD+ and non-DD+ content will have
    # a consistent DD+ output as the system alternates between passthrough and
    # encoding.
    passthrough_control: typing.Union[str, "Eac3PassthroughControl"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # When set to shift90Degrees, applies a 90-degree phase shift to the surround
    # channels. Only used for 3/2 coding mode.
    phase_control: typing.Union[str, "Eac3PhaseControl"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Stereo downmix preference. Only used for 3/2 coding mode.
    stereo_downmix: typing.Union[str, "Eac3StereoDownmix"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When encoding 3/2 audio, sets whether an extra center back surround channel
    # is matrix encoded into the left and right surround channels.
    surround_ex_mode: typing.Union[str, "Eac3SurroundExMode"
                                  ] = dataclasses.field(
                                      default=ShapeBase.NOT_SET,
                                  )

    # When encoding 2/0 audio, sets whether Dolby Surround is matrix encoded into
    # the two channels.
    surround_mode: typing.Union[str, "Eac3SurroundMode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class Eac3StereoDownmix(str):
    """
    Placeholder documentation for Eac3StereoDownmix
    """
    DPL2 = "DPL2"
    LO_RO = "LO_RO"
    LT_RT = "LT_RT"
    NOT_INDICATED = "NOT_INDICATED"


class Eac3SurroundExMode(str):
    """
    Placeholder documentation for Eac3SurroundExMode
    """
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"
    NOT_INDICATED = "NOT_INDICATED"


class Eac3SurroundMode(str):
    """
    Placeholder documentation for Eac3SurroundMode
    """
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"
    NOT_INDICATED = "NOT_INDICATED"


class EmbeddedConvert608To708(str):
    """
    Placeholder documentation for EmbeddedConvert608To708
    """
    DISABLED = "DISABLED"
    UPCONVERT = "UPCONVERT"


@dataclasses.dataclass
class EmbeddedDestinationSettings(ShapeBase):
    """
    Placeholder documentation for EmbeddedDestinationSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class EmbeddedPlusScte20DestinationSettings(ShapeBase):
    """
    Placeholder documentation for EmbeddedPlusScte20DestinationSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class EmbeddedScte20Detection(str):
    """
    Placeholder documentation for EmbeddedScte20Detection
    """
    AUTO = "AUTO"
    OFF = "OFF"


@dataclasses.dataclass
class EmbeddedSourceSettings(ShapeBase):
    """
    Placeholder documentation for EmbeddedSourceSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "convert608_to708",
                "Convert608To708",
                TypeInfo(typing.Union[str, EmbeddedConvert608To708]),
            ),
            (
                "scte20_detection",
                "Scte20Detection",
                TypeInfo(typing.Union[str, EmbeddedScte20Detection]),
            ),
            (
                "source608_channel_number",
                "Source608ChannelNumber",
                TypeInfo(int),
            ),
            (
                "source608_track_number",
                "Source608TrackNumber",
                TypeInfo(int),
            ),
        ]

    # If upconvert, 608 data is both passed through via the "608 compatibility
    # bytes" fields of the 708 wrapper as well as translated into 708. 708 data
    # present in the source content will be discarded.
    convert608_to708: typing.Union[str, "EmbeddedConvert608To708"
                                  ] = dataclasses.field(
                                      default=ShapeBase.NOT_SET,
                                  )

    # Set to "auto" to handle streams with intermittent and/or non-aligned
    # SCTE-20 and Embedded captions.
    scte20_detection: typing.Union[str, "EmbeddedScte20Detection"
                                  ] = dataclasses.field(
                                      default=ShapeBase.NOT_SET,
                                  )

    # Specifies the 608/708 channel number within the video track from which to
    # extract captions. Unused for passthrough.
    source608_channel_number: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # This field is unused and deprecated.
    source608_track_number: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Empty(ShapeBase):
    """
    Placeholder documentation for Empty
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class EncoderSettings(ShapeBase):
    """
    Placeholder documentation for EncoderSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "audio_descriptions",
                "AudioDescriptions",
                TypeInfo(typing.List[AudioDescription]),
            ),
            (
                "output_groups",
                "OutputGroups",
                TypeInfo(typing.List[OutputGroup]),
            ),
            (
                "timecode_config",
                "TimecodeConfig",
                TypeInfo(TimecodeConfig),
            ),
            (
                "video_descriptions",
                "VideoDescriptions",
                TypeInfo(typing.List[VideoDescription]),
            ),
            (
                "avail_blanking",
                "AvailBlanking",
                TypeInfo(AvailBlanking),
            ),
            (
                "avail_configuration",
                "AvailConfiguration",
                TypeInfo(AvailConfiguration),
            ),
            (
                "blackout_slate",
                "BlackoutSlate",
                TypeInfo(BlackoutSlate),
            ),
            (
                "caption_descriptions",
                "CaptionDescriptions",
                TypeInfo(typing.List[CaptionDescription]),
            ),
            (
                "global_configuration",
                "GlobalConfiguration",
                TypeInfo(GlobalConfiguration),
            ),
        ]

    # Placeholder documentation for __listOfAudioDescription
    audio_descriptions: typing.List["AudioDescription"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Placeholder documentation for __listOfOutputGroup
    output_groups: typing.List["OutputGroup"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains settings used to acquire and adjust timecode information from
    # inputs.
    timecode_config: "TimecodeConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Placeholder documentation for __listOfVideoDescription
    video_descriptions: typing.List["VideoDescription"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Settings for ad avail blanking.
    avail_blanking: "AvailBlanking" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Event-wide configuration settings for ad avail insertion.
    avail_configuration: "AvailConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Settings for blackout slate.
    blackout_slate: "BlackoutSlate" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Settings for caption decriptions
    caption_descriptions: typing.List["CaptionDescription"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Configuration settings that apply to the event as a whole.
    global_configuration: "GlobalConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class FecOutputIncludeFec(str):
    """
    Placeholder documentation for FecOutputIncludeFec
    """
    COLUMN = "COLUMN"
    COLUMN_AND_ROW = "COLUMN_AND_ROW"


@dataclasses.dataclass
class FecOutputSettings(ShapeBase):
    """
    Placeholder documentation for FecOutputSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "column_depth",
                "ColumnDepth",
                TypeInfo(int),
            ),
            (
                "include_fec",
                "IncludeFec",
                TypeInfo(typing.Union[str, FecOutputIncludeFec]),
            ),
            (
                "row_length",
                "RowLength",
                TypeInfo(int),
            ),
        ]

    # Parameter D from SMPTE 2022-1. The height of the FEC protection matrix. The
    # number of transport stream packets per column error correction packet. Must
    # be between 4 and 20, inclusive.
    column_depth: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Enables column only or column and row based FEC
    include_fec: typing.Union[str, "FecOutputIncludeFec"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Parameter L from SMPTE 2022-1. The width of the FEC protection matrix. Must
    # be between 1 and 20, inclusive. If only Column FEC is used, then larger
    # values increase robustness. If Row FEC is used, then this is the number of
    # transport stream packets per row error correction packet, and the value
    # must be between 4 and 20, inclusive, if includeFec is columnAndRow. If
    # includeFec is column, this value must be 1 to 20, inclusive.
    row_length: int = dataclasses.field(default=ShapeBase.NOT_SET, )


class FixedAfd(str):
    """
    Placeholder documentation for FixedAfd
    """
    AFD_0000 = "AFD_0000"
    AFD_0010 = "AFD_0010"
    AFD_0011 = "AFD_0011"
    AFD_0100 = "AFD_0100"
    AFD_1000 = "AFD_1000"
    AFD_1001 = "AFD_1001"
    AFD_1010 = "AFD_1010"
    AFD_1011 = "AFD_1011"
    AFD_1101 = "AFD_1101"
    AFD_1110 = "AFD_1110"
    AFD_1111 = "AFD_1111"


@dataclasses.dataclass
class FixedModeScheduleActionStartSettings(ShapeBase):
    """
    Fixed mode schedule action start settings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "time",
                "Time",
                TypeInfo(str),
            ),
        ]

    # Fixed timestamp action start. Conforms to ISO-8601.
    time: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ForbiddenException(ShapeBase):
    """
    Placeholder documentation for ForbiddenException
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    # Placeholder documentation for __string
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GatewayTimeoutException(ShapeBase):
    """
    Placeholder documentation for GatewayTimeoutException
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    # Placeholder documentation for __string
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GlobalConfiguration(ShapeBase):
    """
    Placeholder documentation for GlobalConfiguration
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "initial_audio_gain",
                "InitialAudioGain",
                TypeInfo(int),
            ),
            (
                "input_end_action",
                "InputEndAction",
                TypeInfo(typing.Union[str, GlobalConfigurationInputEndAction]),
            ),
            (
                "input_loss_behavior",
                "InputLossBehavior",
                TypeInfo(InputLossBehavior),
            ),
            (
                "output_timing_source",
                "OutputTimingSource",
                TypeInfo(
                    typing.Union[str, GlobalConfigurationOutputTimingSource]
                ),
            ),
            (
                "support_low_framerate_inputs",
                "SupportLowFramerateInputs",
                TypeInfo(
                    typing.Union[str, GlobalConfigurationLowFramerateInputs]
                ),
            ),
        ]

    # Value to set the initial audio gain for the Live Event.
    initial_audio_gain: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates the action to take when an input completes (e.g. end-of-file.)
    # Options include immediately switching to the next sequential input (via
    # "switchInput"), switching to the next input and looping back to the first
    # input when last input ends (via "switchAndLoopInputs") or not switching
    # inputs and instead transcoding black / color / slate images per the "Input
    # Loss Behavior" configuration until an activateInput REST command is
    # received (via "none").
    input_end_action: typing.Union[str, "GlobalConfigurationInputEndAction"
                                  ] = dataclasses.field(
                                      default=ShapeBase.NOT_SET,
                                  )

    # Settings for system actions when input is lost.
    input_loss_behavior: "InputLossBehavior" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates whether the rate of frames emitted by the Live encoder should be
    # paced by its system clock (which optionally may be locked to another source
    # via NTP) or should be locked to the clock of the source that is providing
    # the input stream.
    output_timing_source: typing.Union[
        str, "GlobalConfigurationOutputTimingSource"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # Adjusts video input buffer for streams with very low video framerates. This
    # is commonly set to enabled for music channels with less than one video
    # frame per second.
    support_low_framerate_inputs: typing.Union[
        str, "GlobalConfigurationLowFramerateInputs"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )


class GlobalConfigurationInputEndAction(str):
    """
    Placeholder documentation for GlobalConfigurationInputEndAction
    """
    NONE = "NONE"
    SWITCH_AND_LOOP_INPUTS = "SWITCH_AND_LOOP_INPUTS"


class GlobalConfigurationLowFramerateInputs(str):
    """
    Placeholder documentation for GlobalConfigurationLowFramerateInputs
    """
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class GlobalConfigurationOutputTimingSource(str):
    """
    Placeholder documentation for GlobalConfigurationOutputTimingSource
    """
    INPUT_CLOCK = "INPUT_CLOCK"
    SYSTEM_CLOCK = "SYSTEM_CLOCK"


class H264AdaptiveQuantization(str):
    """
    Placeholder documentation for H264AdaptiveQuantization
    """
    HIGH = "HIGH"
    HIGHER = "HIGHER"
    LOW = "LOW"
    MAX = "MAX"
    MEDIUM = "MEDIUM"
    OFF = "OFF"


class H264ColorMetadata(str):
    """
    Placeholder documentation for H264ColorMetadata
    """
    IGNORE = "IGNORE"
    INSERT = "INSERT"


class H264EntropyEncoding(str):
    """
    Placeholder documentation for H264EntropyEncoding
    """
    CABAC = "CABAC"
    CAVLC = "CAVLC"


class H264FlickerAq(str):
    """
    Placeholder documentation for H264FlickerAq
    """
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H264FramerateControl(str):
    """
    Placeholder documentation for H264FramerateControl
    """
    INITIALIZE_FROM_SOURCE = "INITIALIZE_FROM_SOURCE"
    SPECIFIED = "SPECIFIED"


class H264GopBReference(str):
    """
    Placeholder documentation for H264GopBReference
    """
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H264GopSizeUnits(str):
    """
    Placeholder documentation for H264GopSizeUnits
    """
    FRAMES = "FRAMES"
    SECONDS = "SECONDS"


class H264Level(str):
    """
    Placeholder documentation for H264Level
    """
    H264_LEVEL_1 = "H264_LEVEL_1"
    H264_LEVEL_1_1 = "H264_LEVEL_1_1"
    H264_LEVEL_1_2 = "H264_LEVEL_1_2"
    H264_LEVEL_1_3 = "H264_LEVEL_1_3"
    H264_LEVEL_2 = "H264_LEVEL_2"
    H264_LEVEL_2_1 = "H264_LEVEL_2_1"
    H264_LEVEL_2_2 = "H264_LEVEL_2_2"
    H264_LEVEL_3 = "H264_LEVEL_3"
    H264_LEVEL_3_1 = "H264_LEVEL_3_1"
    H264_LEVEL_3_2 = "H264_LEVEL_3_2"
    H264_LEVEL_4 = "H264_LEVEL_4"
    H264_LEVEL_4_1 = "H264_LEVEL_4_1"
    H264_LEVEL_4_2 = "H264_LEVEL_4_2"
    H264_LEVEL_5 = "H264_LEVEL_5"
    H264_LEVEL_5_1 = "H264_LEVEL_5_1"
    H264_LEVEL_5_2 = "H264_LEVEL_5_2"
    H264_LEVEL_AUTO = "H264_LEVEL_AUTO"


class H264LookAheadRateControl(str):
    """
    Placeholder documentation for H264LookAheadRateControl
    """
    HIGH = "HIGH"
    LOW = "LOW"
    MEDIUM = "MEDIUM"


class H264ParControl(str):
    """
    Placeholder documentation for H264ParControl
    """
    INITIALIZE_FROM_SOURCE = "INITIALIZE_FROM_SOURCE"
    SPECIFIED = "SPECIFIED"


class H264Profile(str):
    """
    Placeholder documentation for H264Profile
    """
    BASELINE = "BASELINE"
    HIGH = "HIGH"
    HIGH_10BIT = "HIGH_10BIT"
    HIGH_422 = "HIGH_422"
    HIGH_422_10BIT = "HIGH_422_10BIT"
    MAIN = "MAIN"


class H264RateControlMode(str):
    """
    Placeholder documentation for H264RateControlMode
    """
    CBR = "CBR"
    VBR = "VBR"


class H264ScanType(str):
    """
    Placeholder documentation for H264ScanType
    """
    INTERLACED = "INTERLACED"
    PROGRESSIVE = "PROGRESSIVE"


class H264SceneChangeDetect(str):
    """
    Placeholder documentation for H264SceneChangeDetect
    """
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


@dataclasses.dataclass
class H264Settings(ShapeBase):
    """
    Placeholder documentation for H264Settings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "adaptive_quantization",
                "AdaptiveQuantization",
                TypeInfo(typing.Union[str, H264AdaptiveQuantization]),
            ),
            (
                "afd_signaling",
                "AfdSignaling",
                TypeInfo(typing.Union[str, AfdSignaling]),
            ),
            (
                "bitrate",
                "Bitrate",
                TypeInfo(int),
            ),
            (
                "buf_fill_pct",
                "BufFillPct",
                TypeInfo(int),
            ),
            (
                "buf_size",
                "BufSize",
                TypeInfo(int),
            ),
            (
                "color_metadata",
                "ColorMetadata",
                TypeInfo(typing.Union[str, H264ColorMetadata]),
            ),
            (
                "entropy_encoding",
                "EntropyEncoding",
                TypeInfo(typing.Union[str, H264EntropyEncoding]),
            ),
            (
                "fixed_afd",
                "FixedAfd",
                TypeInfo(typing.Union[str, FixedAfd]),
            ),
            (
                "flicker_aq",
                "FlickerAq",
                TypeInfo(typing.Union[str, H264FlickerAq]),
            ),
            (
                "framerate_control",
                "FramerateControl",
                TypeInfo(typing.Union[str, H264FramerateControl]),
            ),
            (
                "framerate_denominator",
                "FramerateDenominator",
                TypeInfo(int),
            ),
            (
                "framerate_numerator",
                "FramerateNumerator",
                TypeInfo(int),
            ),
            (
                "gop_b_reference",
                "GopBReference",
                TypeInfo(typing.Union[str, H264GopBReference]),
            ),
            (
                "gop_closed_cadence",
                "GopClosedCadence",
                TypeInfo(int),
            ),
            (
                "gop_num_b_frames",
                "GopNumBFrames",
                TypeInfo(int),
            ),
            (
                "gop_size",
                "GopSize",
                TypeInfo(float),
            ),
            (
                "gop_size_units",
                "GopSizeUnits",
                TypeInfo(typing.Union[str, H264GopSizeUnits]),
            ),
            (
                "level",
                "Level",
                TypeInfo(typing.Union[str, H264Level]),
            ),
            (
                "look_ahead_rate_control",
                "LookAheadRateControl",
                TypeInfo(typing.Union[str, H264LookAheadRateControl]),
            ),
            (
                "max_bitrate",
                "MaxBitrate",
                TypeInfo(int),
            ),
            (
                "min_i_interval",
                "MinIInterval",
                TypeInfo(int),
            ),
            (
                "num_ref_frames",
                "NumRefFrames",
                TypeInfo(int),
            ),
            (
                "par_control",
                "ParControl",
                TypeInfo(typing.Union[str, H264ParControl]),
            ),
            (
                "par_denominator",
                "ParDenominator",
                TypeInfo(int),
            ),
            (
                "par_numerator",
                "ParNumerator",
                TypeInfo(int),
            ),
            (
                "profile",
                "Profile",
                TypeInfo(typing.Union[str, H264Profile]),
            ),
            (
                "rate_control_mode",
                "RateControlMode",
                TypeInfo(typing.Union[str, H264RateControlMode]),
            ),
            (
                "scan_type",
                "ScanType",
                TypeInfo(typing.Union[str, H264ScanType]),
            ),
            (
                "scene_change_detect",
                "SceneChangeDetect",
                TypeInfo(typing.Union[str, H264SceneChangeDetect]),
            ),
            (
                "slices",
                "Slices",
                TypeInfo(int),
            ),
            (
                "softness",
                "Softness",
                TypeInfo(int),
            ),
            (
                "spatial_aq",
                "SpatialAq",
                TypeInfo(typing.Union[str, H264SpatialAq]),
            ),
            (
                "syntax",
                "Syntax",
                TypeInfo(typing.Union[str, H264Syntax]),
            ),
            (
                "temporal_aq",
                "TemporalAq",
                TypeInfo(typing.Union[str, H264TemporalAq]),
            ),
            (
                "timecode_insertion",
                "TimecodeInsertion",
                TypeInfo(typing.Union[str, H264TimecodeInsertionBehavior]),
            ),
        ]

    # Adaptive quantization. Allows intra-frame quantizers to vary to improve
    # visual quality.
    adaptive_quantization: typing.Union[str, "H264AdaptiveQuantization"
                                       ] = dataclasses.field(
                                           default=ShapeBase.NOT_SET,
                                       )

    # Indicates that AFD values will be written into the output stream. If
    # afdSignaling is "auto", the system will try to preserve the input AFD value
    # (in cases where multiple AFD values are valid). If set to "fixed", the AFD
    # value will be the value configured in the fixedAfd parameter.
    afd_signaling: typing.Union[str, "AfdSignaling"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Average bitrate in bits/second. Required for VBR, CBR, and ABR. For MS
    # Smooth outputs, bitrates must be unique when rounded down to the nearest
    # multiple of 1000.
    bitrate: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Percentage of the buffer that should initially be filled (HRD buffer
    # model).
    buf_fill_pct: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Size of buffer (HRD buffer model) in bits/second.
    buf_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Includes colorspace metadata in the output.
    color_metadata: typing.Union[str, "H264ColorMetadata"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Entropy encoding mode. Use cabac (must be in Main or High profile) or
    # cavlc.
    entropy_encoding: typing.Union[str, "H264EntropyEncoding"
                                  ] = dataclasses.field(
                                      default=ShapeBase.NOT_SET,
                                  )

    # Four bit AFD value to write on all frames of video in the output stream.
    # Only valid when afdSignaling is set to 'Fixed'.
    fixed_afd: typing.Union[str, "FixedAfd"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If set to enabled, adjust quantization within each frame to reduce flicker
    # or 'pop' on I-frames.
    flicker_aq: typing.Union[str, "H264FlickerAq"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # This field indicates how the output video frame rate is specified. If
    # "specified" is selected then the output video frame rate is determined by
    # framerateNumerator and framerateDenominator, else if "initializeFromSource"
    # is selected then the output video frame rate will be set equal to the input
    # video frame rate of the first input.
    framerate_control: typing.Union[str, "H264FramerateControl"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # Framerate denominator.
    framerate_denominator: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Framerate numerator - framerate is a fraction, e.g. 24000 / 1001 = 23.976
    # fps.
    framerate_numerator: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Documentation update needed
    gop_b_reference: typing.Union[str, "H264GopBReference"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Frequency of closed GOPs. In streaming applications, it is recommended that
    # this be set to 1 so a decoder joining mid-stream will receive an IDR frame
    # as quickly as possible. Setting this value to 0 will break output
    # segmenting.
    gop_closed_cadence: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Number of B-frames between reference frames.
    gop_num_b_frames: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # GOP size (keyframe interval) in units of either frames or seconds per
    # gopSizeUnits. Must be greater than zero.
    gop_size: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates if the gopSize is specified in frames or seconds. If seconds the
    # system will convert the gopSize into a frame count at run time.
    gop_size_units: typing.Union[str, "H264GopSizeUnits"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # H.264 Level.
    level: typing.Union[str, "H264Level"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Amount of lookahead. A value of low can decrease latency and memory usage,
    # while high can produce better quality for certain content.
    look_ahead_rate_control: typing.Union[str, "H264LookAheadRateControl"
                                         ] = dataclasses.field(
                                             default=ShapeBase.NOT_SET,
                                         )

    # Maximum bitrate in bits/second (for VBR mode only).
    max_bitrate: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Only meaningful if sceneChangeDetect is set to enabled. Enforces separation
    # between repeated (cadence) I-frames and I-frames inserted by Scene Change
    # Detection. If a scene change I-frame is within I-interval frames of a
    # cadence I-frame, the GOP is shrunk and/or stretched to the scene change
    # I-frame. GOP stretch requires enabling lookahead as well as setting
    # I-interval. The normal cadence resumes for the next GOP. Note: Maximum GOP
    # stretch = GOP size + Min-I-interval - 1
    min_i_interval: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Number of reference frames to use. The encoder may use more than requested
    # if using B-frames and/or interlaced encoding.
    num_ref_frames: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This field indicates how the output pixel aspect ratio is specified. If
    # "specified" is selected then the output video pixel aspect ratio is
    # determined by parNumerator and parDenominator, else if
    # "initializeFromSource" is selected then the output pixsel aspect ratio will
    # be set equal to the input video pixel aspect ratio of the first input.
    par_control: typing.Union[str, "H264ParControl"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Pixel Aspect Ratio denominator.
    par_denominator: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Pixel Aspect Ratio numerator.
    par_numerator: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # H.264 Profile.
    profile: typing.Union[str, "H264Profile"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Rate control mode.
    rate_control_mode: typing.Union[str, "H264RateControlMode"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # Sets the scan type of the output to progressive or top-field-first
    # interlaced.
    scan_type: typing.Union[str, "H264ScanType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Scene change detection. Inserts I-frames on scene changes when enabled.
    scene_change_detect: typing.Union[str, "H264SceneChangeDetect"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # Number of slices per picture. Must be less than or equal to the number of
    # macroblock rows for progressive pictures, and less than or equal to half
    # the number of macroblock rows for interlaced pictures. This field is
    # optional; when no value is specified the encoder will choose the number of
    # slices based on encode resolution.
    slices: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Softness. Selects quantizer matrix, larger values reduce high-frequency
    # content in the encoded image.
    softness: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If set to enabled, adjust quantization within each frame based on spatial
    # variation of content complexity.
    spatial_aq: typing.Union[str, "H264SpatialAq"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Produces a bitstream compliant with SMPTE RP-2027.
    syntax: typing.Union[str, "H264Syntax"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If set to enabled, adjust quantization within each frame based on temporal
    # variation of content complexity.
    temporal_aq: typing.Union[str, "H264TemporalAq"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Determines how timecodes should be inserted into the video elementary
    # stream. \- 'disabled': Do not include timecodes \- 'picTimingSei': Pass
    # through picture timing SEI messages from the source specified in Timecode
    # Config
    timecode_insertion: typing.Union[str, "H264TimecodeInsertionBehavior"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )


class H264SpatialAq(str):
    """
    Placeholder documentation for H264SpatialAq
    """
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H264Syntax(str):
    """
    Placeholder documentation for H264Syntax
    """
    DEFAULT = "DEFAULT"
    RP2027 = "RP2027"


class H264TemporalAq(str):
    """
    Placeholder documentation for H264TemporalAq
    """
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H264TimecodeInsertionBehavior(str):
    """
    Placeholder documentation for H264TimecodeInsertionBehavior
    """
    DISABLED = "DISABLED"
    PIC_TIMING_SEI = "PIC_TIMING_SEI"


class HlsAdMarkers(str):
    """
    Placeholder documentation for HlsAdMarkers
    """
    ADOBE = "ADOBE"
    ELEMENTAL = "ELEMENTAL"
    ELEMENTAL_SCTE35 = "ELEMENTAL_SCTE35"


class HlsAkamaiHttpTransferMode(str):
    """
    Placeholder documentation for HlsAkamaiHttpTransferMode
    """
    CHUNKED = "CHUNKED"
    NON_CHUNKED = "NON_CHUNKED"


@dataclasses.dataclass
class HlsAkamaiSettings(ShapeBase):
    """
    Placeholder documentation for HlsAkamaiSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "connection_retry_interval",
                "ConnectionRetryInterval",
                TypeInfo(int),
            ),
            (
                "filecache_duration",
                "FilecacheDuration",
                TypeInfo(int),
            ),
            (
                "http_transfer_mode",
                "HttpTransferMode",
                TypeInfo(typing.Union[str, HlsAkamaiHttpTransferMode]),
            ),
            (
                "num_retries",
                "NumRetries",
                TypeInfo(int),
            ),
            (
                "restart_delay",
                "RestartDelay",
                TypeInfo(int),
            ),
            (
                "salt",
                "Salt",
                TypeInfo(str),
            ),
            (
                "token",
                "Token",
                TypeInfo(str),
            ),
        ]

    # Number of seconds to wait before retrying connection to the CDN if the
    # connection is lost.
    connection_retry_interval: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Size in seconds of file cache for streaming outputs.
    filecache_duration: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specify whether or not to use chunked transfer encoding to Akamai. User
    # should contact Akamai to enable this feature.
    http_transfer_mode: typing.Union[str, "HlsAkamaiHttpTransferMode"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )

    # Number of retry attempts that will be made before the Live Event is put
    # into an error state.
    num_retries: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If a streaming output fails, number of seconds to wait until a restart is
    # initiated. A value of 0 means never restart.
    restart_delay: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Salt for authenticated Akamai.
    salt: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Token parameter for authenticated akamai. If not specified, _gda_ is used.
    token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class HlsBasicPutSettings(ShapeBase):
    """
    Placeholder documentation for HlsBasicPutSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "connection_retry_interval",
                "ConnectionRetryInterval",
                TypeInfo(int),
            ),
            (
                "filecache_duration",
                "FilecacheDuration",
                TypeInfo(int),
            ),
            (
                "num_retries",
                "NumRetries",
                TypeInfo(int),
            ),
            (
                "restart_delay",
                "RestartDelay",
                TypeInfo(int),
            ),
        ]

    # Number of seconds to wait before retrying connection to the CDN if the
    # connection is lost.
    connection_retry_interval: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Size in seconds of file cache for streaming outputs.
    filecache_duration: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Number of retry attempts that will be made before the Live Event is put
    # into an error state.
    num_retries: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If a streaming output fails, number of seconds to wait until a restart is
    # initiated. A value of 0 means never restart.
    restart_delay: int = dataclasses.field(default=ShapeBase.NOT_SET, )


class HlsCaptionLanguageSetting(str):
    """
    Placeholder documentation for HlsCaptionLanguageSetting
    """
    INSERT = "INSERT"
    NONE = "NONE"
    OMIT = "OMIT"


@dataclasses.dataclass
class HlsCdnSettings(ShapeBase):
    """
    Placeholder documentation for HlsCdnSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hls_akamai_settings",
                "HlsAkamaiSettings",
                TypeInfo(HlsAkamaiSettings),
            ),
            (
                "hls_basic_put_settings",
                "HlsBasicPutSettings",
                TypeInfo(HlsBasicPutSettings),
            ),
            (
                "hls_media_store_settings",
                "HlsMediaStoreSettings",
                TypeInfo(HlsMediaStoreSettings),
            ),
            (
                "hls_webdav_settings",
                "HlsWebdavSettings",
                TypeInfo(HlsWebdavSettings),
            ),
        ]

    # Placeholder documentation for HlsAkamaiSettings
    hls_akamai_settings: "HlsAkamaiSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Placeholder documentation for HlsBasicPutSettings
    hls_basic_put_settings: "HlsBasicPutSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Placeholder documentation for HlsMediaStoreSettings
    hls_media_store_settings: "HlsMediaStoreSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Placeholder documentation for HlsWebdavSettings
    hls_webdav_settings: "HlsWebdavSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class HlsClientCache(str):
    """
    Placeholder documentation for HlsClientCache
    """
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class HlsCodecSpecification(str):
    """
    Placeholder documentation for HlsCodecSpecification
    """
    RFC_4281 = "RFC_4281"
    RFC_6381 = "RFC_6381"


class HlsDirectoryStructure(str):
    """
    Placeholder documentation for HlsDirectoryStructure
    """
    SINGLE_DIRECTORY = "SINGLE_DIRECTORY"
    SUBDIRECTORY_PER_STREAM = "SUBDIRECTORY_PER_STREAM"


class HlsEncryptionType(str):
    """
    Placeholder documentation for HlsEncryptionType
    """
    AES128 = "AES128"
    SAMPLE_AES = "SAMPLE_AES"


@dataclasses.dataclass
class HlsGroupSettings(ShapeBase):
    """
    Placeholder documentation for HlsGroupSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "destination",
                "Destination",
                TypeInfo(OutputLocationRef),
            ),
            (
                "ad_markers",
                "AdMarkers",
                TypeInfo(typing.List[typing.Union[str, HlsAdMarkers]]),
            ),
            (
                "base_url_content",
                "BaseUrlContent",
                TypeInfo(str),
            ),
            (
                "base_url_manifest",
                "BaseUrlManifest",
                TypeInfo(str),
            ),
            (
                "caption_language_mappings",
                "CaptionLanguageMappings",
                TypeInfo(typing.List[CaptionLanguageMapping]),
            ),
            (
                "caption_language_setting",
                "CaptionLanguageSetting",
                TypeInfo(typing.Union[str, HlsCaptionLanguageSetting]),
            ),
            (
                "client_cache",
                "ClientCache",
                TypeInfo(typing.Union[str, HlsClientCache]),
            ),
            (
                "codec_specification",
                "CodecSpecification",
                TypeInfo(typing.Union[str, HlsCodecSpecification]),
            ),
            (
                "constant_iv",
                "ConstantIv",
                TypeInfo(str),
            ),
            (
                "directory_structure",
                "DirectoryStructure",
                TypeInfo(typing.Union[str, HlsDirectoryStructure]),
            ),
            (
                "encryption_type",
                "EncryptionType",
                TypeInfo(typing.Union[str, HlsEncryptionType]),
            ),
            (
                "hls_cdn_settings",
                "HlsCdnSettings",
                TypeInfo(HlsCdnSettings),
            ),
            (
                "index_n_segments",
                "IndexNSegments",
                TypeInfo(int),
            ),
            (
                "input_loss_action",
                "InputLossAction",
                TypeInfo(typing.Union[str, InputLossActionForHlsOut]),
            ),
            (
                "iv_in_manifest",
                "IvInManifest",
                TypeInfo(typing.Union[str, HlsIvInManifest]),
            ),
            (
                "iv_source",
                "IvSource",
                TypeInfo(typing.Union[str, HlsIvSource]),
            ),
            (
                "keep_segments",
                "KeepSegments",
                TypeInfo(int),
            ),
            (
                "key_format",
                "KeyFormat",
                TypeInfo(str),
            ),
            (
                "key_format_versions",
                "KeyFormatVersions",
                TypeInfo(str),
            ),
            (
                "key_provider_settings",
                "KeyProviderSettings",
                TypeInfo(KeyProviderSettings),
            ),
            (
                "manifest_compression",
                "ManifestCompression",
                TypeInfo(typing.Union[str, HlsManifestCompression]),
            ),
            (
                "manifest_duration_format",
                "ManifestDurationFormat",
                TypeInfo(typing.Union[str, HlsManifestDurationFormat]),
            ),
            (
                "min_segment_length",
                "MinSegmentLength",
                TypeInfo(int),
            ),
            (
                "mode",
                "Mode",
                TypeInfo(typing.Union[str, HlsMode]),
            ),
            (
                "output_selection",
                "OutputSelection",
                TypeInfo(typing.Union[str, HlsOutputSelection]),
            ),
            (
                "program_date_time",
                "ProgramDateTime",
                TypeInfo(typing.Union[str, HlsProgramDateTime]),
            ),
            (
                "program_date_time_period",
                "ProgramDateTimePeriod",
                TypeInfo(int),
            ),
            (
                "segment_length",
                "SegmentLength",
                TypeInfo(int),
            ),
            (
                "segmentation_mode",
                "SegmentationMode",
                TypeInfo(typing.Union[str, HlsSegmentationMode]),
            ),
            (
                "segments_per_subdirectory",
                "SegmentsPerSubdirectory",
                TypeInfo(int),
            ),
            (
                "stream_inf_resolution",
                "StreamInfResolution",
                TypeInfo(typing.Union[str, HlsStreamInfResolution]),
            ),
            (
                "timed_metadata_id3_frame",
                "TimedMetadataId3Frame",
                TypeInfo(typing.Union[str, HlsTimedMetadataId3Frame]),
            ),
            (
                "timed_metadata_id3_period",
                "TimedMetadataId3Period",
                TypeInfo(int),
            ),
            (
                "timestamp_delta_milliseconds",
                "TimestampDeltaMilliseconds",
                TypeInfo(int),
            ),
            (
                "ts_file_mode",
                "TsFileMode",
                TypeInfo(typing.Union[str, HlsTsFileMode]),
            ),
        ]

    # A directory or HTTP destination for the HLS segments, manifest files, and
    # encryption keys (if enabled).
    destination: "OutputLocationRef" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Choose one or more ad marker types to pass SCTE35 signals through to this
    # group of Apple HLS outputs.
    ad_markers: typing.List[typing.Union[str, "HlsAdMarkers"]
                           ] = dataclasses.field(
                               default=ShapeBase.NOT_SET,
                           )

    # A partial URI prefix that will be prepended to each output in the media
    # .m3u8 file. Can be used if base manifest is delivered from a different URL
    # than the main .m3u8 file.
    base_url_content: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A partial URI prefix that will be prepended to each output in the media
    # .m3u8 file. Can be used if base manifest is delivered from a different URL
    # than the main .m3u8 file.
    base_url_manifest: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Mapping of up to 4 caption channels to caption languages. Is only
    # meaningful if captionLanguageSetting is set to "insert".
    caption_language_mappings: typing.List["CaptionLanguageMapping"
                                          ] = dataclasses.field(
                                              default=ShapeBase.NOT_SET,
                                          )

    # Applies only to 608 Embedded output captions. insert: Include CLOSED-
    # CAPTIONS lines in the manifest. Specify at least one language in the CC1
    # Language Code field. One CLOSED-CAPTION line is added for each Language
    # Code you specify. Make sure to specify the languages in the order in which
    # they appear in the original source (if the source is embedded format) or
    # the order of the caption selectors (if the source is other than embedded).
    # Otherwise, languages in the manifest will not match up properly with the
    # output captions. none: Include CLOSED-CAPTIONS=NONE line in the manifest.
    # omit: Omit any CLOSED-CAPTIONS line from the manifest.
    caption_language_setting: typing.Union[str, "HlsCaptionLanguageSetting"
                                          ] = dataclasses.field(
                                              default=ShapeBase.NOT_SET,
                                          )

    # When set to "disabled", sets the #EXT-X-ALLOW-CACHE:no tag in the manifest,
    # which prevents clients from saving media segments for later replay.
    client_cache: typing.Union[str, "HlsClientCache"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specification to use (RFC-6381 or the default RFC-4281) during m3u8
    # playlist generation.
    codec_specification: typing.Union[str, "HlsCodecSpecification"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # For use with encryptionType. This is a 128-bit, 16-byte hex value
    # represented by a 32-character text string. If ivSource is set to "explicit"
    # then this parameter is required and is used as the IV for encryption.
    constant_iv: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Place segments in subdirectories.
    directory_structure: typing.Union[str, "HlsDirectoryStructure"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # Encrypts the segments with the given encryption scheme. Exclude this
    # parameter if no encryption is desired.
    encryption_type: typing.Union[str, "HlsEncryptionType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Parameters that control interactions with the CDN.
    hls_cdn_settings: "HlsCdnSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If mode is "live", the number of segments to retain in the manifest (.m3u8)
    # file. This number must be less than or equal to keepSegments. If mode is
    # "vod", this parameter has no effect.
    index_n_segments: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Parameter that control output group behavior on input loss.
    input_loss_action: typing.Union[str, "InputLossActionForHlsOut"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # For use with encryptionType. The IV (Initialization Vector) is a 128-bit
    # number used in conjunction with the key for encrypting blocks. If set to
    # "include", IV is listed in the manifest, otherwise the IV is not in the
    # manifest.
    iv_in_manifest: typing.Union[str, "HlsIvInManifest"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # For use with encryptionType. The IV (Initialization Vector) is a 128-bit
    # number used in conjunction with the key for encrypting blocks. If this
    # setting is "followsSegmentNumber", it will cause the IV to change every
    # segment (to match the segment number). If this is set to "explicit", you
    # must enter a constantIv value.
    iv_source: typing.Union[str, "HlsIvSource"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If mode is "live", the number of TS segments to retain in the destination
    # directory. If mode is "vod", this parameter has no effect.
    keep_segments: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value specifies how the key is represented in the resource identified
    # by the URI. If parameter is absent, an implicit value of "identity" is
    # used. A reverse DNS string can also be given.
    key_format: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Either a single positive integer version value or a slash delimited list of
    # version values (1/2/3).
    key_format_versions: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The key provider settings.
    key_provider_settings: "KeyProviderSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When set to gzip, compresses HLS playlist.
    manifest_compression: typing.Union[str, "HlsManifestCompression"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    # Indicates whether the output manifest should use floating point or integer
    # values for segment duration.
    manifest_duration_format: typing.Union[str, "HlsManifestDurationFormat"
                                          ] = dataclasses.field(
                                              default=ShapeBase.NOT_SET,
                                          )

    # When set, minimumSegmentLength is enforced by looking ahead and back within
    # the specified range for a nearby avail and extending the segment size if
    # needed.
    min_segment_length: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If "vod", all segments are indexed and kept permanently in the destination
    # and manifest. If "live", only the number segments specified in keepSegments
    # and indexNSegments are kept; newer segments replace older segments, which
    # may prevent players from rewinding all the way to the beginning of the
    # event. VOD mode uses HLS EXT-X-PLAYLIST-TYPE of EVENT while the channel is
    # running, converting it to a "VOD" type manifest on completion of the
    # stream.
    mode: typing.Union[str, "HlsMode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Generates the .m3u8 playlist file for this HLS output group. The
    # segmentsOnly option will output segments without the .m3u8 file.
    output_selection: typing.Union[str, "HlsOutputSelection"
                                  ] = dataclasses.field(
                                      default=ShapeBase.NOT_SET,
                                  )

    # Includes or excludes EXT-X-PROGRAM-DATE-TIME tag in .m3u8 manifest files.
    # The value is calculated as follows: either the program date and time are
    # initialized using the input timecode source, or the time is initialized
    # using the input timecode source and the date is initialized using the
    # timestampOffset.
    program_date_time: typing.Union[str, "HlsProgramDateTime"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # Period of insertion of EXT-X-PROGRAM-DATE-TIME entry, in seconds.
    program_date_time_period: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Length of MPEG-2 Transport Stream segments to create (in seconds). Note
    # that segments will end on the next keyframe after this number of seconds,
    # so actual segment length may be longer.
    segment_length: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When set to useInputSegmentation, the output segment or fragment points are
    # set by the RAI markers from the input streams.
    segmentation_mode: typing.Union[str, "HlsSegmentationMode"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # Number of segments to write to a subdirectory before starting a new one.
    # directoryStructure must be subdirectoryPerStream for this setting to have
    # an effect.
    segments_per_subdirectory: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Include or exclude RESOLUTION attribute for video in EXT-X-STREAM-INF tag
    # of variant manifest.
    stream_inf_resolution: typing.Union[str, "HlsStreamInfResolution"
                                       ] = dataclasses.field(
                                           default=ShapeBase.NOT_SET,
                                       )

    # Indicates ID3 frame that has the timecode.
    timed_metadata_id3_frame: typing.Union[str, "HlsTimedMetadataId3Frame"
                                          ] = dataclasses.field(
                                              default=ShapeBase.NOT_SET,
                                          )

    # Timed Metadata interval in seconds.
    timed_metadata_id3_period: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Provides an extra millisecond delta offset to fine tune the timestamps.
    timestamp_delta_milliseconds: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When set to "singleFile", emits the program as a single media resource
    # (.ts) file, and uses #EXT-X-BYTERANGE tags to index segment for playback.
    # Playback of VOD mode content during event is not guaranteed due to HTTP
    # server caching.
    ts_file_mode: typing.Union[str, "HlsTsFileMode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class HlsInputSettings(ShapeBase):
    """
    Placeholder documentation for HlsInputSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bandwidth",
                "Bandwidth",
                TypeInfo(int),
            ),
            (
                "buffer_segments",
                "BufferSegments",
                TypeInfo(int),
            ),
            (
                "retries",
                "Retries",
                TypeInfo(int),
            ),
            (
                "retry_interval",
                "RetryInterval",
                TypeInfo(int),
            ),
        ]

    # When specified the HLS stream with the m3u8 BANDWIDTH that most closely
    # matches this value will be chosen, otherwise the highest bandwidth stream
    # in the m3u8 will be chosen. The bitrate is specified in bits per second, as
    # in an HLS manifest.
    bandwidth: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When specified, reading of the HLS input will begin this many buffer
    # segments from the end (most recently written segment). When not specified,
    # the HLS input will begin with the first segment specified in the m3u8.
    buffer_segments: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of consecutive times that attempts to read a manifest or segment
    # must fail before the input is considered unavailable.
    retries: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of seconds between retries when an attempt to read a manifest or
    # segment fails.
    retry_interval: int = dataclasses.field(default=ShapeBase.NOT_SET, )


class HlsIvInManifest(str):
    """
    Placeholder documentation for HlsIvInManifest
    """
    EXCLUDE = "EXCLUDE"
    INCLUDE = "INCLUDE"


class HlsIvSource(str):
    """
    Placeholder documentation for HlsIvSource
    """
    EXPLICIT = "EXPLICIT"
    FOLLOWS_SEGMENT_NUMBER = "FOLLOWS_SEGMENT_NUMBER"


class HlsManifestCompression(str):
    """
    Placeholder documentation for HlsManifestCompression
    """
    GZIP = "GZIP"
    NONE = "NONE"


class HlsManifestDurationFormat(str):
    """
    Placeholder documentation for HlsManifestDurationFormat
    """
    FLOATING_POINT = "FLOATING_POINT"
    INTEGER = "INTEGER"


@dataclasses.dataclass
class HlsMediaStoreSettings(ShapeBase):
    """
    Placeholder documentation for HlsMediaStoreSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "connection_retry_interval",
                "ConnectionRetryInterval",
                TypeInfo(int),
            ),
            (
                "filecache_duration",
                "FilecacheDuration",
                TypeInfo(int),
            ),
            (
                "media_store_storage_class",
                "MediaStoreStorageClass",
                TypeInfo(typing.Union[str, HlsMediaStoreStorageClass]),
            ),
            (
                "num_retries",
                "NumRetries",
                TypeInfo(int),
            ),
            (
                "restart_delay",
                "RestartDelay",
                TypeInfo(int),
            ),
        ]

    # Number of seconds to wait before retrying connection to the CDN if the
    # connection is lost.
    connection_retry_interval: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Size in seconds of file cache for streaming outputs.
    filecache_duration: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When set to temporal, output files are stored in non-persistent memory for
    # faster reading and writing.
    media_store_storage_class: typing.Union[str, "HlsMediaStoreStorageClass"
                                           ] = dataclasses.field(
                                               default=ShapeBase.NOT_SET,
                                           )

    # Number of retry attempts that will be made before the Live Event is put
    # into an error state.
    num_retries: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If a streaming output fails, number of seconds to wait until a restart is
    # initiated. A value of 0 means never restart.
    restart_delay: int = dataclasses.field(default=ShapeBase.NOT_SET, )


class HlsMediaStoreStorageClass(str):
    """
    Placeholder documentation for HlsMediaStoreStorageClass
    """
    TEMPORAL = "TEMPORAL"


class HlsMode(str):
    """
    Placeholder documentation for HlsMode
    """
    LIVE = "LIVE"
    VOD = "VOD"


class HlsOutputSelection(str):
    """
    Placeholder documentation for HlsOutputSelection
    """
    MANIFESTS_AND_SEGMENTS = "MANIFESTS_AND_SEGMENTS"
    SEGMENTS_ONLY = "SEGMENTS_ONLY"


@dataclasses.dataclass
class HlsOutputSettings(ShapeBase):
    """
    Placeholder documentation for HlsOutputSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hls_settings",
                "HlsSettings",
                TypeInfo(HlsSettings),
            ),
            (
                "name_modifier",
                "NameModifier",
                TypeInfo(str),
            ),
            (
                "segment_modifier",
                "SegmentModifier",
                TypeInfo(str),
            ),
        ]

    # Settings regarding the underlying stream. These settings are different for
    # audio-only outputs.
    hls_settings: "HlsSettings" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # String concatenated to the end of the destination filename. Accepts
    # \"Format Identifiers\":#formatIdentifierParameters.
    name_modifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # String concatenated to end of segment filenames.
    segment_modifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class HlsProgramDateTime(str):
    """
    Placeholder documentation for HlsProgramDateTime
    """
    EXCLUDE = "EXCLUDE"
    INCLUDE = "INCLUDE"


class HlsSegmentationMode(str):
    """
    Placeholder documentation for HlsSegmentationMode
    """
    USE_INPUT_SEGMENTATION = "USE_INPUT_SEGMENTATION"
    USE_SEGMENT_DURATION = "USE_SEGMENT_DURATION"


@dataclasses.dataclass
class HlsSettings(ShapeBase):
    """
    Placeholder documentation for HlsSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "audio_only_hls_settings",
                "AudioOnlyHlsSettings",
                TypeInfo(AudioOnlyHlsSettings),
            ),
            (
                "standard_hls_settings",
                "StandardHlsSettings",
                TypeInfo(StandardHlsSettings),
            ),
        ]

    # Placeholder documentation for AudioOnlyHlsSettings
    audio_only_hls_settings: "AudioOnlyHlsSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Placeholder documentation for StandardHlsSettings
    standard_hls_settings: "StandardHlsSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class HlsStreamInfResolution(str):
    """
    Placeholder documentation for HlsStreamInfResolution
    """
    EXCLUDE = "EXCLUDE"
    INCLUDE = "INCLUDE"


class HlsTimedMetadataId3Frame(str):
    """
    Placeholder documentation for HlsTimedMetadataId3Frame
    """
    NONE = "NONE"
    PRIV = "PRIV"
    TDRL = "TDRL"


class HlsTsFileMode(str):
    """
    Placeholder documentation for HlsTsFileMode
    """
    SEGMENTED_FILES = "SEGMENTED_FILES"
    SINGLE_FILE = "SINGLE_FILE"


class HlsWebdavHttpTransferMode(str):
    """
    Placeholder documentation for HlsWebdavHttpTransferMode
    """
    CHUNKED = "CHUNKED"
    NON_CHUNKED = "NON_CHUNKED"


@dataclasses.dataclass
class HlsWebdavSettings(ShapeBase):
    """
    Placeholder documentation for HlsWebdavSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "connection_retry_interval",
                "ConnectionRetryInterval",
                TypeInfo(int),
            ),
            (
                "filecache_duration",
                "FilecacheDuration",
                TypeInfo(int),
            ),
            (
                "http_transfer_mode",
                "HttpTransferMode",
                TypeInfo(typing.Union[str, HlsWebdavHttpTransferMode]),
            ),
            (
                "num_retries",
                "NumRetries",
                TypeInfo(int),
            ),
            (
                "restart_delay",
                "RestartDelay",
                TypeInfo(int),
            ),
        ]

    # Number of seconds to wait before retrying connection to the CDN if the
    # connection is lost.
    connection_retry_interval: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Size in seconds of file cache for streaming outputs.
    filecache_duration: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specify whether or not to use chunked transfer encoding to WebDAV.
    http_transfer_mode: typing.Union[str, "HlsWebdavHttpTransferMode"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )

    # Number of retry attempts that will be made before the Live Event is put
    # into an error state.
    num_retries: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If a streaming output fails, number of seconds to wait until a restart is
    # initiated. A value of 0 means never restart.
    restart_delay: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Input(ShapeBase):
    """
    Placeholder documentation for Input
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
                "attached_channels",
                "AttachedChannels",
                TypeInfo(typing.List[str]),
            ),
            (
                "destinations",
                "Destinations",
                TypeInfo(typing.List[InputDestination]),
            ),
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
                "security_groups",
                "SecurityGroups",
                TypeInfo(typing.List[str]),
            ),
            (
                "sources",
                "Sources",
                TypeInfo(typing.List[InputSource]),
            ),
            (
                "state",
                "State",
                TypeInfo(typing.Union[str, InputState]),
            ),
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, InputType]),
            ),
        ]

    # The Unique ARN of the input (generated, immutable).
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of channel IDs that that input is attached to (currently an input
    # can only be attached to one channel).
    attached_channels: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of the destinations of the input (PUSH-type).
    destinations: typing.List["InputDestination"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The generated ID of the input (unique for user account, immutable).
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The user-assigned name (This is a mutable value).
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of IDs for all the security groups attached to the input.
    security_groups: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of the sources of the input (PULL-type).
    sources: typing.List["InputSource"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Placeholder documentation for InputState
    state: typing.Union[str, "InputState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Placeholder documentation for InputType
    type: typing.Union[str, "InputType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InputAttachment(ShapeBase):
    """
    Placeholder documentation for InputAttachment
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "input_id",
                "InputId",
                TypeInfo(str),
            ),
            (
                "input_settings",
                "InputSettings",
                TypeInfo(InputSettings),
            ),
        ]

    # The ID of the input
    input_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Settings of an input (caption selector, etc.)
    input_settings: "InputSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InputChannelLevel(ShapeBase):
    """
    Placeholder documentation for InputChannelLevel
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "gain",
                "Gain",
                TypeInfo(int),
            ),
            (
                "input_channel",
                "InputChannel",
                TypeInfo(int),
            ),
        ]

    # Remixing value. Units are in dB and acceptable values are within the range
    # from -60 (mute) and 6 dB.
    gain: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The index of the input channel used as a source.
    input_channel: int = dataclasses.field(default=ShapeBase.NOT_SET, )


class InputCodec(str):
    """
    codec in increasing order of complexity
    """
    MPEG2 = "MPEG2"
    AVC = "AVC"
    HEVC = "HEVC"


class InputDeblockFilter(str):
    """
    Placeholder documentation for InputDeblockFilter
    """
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class InputDenoiseFilter(str):
    """
    Placeholder documentation for InputDenoiseFilter
    """
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


@dataclasses.dataclass
class InputDestination(ShapeBase):
    """
    The settings for a PUSH type input.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ip",
                "Ip",
                TypeInfo(str),
            ),
            (
                "port",
                "Port",
                TypeInfo(str),
            ),
            (
                "url",
                "Url",
                TypeInfo(str),
            ),
        ]

    # The system-generated static IP address of endpoint. It remains fixed for
    # the lifetime of the input.
    ip: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The port number for the input.
    port: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This represents the endpoint that the customer stream will be pushed to.
    url: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InputDestinationRequest(ShapeBase):
    """
    Endpoint settings for a PUSH type input.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stream_name",
                "StreamName",
                TypeInfo(str),
            ),
        ]

    # A unique name for the location the RTMP stream is being pushed to.
    stream_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class InputFilter(str):
    """
    Placeholder documentation for InputFilter
    """
    AUTO = "AUTO"
    DISABLED = "DISABLED"
    FORCED = "FORCED"


@dataclasses.dataclass
class InputLocation(ShapeBase):
    """
    Placeholder documentation for InputLocation
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "uri",
                "Uri",
                TypeInfo(str),
            ),
            (
                "password_param",
                "PasswordParam",
                TypeInfo(str),
            ),
            (
                "username",
                "Username",
                TypeInfo(str),
            ),
        ]

    # Uniform Resource Identifier - This should be a path to a file accessible to
    # the Live system (eg. a http:// URI) depending on the output type. For
    # example, a RTMP destination should have a uri simliar to:
    # "rtmp://fmsserver/live".
    uri: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # key used to extract the password from EC2 Parameter store
    password_param: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Documentation update needed
    username: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class InputLossActionForHlsOut(str):
    """
    Placeholder documentation for InputLossActionForHlsOut
    """
    EMIT_OUTPUT = "EMIT_OUTPUT"
    PAUSE_OUTPUT = "PAUSE_OUTPUT"


class InputLossActionForMsSmoothOut(str):
    """
    Placeholder documentation for InputLossActionForMsSmoothOut
    """
    EMIT_OUTPUT = "EMIT_OUTPUT"
    PAUSE_OUTPUT = "PAUSE_OUTPUT"


class InputLossActionForUdpOut(str):
    """
    Placeholder documentation for InputLossActionForUdpOut
    """
    DROP_PROGRAM = "DROP_PROGRAM"
    DROP_TS = "DROP_TS"
    EMIT_PROGRAM = "EMIT_PROGRAM"


@dataclasses.dataclass
class InputLossBehavior(ShapeBase):
    """
    Placeholder documentation for InputLossBehavior
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "black_frame_msec",
                "BlackFrameMsec",
                TypeInfo(int),
            ),
            (
                "input_loss_image_color",
                "InputLossImageColor",
                TypeInfo(str),
            ),
            (
                "input_loss_image_slate",
                "InputLossImageSlate",
                TypeInfo(InputLocation),
            ),
            (
                "input_loss_image_type",
                "InputLossImageType",
                TypeInfo(typing.Union[str, InputLossImageType]),
            ),
            (
                "repeat_frame_msec",
                "RepeatFrameMsec",
                TypeInfo(int),
            ),
        ]

    # Documentation update needed
    black_frame_msec: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When input loss image type is "color" this field specifies the color to
    # use. Value: 6 hex characters representing the values of RGB.
    input_loss_image_color: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When input loss image type is "slate" these fields specify the parameters
    # for accessing the slate.
    input_loss_image_slate: "InputLocation" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates whether to substitute a solid color or a slate into the output
    # after input loss exceeds blackFrameMsec.
    input_loss_image_type: typing.Union[str, "InputLossImageType"
                                       ] = dataclasses.field(
                                           default=ShapeBase.NOT_SET,
                                       )

    # Documentation update needed
    repeat_frame_msec: int = dataclasses.field(default=ShapeBase.NOT_SET, )


class InputLossImageType(str):
    """
    Placeholder documentation for InputLossImageType
    """
    COLOR = "COLOR"
    SLATE = "SLATE"


class InputMaximumBitrate(str):
    """
    Maximum input bitrate in megabits per second. Bitrates up to 50 Mbps are
    supported currently.
    """
    MAX_10_MBPS = "MAX_10_MBPS"
    MAX_20_MBPS = "MAX_20_MBPS"
    MAX_50_MBPS = "MAX_50_MBPS"


class InputResolution(str):
    """
    Input resolution based on lines of vertical resolution in the input; SD is less
    than 720 lines, HD is 720 to 1080 lines, UHD is greater than 1080 lines
    """
    SD = "SD"
    HD = "HD"
    UHD = "UHD"


@dataclasses.dataclass
class InputSecurityGroup(ShapeBase):
    """
    An Input Security Group
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
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "inputs",
                "Inputs",
                TypeInfo(typing.List[str]),
            ),
            (
                "state",
                "State",
                TypeInfo(typing.Union[str, InputSecurityGroupState]),
            ),
            (
                "whitelist_rules",
                "WhitelistRules",
                TypeInfo(typing.List[InputWhitelistRule]),
            ),
        ]

    # Unique ARN of Input Security Group
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Id of the Input Security Group
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of inputs currently using this Input Security Group.
    inputs: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current state of the Input Security Group.
    state: typing.Union[str, "InputSecurityGroupState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Whitelist rules and their sync status
    whitelist_rules: typing.List["InputWhitelistRule"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class InputSecurityGroupState(str):
    """
    Placeholder documentation for InputSecurityGroupState
    """
    IDLE = "IDLE"
    IN_USE = "IN_USE"
    UPDATING = "UPDATING"
    DELETED = "DELETED"


@dataclasses.dataclass
class InputSecurityGroupWhitelistRequest(ShapeBase):
    """
    Request of IPv4 CIDR addresses to whitelist in a security group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "whitelist_rules",
                "WhitelistRules",
                TypeInfo(typing.List[InputWhitelistRuleCidr]),
            ),
        ]

    # List of IPv4 CIDR addresses to whitelist
    whitelist_rules: typing.List["InputWhitelistRuleCidr"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InputSettings(ShapeBase):
    """
    Live Event input parameters. There can be multiple inputs in a single Live
    Event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "audio_selectors",
                "AudioSelectors",
                TypeInfo(typing.List[AudioSelector]),
            ),
            (
                "caption_selectors",
                "CaptionSelectors",
                TypeInfo(typing.List[CaptionSelector]),
            ),
            (
                "deblock_filter",
                "DeblockFilter",
                TypeInfo(typing.Union[str, InputDeblockFilter]),
            ),
            (
                "denoise_filter",
                "DenoiseFilter",
                TypeInfo(typing.Union[str, InputDenoiseFilter]),
            ),
            (
                "filter_strength",
                "FilterStrength",
                TypeInfo(int),
            ),
            (
                "input_filter",
                "InputFilter",
                TypeInfo(typing.Union[str, InputFilter]),
            ),
            (
                "network_input_settings",
                "NetworkInputSettings",
                TypeInfo(NetworkInputSettings),
            ),
            (
                "source_end_behavior",
                "SourceEndBehavior",
                TypeInfo(typing.Union[str, InputSourceEndBehavior]),
            ),
            (
                "video_selector",
                "VideoSelector",
                TypeInfo(VideoSelector),
            ),
        ]

    # Used to select the audio stream to decode for inputs that have multiple
    # available.
    audio_selectors: typing.List["AudioSelector"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Used to select the caption input to use for inputs that have multiple
    # available.
    caption_selectors: typing.List["CaptionSelector"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Enable or disable the deblock filter when filtering.
    deblock_filter: typing.Union[str, "InputDeblockFilter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Enable or disable the denoise filter when filtering.
    denoise_filter: typing.Union[str, "InputDenoiseFilter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Adjusts the magnitude of filtering from 1 (minimal) to 5 (strongest).
    filter_strength: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Turns on the filter for this input. MPEG-2 inputs have the deblocking
    # filter enabled by default. 1) auto - filtering will be applied depending on
    # input type/quality 2) disabled - no filtering will be applied to the input
    # 3) forced - filtering will be applied regardless of input type
    input_filter: typing.Union[str, "InputFilter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Input settings.
    network_input_settings: "NetworkInputSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Loop input if it is a file. This allows a file input to be streamed
    # indefinitely.
    source_end_behavior: typing.Union[str, "InputSourceEndBehavior"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # Informs which video elementary stream to decode for input types that have
    # multiple available.
    video_selector: "VideoSelector" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InputSource(ShapeBase):
    """
    The settings for a PULL type input.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "password_param",
                "PasswordParam",
                TypeInfo(str),
            ),
            (
                "url",
                "Url",
                TypeInfo(str),
            ),
            (
                "username",
                "Username",
                TypeInfo(str),
            ),
        ]

    # The key used to extract the password from EC2 Parameter store.
    password_param: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This represents the customer's source URL where stream is pulled from.
    url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The username for the input source.
    username: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class InputSourceEndBehavior(str):
    """
    Placeholder documentation for InputSourceEndBehavior
    """
    CONTINUE = "CONTINUE"
    LOOP = "LOOP"


@dataclasses.dataclass
class InputSourceRequest(ShapeBase):
    """
    Settings for for a PULL type input.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "password_param",
                "PasswordParam",
                TypeInfo(str),
            ),
            (
                "url",
                "Url",
                TypeInfo(str),
            ),
            (
                "username",
                "Username",
                TypeInfo(str),
            ),
        ]

    # The key used to extract the password from EC2 Parameter store.
    password_param: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This represents the customer's source URL where stream is pulled from.
    url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The username for the input source.
    username: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InputSpecification(ShapeBase):
    """
    Placeholder documentation for InputSpecification
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "codec",
                "Codec",
                TypeInfo(typing.Union[str, InputCodec]),
            ),
            (
                "maximum_bitrate",
                "MaximumBitrate",
                TypeInfo(typing.Union[str, InputMaximumBitrate]),
            ),
            (
                "resolution",
                "Resolution",
                TypeInfo(typing.Union[str, InputResolution]),
            ),
        ]

    # Input codec
    codec: typing.Union[str, "InputCodec"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Maximum input bitrate, categorized coarsely
    maximum_bitrate: typing.Union[str, "InputMaximumBitrate"
                                 ] = dataclasses.field(
                                     default=ShapeBase.NOT_SET,
                                 )

    # Input resolution, categorized coarsely
    resolution: typing.Union[str, "InputResolution"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class InputState(str):
    """
    Placeholder documentation for InputState
    """
    CREATING = "CREATING"
    DETACHED = "DETACHED"
    ATTACHED = "ATTACHED"
    DELETING = "DELETING"
    DELETED = "DELETED"


class InputType(str):
    """
    Placeholder documentation for InputType
    """
    UDP_PUSH = "UDP_PUSH"
    RTP_PUSH = "RTP_PUSH"
    RTMP_PUSH = "RTMP_PUSH"
    RTMP_PULL = "RTMP_PULL"
    URL_PULL = "URL_PULL"


@dataclasses.dataclass
class InputWhitelistRule(ShapeBase):
    """
    Whitelist rule
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cidr",
                "Cidr",
                TypeInfo(str),
            ),
        ]

    # The IPv4 CIDR that's whitelisted.
    cidr: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InputWhitelistRuleCidr(ShapeBase):
    """
    An IPv4 CIDR to whitelist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cidr",
                "Cidr",
                TypeInfo(str),
            ),
        ]

    # The IPv4 CIDR to whitelist.
    cidr: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InternalServerErrorException(ShapeBase):
    """
    Placeholder documentation for InternalServerErrorException
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    # Placeholder documentation for __string
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InternalServiceError(ShapeBase):
    """
    Placeholder documentation for InternalServiceError
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    # Placeholder documentation for __string
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidRequest(ShapeBase):
    """
    Placeholder documentation for InvalidRequest
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    # Placeholder documentation for __string
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class KeyProviderSettings(ShapeBase):
    """
    Placeholder documentation for KeyProviderSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "static_key_settings",
                "StaticKeySettings",
                TypeInfo(StaticKeySettings),
            ),
        ]

    # Placeholder documentation for StaticKeySettings
    static_key_settings: "StaticKeySettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class LimitExceeded(ShapeBase):
    """
    Placeholder documentation for LimitExceeded
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    # Placeholder documentation for __string
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListChannelsRequest(ShapeBase):
    """
    Placeholder documentation for ListChannelsRequest
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "max_results",
                "MaxResults",
                TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # Placeholder documentation for MaxResults
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Placeholder documentation for __string
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListChannelsResponse(OutputShapeBase):
    """
    Placeholder documentation for ListChannelsResponse
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
                "channels",
                "Channels",
                TypeInfo(typing.List[ChannelSummary]),
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

    # Placeholder documentation for __listOfChannelSummary
    channels: typing.List["ChannelSummary"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Placeholder documentation for __string
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ListChannelsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListChannelsResultModel(ShapeBase):
    """
    Placeholder documentation for ListChannelsResultModel
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "channels",
                "Channels",
                TypeInfo(typing.List[ChannelSummary]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # Placeholder documentation for __listOfChannelSummary
    channels: typing.List["ChannelSummary"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Placeholder documentation for __string
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListInputSecurityGroupsRequest(ShapeBase):
    """
    Placeholder documentation for ListInputSecurityGroupsRequest
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "max_results",
                "MaxResults",
                TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # Placeholder documentation for MaxResults
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Placeholder documentation for __string
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListInputSecurityGroupsResponse(OutputShapeBase):
    """
    Placeholder documentation for ListInputSecurityGroupsResponse
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
                "input_security_groups",
                "InputSecurityGroups",
                TypeInfo(typing.List[InputSecurityGroup]),
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

    # List of input security groups
    input_security_groups: typing.List["InputSecurityGroup"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    # Placeholder documentation for __string
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["ListInputSecurityGroupsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListInputSecurityGroupsResultModel(ShapeBase):
    """
    Result of input security group list request
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "input_security_groups",
                "InputSecurityGroups",
                TypeInfo(typing.List[InputSecurityGroup]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # List of input security groups
    input_security_groups: typing.List["InputSecurityGroup"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    # Placeholder documentation for __string
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListInputsRequest(ShapeBase):
    """
    Placeholder documentation for ListInputsRequest
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "max_results",
                "MaxResults",
                TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # Placeholder documentation for MaxResults
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Placeholder documentation for __string
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListInputsResponse(OutputShapeBase):
    """
    Placeholder documentation for ListInputsResponse
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
                "inputs",
                "Inputs",
                TypeInfo(typing.List[Input]),
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

    # Placeholder documentation for __listOfInput
    inputs: typing.List["Input"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Placeholder documentation for __string
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["ListInputsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListInputsResultModel(ShapeBase):
    """
    Placeholder documentation for ListInputsResultModel
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "inputs",
                "Inputs",
                TypeInfo(typing.List[Input]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # Placeholder documentation for __listOfInput
    inputs: typing.List["Input"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Placeholder documentation for __string
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListOfferingsRequest(ShapeBase):
    """
    Placeholder documentation for ListOfferingsRequest
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "channel_configuration",
                "ChannelConfiguration",
                TypeInfo(str),
            ),
            (
                "codec",
                "Codec",
                TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                TypeInfo(int),
            ),
            (
                "maximum_bitrate",
                "MaximumBitrate",
                TypeInfo(str),
            ),
            (
                "maximum_framerate",
                "MaximumFramerate",
                TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "resolution",
                "Resolution",
                TypeInfo(str),
            ),
            (
                "resource_type",
                "ResourceType",
                TypeInfo(str),
            ),
            (
                "special_feature",
                "SpecialFeature",
                TypeInfo(str),
            ),
            (
                "video_quality",
                "VideoQuality",
                TypeInfo(str),
            ),
        ]

    # Filter to offerings that match the configuration of an existing channel,
    # e.g. '2345678' (a channel ID)
    channel_configuration: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Filter by codec, 'AVC', 'HEVC', 'MPEG2', or 'AUDIO'
    codec: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Placeholder documentation for MaxResults
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Filter by bitrate, 'MAX_10_MBPS', 'MAX_20_MBPS', or 'MAX_50_MBPS'
    maximum_bitrate: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Filter by framerate, 'MAX_30_FPS' or 'MAX_60_FPS'
    maximum_framerate: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Placeholder documentation for __string
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Filter by resolution, 'SD', 'HD', or 'UHD'
    resolution: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Filter by resource type, 'INPUT', 'OUTPUT', or 'CHANNEL'
    resource_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Filter by special feature, 'ADVANCED_AUDIO' or 'AUDIO_NORMALIZATION'
    special_feature: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Filter by video quality, 'STANDARD', 'ENHANCED', or 'PREMIUM'
    video_quality: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListOfferingsResponse(OutputShapeBase):
    """
    Placeholder documentation for ListOfferingsResponse
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
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "offerings",
                "Offerings",
                TypeInfo(typing.List[Offering]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Token to retrieve the next page of results
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # List of offerings
    offerings: typing.List["Offering"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(self,
                ) -> typing.Generator["ListOfferingsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListOfferingsResultModel(ShapeBase):
    """
    ListOfferings response
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
                "offerings",
                "Offerings",
                TypeInfo(typing.List[Offering]),
            ),
        ]

    # Token to retrieve the next page of results
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # List of offerings
    offerings: typing.List["Offering"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListReservationsRequest(ShapeBase):
    """
    Placeholder documentation for ListReservationsRequest
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "codec",
                "Codec",
                TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                TypeInfo(int),
            ),
            (
                "maximum_bitrate",
                "MaximumBitrate",
                TypeInfo(str),
            ),
            (
                "maximum_framerate",
                "MaximumFramerate",
                TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "resolution",
                "Resolution",
                TypeInfo(str),
            ),
            (
                "resource_type",
                "ResourceType",
                TypeInfo(str),
            ),
            (
                "special_feature",
                "SpecialFeature",
                TypeInfo(str),
            ),
            (
                "video_quality",
                "VideoQuality",
                TypeInfo(str),
            ),
        ]

    # Filter by codec, 'AVC', 'HEVC', 'MPEG2', or 'AUDIO'
    codec: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Placeholder documentation for MaxResults
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Filter by bitrate, 'MAX_10_MBPS', 'MAX_20_MBPS', or 'MAX_50_MBPS'
    maximum_bitrate: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Filter by framerate, 'MAX_30_FPS' or 'MAX_60_FPS'
    maximum_framerate: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Placeholder documentation for __string
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Filter by resolution, 'SD', 'HD', or 'UHD'
    resolution: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Filter by resource type, 'INPUT', 'OUTPUT', or 'CHANNEL'
    resource_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Filter by special feature, 'ADVANCED_AUDIO' or 'AUDIO_NORMALIZATION'
    special_feature: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Filter by video quality, 'STANDARD', 'ENHANCED', or 'PREMIUM'
    video_quality: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListReservationsResponse(OutputShapeBase):
    """
    Placeholder documentation for ListReservationsResponse
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
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "reservations",
                "Reservations",
                TypeInfo(typing.List[Reservation]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Token to retrieve the next page of results
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # List of reservations
    reservations: typing.List["Reservation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(self,
                ) -> typing.Generator["ListReservationsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListReservationsResultModel(ShapeBase):
    """
    ListReservations response
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
                "reservations",
                "Reservations",
                TypeInfo(typing.List[Reservation]),
            ),
        ]

    # Token to retrieve the next page of results
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # List of reservations
    reservations: typing.List["Reservation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class LogLevel(str):
    """
    The log level the user wants for their channel.
    """
    ERROR = "ERROR"
    WARNING = "WARNING"
    INFO = "INFO"
    DEBUG = "DEBUG"
    DISABLED = "DISABLED"


class M2tsAbsentInputAudioBehavior(str):
    """
    Placeholder documentation for M2tsAbsentInputAudioBehavior
    """
    DROP = "DROP"
    ENCODE_SILENCE = "ENCODE_SILENCE"


class M2tsArib(str):
    """
    Placeholder documentation for M2tsArib
    """
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class M2tsAribCaptionsPidControl(str):
    """
    Placeholder documentation for M2tsAribCaptionsPidControl
    """
    AUTO = "AUTO"
    USE_CONFIGURED = "USE_CONFIGURED"


class M2tsAudioBufferModel(str):
    """
    Placeholder documentation for M2tsAudioBufferModel
    """
    ATSC = "ATSC"
    DVB = "DVB"


class M2tsAudioInterval(str):
    """
    Placeholder documentation for M2tsAudioInterval
    """
    VIDEO_AND_FIXED_INTERVALS = "VIDEO_AND_FIXED_INTERVALS"
    VIDEO_INTERVAL = "VIDEO_INTERVAL"


class M2tsAudioStreamType(str):
    """
    Placeholder documentation for M2tsAudioStreamType
    """
    ATSC = "ATSC"
    DVB = "DVB"


class M2tsBufferModel(str):
    """
    Placeholder documentation for M2tsBufferModel
    """
    MULTIPLEX = "MULTIPLEX"
    NONE = "NONE"


class M2tsCcDescriptor(str):
    """
    Placeholder documentation for M2tsCcDescriptor
    """
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class M2tsEbifControl(str):
    """
    Placeholder documentation for M2tsEbifControl
    """
    NONE = "NONE"
    PASSTHROUGH = "PASSTHROUGH"


class M2tsEbpPlacement(str):
    """
    Placeholder documentation for M2tsEbpPlacement
    """
    VIDEO_AND_AUDIO_PIDS = "VIDEO_AND_AUDIO_PIDS"
    VIDEO_PID = "VIDEO_PID"


class M2tsEsRateInPes(str):
    """
    Placeholder documentation for M2tsEsRateInPes
    """
    EXCLUDE = "EXCLUDE"
    INCLUDE = "INCLUDE"


class M2tsKlv(str):
    """
    Placeholder documentation for M2tsKlv
    """
    NONE = "NONE"
    PASSTHROUGH = "PASSTHROUGH"


class M2tsPcrControl(str):
    """
    Placeholder documentation for M2tsPcrControl
    """
    CONFIGURED_PCR_PERIOD = "CONFIGURED_PCR_PERIOD"
    PCR_EVERY_PES_PACKET = "PCR_EVERY_PES_PACKET"


class M2tsRateMode(str):
    """
    Placeholder documentation for M2tsRateMode
    """
    CBR = "CBR"
    VBR = "VBR"


class M2tsScte35Control(str):
    """
    Placeholder documentation for M2tsScte35Control
    """
    NONE = "NONE"
    PASSTHROUGH = "PASSTHROUGH"


class M2tsSegmentationMarkers(str):
    """
    Placeholder documentation for M2tsSegmentationMarkers
    """
    EBP = "EBP"
    EBP_LEGACY = "EBP_LEGACY"
    NONE = "NONE"
    PSI_SEGSTART = "PSI_SEGSTART"
    RAI_ADAPT = "RAI_ADAPT"
    RAI_SEGSTART = "RAI_SEGSTART"


class M2tsSegmentationStyle(str):
    """
    Placeholder documentation for M2tsSegmentationStyle
    """
    MAINTAIN_CADENCE = "MAINTAIN_CADENCE"
    RESET_CADENCE = "RESET_CADENCE"


@dataclasses.dataclass
class M2tsSettings(ShapeBase):
    """
    Placeholder documentation for M2tsSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "absent_input_audio_behavior",
                "AbsentInputAudioBehavior",
                TypeInfo(typing.Union[str, M2tsAbsentInputAudioBehavior]),
            ),
            (
                "arib",
                "Arib",
                TypeInfo(typing.Union[str, M2tsArib]),
            ),
            (
                "arib_captions_pid",
                "AribCaptionsPid",
                TypeInfo(str),
            ),
            (
                "arib_captions_pid_control",
                "AribCaptionsPidControl",
                TypeInfo(typing.Union[str, M2tsAribCaptionsPidControl]),
            ),
            (
                "audio_buffer_model",
                "AudioBufferModel",
                TypeInfo(typing.Union[str, M2tsAudioBufferModel]),
            ),
            (
                "audio_frames_per_pes",
                "AudioFramesPerPes",
                TypeInfo(int),
            ),
            (
                "audio_pids",
                "AudioPids",
                TypeInfo(str),
            ),
            (
                "audio_stream_type",
                "AudioStreamType",
                TypeInfo(typing.Union[str, M2tsAudioStreamType]),
            ),
            (
                "bitrate",
                "Bitrate",
                TypeInfo(int),
            ),
            (
                "buffer_model",
                "BufferModel",
                TypeInfo(typing.Union[str, M2tsBufferModel]),
            ),
            (
                "cc_descriptor",
                "CcDescriptor",
                TypeInfo(typing.Union[str, M2tsCcDescriptor]),
            ),
            (
                "dvb_nit_settings",
                "DvbNitSettings",
                TypeInfo(DvbNitSettings),
            ),
            (
                "dvb_sdt_settings",
                "DvbSdtSettings",
                TypeInfo(DvbSdtSettings),
            ),
            (
                "dvb_sub_pids",
                "DvbSubPids",
                TypeInfo(str),
            ),
            (
                "dvb_tdt_settings",
                "DvbTdtSettings",
                TypeInfo(DvbTdtSettings),
            ),
            (
                "dvb_teletext_pid",
                "DvbTeletextPid",
                TypeInfo(str),
            ),
            (
                "ebif",
                "Ebif",
                TypeInfo(typing.Union[str, M2tsEbifControl]),
            ),
            (
                "ebp_audio_interval",
                "EbpAudioInterval",
                TypeInfo(typing.Union[str, M2tsAudioInterval]),
            ),
            (
                "ebp_lookahead_ms",
                "EbpLookaheadMs",
                TypeInfo(int),
            ),
            (
                "ebp_placement",
                "EbpPlacement",
                TypeInfo(typing.Union[str, M2tsEbpPlacement]),
            ),
            (
                "ecm_pid",
                "EcmPid",
                TypeInfo(str),
            ),
            (
                "es_rate_in_pes",
                "EsRateInPes",
                TypeInfo(typing.Union[str, M2tsEsRateInPes]),
            ),
            (
                "etv_platform_pid",
                "EtvPlatformPid",
                TypeInfo(str),
            ),
            (
                "etv_signal_pid",
                "EtvSignalPid",
                TypeInfo(str),
            ),
            (
                "fragment_time",
                "FragmentTime",
                TypeInfo(float),
            ),
            (
                "klv",
                "Klv",
                TypeInfo(typing.Union[str, M2tsKlv]),
            ),
            (
                "klv_data_pids",
                "KlvDataPids",
                TypeInfo(str),
            ),
            (
                "null_packet_bitrate",
                "NullPacketBitrate",
                TypeInfo(float),
            ),
            (
                "pat_interval",
                "PatInterval",
                TypeInfo(int),
            ),
            (
                "pcr_control",
                "PcrControl",
                TypeInfo(typing.Union[str, M2tsPcrControl]),
            ),
            (
                "pcr_period",
                "PcrPeriod",
                TypeInfo(int),
            ),
            (
                "pcr_pid",
                "PcrPid",
                TypeInfo(str),
            ),
            (
                "pmt_interval",
                "PmtInterval",
                TypeInfo(int),
            ),
            (
                "pmt_pid",
                "PmtPid",
                TypeInfo(str),
            ),
            (
                "program_num",
                "ProgramNum",
                TypeInfo(int),
            ),
            (
                "rate_mode",
                "RateMode",
                TypeInfo(typing.Union[str, M2tsRateMode]),
            ),
            (
                "scte27_pids",
                "Scte27Pids",
                TypeInfo(str),
            ),
            (
                "scte35_control",
                "Scte35Control",
                TypeInfo(typing.Union[str, M2tsScte35Control]),
            ),
            (
                "scte35_pid",
                "Scte35Pid",
                TypeInfo(str),
            ),
            (
                "segmentation_markers",
                "SegmentationMarkers",
                TypeInfo(typing.Union[str, M2tsSegmentationMarkers]),
            ),
            (
                "segmentation_style",
                "SegmentationStyle",
                TypeInfo(typing.Union[str, M2tsSegmentationStyle]),
            ),
            (
                "segmentation_time",
                "SegmentationTime",
                TypeInfo(float),
            ),
            (
                "timed_metadata_behavior",
                "TimedMetadataBehavior",
                TypeInfo(typing.Union[str, M2tsTimedMetadataBehavior]),
            ),
            (
                "timed_metadata_pid",
                "TimedMetadataPid",
                TypeInfo(str),
            ),
            (
                "transport_stream_id",
                "TransportStreamId",
                TypeInfo(int),
            ),
            (
                "video_pid",
                "VideoPid",
                TypeInfo(str),
            ),
        ]

    # When set to drop, output audio streams will be removed from the program if
    # the selected input audio stream is removed from the input. This allows the
    # output audio configuration to dynamically change based on input
    # configuration. If this is set to encodeSilence, all output audio streams
    # will output encoded silence when not connected to an active input stream.
    absent_input_audio_behavior: typing.Union[
        str, "M2tsAbsentInputAudioBehavior"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # When set to enabled, uses ARIB-compliant field muxing and removes video
    # descriptor.
    arib: typing.Union[str, "M2tsArib"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Packet Identifier (PID) for ARIB Captions in the transport stream. Can be
    # entered as a decimal or hexadecimal value. Valid values are 32 (or
    # 0x20)..8182 (or 0x1ff6).
    arib_captions_pid: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If set to auto, pid number used for ARIB Captions will be auto-selected
    # from unused pids. If set to useConfigured, ARIB Captions will be on the
    # configured pid number.
    arib_captions_pid_control: typing.Union[str, "M2tsAribCaptionsPidControl"
                                           ] = dataclasses.field(
                                               default=ShapeBase.NOT_SET,
                                           )

    # When set to dvb, uses DVB buffer model for Dolby Digital audio. When set to
    # atsc, the ATSC model is used.
    audio_buffer_model: typing.Union[str, "M2tsAudioBufferModel"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )

    # The number of audio frames to insert for each PES packet.
    audio_frames_per_pes: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Packet Identifier (PID) of the elementary audio stream(s) in the transport
    # stream. Multiple values are accepted, and can be entered in ranges and/or
    # by comma separation. Can be entered as decimal or hexadecimal values. Each
    # PID specified must be in the range of 32 (or 0x20)..8182 (or 0x1ff6).
    audio_pids: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When set to atsc, uses stream type = 0x81 for AC3 and stream type = 0x87
    # for EAC3. When set to dvb, uses stream type = 0x06.
    audio_stream_type: typing.Union[str, "M2tsAudioStreamType"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # The output bitrate of the transport stream in bits per second. Setting to 0
    # lets the muxer automatically determine the appropriate bitrate.
    bitrate: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If set to multiplex, use multiplex buffer model for accurate interleaving.
    # Setting to bufferModel to none can lead to lower latency, but low-memory
    # devices may not be able to play back the stream without interruptions.
    buffer_model: typing.Union[str, "M2tsBufferModel"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When set to enabled, generates captionServiceDescriptor in PMT.
    cc_descriptor: typing.Union[str, "M2tsCcDescriptor"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Inserts DVB Network Information Table (NIT) at the specified table
    # repetition interval.
    dvb_nit_settings: "DvbNitSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Inserts DVB Service Description Table (SDT) at the specified table
    # repetition interval.
    dvb_sdt_settings: "DvbSdtSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Packet Identifier (PID) for input source DVB Subtitle data to this output.
    # Multiple values are accepted, and can be entered in ranges and/or by comma
    # separation. Can be entered as decimal or hexadecimal values. Each PID
    # specified must be in the range of 32 (or 0x20)..8182 (or 0x1ff6).
    dvb_sub_pids: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Inserts DVB Time and Date Table (TDT) at the specified table repetition
    # interval.
    dvb_tdt_settings: "DvbTdtSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Packet Identifier (PID) for input source DVB Teletext data to this output.
    # Can be entered as a decimal or hexadecimal value. Valid values are 32 (or
    # 0x20)..8182 (or 0x1ff6).
    dvb_teletext_pid: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If set to passthrough, passes any EBIF data from the input source to this
    # output.
    ebif: typing.Union[str, "M2tsEbifControl"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When videoAndFixedIntervals is selected, audio EBP markers will be added to
    # partitions 3 and 4. The interval between these additional markers will be
    # fixed, and will be slightly shorter than the video EBP marker interval.
    # Only available when EBP Cablelabs segmentation markers are selected.
    # Partitions 1 and 2 will always follow the video interval.
    ebp_audio_interval: typing.Union[str, "M2tsAudioInterval"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )

    # When set, enforces that Encoder Boundary Points do not come within the
    # specified time interval of each other by looking ahead at input video. If
    # another EBP is going to come in within the specified time interval, the
    # current EBP is not emitted, and the segment is "stretched" to the next
    # marker. The lookahead value does not add latency to the system. The Live
    # Event must be configured elsewhere to create sufficient latency to make the
    # lookahead accurate.
    ebp_lookahead_ms: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Controls placement of EBP on Audio PIDs. If set to videoAndAudioPids, EBP
    # markers will be placed on the video PID and all audio PIDs. If set to
    # videoPid, EBP markers will be placed on only the video PID.
    ebp_placement: typing.Union[str, "M2tsEbpPlacement"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # This field is unused and deprecated.
    ecm_pid: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Include or exclude the ES Rate field in the PES header.
    es_rate_in_pes: typing.Union[str, "M2tsEsRateInPes"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Packet Identifier (PID) for input source ETV Platform data to this output.
    # Can be entered as a decimal or hexadecimal value. Valid values are 32 (or
    # 0x20)..8182 (or 0x1ff6).
    etv_platform_pid: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Packet Identifier (PID) for input source ETV Signal data to this output.
    # Can be entered as a decimal or hexadecimal value. Valid values are 32 (or
    # 0x20)..8182 (or 0x1ff6).
    etv_signal_pid: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The length in seconds of each fragment. Only used with EBP markers.
    fragment_time: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If set to passthrough, passes any KLV data from the input source to this
    # output.
    klv: typing.Union[str, "M2tsKlv"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Packet Identifier (PID) for input source KLV data to this output. Multiple
    # values are accepted, and can be entered in ranges and/or by comma
    # separation. Can be entered as decimal or hexadecimal values. Each PID
    # specified must be in the range of 32 (or 0x20)..8182 (or 0x1ff6).
    klv_data_pids: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Value in bits per second of extra null packets to insert into the transport
    # stream. This can be used if a downstream encryption system requires
    # periodic null packets.
    null_packet_bitrate: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of milliseconds between instances of this table in the output
    # transport stream. Valid values are 0, 10..1000.
    pat_interval: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When set to pcrEveryPesPacket, a Program Clock Reference value is inserted
    # for every Packetized Elementary Stream (PES) header. This parameter is
    # effective only when the PCR PID is the same as the video or audio
    # elementary stream.
    pcr_control: typing.Union[str, "M2tsPcrControl"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Maximum time in milliseconds between Program Clock Reference (PCRs)
    # inserted into the transport stream.
    pcr_period: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Packet Identifier (PID) of the Program Clock Reference (PCR) in the
    # transport stream. When no value is given, the encoder will assign the same
    # value as the Video PID. Can be entered as a decimal or hexadecimal value.
    # Valid values are 32 (or 0x20)..8182 (or 0x1ff6).
    pcr_pid: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of milliseconds between instances of this table in the output
    # transport stream. Valid values are 0, 10..1000.
    pmt_interval: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Packet Identifier (PID) for the Program Map Table (PMT) in the transport
    # stream. Can be entered as a decimal or hexadecimal value. Valid values are
    # 32 (or 0x20)..8182 (or 0x1ff6).
    pmt_pid: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of the program number field in the Program Map Table.
    program_num: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When vbr, does not insert null packets into transport stream to fill
    # specified bitrate. The bitrate setting acts as the maximum bitrate when vbr
    # is set.
    rate_mode: typing.Union[str, "M2tsRateMode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Packet Identifier (PID) for input source SCTE-27 data to this output.
    # Multiple values are accepted, and can be entered in ranges and/or by comma
    # separation. Can be entered as decimal or hexadecimal values. Each PID
    # specified must be in the range of 32 (or 0x20)..8182 (or 0x1ff6).
    scte27_pids: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Optionally pass SCTE-35 signals from the input source to this output.
    scte35_control: typing.Union[str, "M2tsScte35Control"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Packet Identifier (PID) of the SCTE-35 stream in the transport stream. Can
    # be entered as a decimal or hexadecimal value. Valid values are 32 (or
    # 0x20)..8182 (or 0x1ff6).
    scte35_pid: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Inserts segmentation markers at each segmentationTime period. raiSegstart
    # sets the Random Access Indicator bit in the adaptation field. raiAdapt sets
    # the RAI bit and adds the current timecode in the private data bytes.
    # psiSegstart inserts PAT and PMT tables at the start of segments. ebp adds
    # Encoder Boundary Point information to the adaptation field as per OpenCable
    # specification OC-SP-EBP-I01-130118. ebpLegacy adds Encoder Boundary Point
    # information to the adaptation field using a legacy proprietary format.
    segmentation_markers: typing.Union[str, "M2tsSegmentationMarkers"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    # The segmentation style parameter controls how segmentation markers are
    # inserted into the transport stream. With avails, it is possible that
    # segments may be truncated, which can influence where future segmentation
    # markers are inserted. When a segmentation style of "resetCadence" is
    # selected and a segment is truncated due to an avail, we will reset the
    # segmentation cadence. This means the subsequent segment will have a
    # duration of $segmentationTime seconds. When a segmentation style of
    # "maintainCadence" is selected and a segment is truncated due to an avail,
    # we will not reset the segmentation cadence. This means the subsequent
    # segment will likely be truncated as well. However, all segments after that
    # will have a duration of $segmentationTime seconds. Note that EBP lookahead
    # is a slight exception to this rule.
    segmentation_style: typing.Union[str, "M2tsSegmentationStyle"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )

    # The length in seconds of each segment. Required unless markers is set to
    # None_.
    segmentation_time: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When set to passthrough, timed metadata will be passed through from input
    # to output.
    timed_metadata_behavior: typing.Union[str, "M2tsTimedMetadataBehavior"
                                         ] = dataclasses.field(
                                             default=ShapeBase.NOT_SET,
                                         )

    # Packet Identifier (PID) of the timed metadata stream in the transport
    # stream. Can be entered as a decimal or hexadecimal value. Valid values are
    # 32 (or 0x20)..8182 (or 0x1ff6).
    timed_metadata_pid: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of the transport stream ID field in the Program Map Table.
    transport_stream_id: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Packet Identifier (PID) of the elementary video stream in the transport
    # stream. Can be entered as a decimal or hexadecimal value. Valid values are
    # 32 (or 0x20)..8182 (or 0x1ff6).
    video_pid: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class M2tsTimedMetadataBehavior(str):
    """
    Placeholder documentation for M2tsTimedMetadataBehavior
    """
    NO_PASSTHROUGH = "NO_PASSTHROUGH"
    PASSTHROUGH = "PASSTHROUGH"


class M3u8PcrControl(str):
    """
    Placeholder documentation for M3u8PcrControl
    """
    CONFIGURED_PCR_PERIOD = "CONFIGURED_PCR_PERIOD"
    PCR_EVERY_PES_PACKET = "PCR_EVERY_PES_PACKET"


class M3u8Scte35Behavior(str):
    """
    Placeholder documentation for M3u8Scte35Behavior
    """
    NO_PASSTHROUGH = "NO_PASSTHROUGH"
    PASSTHROUGH = "PASSTHROUGH"


@dataclasses.dataclass
class M3u8Settings(ShapeBase):
    """
    Settings information for the .m3u8 container
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "audio_frames_per_pes",
                "AudioFramesPerPes",
                TypeInfo(int),
            ),
            (
                "audio_pids",
                "AudioPids",
                TypeInfo(str),
            ),
            (
                "ecm_pid",
                "EcmPid",
                TypeInfo(str),
            ),
            (
                "pat_interval",
                "PatInterval",
                TypeInfo(int),
            ),
            (
                "pcr_control",
                "PcrControl",
                TypeInfo(typing.Union[str, M3u8PcrControl]),
            ),
            (
                "pcr_period",
                "PcrPeriod",
                TypeInfo(int),
            ),
            (
                "pcr_pid",
                "PcrPid",
                TypeInfo(str),
            ),
            (
                "pmt_interval",
                "PmtInterval",
                TypeInfo(int),
            ),
            (
                "pmt_pid",
                "PmtPid",
                TypeInfo(str),
            ),
            (
                "program_num",
                "ProgramNum",
                TypeInfo(int),
            ),
            (
                "scte35_behavior",
                "Scte35Behavior",
                TypeInfo(typing.Union[str, M3u8Scte35Behavior]),
            ),
            (
                "scte35_pid",
                "Scte35Pid",
                TypeInfo(str),
            ),
            (
                "timed_metadata_behavior",
                "TimedMetadataBehavior",
                TypeInfo(typing.Union[str, M3u8TimedMetadataBehavior]),
            ),
            (
                "timed_metadata_pid",
                "TimedMetadataPid",
                TypeInfo(str),
            ),
            (
                "transport_stream_id",
                "TransportStreamId",
                TypeInfo(int),
            ),
            (
                "video_pid",
                "VideoPid",
                TypeInfo(str),
            ),
        ]

    # The number of audio frames to insert for each PES packet.
    audio_frames_per_pes: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Packet Identifier (PID) of the elementary audio stream(s) in the transport
    # stream. Multiple values are accepted, and can be entered in ranges and/or
    # by comma separation. Can be entered as decimal or hexadecimal values.
    audio_pids: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This parameter is unused and deprecated.
    ecm_pid: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of milliseconds between instances of this table in the output
    # transport stream. A value of \"0\" writes out the PMT once per segment
    # file.
    pat_interval: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When set to pcrEveryPesPacket, a Program Clock Reference value is inserted
    # for every Packetized Elementary Stream (PES) header. This parameter is
    # effective only when the PCR PID is the same as the video or audio
    # elementary stream.
    pcr_control: typing.Union[str, "M3u8PcrControl"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Maximum time in milliseconds between Program Clock References (PCRs)
    # inserted into the transport stream.
    pcr_period: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Packet Identifier (PID) of the Program Clock Reference (PCR) in the
    # transport stream. When no value is given, the encoder will assign the same
    # value as the Video PID. Can be entered as a decimal or hexadecimal value.
    pcr_pid: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of milliseconds between instances of this table in the output
    # transport stream. A value of \"0\" writes out the PMT once per segment
    # file.
    pmt_interval: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Packet Identifier (PID) for the Program Map Table (PMT) in the transport
    # stream. Can be entered as a decimal or hexadecimal value.
    pmt_pid: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of the program number field in the Program Map Table.
    program_num: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If set to passthrough, passes any SCTE-35 signals from the input source to
    # this output.
    scte35_behavior: typing.Union[str, "M3u8Scte35Behavior"
                                 ] = dataclasses.field(
                                     default=ShapeBase.NOT_SET,
                                 )

    # Packet Identifier (PID) of the SCTE-35 stream in the transport stream. Can
    # be entered as a decimal or hexadecimal value.
    scte35_pid: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When set to passthrough, timed metadata is passed through from input to
    # output.
    timed_metadata_behavior: typing.Union[str, "M3u8TimedMetadataBehavior"
                                         ] = dataclasses.field(
                                             default=ShapeBase.NOT_SET,
                                         )

    # Packet Identifier (PID) of the timed metadata stream in the transport
    # stream. Can be entered as a decimal or hexadecimal value. Valid values are
    # 32 (or 0x20)..8182 (or 0x1ff6).
    timed_metadata_pid: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of the transport stream ID field in the Program Map Table.
    transport_stream_id: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Packet Identifier (PID) of the elementary video stream in the transport
    # stream. Can be entered as a decimal or hexadecimal value.
    video_pid: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class M3u8TimedMetadataBehavior(str):
    """
    Placeholder documentation for M3u8TimedMetadataBehavior
    """
    NO_PASSTHROUGH = "NO_PASSTHROUGH"
    PASSTHROUGH = "PASSTHROUGH"


class Mp2CodingMode(str):
    """
    Placeholder documentation for Mp2CodingMode
    """
    CODING_MODE_1_0 = "CODING_MODE_1_0"
    CODING_MODE_2_0 = "CODING_MODE_2_0"


@dataclasses.dataclass
class Mp2Settings(ShapeBase):
    """
    Placeholder documentation for Mp2Settings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bitrate",
                "Bitrate",
                TypeInfo(float),
            ),
            (
                "coding_mode",
                "CodingMode",
                TypeInfo(typing.Union[str, Mp2CodingMode]),
            ),
            (
                "sample_rate",
                "SampleRate",
                TypeInfo(float),
            ),
        ]

    # Average bitrate in bits/second.
    bitrate: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The MPEG2 Audio coding mode. Valid values are codingMode10 (for mono) or
    # codingMode20 (for stereo).
    coding_mode: typing.Union[str, "Mp2CodingMode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Sample rate in Hz.
    sample_rate: float = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MsSmoothGroupSettings(ShapeBase):
    """
    Placeholder documentation for MsSmoothGroupSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "destination",
                "Destination",
                TypeInfo(OutputLocationRef),
            ),
            (
                "acquisition_point_id",
                "AcquisitionPointId",
                TypeInfo(str),
            ),
            (
                "audio_only_timecode_control",
                "AudioOnlyTimecodeControl",
                TypeInfo(
                    typing.Union[str, SmoothGroupAudioOnlyTimecodeControl]
                ),
            ),
            (
                "certificate_mode",
                "CertificateMode",
                TypeInfo(typing.Union[str, SmoothGroupCertificateMode]),
            ),
            (
                "connection_retry_interval",
                "ConnectionRetryInterval",
                TypeInfo(int),
            ),
            (
                "event_id",
                "EventId",
                TypeInfo(str),
            ),
            (
                "event_id_mode",
                "EventIdMode",
                TypeInfo(typing.Union[str, SmoothGroupEventIdMode]),
            ),
            (
                "event_stop_behavior",
                "EventStopBehavior",
                TypeInfo(typing.Union[str, SmoothGroupEventStopBehavior]),
            ),
            (
                "filecache_duration",
                "FilecacheDuration",
                TypeInfo(int),
            ),
            (
                "fragment_length",
                "FragmentLength",
                TypeInfo(int),
            ),
            (
                "input_loss_action",
                "InputLossAction",
                TypeInfo(typing.Union[str, InputLossActionForMsSmoothOut]),
            ),
            (
                "num_retries",
                "NumRetries",
                TypeInfo(int),
            ),
            (
                "restart_delay",
                "RestartDelay",
                TypeInfo(int),
            ),
            (
                "segmentation_mode",
                "SegmentationMode",
                TypeInfo(typing.Union[str, SmoothGroupSegmentationMode]),
            ),
            (
                "send_delay_ms",
                "SendDelayMs",
                TypeInfo(int),
            ),
            (
                "sparse_track_type",
                "SparseTrackType",
                TypeInfo(typing.Union[str, SmoothGroupSparseTrackType]),
            ),
            (
                "stream_manifest_behavior",
                "StreamManifestBehavior",
                TypeInfo(typing.Union[str, SmoothGroupStreamManifestBehavior]),
            ),
            (
                "timestamp_offset",
                "TimestampOffset",
                TypeInfo(str),
            ),
            (
                "timestamp_offset_mode",
                "TimestampOffsetMode",
                TypeInfo(typing.Union[str, SmoothGroupTimestampOffsetMode]),
            ),
        ]

    # Smooth Streaming publish point on an IIS server. Elemental Live acts as a
    # "Push" encoder to IIS.
    destination: "OutputLocationRef" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The value of the "Acquisition Point Identity" element used in each message
    # placed in the sparse track. Only enabled if sparseTrackType is not "none".
    acquisition_point_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If set to passthrough for an audio-only MS Smooth output, the fragment
    # absolute time will be set to the current timecode. This option does not
    # write timecodes to the audio elementary stream.
    audio_only_timecode_control: typing.Union[
        str, "SmoothGroupAudioOnlyTimecodeControl"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # If set to verifyAuthenticity, verify the https certificate chain to a
    # trusted Certificate Authority (CA). This will cause https outputs to self-
    # signed certificates to fail.
    certificate_mode: typing.Union[str, "SmoothGroupCertificateMode"
                                  ] = dataclasses.field(
                                      default=ShapeBase.NOT_SET,
                                  )

    # Number of seconds to wait before retrying connection to the IIS server if
    # the connection is lost. Content will be cached during this time and the
    # cache will be be delivered to the IIS server once the connection is re-
    # established.
    connection_retry_interval: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # MS Smooth event ID to be sent to the IIS server. Should only be specified
    # if eventIdMode is set to useConfigured.
    event_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies whether or not to send an event ID to the IIS server. If no event
    # ID is sent and the same Live Event is used without changing the publishing
    # point, clients might see cached video from the previous run. Options: \-
    # "useConfigured" - use the value provided in eventId \- "useTimestamp" -
    # generate and send an event ID based on the current timestamp \- "noEventId"
    # - do not send an event ID to the IIS server.
    event_id_mode: typing.Union[str, "SmoothGroupEventIdMode"
                               ] = dataclasses.field(
                                   default=ShapeBase.NOT_SET,
                               )

    # When set to sendEos, send EOS signal to IIS server when stopping the event
    event_stop_behavior: typing.Union[str, "SmoothGroupEventStopBehavior"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # Size in seconds of file cache for streaming outputs.
    filecache_duration: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Length of mp4 fragments to generate (in seconds). Fragment length must be
    # compatible with GOP size and framerate.
    fragment_length: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Parameter that control output group behavior on input loss.
    input_loss_action: typing.Union[str, "InputLossActionForMsSmoothOut"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # Number of retry attempts.
    num_retries: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Number of seconds before initiating a restart due to output failure, due to
    # exhausting the numRetries on one segment, or exceeding filecacheDuration.
    restart_delay: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When set to useInputSegmentation, the output segment or fragment points are
    # set by the RAI markers from the input streams.
    segmentation_mode: typing.Union[str, "SmoothGroupSegmentationMode"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # Outputs that are "output locked" can use this delay. Assign a delay to the
    # output that is "secondary". Do not assign a delay to the "primary" output.
    # The delay means that the primary output will always reach the downstream
    # system before the secondary, which helps ensure that the downstream system
    # always uses the primary output. (If there were no delay, the downstream
    # system might flip-flop between whichever output happens to arrive first.)
    # If the primary fails, the downstream system will switch to the secondary
    # output. When the primary is restarted, the downstream system will switch
    # back to the primary (because once again it is always arriving first)
    send_delay_ms: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If set to scte35, use incoming SCTE-35 messages to generate a sparse track
    # in this group of MS-Smooth outputs.
    sparse_track_type: typing.Union[str, "SmoothGroupSparseTrackType"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # When set to send, send stream manifest so publishing point doesn't start
    # until all streams start.
    stream_manifest_behavior: typing.Union[
        str, "SmoothGroupStreamManifestBehavior"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # Timestamp offset for the event. Only used if timestampOffsetMode is set to
    # useConfiguredOffset.
    timestamp_offset: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Type of timestamp date offset to use. \- useEventStartDate: Use the date
    # the event was started as the offset \- useConfiguredOffset: Use an
    # explicitly configured date as the offset
    timestamp_offset_mode: typing.Union[str, "SmoothGroupTimestampOffsetMode"
                                       ] = dataclasses.field(
                                           default=ShapeBase.NOT_SET,
                                       )


@dataclasses.dataclass
class MsSmoothOutputSettings(ShapeBase):
    """
    Placeholder documentation for MsSmoothOutputSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name_modifier",
                "NameModifier",
                TypeInfo(str),
            ),
        ]

    # String concatenated to the end of the destination filename. Required for
    # multiple outputs of the same type.
    name_modifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class NetworkInputServerValidation(str):
    """
    Placeholder documentation for NetworkInputServerValidation
    """
    CHECK_CRYPTOGRAPHY_AND_VALIDATE_NAME = "CHECK_CRYPTOGRAPHY_AND_VALIDATE_NAME"
    CHECK_CRYPTOGRAPHY_ONLY = "CHECK_CRYPTOGRAPHY_ONLY"


@dataclasses.dataclass
class NetworkInputSettings(ShapeBase):
    """
    Network source to transcode. Must be accessible to the Elemental Live node that
    is running the live event through a network connection.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hls_input_settings",
                "HlsInputSettings",
                TypeInfo(HlsInputSettings),
            ),
            (
                "server_validation",
                "ServerValidation",
                TypeInfo(typing.Union[str, NetworkInputServerValidation]),
            ),
        ]

    # Specifies HLS input settings when the uri is for a HLS manifest.
    hls_input_settings: "HlsInputSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Check HTTPS server certificates. When set to checkCryptographyOnly,
    # cryptography in the certificate will be checked, but not the server's name.
    # Certain subdomains (notably S3 buckets that use dots in the bucket name) do
    # not strictly match the corresponding certificate's wildcard pattern and
    # would otherwise cause the event to error. This setting is ignored for
    # protocols that do not use https.
    server_validation: typing.Union[str, "NetworkInputServerValidation"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )


@dataclasses.dataclass
class NotFoundException(ShapeBase):
    """
    Placeholder documentation for NotFoundException
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    # Placeholder documentation for __string
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Offering(ShapeBase):
    """
    Reserved resources available for purchase
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
                "currency_code",
                "CurrencyCode",
                TypeInfo(str),
            ),
            (
                "duration",
                "Duration",
                TypeInfo(int),
            ),
            (
                "duration_units",
                "DurationUnits",
                TypeInfo(typing.Union[str, OfferingDurationUnits]),
            ),
            (
                "fixed_price",
                "FixedPrice",
                TypeInfo(float),
            ),
            (
                "offering_description",
                "OfferingDescription",
                TypeInfo(str),
            ),
            (
                "offering_id",
                "OfferingId",
                TypeInfo(str),
            ),
            (
                "offering_type",
                "OfferingType",
                TypeInfo(typing.Union[str, OfferingType]),
            ),
            (
                "region",
                "Region",
                TypeInfo(str),
            ),
            (
                "resource_specification",
                "ResourceSpecification",
                TypeInfo(ReservationResourceSpecification),
            ),
            (
                "usage_price",
                "UsagePrice",
                TypeInfo(float),
            ),
        ]

    # Unique offering ARN, e.g. 'arn:aws:medialive:us-
    # west-2:123456789012:offering:87654321'
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Currency code for usagePrice and fixedPrice in ISO-4217 format, e.g. 'USD'
    currency_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Lease duration, e.g. '12'
    duration: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Units for duration, e.g. 'MONTHS'
    duration_units: typing.Union[str, "OfferingDurationUnits"
                                ] = dataclasses.field(
                                    default=ShapeBase.NOT_SET,
                                )

    # One-time charge for each reserved resource, e.g. '0.0' for a NO_UPFRONT
    # offering
    fixed_price: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Offering description, e.g. 'HD AVC output at 10-20 Mbps, 30 fps, and
    # standard VQ in US West (Oregon)'
    offering_description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique offering ID, e.g. '87654321'
    offering_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Offering type, e.g. 'NO_UPFRONT'
    offering_type: typing.Union[str, "OfferingType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # AWS region, e.g. 'us-west-2'
    region: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Resource configuration details
    resource_specification: "ReservationResourceSpecification" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Recurring usage charge for each reserved resource, e.g. '157.0'
    usage_price: float = dataclasses.field(default=ShapeBase.NOT_SET, )


class OfferingDurationUnits(str):
    """
    Units for duration, e.g. 'MONTHS'
    """
    MONTHS = "MONTHS"


class OfferingType(str):
    """
    Offering type, e.g. 'NO_UPFRONT'
    """
    NO_UPFRONT = "NO_UPFRONT"


@dataclasses.dataclass
class Output(ShapeBase):
    """
    Output settings. There can be multiple outputs within a group.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "output_settings",
                "OutputSettings",
                TypeInfo(OutputSettings),
            ),
            (
                "audio_description_names",
                "AudioDescriptionNames",
                TypeInfo(typing.List[str]),
            ),
            (
                "caption_description_names",
                "CaptionDescriptionNames",
                TypeInfo(typing.List[str]),
            ),
            (
                "output_name",
                "OutputName",
                TypeInfo(str),
            ),
            (
                "video_description_name",
                "VideoDescriptionName",
                TypeInfo(str),
            ),
        ]

    # Output type-specific settings.
    output_settings: "OutputSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The names of the AudioDescriptions used as audio sources for this output.
    audio_description_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The names of the CaptionDescriptions used as caption sources for this
    # output.
    caption_description_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name used to identify an output.
    output_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the VideoDescription used as the source for this output.
    video_description_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class OutputDestination(ShapeBase):
    """
    Placeholder documentation for OutputDestination
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
                "settings",
                "Settings",
                TypeInfo(typing.List[OutputDestinationSettings]),
            ),
        ]

    # User-specified id. This is used in an output group or an output.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Destination settings for output; one for each redundant encoder.
    settings: typing.List["OutputDestinationSettings"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class OutputDestinationSettings(ShapeBase):
    """
    Placeholder documentation for OutputDestinationSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "password_param",
                "PasswordParam",
                TypeInfo(str),
            ),
            (
                "stream_name",
                "StreamName",
                TypeInfo(str),
            ),
            (
                "url",
                "Url",
                TypeInfo(str),
            ),
            (
                "username",
                "Username",
                TypeInfo(str),
            ),
        ]

    # key used to extract the password from EC2 Parameter store
    password_param: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Stream name for RTMP destinations (URLs of type rtmp://)
    stream_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A URL specifying a destination
    url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # username for destination
    username: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class OutputGroup(ShapeBase):
    """
    Output groups for this Live Event. Output groups contain information about where
    streams should be distributed.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "output_group_settings",
                "OutputGroupSettings",
                TypeInfo(OutputGroupSettings),
            ),
            (
                "outputs",
                "Outputs",
                TypeInfo(typing.List[Output]),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # Settings associated with the output group.
    output_group_settings: "OutputGroupSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Placeholder documentation for __listOfOutput
    outputs: typing.List["Output"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Custom output group name optionally defined by the user. Only letters,
    # numbers, and the underscore character allowed; only 32 characters allowed.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class OutputGroupSettings(ShapeBase):
    """
    Placeholder documentation for OutputGroupSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "archive_group_settings",
                "ArchiveGroupSettings",
                TypeInfo(ArchiveGroupSettings),
            ),
            (
                "hls_group_settings",
                "HlsGroupSettings",
                TypeInfo(HlsGroupSettings),
            ),
            (
                "ms_smooth_group_settings",
                "MsSmoothGroupSettings",
                TypeInfo(MsSmoothGroupSettings),
            ),
            (
                "rtmp_group_settings",
                "RtmpGroupSettings",
                TypeInfo(RtmpGroupSettings),
            ),
            (
                "udp_group_settings",
                "UdpGroupSettings",
                TypeInfo(UdpGroupSettings),
            ),
        ]

    # Placeholder documentation for ArchiveGroupSettings
    archive_group_settings: "ArchiveGroupSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Placeholder documentation for HlsGroupSettings
    hls_group_settings: "HlsGroupSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Placeholder documentation for MsSmoothGroupSettings
    ms_smooth_group_settings: "MsSmoothGroupSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Placeholder documentation for RtmpGroupSettings
    rtmp_group_settings: "RtmpGroupSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Placeholder documentation for UdpGroupSettings
    udp_group_settings: "UdpGroupSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class OutputLocationRef(ShapeBase):
    """
    Reference to an OutputDestination ID defined in the channel
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "destination_ref_id",
                "DestinationRefId",
                TypeInfo(str),
            ),
        ]

    # Placeholder documentation for __string
    destination_ref_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class OutputSettings(ShapeBase):
    """
    Placeholder documentation for OutputSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "archive_output_settings",
                "ArchiveOutputSettings",
                TypeInfo(ArchiveOutputSettings),
            ),
            (
                "hls_output_settings",
                "HlsOutputSettings",
                TypeInfo(HlsOutputSettings),
            ),
            (
                "ms_smooth_output_settings",
                "MsSmoothOutputSettings",
                TypeInfo(MsSmoothOutputSettings),
            ),
            (
                "rtmp_output_settings",
                "RtmpOutputSettings",
                TypeInfo(RtmpOutputSettings),
            ),
            (
                "udp_output_settings",
                "UdpOutputSettings",
                TypeInfo(UdpOutputSettings),
            ),
        ]

    # Placeholder documentation for ArchiveOutputSettings
    archive_output_settings: "ArchiveOutputSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Placeholder documentation for HlsOutputSettings
    hls_output_settings: "HlsOutputSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Placeholder documentation for MsSmoothOutputSettings
    ms_smooth_output_settings: "MsSmoothOutputSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Placeholder documentation for RtmpOutputSettings
    rtmp_output_settings: "RtmpOutputSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Placeholder documentation for UdpOutputSettings
    udp_output_settings: "UdpOutputSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PassThroughSettings(ShapeBase):
    """
    Placeholder documentation for PassThroughSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class PurchaseOffering(ShapeBase):
    """
    PurchaseOffering request
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "count",
                "Count",
                TypeInfo(int),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "request_id",
                "RequestId",
                TypeInfo(str),
            ),
        ]

    # Number of resources
    count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Name for the new reservation
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique request ID to be specified. This is needed to prevent retries from
    # creating multiple resources.
    request_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PurchaseOfferingRequest(ShapeBase):
    """
    Placeholder documentation for PurchaseOfferingRequest
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "offering_id",
                "OfferingId",
                TypeInfo(str),
            ),
            (
                "count",
                "Count",
                TypeInfo(int),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "request_id",
                "RequestId",
                TypeInfo(str),
            ),
        ]

    # Offering to purchase, e.g. '87654321'
    offering_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Number of resources
    count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Name for the new reservation
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique request ID to be specified. This is needed to prevent retries from
    # creating multiple resources.
    request_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PurchaseOfferingResponse(OutputShapeBase):
    """
    Placeholder documentation for PurchaseOfferingResponse
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
                "reservation",
                "Reservation",
                TypeInfo(Reservation),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Reserved resources available to use
    reservation: "Reservation" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PurchaseOfferingResultModel(ShapeBase):
    """
    PurchaseOffering response
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "reservation",
                "Reservation",
                TypeInfo(Reservation),
            ),
        ]

    # Reserved resources available to use
    reservation: "Reservation" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RemixSettings(ShapeBase):
    """
    Placeholder documentation for RemixSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "channel_mappings",
                "ChannelMappings",
                TypeInfo(typing.List[AudioChannelMapping]),
            ),
            (
                "channels_in",
                "ChannelsIn",
                TypeInfo(int),
            ),
            (
                "channels_out",
                "ChannelsOut",
                TypeInfo(int),
            ),
        ]

    # Mapping of input channels to output channels, with appropriate gain
    # adjustments.
    channel_mappings: typing.List["AudioChannelMapping"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Number of input channels to be used.
    channels_in: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Number of output channels to be produced. Valid values: 1, 2, 4, 6, 8
    channels_out: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Reservation(ShapeBase):
    """
    Reserved resources available to use
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
                "count",
                "Count",
                TypeInfo(int),
            ),
            (
                "currency_code",
                "CurrencyCode",
                TypeInfo(str),
            ),
            (
                "duration",
                "Duration",
                TypeInfo(int),
            ),
            (
                "duration_units",
                "DurationUnits",
                TypeInfo(typing.Union[str, OfferingDurationUnits]),
            ),
            (
                "end",
                "End",
                TypeInfo(str),
            ),
            (
                "fixed_price",
                "FixedPrice",
                TypeInfo(float),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "offering_description",
                "OfferingDescription",
                TypeInfo(str),
            ),
            (
                "offering_id",
                "OfferingId",
                TypeInfo(str),
            ),
            (
                "offering_type",
                "OfferingType",
                TypeInfo(typing.Union[str, OfferingType]),
            ),
            (
                "region",
                "Region",
                TypeInfo(str),
            ),
            (
                "reservation_id",
                "ReservationId",
                TypeInfo(str),
            ),
            (
                "resource_specification",
                "ResourceSpecification",
                TypeInfo(ReservationResourceSpecification),
            ),
            (
                "start",
                "Start",
                TypeInfo(str),
            ),
            (
                "state",
                "State",
                TypeInfo(typing.Union[str, ReservationState]),
            ),
            (
                "usage_price",
                "UsagePrice",
                TypeInfo(float),
            ),
        ]

    # Unique reservation ARN, e.g. 'arn:aws:medialive:us-
    # west-2:123456789012:reservation:1234567'
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Number of reserved resources
    count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Currency code for usagePrice and fixedPrice in ISO-4217 format, e.g. 'USD'
    currency_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Lease duration, e.g. '12'
    duration: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Units for duration, e.g. 'MONTHS'
    duration_units: typing.Union[str, "OfferingDurationUnits"
                                ] = dataclasses.field(
                                    default=ShapeBase.NOT_SET,
                                )

    # Reservation UTC end date and time in ISO-8601 format, e.g.
    # '2019-03-01T00:00:00'
    end: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # One-time charge for each reserved resource, e.g. '0.0' for a NO_UPFRONT
    # offering
    fixed_price: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # User specified reservation name
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Offering description, e.g. 'HD AVC output at 10-20 Mbps, 30 fps, and
    # standard VQ in US West (Oregon)'
    offering_description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique offering ID, e.g. '87654321'
    offering_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Offering type, e.g. 'NO_UPFRONT'
    offering_type: typing.Union[str, "OfferingType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # AWS region, e.g. 'us-west-2'
    region: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique reservation ID, e.g. '1234567'
    reservation_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Resource configuration details
    resource_specification: "ReservationResourceSpecification" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Reservation UTC start date and time in ISO-8601 format, e.g.
    # '2018-03-01T00:00:00'
    start: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Current state of reservation, e.g. 'ACTIVE'
    state: typing.Union[str, "ReservationState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Recurring usage charge for each reserved resource, e.g. '157.0'
    usage_price: float = dataclasses.field(default=ShapeBase.NOT_SET, )


class ReservationCodec(str):
    """
    Codec, 'MPEG2', 'AVC', 'HEVC', or 'AUDIO'
    """
    MPEG2 = "MPEG2"
    AVC = "AVC"
    HEVC = "HEVC"
    AUDIO = "AUDIO"


class ReservationMaximumBitrate(str):
    """
    Maximum bitrate in megabits per second
    """
    MAX_10_MBPS = "MAX_10_MBPS"
    MAX_20_MBPS = "MAX_20_MBPS"
    MAX_50_MBPS = "MAX_50_MBPS"


class ReservationMaximumFramerate(str):
    """
    Maximum framerate in frames per second (Outputs only)
    """
    MAX_30_FPS = "MAX_30_FPS"
    MAX_60_FPS = "MAX_60_FPS"


class ReservationResolution(str):
    """
    Resolution based on lines of vertical resolution; SD is less than 720 lines, HD
    is 720 to 1080 lines, UHD is greater than 1080 lines
    """
    SD = "SD"
    HD = "HD"
    UHD = "UHD"


@dataclasses.dataclass
class ReservationResourceSpecification(ShapeBase):
    """
    Resource configuration (codec, resolution, bitrate, ...)
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "codec",
                "Codec",
                TypeInfo(typing.Union[str, ReservationCodec]),
            ),
            (
                "maximum_bitrate",
                "MaximumBitrate",
                TypeInfo(typing.Union[str, ReservationMaximumBitrate]),
            ),
            (
                "maximum_framerate",
                "MaximumFramerate",
                TypeInfo(typing.Union[str, ReservationMaximumFramerate]),
            ),
            (
                "resolution",
                "Resolution",
                TypeInfo(typing.Union[str, ReservationResolution]),
            ),
            (
                "resource_type",
                "ResourceType",
                TypeInfo(typing.Union[str, ReservationResourceType]),
            ),
            (
                "special_feature",
                "SpecialFeature",
                TypeInfo(typing.Union[str, ReservationSpecialFeature]),
            ),
            (
                "video_quality",
                "VideoQuality",
                TypeInfo(typing.Union[str, ReservationVideoQuality]),
            ),
        ]

    # Codec, e.g. 'AVC'
    codec: typing.Union[str, "ReservationCodec"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Maximum bitrate, e.g. 'MAX_20_MBPS'
    maximum_bitrate: typing.Union[str, "ReservationMaximumBitrate"
                                 ] = dataclasses.field(
                                     default=ShapeBase.NOT_SET,
                                 )

    # Maximum framerate, e.g. 'MAX_30_FPS' (Outputs only)
    maximum_framerate: typing.Union[str, "ReservationMaximumFramerate"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # Resolution, e.g. 'HD'
    resolution: typing.Union[str, "ReservationResolution"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Resource type, 'INPUT', 'OUTPUT', or 'CHANNEL'
    resource_type: typing.Union[str, "ReservationResourceType"
                               ] = dataclasses.field(
                                   default=ShapeBase.NOT_SET,
                               )

    # Special feature, e.g. 'AUDIO_NORMALIZATION' (Channels only)
    special_feature: typing.Union[str, "ReservationSpecialFeature"
                                 ] = dataclasses.field(
                                     default=ShapeBase.NOT_SET,
                                 )

    # Video quality, e.g. 'STANDARD' (Outputs only)
    video_quality: typing.Union[str, "ReservationVideoQuality"
                               ] = dataclasses.field(
                                   default=ShapeBase.NOT_SET,
                               )


class ReservationResourceType(str):
    """
    Resource type, 'INPUT', 'OUTPUT', or 'CHANNEL'
    """
    INPUT = "INPUT"
    OUTPUT = "OUTPUT"
    CHANNEL = "CHANNEL"


class ReservationSpecialFeature(str):
    """
    Special features, 'ADVANCED_AUDIO' or 'AUDIO_NORMALIZATION'
    """
    ADVANCED_AUDIO = "ADVANCED_AUDIO"
    AUDIO_NORMALIZATION = "AUDIO_NORMALIZATION"


class ReservationState(str):
    """
    Current reservation state
    """
    ACTIVE = "ACTIVE"
    EXPIRED = "EXPIRED"
    CANCELED = "CANCELED"
    DELETED = "DELETED"


class ReservationVideoQuality(str):
    """
    Video quality, e.g. 'STANDARD' (Outputs only)
    """
    STANDARD = "STANDARD"
    ENHANCED = "ENHANCED"
    PREMIUM = "PREMIUM"


@dataclasses.dataclass
class ResourceConflict(ShapeBase):
    """
    Placeholder documentation for ResourceConflict
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    # Placeholder documentation for __string
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceNotFound(ShapeBase):
    """
    Placeholder documentation for ResourceNotFound
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    # Placeholder documentation for __string
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class RtmpCacheFullBehavior(str):
    """
    Placeholder documentation for RtmpCacheFullBehavior
    """
    DISCONNECT_IMMEDIATELY = "DISCONNECT_IMMEDIATELY"
    WAIT_FOR_SERVER = "WAIT_FOR_SERVER"


class RtmpCaptionData(str):
    """
    Placeholder documentation for RtmpCaptionData
    """
    ALL = "ALL"
    FIELD1_608 = "FIELD1_608"
    FIELD1_AND_FIELD2_608 = "FIELD1_AND_FIELD2_608"


@dataclasses.dataclass
class RtmpCaptionInfoDestinationSettings(ShapeBase):
    """
    Placeholder documentation for RtmpCaptionInfoDestinationSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class RtmpGroupSettings(ShapeBase):
    """
    Placeholder documentation for RtmpGroupSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "authentication_scheme",
                "AuthenticationScheme",
                TypeInfo(typing.Union[str, AuthenticationScheme]),
            ),
            (
                "cache_full_behavior",
                "CacheFullBehavior",
                TypeInfo(typing.Union[str, RtmpCacheFullBehavior]),
            ),
            (
                "cache_length",
                "CacheLength",
                TypeInfo(int),
            ),
            (
                "caption_data",
                "CaptionData",
                TypeInfo(typing.Union[str, RtmpCaptionData]),
            ),
            (
                "restart_delay",
                "RestartDelay",
                TypeInfo(int),
            ),
        ]

    # Authentication scheme to use when connecting with CDN
    authentication_scheme: typing.Union[str, "AuthenticationScheme"
                                       ] = dataclasses.field(
                                           default=ShapeBase.NOT_SET,
                                       )

    # Controls behavior when content cache fills up. If remote origin server
    # stalls the RTMP connection and does not accept content fast enough the
    # 'Media Cache' will fill up. When the cache reaches the duration specified
    # by cacheLength the cache will stop accepting new content. If set to
    # disconnectImmediately, the RTMP output will force a disconnect. Clear the
    # media cache, and reconnect after restartDelay seconds. If set to
    # waitForServer, the RTMP output will wait up to 5 minutes to allow the
    # origin server to begin accepting data again.
    cache_full_behavior: typing.Union[str, "RtmpCacheFullBehavior"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # Cache length, in seconds, is used to calculate buffer size.
    cache_length: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Controls the types of data that passes to onCaptionInfo outputs. If set to
    # 'all' then 608 and 708 carried DTVCC data will be passed. If set to
    # 'field1AndField2608' then DTVCC data will be stripped out, but 608 data
    # from both fields will be passed. If set to 'field1608' then only the data
    # carried in 608 from field 1 video will be passed.
    caption_data: typing.Union[str, "RtmpCaptionData"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If a streaming output fails, number of seconds to wait until a restart is
    # initiated. A value of 0 means never restart.
    restart_delay: int = dataclasses.field(default=ShapeBase.NOT_SET, )


class RtmpOutputCertificateMode(str):
    """
    Placeholder documentation for RtmpOutputCertificateMode
    """
    SELF_SIGNED = "SELF_SIGNED"
    VERIFY_AUTHENTICITY = "VERIFY_AUTHENTICITY"


@dataclasses.dataclass
class RtmpOutputSettings(ShapeBase):
    """
    Placeholder documentation for RtmpOutputSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "destination",
                "Destination",
                TypeInfo(OutputLocationRef),
            ),
            (
                "certificate_mode",
                "CertificateMode",
                TypeInfo(typing.Union[str, RtmpOutputCertificateMode]),
            ),
            (
                "connection_retry_interval",
                "ConnectionRetryInterval",
                TypeInfo(int),
            ),
            (
                "num_retries",
                "NumRetries",
                TypeInfo(int),
            ),
        ]

    # The RTMP endpoint excluding the stream name (eg. rtmp://host/appname). For
    # connection to Akamai, a username and password must be supplied. URI fields
    # accept format identifiers.
    destination: "OutputLocationRef" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If set to verifyAuthenticity, verify the tls certificate chain to a trusted
    # Certificate Authority (CA). This will cause rtmps outputs with self-signed
    # certificates to fail.
    certificate_mode: typing.Union[str, "RtmpOutputCertificateMode"
                                  ] = dataclasses.field(
                                      default=ShapeBase.NOT_SET,
                                  )

    # Number of seconds to wait before retrying a connection to the Flash Media
    # server if the connection is lost.
    connection_retry_interval: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Number of retry attempts.
    num_retries: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ScheduleAction(ShapeBase):
    """
    A single schedule action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "action_name",
                "ActionName",
                TypeInfo(str),
            ),
            (
                "schedule_action_settings",
                "ScheduleActionSettings",
                TypeInfo(ScheduleActionSettings),
            ),
            (
                "schedule_action_start_settings",
                "ScheduleActionStartSettings",
                TypeInfo(ScheduleActionStartSettings),
            ),
        ]

    # The name of the action, must be unique within the schedule.
    action_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Settings for this schedule action.
    schedule_action_settings: "ScheduleActionSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When the action takes effect.
    schedule_action_start_settings: "ScheduleActionStartSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ScheduleActionSettings(ShapeBase):
    """
    Settings for a single schedule action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "scte35_return_to_network_settings",
                "Scte35ReturnToNetworkSettings",
                TypeInfo(Scte35ReturnToNetworkScheduleActionSettings),
            ),
            (
                "scte35_splice_insert_settings",
                "Scte35SpliceInsertSettings",
                TypeInfo(Scte35SpliceInsertScheduleActionSettings),
            ),
            (
                "scte35_time_signal_settings",
                "Scte35TimeSignalSettings",
                TypeInfo(Scte35TimeSignalScheduleActionSettings),
            ),
            (
                "static_image_activate_settings",
                "StaticImageActivateSettings",
                TypeInfo(StaticImageActivateScheduleActionSettings),
            ),
            (
                "static_image_deactivate_settings",
                "StaticImageDeactivateSettings",
                TypeInfo(StaticImageDeactivateScheduleActionSettings),
            ),
        ]

    # SCTE-35 Return to Network Settings
    scte35_return_to_network_settings: "Scte35ReturnToNetworkScheduleActionSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # SCTE-35 Splice Insert Settings
    scte35_splice_insert_settings: "Scte35SpliceInsertScheduleActionSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # SCTE-35 Time Signal Settings
    scte35_time_signal_settings: "Scte35TimeSignalScheduleActionSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Static Image Activate
    static_image_activate_settings: "StaticImageActivateScheduleActionSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Static Image Deactivate
    static_image_deactivate_settings: "StaticImageDeactivateScheduleActionSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ScheduleActionStartSettings(ShapeBase):
    """
    When the schedule action starts.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "fixed_mode_schedule_action_start_settings",
                "FixedModeScheduleActionStartSettings",
                TypeInfo(FixedModeScheduleActionStartSettings),
            ),
        ]

    # Fixed timestamp action start. Conforms to ISO-8601.
    fixed_mode_schedule_action_start_settings: "FixedModeScheduleActionStartSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ScheduleDescribeResultModel(ShapeBase):
    """
    A complete schedule description.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "schedule_actions",
                "ScheduleActions",
                TypeInfo(typing.List[ScheduleAction]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The list of schedule actions.
    schedule_actions: typing.List["ScheduleAction"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The next token; for use in pagination.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class Scte20Convert608To708(str):
    """
    Placeholder documentation for Scte20Convert608To708
    """
    DISABLED = "DISABLED"
    UPCONVERT = "UPCONVERT"


@dataclasses.dataclass
class Scte20PlusEmbeddedDestinationSettings(ShapeBase):
    """
    Placeholder documentation for Scte20PlusEmbeddedDestinationSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class Scte20SourceSettings(ShapeBase):
    """
    Placeholder documentation for Scte20SourceSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "convert608_to708",
                "Convert608To708",
                TypeInfo(typing.Union[str, Scte20Convert608To708]),
            ),
            (
                "source608_channel_number",
                "Source608ChannelNumber",
                TypeInfo(int),
            ),
        ]

    # If upconvert, 608 data is both passed through via the "608 compatibility
    # bytes" fields of the 708 wrapper as well as translated into 708. 708 data
    # present in the source content will be discarded.
    convert608_to708: typing.Union[str, "Scte20Convert608To708"
                                  ] = dataclasses.field(
                                      default=ShapeBase.NOT_SET,
                                  )

    # Specifies the 608/708 channel number within the video track from which to
    # extract captions. Unused for passthrough.
    source608_channel_number: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Scte27DestinationSettings(ShapeBase):
    """
    Placeholder documentation for Scte27DestinationSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class Scte27SourceSettings(ShapeBase):
    """
    Placeholder documentation for Scte27SourceSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pid",
                "Pid",
                TypeInfo(int),
            ),
        ]

    # The pid field is used in conjunction with the caption selector languageCode
    # field as follows: \- Specify PID and Language: Extracts captions from that
    # PID; the language is "informational". \- Specify PID and omit Language:
    # Extracts the specified PID. \- Omit PID and specify Language: Extracts the
    # specified language, whichever PID that happens to be. \- Omit PID and omit
    # Language: Valid only if source is DVB-Sub that is being passed through; all
    # languages will be passed through.
    pid: int = dataclasses.field(default=ShapeBase.NOT_SET, )


class Scte35AposNoRegionalBlackoutBehavior(str):
    """
    Placeholder documentation for Scte35AposNoRegionalBlackoutBehavior
    """
    FOLLOW = "FOLLOW"
    IGNORE = "IGNORE"


class Scte35AposWebDeliveryAllowedBehavior(str):
    """
    Placeholder documentation for Scte35AposWebDeliveryAllowedBehavior
    """
    FOLLOW = "FOLLOW"
    IGNORE = "IGNORE"


class Scte35ArchiveAllowedFlag(str):
    """
    SCTE-35 segmentation_descriptor archive_allowed_flag.
    """
    ARCHIVE_NOT_ALLOWED = "ARCHIVE_NOT_ALLOWED"
    ARCHIVE_ALLOWED = "ARCHIVE_ALLOWED"


@dataclasses.dataclass
class Scte35DeliveryRestrictions(ShapeBase):
    """
    SCTE-35 Delivery Restrictions.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "archive_allowed_flag",
                "ArchiveAllowedFlag",
                TypeInfo(typing.Union[str, Scte35ArchiveAllowedFlag]),
            ),
            (
                "device_restrictions",
                "DeviceRestrictions",
                TypeInfo(typing.Union[str, Scte35DeviceRestrictions]),
            ),
            (
                "no_regional_blackout_flag",
                "NoRegionalBlackoutFlag",
                TypeInfo(typing.Union[str, Scte35NoRegionalBlackoutFlag]),
            ),
            (
                "web_delivery_allowed_flag",
                "WebDeliveryAllowedFlag",
                TypeInfo(typing.Union[str, Scte35WebDeliveryAllowedFlag]),
            ),
        ]

    # SCTE-35 segmentation_descriptor archive_allowed_flag.
    archive_allowed_flag: typing.Union[str, "Scte35ArchiveAllowedFlag"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    # SCTE-35 segmentation_descriptor web_delivery_allowed_flag.
    device_restrictions: typing.Union[str, "Scte35DeviceRestrictions"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # SCTE-35 segmentation_descriptor no_regional_blackout_flag.
    no_regional_blackout_flag: typing.Union[str, "Scte35NoRegionalBlackoutFlag"
                                           ] = dataclasses.field(
                                               default=ShapeBase.NOT_SET,
                                           )

    # SCTE-35 segmentation_descriptor web_delivery_allowed_flag.
    web_delivery_allowed_flag: typing.Union[str, "Scte35WebDeliveryAllowedFlag"
                                           ] = dataclasses.field(
                                               default=ShapeBase.NOT_SET,
                                           )


@dataclasses.dataclass
class Scte35Descriptor(ShapeBase):
    """
    SCTE-35 Descriptor.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "scte35_descriptor_settings",
                "Scte35DescriptorSettings",
                TypeInfo(Scte35DescriptorSettings),
            ),
        ]

    # SCTE-35 Descriptor Settings.
    scte35_descriptor_settings: "Scte35DescriptorSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Scte35DescriptorSettings(ShapeBase):
    """
    SCTE-35 Descriptor settings.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "segmentation_descriptor_scte35_descriptor_settings",
                "SegmentationDescriptorScte35DescriptorSettings",
                TypeInfo(Scte35SegmentationDescriptor),
            ),
        ]

    # SCTE-35 Segmentation Descriptor.
    segmentation_descriptor_scte35_descriptor_settings: "Scte35SegmentationDescriptor" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class Scte35DeviceRestrictions(str):
    """
    SCTE-35 Device Restrictions.
    """
    NONE = "NONE"
    RESTRICT_GROUP0 = "RESTRICT_GROUP0"
    RESTRICT_GROUP1 = "RESTRICT_GROUP1"
    RESTRICT_GROUP2 = "RESTRICT_GROUP2"


class Scte35NoRegionalBlackoutFlag(str):
    """
    SCTE-35 segmentation_descriptor no_regional_blackout_flag.
    """
    REGIONAL_BLACKOUT = "REGIONAL_BLACKOUT"
    NO_REGIONAL_BLACKOUT = "NO_REGIONAL_BLACKOUT"


@dataclasses.dataclass
class Scte35ReturnToNetworkScheduleActionSettings(ShapeBase):
    """
    SCTE-35 Return to Network Settings.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "splice_event_id",
                "SpliceEventId",
                TypeInfo(int),
            ),
        ]

    # The splice_event_id for the SCTE-35 splice_insert, as defined in SCTE-35.
    splice_event_id: int = dataclasses.field(default=ShapeBase.NOT_SET, )


class Scte35SegmentationCancelIndicator(str):
    """
    SCTE-35 segmentation_descriptor segmentation_event_cancel_indicator.
    """
    SEGMENTATION_EVENT_NOT_CANCELED = "SEGMENTATION_EVENT_NOT_CANCELED"
    SEGMENTATION_EVENT_CANCELED = "SEGMENTATION_EVENT_CANCELED"


@dataclasses.dataclass
class Scte35SegmentationDescriptor(ShapeBase):
    """
    SCTE-35 Segmentation Descriptor.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "segmentation_cancel_indicator",
                "SegmentationCancelIndicator",
                TypeInfo(typing.Union[str, Scte35SegmentationCancelIndicator]),
            ),
            (
                "segmentation_event_id",
                "SegmentationEventId",
                TypeInfo(int),
            ),
            (
                "delivery_restrictions",
                "DeliveryRestrictions",
                TypeInfo(Scte35DeliveryRestrictions),
            ),
            (
                "segment_num",
                "SegmentNum",
                TypeInfo(int),
            ),
            (
                "segmentation_duration",
                "SegmentationDuration",
                TypeInfo(int),
            ),
            (
                "segmentation_type_id",
                "SegmentationTypeId",
                TypeInfo(int),
            ),
            (
                "segmentation_upid",
                "SegmentationUpid",
                TypeInfo(str),
            ),
            (
                "segmentation_upid_type",
                "SegmentationUpidType",
                TypeInfo(int),
            ),
            (
                "segments_expected",
                "SegmentsExpected",
                TypeInfo(int),
            ),
            (
                "sub_segment_num",
                "SubSegmentNum",
                TypeInfo(int),
            ),
            (
                "sub_segments_expected",
                "SubSegmentsExpected",
                TypeInfo(int),
            ),
        ]

    # SCTE-35 segmentation_descriptor segmentation_event_cancel_indicator.
    segmentation_cancel_indicator: typing.Union[
        str, "Scte35SegmentationCancelIndicator"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # SCTE-35 segmentation_descriptor segmentation_event_id.
    segmentation_event_id: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # SCTE-35 delivery restrictions.
    delivery_restrictions: "Scte35DeliveryRestrictions" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # SCTE-35 segmentation_descriptor segment_num.
    segment_num: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # SCTE-35 segmentation_descriptor segmentation_duration specified in 90 KHz
    # clock ticks.
    segmentation_duration: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # SCTE-35 segmentation_descriptor segmentation_type_id.
    segmentation_type_id: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # SCTE-35 segmentation_descriptor segmentation_upid as a hex string.
    segmentation_upid: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # SCTE-35 segmentation_descriptor segmentation_upid_type.
    segmentation_upid_type: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # SCTE-35 segmentation_descriptor segments_expected.
    segments_expected: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # SCTE-35 segmentation_descriptor sub_segment_num.
    sub_segment_num: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # SCTE-35 segmentation_descriptor sub_segments_expected.
    sub_segments_expected: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Scte35SpliceInsert(ShapeBase):
    """
    Placeholder documentation for Scte35SpliceInsert
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ad_avail_offset",
                "AdAvailOffset",
                TypeInfo(int),
            ),
            (
                "no_regional_blackout_flag",
                "NoRegionalBlackoutFlag",
                TypeInfo(
                    typing.
                    Union[str, Scte35SpliceInsertNoRegionalBlackoutBehavior]
                ),
            ),
            (
                "web_delivery_allowed_flag",
                "WebDeliveryAllowedFlag",
                TypeInfo(
                    typing.
                    Union[str, Scte35SpliceInsertWebDeliveryAllowedBehavior]
                ),
            ),
        ]

    # When specified, this offset (in milliseconds) is added to the input Ad
    # Avail PTS time. This only applies to embedded SCTE 104/35 messages and does
    # not apply to OOB messages.
    ad_avail_offset: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When set to ignore, Segment Descriptors with noRegionalBlackoutFlag set to
    # 0 will no longer trigger blackouts or Ad Avail slates
    no_regional_blackout_flag: typing.Union[
        str, "Scte35SpliceInsertNoRegionalBlackoutBehavior"
    ] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When set to ignore, Segment Descriptors with webDeliveryAllowedFlag set to
    # 0 will no longer trigger blackouts or Ad Avail slates
    web_delivery_allowed_flag: typing.Union[
        str, "Scte35SpliceInsertWebDeliveryAllowedBehavior"
    ] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class Scte35SpliceInsertNoRegionalBlackoutBehavior(str):
    """
    Placeholder documentation for Scte35SpliceInsertNoRegionalBlackoutBehavior
    """
    FOLLOW = "FOLLOW"
    IGNORE = "IGNORE"


@dataclasses.dataclass
class Scte35SpliceInsertScheduleActionSettings(ShapeBase):
    """
    SCTE-35 Splice Insert Settings.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "splice_event_id",
                "SpliceEventId",
                TypeInfo(int),
            ),
            (
                "duration",
                "Duration",
                TypeInfo(int),
            ),
        ]

    # The splice_event_id for the SCTE-35 splice_insert, as defined in SCTE-35.
    splice_event_id: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The duration for the SCTE-35 splice_insert specified in 90KHz clock ticks.
    # When duration is not specified the expectation is that a
    # Scte35ReturnToNetwork action will be scheduled.
    duration: int = dataclasses.field(default=ShapeBase.NOT_SET, )


class Scte35SpliceInsertWebDeliveryAllowedBehavior(str):
    """
    Placeholder documentation for Scte35SpliceInsertWebDeliveryAllowedBehavior
    """
    FOLLOW = "FOLLOW"
    IGNORE = "IGNORE"


@dataclasses.dataclass
class Scte35TimeSignalApos(ShapeBase):
    """
    Placeholder documentation for Scte35TimeSignalApos
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ad_avail_offset",
                "AdAvailOffset",
                TypeInfo(int),
            ),
            (
                "no_regional_blackout_flag",
                "NoRegionalBlackoutFlag",
                TypeInfo(
                    typing.Union[str, Scte35AposNoRegionalBlackoutBehavior]
                ),
            ),
            (
                "web_delivery_allowed_flag",
                "WebDeliveryAllowedFlag",
                TypeInfo(
                    typing.Union[str, Scte35AposWebDeliveryAllowedBehavior]
                ),
            ),
        ]

    # When specified, this offset (in milliseconds) is added to the input Ad
    # Avail PTS time. This only applies to embedded SCTE 104/35 messages and does
    # not apply to OOB messages.
    ad_avail_offset: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When set to ignore, Segment Descriptors with noRegionalBlackoutFlag set to
    # 0 will no longer trigger blackouts or Ad Avail slates
    no_regional_blackout_flag: typing.Union[
        str, "Scte35AposNoRegionalBlackoutBehavior"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # When set to ignore, Segment Descriptors with webDeliveryAllowedFlag set to
    # 0 will no longer trigger blackouts or Ad Avail slates
    web_delivery_allowed_flag: typing.Union[
        str, "Scte35AposWebDeliveryAllowedBehavior"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )


@dataclasses.dataclass
class Scte35TimeSignalScheduleActionSettings(ShapeBase):
    """
    SCTE-35 Time Signal Settings.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "scte35_descriptors",
                "Scte35Descriptors",
                TypeInfo(typing.List[Scte35Descriptor]),
            ),
        ]

    # The list of SCTE-35 descriptors accompanying the SCTE-35 time_signal.
    scte35_descriptors: typing.List["Scte35Descriptor"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class Scte35WebDeliveryAllowedFlag(str):
    """
    SCTE-35 segmentation_descriptor web_delivery_allowed_flag.
    """
    WEB_DELIVERY_NOT_ALLOWED = "WEB_DELIVERY_NOT_ALLOWED"
    WEB_DELIVERY_ALLOWED = "WEB_DELIVERY_ALLOWED"


class SmoothGroupAudioOnlyTimecodeControl(str):
    """
    Placeholder documentation for SmoothGroupAudioOnlyTimecodeControl
    """
    PASSTHROUGH = "PASSTHROUGH"
    USE_CONFIGURED_CLOCK = "USE_CONFIGURED_CLOCK"


class SmoothGroupCertificateMode(str):
    """
    Placeholder documentation for SmoothGroupCertificateMode
    """
    SELF_SIGNED = "SELF_SIGNED"
    VERIFY_AUTHENTICITY = "VERIFY_AUTHENTICITY"


class SmoothGroupEventIdMode(str):
    """
    Placeholder documentation for SmoothGroupEventIdMode
    """
    NO_EVENT_ID = "NO_EVENT_ID"
    USE_CONFIGURED = "USE_CONFIGURED"
    USE_TIMESTAMP = "USE_TIMESTAMP"


class SmoothGroupEventStopBehavior(str):
    """
    Placeholder documentation for SmoothGroupEventStopBehavior
    """
    NONE = "NONE"
    SEND_EOS = "SEND_EOS"


class SmoothGroupSegmentationMode(str):
    """
    Placeholder documentation for SmoothGroupSegmentationMode
    """
    USE_INPUT_SEGMENTATION = "USE_INPUT_SEGMENTATION"
    USE_SEGMENT_DURATION = "USE_SEGMENT_DURATION"


class SmoothGroupSparseTrackType(str):
    """
    Placeholder documentation for SmoothGroupSparseTrackType
    """
    NONE = "NONE"
    SCTE_35 = "SCTE_35"


class SmoothGroupStreamManifestBehavior(str):
    """
    Placeholder documentation for SmoothGroupStreamManifestBehavior
    """
    DO_NOT_SEND = "DO_NOT_SEND"
    SEND = "SEND"


class SmoothGroupTimestampOffsetMode(str):
    """
    Placeholder documentation for SmoothGroupTimestampOffsetMode
    """
    USE_CONFIGURED_OFFSET = "USE_CONFIGURED_OFFSET"
    USE_EVENT_START_DATE = "USE_EVENT_START_DATE"


@dataclasses.dataclass
class SmpteTtDestinationSettings(ShapeBase):
    """
    Placeholder documentation for SmpteTtDestinationSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class StandardHlsSettings(ShapeBase):
    """
    Placeholder documentation for StandardHlsSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "m3u8_settings",
                "M3u8Settings",
                TypeInfo(M3u8Settings),
            ),
            (
                "audio_rendition_sets",
                "AudioRenditionSets",
                TypeInfo(str),
            ),
        ]

    # Settings information for the .m3u8 container
    m3u8_settings: "M3u8Settings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # List all the audio groups that are used with the video output stream. Input
    # all the audio GROUP-IDs that are associated to the video, separate by ','.
    audio_rendition_sets: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartChannelRequest(ShapeBase):
    """
    Placeholder documentation for StartChannelRequest
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "channel_id",
                "ChannelId",
                TypeInfo(str),
            ),
        ]

    # A request to start a channel
    channel_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartChannelResponse(OutputShapeBase):
    """
    Placeholder documentation for StartChannelResponse
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
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "destinations",
                "Destinations",
                TypeInfo(typing.List[OutputDestination]),
            ),
            (
                "egress_endpoints",
                "EgressEndpoints",
                TypeInfo(typing.List[ChannelEgressEndpoint]),
            ),
            (
                "encoder_settings",
                "EncoderSettings",
                TypeInfo(EncoderSettings),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "input_attachments",
                "InputAttachments",
                TypeInfo(typing.List[InputAttachment]),
            ),
            (
                "input_specification",
                "InputSpecification",
                TypeInfo(InputSpecification),
            ),
            (
                "log_level",
                "LogLevel",
                TypeInfo(typing.Union[str, LogLevel]),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "pipelines_running_count",
                "PipelinesRunningCount",
                TypeInfo(int),
            ),
            (
                "role_arn",
                "RoleArn",
                TypeInfo(str),
            ),
            (
                "state",
                "State",
                TypeInfo(typing.Union[str, ChannelState]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unique arn of the channel.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of destinations of the channel. For UDP outputs, there is one
    # destination per output. For other types (HLS, for example), there is one
    # destination per packager.
    destinations: typing.List["OutputDestination"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The endpoints where outgoing connections initiate from
    egress_endpoints: typing.List["ChannelEgressEndpoint"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Placeholder documentation for EncoderSettings
    encoder_settings: "EncoderSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unique id of the channel.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # List of input attachments for channel.
    input_attachments: typing.List["InputAttachment"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Placeholder documentation for InputSpecification
    input_specification: "InputSpecification" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The log level being written to CloudWatch Logs.
    log_level: typing.Union[str, "LogLevel"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the channel. (user-mutable)
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of currently healthy pipelines.
    pipelines_running_count: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the role assumed when running the
    # Channel.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Placeholder documentation for ChannelState
    state: typing.Union[str, "ChannelState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StaticImageActivateScheduleActionSettings(ShapeBase):
    """
    Static image activate.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "image",
                "Image",
                TypeInfo(InputLocation),
            ),
            (
                "duration",
                "Duration",
                TypeInfo(int),
            ),
            (
                "fade_in",
                "FadeIn",
                TypeInfo(int),
            ),
            (
                "fade_out",
                "FadeOut",
                TypeInfo(int),
            ),
            (
                "height",
                "Height",
                TypeInfo(int),
            ),
            (
                "image_x",
                "ImageX",
                TypeInfo(int),
            ),
            (
                "image_y",
                "ImageY",
                TypeInfo(int),
            ),
            (
                "layer",
                "Layer",
                TypeInfo(int),
            ),
            (
                "opacity",
                "Opacity",
                TypeInfo(int),
            ),
            (
                "width",
                "Width",
                TypeInfo(int),
            ),
        ]

    # The image to overlay on the video. Must be a 32 bit BMP, PNG, or TGA file.
    # Must not be larger than the input video.
    image: "InputLocation" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The duration in milliseconds for the image to remain in the video. If
    # omitted or set to 0, duration is infinite and image will remain until
    # explicitly deactivated.
    duration: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time in milliseconds for the image to fade in. Defaults to 0.
    fade_in: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time in milliseconds for the image to fade out. Defaults to 0.
    fade_out: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The height of the image when inserted into the video. Defaults to the
    # native height of the image.
    height: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Placement of the left edge of the image on the horizontal axis in pixels. 0
    # is the left edge of the frame. Defaults to 0.
    image_x: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Placement of the top edge of the image on the vertical axis in pixels. 0 is
    # the top edge of the frame. Defaults to 0.
    image_y: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Z order of the inserted image. Images with higher layer values will be
    # inserted on top of images with lower layer values. Permitted values are 0-7
    # inclusive. Defaults to 0.
    layer: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Opacity of image where 0 is transparent and 100 is fully opaque. Defaults
    # to 100.
    opacity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The width of the image when inserted into the video. Defaults to the native
    # width of the image.
    width: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StaticImageDeactivateScheduleActionSettings(ShapeBase):
    """
    Static image deactivate.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "fade_out",
                "FadeOut",
                TypeInfo(int),
            ),
            (
                "layer",
                "Layer",
                TypeInfo(int),
            ),
        ]

    # The time in milliseconds for the image to fade out. Defaults to 0.
    fade_out: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Z order of the inserted image. Images with higher layer values will be
    # inserted on top of images with lower layer values. Permitted values are 0-7
    # inclusive. Defaults to 0.
    layer: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StaticKeySettings(ShapeBase):
    """
    Placeholder documentation for StaticKeySettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "static_key_value",
                "StaticKeyValue",
                TypeInfo(str),
            ),
            (
                "key_provider_server",
                "KeyProviderServer",
                TypeInfo(InputLocation),
            ),
        ]

    # Static key value as a 32 character hexadecimal string.
    static_key_value: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The URL of the license server used for protecting content.
    key_provider_server: "InputLocation" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StopChannelRequest(ShapeBase):
    """
    Placeholder documentation for StopChannelRequest
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "channel_id",
                "ChannelId",
                TypeInfo(str),
            ),
        ]

    # A request to stop a running channel
    channel_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StopChannelResponse(OutputShapeBase):
    """
    Placeholder documentation for StopChannelResponse
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
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "destinations",
                "Destinations",
                TypeInfo(typing.List[OutputDestination]),
            ),
            (
                "egress_endpoints",
                "EgressEndpoints",
                TypeInfo(typing.List[ChannelEgressEndpoint]),
            ),
            (
                "encoder_settings",
                "EncoderSettings",
                TypeInfo(EncoderSettings),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "input_attachments",
                "InputAttachments",
                TypeInfo(typing.List[InputAttachment]),
            ),
            (
                "input_specification",
                "InputSpecification",
                TypeInfo(InputSpecification),
            ),
            (
                "log_level",
                "LogLevel",
                TypeInfo(typing.Union[str, LogLevel]),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "pipelines_running_count",
                "PipelinesRunningCount",
                TypeInfo(int),
            ),
            (
                "role_arn",
                "RoleArn",
                TypeInfo(str),
            ),
            (
                "state",
                "State",
                TypeInfo(typing.Union[str, ChannelState]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unique arn of the channel.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of destinations of the channel. For UDP outputs, there is one
    # destination per output. For other types (HLS, for example), there is one
    # destination per packager.
    destinations: typing.List["OutputDestination"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The endpoints where outgoing connections initiate from
    egress_endpoints: typing.List["ChannelEgressEndpoint"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Placeholder documentation for EncoderSettings
    encoder_settings: "EncoderSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unique id of the channel.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # List of input attachments for channel.
    input_attachments: typing.List["InputAttachment"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Placeholder documentation for InputSpecification
    input_specification: "InputSpecification" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The log level being written to CloudWatch Logs.
    log_level: typing.Union[str, "LogLevel"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the channel. (user-mutable)
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of currently healthy pipelines.
    pipelines_running_count: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the role assumed when running the
    # Channel.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Placeholder documentation for ChannelState
    state: typing.Union[str, "ChannelState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class TeletextDestinationSettings(ShapeBase):
    """
    Placeholder documentation for TeletextDestinationSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class TeletextSourceSettings(ShapeBase):
    """
    Placeholder documentation for TeletextSourceSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "page_number",
                "PageNumber",
                TypeInfo(str),
            ),
        ]

    # Specifies the teletext page number within the data stream from which to
    # extract captions. Range of 0x100 (256) to 0x8FF (2303). Unused for
    # passthrough. Should be specified as a hexadecimal string with no "0x"
    # prefix.
    page_number: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TimecodeConfig(ShapeBase):
    """
    Placeholder documentation for TimecodeConfig
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "source",
                "Source",
                TypeInfo(typing.Union[str, TimecodeConfigSource]),
            ),
            (
                "sync_threshold",
                "SyncThreshold",
                TypeInfo(int),
            ),
        ]

    # Identifies the source for the timecode that will be associated with the
    # events outputs. -Embedded (embedded): Initialize the output timecode with
    # timecode from the the source. If no embedded timecode is detected in the
    # source, the system falls back to using "Start at 0" (zerobased). -System
    # Clock (systemclock): Use the UTC time. -Start at 0 (zerobased): The time of
    # the first frame of the event will be 00:00:00:00.
    source: typing.Union[str, "TimecodeConfigSource"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Threshold in frames beyond which output timecode is resynchronized to the
    # input timecode. Discrepancies below this threshold are permitted to avoid
    # unnecessary discontinuities in the output timecode. No timecode sync when
    # this is not specified.
    sync_threshold: int = dataclasses.field(default=ShapeBase.NOT_SET, )


class TimecodeConfigSource(str):
    """
    Placeholder documentation for TimecodeConfigSource
    """
    EMBEDDED = "EMBEDDED"
    SYSTEMCLOCK = "SYSTEMCLOCK"
    ZEROBASED = "ZEROBASED"


@dataclasses.dataclass
class TooManyRequestsException(ShapeBase):
    """
    Placeholder documentation for TooManyRequestsException
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    # Placeholder documentation for __string
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TtmlDestinationSettings(ShapeBase):
    """
    Placeholder documentation for TtmlDestinationSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "style_control",
                "StyleControl",
                TypeInfo(typing.Union[str, TtmlDestinationStyleControl]),
            ),
        ]

    # When set to passthrough, passes through style and position information from
    # a TTML-like input source (TTML, SMPTE-TT, CFF-TT) to the CFF-TT output or
    # TTML output.
    style_control: typing.Union[str, "TtmlDestinationStyleControl"
                               ] = dataclasses.field(
                                   default=ShapeBase.NOT_SET,
                               )


class TtmlDestinationStyleControl(str):
    """
    Placeholder documentation for TtmlDestinationStyleControl
    """
    PASSTHROUGH = "PASSTHROUGH"
    USE_CONFIGURED = "USE_CONFIGURED"


@dataclasses.dataclass
class UdpContainerSettings(ShapeBase):
    """
    Placeholder documentation for UdpContainerSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "m2ts_settings",
                "M2tsSettings",
                TypeInfo(M2tsSettings),
            ),
        ]

    # Placeholder documentation for M2tsSettings
    m2ts_settings: "M2tsSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UdpGroupSettings(ShapeBase):
    """
    Placeholder documentation for UdpGroupSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "input_loss_action",
                "InputLossAction",
                TypeInfo(typing.Union[str, InputLossActionForUdpOut]),
            ),
            (
                "timed_metadata_id3_frame",
                "TimedMetadataId3Frame",
                TypeInfo(typing.Union[str, UdpTimedMetadataId3Frame]),
            ),
            (
                "timed_metadata_id3_period",
                "TimedMetadataId3Period",
                TypeInfo(int),
            ),
        ]

    # Specifies behavior of last resort when input video is lost, and no more
    # backup inputs are available. When dropTs is selected the entire transport
    # stream will stop being emitted. When dropProgram is selected the program
    # can be dropped from the transport stream (and replaced with null packets to
    # meet the TS bitrate requirement). Or, when emitProgram is chosen the
    # transport stream will continue to be produced normally with repeat frames,
    # black frames, or slate frames substituted for the absent input video.
    input_loss_action: typing.Union[str, "InputLossActionForUdpOut"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # Indicates ID3 frame that has the timecode.
    timed_metadata_id3_frame: typing.Union[str, "UdpTimedMetadataId3Frame"
                                          ] = dataclasses.field(
                                              default=ShapeBase.NOT_SET,
                                          )

    # Timed Metadata interval in seconds.
    timed_metadata_id3_period: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UdpOutputSettings(ShapeBase):
    """
    Placeholder documentation for UdpOutputSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "container_settings",
                "ContainerSettings",
                TypeInfo(UdpContainerSettings),
            ),
            (
                "destination",
                "Destination",
                TypeInfo(OutputLocationRef),
            ),
            (
                "buffer_msec",
                "BufferMsec",
                TypeInfo(int),
            ),
            (
                "fec_output_settings",
                "FecOutputSettings",
                TypeInfo(FecOutputSettings),
            ),
        ]

    # Placeholder documentation for UdpContainerSettings
    container_settings: "UdpContainerSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Destination address and port number for RTP or UDP packets. Can be unicast
    # or multicast RTP or UDP (eg. rtp://239.10.10.10:5001 or
    # udp://10.100.100.100:5002).
    destination: "OutputLocationRef" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # UDP output buffering in milliseconds. Larger values increase latency
    # through the transcoder but simultaneously assist the transcoder in
    # maintaining a constant, low-jitter UDP/RTP output while accommodating clock
    # recovery, input switching, input disruptions, picture reordering, etc.
    buffer_msec: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Settings for enabling and adjusting Forward Error Correction on UDP
    # outputs.
    fec_output_settings: "FecOutputSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class UdpTimedMetadataId3Frame(str):
    """
    Placeholder documentation for UdpTimedMetadataId3Frame
    """
    NONE = "NONE"
    PRIV = "PRIV"
    TDRL = "TDRL"


@dataclasses.dataclass
class UnprocessableEntityException(ShapeBase):
    """
    Placeholder documentation for UnprocessableEntityException
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
                "validation_errors",
                "ValidationErrors",
                TypeInfo(typing.List[ValidationError]),
            ),
        ]

    # Placeholder documentation for __string
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A collection of validation error responses.
    validation_errors: typing.List["ValidationError"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateChannel(ShapeBase):
    """
    Placeholder documentation for UpdateChannel
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "destinations",
                "Destinations",
                TypeInfo(typing.List[OutputDestination]),
            ),
            (
                "encoder_settings",
                "EncoderSettings",
                TypeInfo(EncoderSettings),
            ),
            (
                "input_attachments",
                "InputAttachments",
                TypeInfo(typing.List[InputAttachment]),
            ),
            (
                "input_specification",
                "InputSpecification",
                TypeInfo(InputSpecification),
            ),
            (
                "log_level",
                "LogLevel",
                TypeInfo(typing.Union[str, LogLevel]),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "role_arn",
                "RoleArn",
                TypeInfo(str),
            ),
        ]

    # A list of output destinations for this channel.
    destinations: typing.List["OutputDestination"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The encoder settings for this channel.
    encoder_settings: "EncoderSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Placeholder documentation for __listOfInputAttachment
    input_attachments: typing.List["InputAttachment"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specification of input for this channel (max. bitrate, resolution, codec,
    # etc.)
    input_specification: "InputSpecification" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The log level to write to CloudWatch Logs.
    log_level: typing.Union[str, "LogLevel"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the channel.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional Amazon Resource Name (ARN) of the role to assume when running
    # the Channel. If you do not specify this on an update call but the role was
    # previously set that role will be removed.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateChannelRequest(ShapeBase):
    """
    A request to update a channel.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "channel_id",
                "ChannelId",
                TypeInfo(str),
            ),
            (
                "destinations",
                "Destinations",
                TypeInfo(typing.List[OutputDestination]),
            ),
            (
                "encoder_settings",
                "EncoderSettings",
                TypeInfo(EncoderSettings),
            ),
            (
                "input_attachments",
                "InputAttachments",
                TypeInfo(typing.List[InputAttachment]),
            ),
            (
                "input_specification",
                "InputSpecification",
                TypeInfo(InputSpecification),
            ),
            (
                "log_level",
                "LogLevel",
                TypeInfo(typing.Union[str, LogLevel]),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "role_arn",
                "RoleArn",
                TypeInfo(str),
            ),
        ]

    # channel ID
    channel_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of output destinations for this channel.
    destinations: typing.List["OutputDestination"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The encoder settings for this channel.
    encoder_settings: "EncoderSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Placeholder documentation for __listOfInputAttachment
    input_attachments: typing.List["InputAttachment"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specification of input for this channel (max. bitrate, resolution, codec,
    # etc.)
    input_specification: "InputSpecification" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The log level to write to CloudWatch Logs.
    log_level: typing.Union[str, "LogLevel"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the channel.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional Amazon Resource Name (ARN) of the role to assume when running
    # the Channel. If you do not specify this on an update call but the role was
    # previously set that role will be removed.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateChannelResponse(OutputShapeBase):
    """
    Placeholder documentation for UpdateChannelResponse
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
                "channel",
                "Channel",
                TypeInfo(Channel),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Placeholder documentation for Channel
    channel: "Channel" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateChannelResultModel(ShapeBase):
    """
    The updated channel's description.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "channel",
                "Channel",
                TypeInfo(Channel),
            ),
        ]

    # Placeholder documentation for Channel
    channel: "Channel" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateInput(ShapeBase):
    """
    Placeholder documentation for UpdateInput
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "destinations",
                "Destinations",
                TypeInfo(typing.List[InputDestinationRequest]),
            ),
            (
                "input_security_groups",
                "InputSecurityGroups",
                TypeInfo(typing.List[str]),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "sources",
                "Sources",
                TypeInfo(typing.List[InputSourceRequest]),
            ),
        ]

    # Destination settings for PUSH type inputs.
    destinations: typing.List["InputDestinationRequest"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of security groups referenced by IDs to attach to the input.
    input_security_groups: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Name of the input.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The source URLs for a PULL-type input. Every PULL type input needs exactly
    # two source URLs for redundancy. Only specify sources for PULL type Inputs.
    # Leave Destinations empty.
    sources: typing.List["InputSourceRequest"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateInputRequest(ShapeBase):
    """
    A request to update an input.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "input_id",
                "InputId",
                TypeInfo(str),
            ),
            (
                "destinations",
                "Destinations",
                TypeInfo(typing.List[InputDestinationRequest]),
            ),
            (
                "input_security_groups",
                "InputSecurityGroups",
                TypeInfo(typing.List[str]),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "sources",
                "Sources",
                TypeInfo(typing.List[InputSourceRequest]),
            ),
        ]

    # Unique ID of the input.
    input_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Destination settings for PUSH type inputs.
    destinations: typing.List["InputDestinationRequest"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of security groups referenced by IDs to attach to the input.
    input_security_groups: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Name of the input.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The source URLs for a PULL-type input. Every PULL type input needs exactly
    # two source URLs for redundancy. Only specify sources for PULL type Inputs.
    # Leave Destinations empty.
    sources: typing.List["InputSourceRequest"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateInputResponse(OutputShapeBase):
    """
    Placeholder documentation for UpdateInputResponse
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
                "input",
                "Input",
                TypeInfo(Input),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Placeholder documentation for Input
    input: "Input" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateInputResultModel(ShapeBase):
    """
    Placeholder documentation for UpdateInputResultModel
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "input",
                "Input",
                TypeInfo(Input),
            ),
        ]

    # Placeholder documentation for Input
    input: "Input" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateInputSecurityGroupRequest(ShapeBase):
    """
    The request to update some combination of the Input Security Group name and the
    IPv4 CIDRs the Input Security Group should allow.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "input_security_group_id",
                "InputSecurityGroupId",
                TypeInfo(str),
            ),
            (
                "whitelist_rules",
                "WhitelistRules",
                TypeInfo(typing.List[InputWhitelistRuleCidr]),
            ),
        ]

    # The id of the Input Security Group to update.
    input_security_group_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # List of IPv4 CIDR addresses to whitelist
    whitelist_rules: typing.List["InputWhitelistRuleCidr"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateInputSecurityGroupResponse(OutputShapeBase):
    """
    Placeholder documentation for UpdateInputSecurityGroupResponse
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
                "security_group",
                "SecurityGroup",
                TypeInfo(InputSecurityGroup),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An Input Security Group
    security_group: "InputSecurityGroup" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateInputSecurityGroupResultModel(ShapeBase):
    """
    Placeholder documentation for UpdateInputSecurityGroupResultModel
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "security_group",
                "SecurityGroup",
                TypeInfo(InputSecurityGroup),
            ),
        ]

    # An Input Security Group
    security_group: "InputSecurityGroup" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ValidationError(ShapeBase):
    """
    Placeholder documentation for ValidationError
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "element_path",
                "ElementPath",
                TypeInfo(str),
            ),
            (
                "error_message",
                "ErrorMessage",
                TypeInfo(str),
            ),
        ]

    # Placeholder documentation for __string
    element_path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Placeholder documentation for __string
    error_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class VideoCodecSettings(ShapeBase):
    """
    Placeholder documentation for VideoCodecSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "h264_settings",
                "H264Settings",
                TypeInfo(H264Settings),
            ),
        ]

    # Placeholder documentation for H264Settings
    h264_settings: "H264Settings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class VideoDescription(ShapeBase):
    """
    Video settings for this stream.
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
                "codec_settings",
                "CodecSettings",
                TypeInfo(VideoCodecSettings),
            ),
            (
                "height",
                "Height",
                TypeInfo(int),
            ),
            (
                "respond_to_afd",
                "RespondToAfd",
                TypeInfo(typing.Union[str, VideoDescriptionRespondToAfd]),
            ),
            (
                "scaling_behavior",
                "ScalingBehavior",
                TypeInfo(typing.Union[str, VideoDescriptionScalingBehavior]),
            ),
            (
                "sharpness",
                "Sharpness",
                TypeInfo(int),
            ),
            (
                "width",
                "Width",
                TypeInfo(int),
            ),
        ]

    # The name of this VideoDescription. Outputs will use this name to uniquely
    # identify this Description. Description names should be unique within this
    # Live Event.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Video codec settings.
    codec_settings: "VideoCodecSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Output video height (in pixels). Leave blank to use source video height. If
    # left blank, width must also be unspecified.
    height: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates how to respond to the AFD values in the input stream. Setting to
    # "respond" causes input video to be clipped, depending on AFD value, input
    # display aspect ratio and output display aspect ratio.
    respond_to_afd: typing.Union[str, "VideoDescriptionRespondToAfd"
                                ] = dataclasses.field(
                                    default=ShapeBase.NOT_SET,
                                )

    # When set to "stretchToOutput", automatically configures the output position
    # to stretch the video to the specified output resolution. This option will
    # override any position value.
    scaling_behavior: typing.Union[str, "VideoDescriptionScalingBehavior"
                                  ] = dataclasses.field(
                                      default=ShapeBase.NOT_SET,
                                  )

    # Changes the width of the anti-alias filter kernel used for scaling. Only
    # applies if scaling is being performed and antiAlias is set to true. 0 is
    # the softest setting, 100 the sharpest, and 50 recommended for most content.
    sharpness: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Output video width (in pixels). Leave out to use source video width. If
    # left out, height must also be left out. Display aspect ratio is always
    # preserved by letterboxing or pillarboxing when necessary.
    width: int = dataclasses.field(default=ShapeBase.NOT_SET, )


class VideoDescriptionRespondToAfd(str):
    """
    Placeholder documentation for VideoDescriptionRespondToAfd
    """
    NONE = "NONE"
    PASSTHROUGH = "PASSTHROUGH"
    RESPOND = "RESPOND"


class VideoDescriptionScalingBehavior(str):
    """
    Placeholder documentation for VideoDescriptionScalingBehavior
    """
    DEFAULT = "DEFAULT"
    STRETCH_TO_OUTPUT = "STRETCH_TO_OUTPUT"


@dataclasses.dataclass
class VideoSelector(ShapeBase):
    """
    Specifies a particular video stream within an input source. An input may have
    only a single video selector.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "color_space",
                "ColorSpace",
                TypeInfo(typing.Union[str, VideoSelectorColorSpace]),
            ),
            (
                "color_space_usage",
                "ColorSpaceUsage",
                TypeInfo(typing.Union[str, VideoSelectorColorSpaceUsage]),
            ),
            (
                "selector_settings",
                "SelectorSettings",
                TypeInfo(VideoSelectorSettings),
            ),
        ]

    # Specifies the colorspace of an input. This setting works in tandem with
    # colorSpaceConversion to determine if any conversion will be performed.
    color_space: typing.Union[str, "VideoSelectorColorSpace"
                             ] = dataclasses.field(
                                 default=ShapeBase.NOT_SET,
                             )

    # Applies only if colorSpace is a value other than follow. This field
    # controls how the value in the colorSpace field will be used. fallback means
    # that when the input does include color space data, that data will be used,
    # but when the input has no color space data, the value in colorSpace will be
    # used. Choose fallback if your input is sometimes missing color space data,
    # but when it does have color space data, that data is correct. force means
    # to always use the value in colorSpace. Choose force if your input usually
    # has no color space data or might have unreliable color space data.
    color_space_usage: typing.Union[str, "VideoSelectorColorSpaceUsage"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # The video selector settings.
    selector_settings: "VideoSelectorSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class VideoSelectorColorSpace(str):
    """
    Placeholder documentation for VideoSelectorColorSpace
    """
    FOLLOW = "FOLLOW"
    REC_601 = "REC_601"
    REC_709 = "REC_709"


class VideoSelectorColorSpaceUsage(str):
    """
    Placeholder documentation for VideoSelectorColorSpaceUsage
    """
    FALLBACK = "FALLBACK"
    FORCE = "FORCE"


@dataclasses.dataclass
class VideoSelectorPid(ShapeBase):
    """
    Placeholder documentation for VideoSelectorPid
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "pid",
                "Pid",
                TypeInfo(int),
            ),
        ]

    # Selects a specific PID from within a video source.
    pid: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class VideoSelectorProgramId(ShapeBase):
    """
    Placeholder documentation for VideoSelectorProgramId
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "program_id",
                "ProgramId",
                TypeInfo(int),
            ),
        ]

    # Selects a specific program from within a multi-program transport stream. If
    # the program doesn't exist, the first program within the transport stream
    # will be selected by default.
    program_id: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class VideoSelectorSettings(ShapeBase):
    """
    Placeholder documentation for VideoSelectorSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "video_selector_pid",
                "VideoSelectorPid",
                TypeInfo(VideoSelectorPid),
            ),
            (
                "video_selector_program_id",
                "VideoSelectorProgramId",
                TypeInfo(VideoSelectorProgramId),
            ),
        ]

    # Placeholder documentation for VideoSelectorPid
    video_selector_pid: "VideoSelectorPid" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Placeholder documentation for VideoSelectorProgramId
    video_selector_program_id: "VideoSelectorProgramId" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class WebvttDestinationSettings(ShapeBase):
    """
    Placeholder documentation for WebvttDestinationSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []
