import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


class AacAudioDescriptionBroadcasterMix(str):
    """
    Choose BROADCASTER_MIXED_AD when the input contains pre-mixed main audio + audio
    description (AD) as a stereo pair. The value for AudioType will be set to 3,
    which signals to downstream systems that this stream contains "broadcaster mixed
    AD". Note that the input received by the encoder must contain pre-mixed audio;
    the encoder does not perform the mixing. When you choose BROADCASTER_MIXED_AD,
    the encoder ignores any values you provide in AudioType and
    FollowInputAudioType. Choose NORMAL when the input does not contain pre-mixed
    audio + audio description (AD). In this case, the encoder will use any values
    you provide for AudioType and FollowInputAudioType.
    """
    BROADCASTER_MIXED_AD = "BROADCASTER_MIXED_AD"
    NORMAL = "NORMAL"


class AacCodecProfile(str):
    """
    AAC Profile.
    """
    LC = "LC"
    HEV1 = "HEV1"
    HEV2 = "HEV2"


class AacCodingMode(str):
    """
    Mono (Audio Description), Mono, Stereo, or 5.1 channel layout. Valid values
    depend on rate control mode and profile. "1.0 - Audio Description (Receiver
    Mix)" setting receives a stereo description plus control track and emits a mono
    AAC encode of the description track, with control data emitted in the PES header
    as per ETSI TS 101 154 Annex E.
    """
    AD_RECEIVER_MIX = "AD_RECEIVER_MIX"
    CODING_MODE_1_0 = "CODING_MODE_1_0"
    CODING_MODE_1_1 = "CODING_MODE_1_1"
    CODING_MODE_2_0 = "CODING_MODE_2_0"
    CODING_MODE_5_1 = "CODING_MODE_5_1"


class AacRateControlMode(str):
    """
    Rate Control Mode.
    """
    CBR = "CBR"
    VBR = "VBR"


class AacRawFormat(str):
    """
    Enables LATM/LOAS AAC output. Note that if you use LATM/LOAS AAC in an output,
    you must choose "No container" for the output container.
    """
    LATM_LOAS = "LATM_LOAS"
    NONE = "NONE"


@dataclasses.dataclass
class AacSettings(ShapeBase):
    """
    Required when you set (Codec) under (AudioDescriptions)>(CodecSettings) to the
    value AAC. The service accepts one of two mutually exclusive groups of AAC
    settings--VBR and CBR. To select one of these modes, set the value of Bitrate
    control mode (rateControlMode) to "VBR" or "CBR". In VBR mode, you control the
    audio quality with the setting VBR quality (vbrQuality). In CBR mode, you use
    the setting Bitrate (bitrate). Defaults and valid values depend on the rate
    control mode.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "audio_description_broadcaster_mix",
                "AudioDescriptionBroadcasterMix",
                TypeInfo(typing.Union[str, AacAudioDescriptionBroadcasterMix]),
            ),
            (
                "bitrate",
                "Bitrate",
                TypeInfo(int),
            ),
            (
                "codec_profile",
                "CodecProfile",
                TypeInfo(typing.Union[str, AacCodecProfile]),
            ),
            (
                "coding_mode",
                "CodingMode",
                TypeInfo(typing.Union[str, AacCodingMode]),
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
                TypeInfo(int),
            ),
            (
                "specification",
                "Specification",
                TypeInfo(typing.Union[str, AacSpecification]),
            ),
            (
                "vbr_quality",
                "VbrQuality",
                TypeInfo(typing.Union[str, AacVbrQuality]),
            ),
        ]

    # Choose BROADCASTER_MIXED_AD when the input contains pre-mixed main audio +
    # audio description (AD) as a stereo pair. The value for AudioType will be
    # set to 3, which signals to downstream systems that this stream contains
    # "broadcaster mixed AD". Note that the input received by the encoder must
    # contain pre-mixed audio; the encoder does not perform the mixing. When you
    # choose BROADCASTER_MIXED_AD, the encoder ignores any values you provide in
    # AudioType and FollowInputAudioType. Choose NORMAL when the input does not
    # contain pre-mixed audio + audio description (AD). In this case, the encoder
    # will use any values you provide for AudioType and FollowInputAudioType.
    audio_description_broadcaster_mix: typing.Union[
        str, "AacAudioDescriptionBroadcasterMix"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # Average bitrate in bits/second. Defaults and valid values depend on rate
    # control mode and profile.
    bitrate: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # AAC Profile.
    codec_profile: typing.Union[str, "AacCodecProfile"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Mono (Audio Description), Mono, Stereo, or 5.1 channel layout. Valid values
    # depend on rate control mode and profile. "1.0 - Audio Description (Receiver
    # Mix)" setting receives a stereo description plus control track and emits a
    # mono AAC encode of the description track, with control data emitted in the
    # PES header as per ETSI TS 101 154 Annex E.
    coding_mode: typing.Union[str, "AacCodingMode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Rate Control Mode.
    rate_control_mode: typing.Union[str, "AacRateControlMode"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # Enables LATM/LOAS AAC output. Note that if you use LATM/LOAS AAC in an
    # output, you must choose "No container" for the output container.
    raw_format: typing.Union[str, "AacRawFormat"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Sample rate in Hz. Valid values depend on rate control mode and profile.
    sample_rate: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use MPEG-2 AAC instead of MPEG-4 AAC audio for raw or MPEG-2 Transport
    # Stream containers.
    specification: typing.Union[str, "AacSpecification"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # VBR Quality Level - Only used if rate_control_mode is VBR.
    vbr_quality: typing.Union[str, "AacVbrQuality"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class AacSpecification(str):
    """
    Use MPEG-2 AAC instead of MPEG-4 AAC audio for raw or MPEG-2 Transport Stream
    containers.
    """
    MPEG2 = "MPEG2"
    MPEG4 = "MPEG4"


class AacVbrQuality(str):
    """
    VBR Quality Level - Only used if rate_control_mode is VBR.
    """
    LOW = "LOW"
    MEDIUM_LOW = "MEDIUM_LOW"
    MEDIUM_HIGH = "MEDIUM_HIGH"
    HIGH = "HIGH"


class Ac3BitstreamMode(str):
    """
    Specifies the "Bitstream Mode" (bsmod) for the emitted AC-3 stream. See ATSC
    A/52-2012 for background on these values.
    """
    COMPLETE_MAIN = "COMPLETE_MAIN"
    COMMENTARY = "COMMENTARY"
    DIALOGUE = "DIALOGUE"
    EMERGENCY = "EMERGENCY"
    HEARING_IMPAIRED = "HEARING_IMPAIRED"
    MUSIC_AND_EFFECTS = "MUSIC_AND_EFFECTS"
    VISUALLY_IMPAIRED = "VISUALLY_IMPAIRED"
    VOICE_OVER = "VOICE_OVER"


class Ac3CodingMode(str):
    """
    Dolby Digital coding mode. Determines number of channels.
    """
    CODING_MODE_1_0 = "CODING_MODE_1_0"
    CODING_MODE_1_1 = "CODING_MODE_1_1"
    CODING_MODE_2_0 = "CODING_MODE_2_0"
    CODING_MODE_3_2_LFE = "CODING_MODE_3_2_LFE"


class Ac3DynamicRangeCompressionProfile(str):
    """
    If set to FILM_STANDARD, adds dynamic range compression signaling to the output
    bitstream as defined in the Dolby Digital specification.
    """
    FILM_STANDARD = "FILM_STANDARD"
    NONE = "NONE"


class Ac3LfeFilter(str):
    """
    Applies a 120Hz lowpass filter to the LFE channel prior to encoding. Only valid
    with 3_2_LFE coding mode.
    """
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class Ac3MetadataControl(str):
    """
    When set to FOLLOW_INPUT, encoder metadata will be sourced from the DD, DD+, or
    DolbyE decoder that supplied this audio data. If audio was not supplied from one
    of these streams, then the static metadata settings will be used.
    """
    FOLLOW_INPUT = "FOLLOW_INPUT"
    USE_CONFIGURED = "USE_CONFIGURED"


@dataclasses.dataclass
class Ac3Settings(ShapeBase):
    """
    Required when you set (Codec) under (AudioDescriptions)>(CodecSettings) to the
    value AC3.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bitrate",
                "Bitrate",
                TypeInfo(int),
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
                "dynamic_range_compression_profile",
                "DynamicRangeCompressionProfile",
                TypeInfo(typing.Union[str, Ac3DynamicRangeCompressionProfile]),
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
            (
                "sample_rate",
                "SampleRate",
                TypeInfo(int),
            ),
        ]

    # Average bitrate in bits/second. Valid bitrates depend on the coding mode.
    bitrate: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the "Bitstream Mode" (bsmod) for the emitted AC-3 stream. See
    # ATSC A/52-2012 for background on these values.
    bitstream_mode: typing.Union[str, "Ac3BitstreamMode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Dolby Digital coding mode. Determines number of channels.
    coding_mode: typing.Union[str, "Ac3CodingMode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Sets the dialnorm for the output. If blank and input audio is Dolby
    # Digital, dialnorm will be passed through.
    dialnorm: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If set to FILM_STANDARD, adds dynamic range compression signaling to the
    # output bitstream as defined in the Dolby Digital specification.
    dynamic_range_compression_profile: typing.Union[
        str, "Ac3DynamicRangeCompressionProfile"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # Applies a 120Hz lowpass filter to the LFE channel prior to encoding. Only
    # valid with 3_2_LFE coding mode.
    lfe_filter: typing.Union[str, "Ac3LfeFilter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When set to FOLLOW_INPUT, encoder metadata will be sourced from the DD,
    # DD+, or DolbyE decoder that supplied this audio data. If audio was not
    # supplied from one of these streams, then the static metadata settings will
    # be used.
    metadata_control: typing.Union[str, "Ac3MetadataControl"
                                  ] = dataclasses.field(
                                      default=ShapeBase.NOT_SET,
                                  )

    # Sample rate in hz. Sample rate is always 48000.
    sample_rate: int = dataclasses.field(default=ShapeBase.NOT_SET, )


class AfdSignaling(str):
    """
    This setting only applies to H.264 and MPEG2 outputs. Use Insert AFD signaling
    (AfdSignaling) to specify whether the service includes AFD values in the output
    video data and what those values are. * Choose None to remove all AFD values
    from this output. * Choose Fixed to ignore input AFD values and instead encode
    the value specified in the job. * Choose Auto to calculate output AFD values
    based on the input AFD scaler data.
    """
    NONE = "NONE"
    AUTO = "AUTO"
    FIXED = "FIXED"


@dataclasses.dataclass
class AiffSettings(ShapeBase):
    """
    Required when you set (Codec) under (AudioDescriptions)>(CodecSettings) to the
    value AIFF.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bit_depth",
                "BitDepth",
                TypeInfo(int),
            ),
            (
                "channels",
                "Channels",
                TypeInfo(int),
            ),
            (
                "sample_rate",
                "SampleRate",
                TypeInfo(int),
            ),
        ]

    # Specify Bit depth (BitDepth), in bits per sample, to choose the encoding
    # quality for this audio track.
    bit_depth: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Set Channels to specify the number of channels in this output audio track.
    # Choosing Mono in the console will give you 1 output channel; choosing
    # Stereo will give you 2. In the API, valid values are 1 and 2.
    channels: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Sample rate in hz.
    sample_rate: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AncillarySourceSettings(ShapeBase):
    """
    Settings for ancillary captions source.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "source_ancillary_channel_number",
                "SourceAncillaryChannelNumber",
                TypeInfo(int),
            ),
        ]

    # Specifies the 608 channel number in the ancillary data track from which to
    # extract captions. Unused for passthrough.
    source_ancillary_channel_number: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class AntiAlias(str):
    """
    Enable Anti-alias (AntiAlias) to enhance sharp edges in video output when your
    input resolution is much larger than your output resolution. Default is enabled.
    """
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class AudioCodec(str):
    """
    Type of Audio codec.
    """
    AAC = "AAC"
    MP2 = "MP2"
    WAV = "WAV"
    AIFF = "AIFF"
    AC3 = "AC3"
    EAC3 = "EAC3"
    PASSTHROUGH = "PASSTHROUGH"


@dataclasses.dataclass
class AudioCodecSettings(ShapeBase):
    """
    Audio codec settings (CodecSettings) under (AudioDescriptions) contains the
    group of settings related to audio encoding. The settings in this group vary
    depending on the value you choose for Audio codec (Codec). For each codec enum
    you choose, define the corresponding settings object. The following lists the
    codec enum, settings object pairs. * AAC, AacSettings * MP2, Mp2Settings * WAV,
    WavSettings * AIFF, AiffSettings * AC3, Ac3Settings * EAC3, Eac3Settings
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
                "aiff_settings",
                "AiffSettings",
                TypeInfo(AiffSettings),
            ),
            (
                "codec",
                "Codec",
                TypeInfo(typing.Union[str, AudioCodec]),
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
                "wav_settings",
                "WavSettings",
                TypeInfo(WavSettings),
            ),
        ]

    # Required when you set (Codec) under (AudioDescriptions)>(CodecSettings) to
    # the value AAC. The service accepts one of two mutually exclusive groups of
    # AAC settings--VBR and CBR. To select one of these modes, set the value of
    # Bitrate control mode (rateControlMode) to "VBR" or "CBR". In VBR mode, you
    # control the audio quality with the setting VBR quality (vbrQuality). In CBR
    # mode, you use the setting Bitrate (bitrate). Defaults and valid values
    # depend on the rate control mode.
    aac_settings: "AacSettings" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Required when you set (Codec) under (AudioDescriptions)>(CodecSettings) to
    # the value AC3.
    ac3_settings: "Ac3Settings" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Required when you set (Codec) under (AudioDescriptions)>(CodecSettings) to
    # the value AIFF.
    aiff_settings: "AiffSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Type of Audio codec.
    codec: typing.Union[str, "AudioCodec"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Required when you set (Codec) under (AudioDescriptions)>(CodecSettings) to
    # the value EAC3.
    eac3_settings: "Eac3Settings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Required when you set (Codec) under (AudioDescriptions)>(CodecSettings) to
    # the value MP2.
    mp2_settings: "Mp2Settings" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Required when you set (Codec) under (AudioDescriptions)>(CodecSettings) to
    # the value WAV.
    wav_settings: "WavSettings" = dataclasses.field(default=ShapeBase.NOT_SET, )


class AudioDefaultSelection(str):
    """
    Enable this setting on one audio selector to set it as the default for the job.
    The service uses this default for outputs where it can't find the specified
    input audio. If you don't set a default, those outputs have no audio.
    """
    DEFAULT = "DEFAULT"
    NOT_DEFAULT = "NOT_DEFAULT"


@dataclasses.dataclass
class AudioDescription(ShapeBase):
    """
    Description of audio output
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "audio_normalization_settings",
                "AudioNormalizationSettings",
                TypeInfo(AudioNormalizationSettings),
            ),
            (
                "audio_source_name",
                "AudioSourceName",
                TypeInfo(str),
            ),
            (
                "audio_type",
                "AudioType",
                TypeInfo(int),
            ),
            (
                "audio_type_control",
                "AudioTypeControl",
                TypeInfo(typing.Union[str, AudioTypeControl]),
            ),
            (
                "codec_settings",
                "CodecSettings",
                TypeInfo(AudioCodecSettings),
            ),
            (
                "custom_language_code",
                "CustomLanguageCode",
                TypeInfo(str),
            ),
            (
                "language_code",
                "LanguageCode",
                TypeInfo(typing.Union[str, LanguageCode]),
            ),
            (
                "language_code_control",
                "LanguageCodeControl",
                TypeInfo(typing.Union[str, AudioLanguageCodeControl]),
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

    # Advanced audio normalization settings.
    audio_normalization_settings: "AudioNormalizationSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies which audio data to use from each input. In the simplest case,
    # specify an "Audio Selector":#inputs-audio_selector by name based on its
    # order within each input. For example if you specify "Audio Selector 3",
    # then the third audio selector will be used from each input. If an input
    # does not have an "Audio Selector 3", then the audio selector marked as
    # "default" in that input will be used. If there is no audio selector marked
    # as "default", silence will be inserted for the duration of that input.
    # Alternatively, an "Audio Selector Group":#inputs-audio_selector_group name
    # may be specified, with similar default/silence behavior. If no
    # audio_source_name is specified, then "Audio Selector 1" will be chosen
    # automatically.
    audio_source_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Applies only if Follow Input Audio Type is unchecked (false). A number
    # between 0 and 255. The following are defined in ISO-IEC 13818-1: 0 =
    # Undefined, 1 = Clean Effects, 2 = Hearing Impaired, 3 = Visually Impaired
    # Commentary, 4-255 = Reserved.
    audio_type: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When set to FOLLOW_INPUT, if the input contains an ISO 639 audio_type, then
    # that value is passed through to the output. If the input contains no ISO
    # 639 audio_type, the value in Audio Type is included in the output.
    # Otherwise the value in Audio Type is included in the output. Note that this
    # field and audioType are both ignored if audioDescriptionBroadcasterMix is
    # set to BROADCASTER_MIXED_AD.
    audio_type_control: typing.Union[str, "AudioTypeControl"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )

    # Audio codec settings (CodecSettings) under (AudioDescriptions) contains the
    # group of settings related to audio encoding. The settings in this group
    # vary depending on the value you choose for Audio codec (Codec). For each
    # codec enum you choose, define the corresponding settings object. The
    # following lists the codec enum, settings object pairs. * AAC, AacSettings *
    # MP2, Mp2Settings * WAV, WavSettings * AIFF, AiffSettings * AC3, Ac3Settings
    # * EAC3, Eac3Settings
    codec_settings: "AudioCodecSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specify the language for this audio output track, using the ISO 639-2 or
    # ISO 639-3 three-letter language code. The language specified will be used
    # when 'Follow Input Language Code' is not selected or when 'Follow Input
    # Language Code' is selected but there is no ISO 639 language code specified
    # by the input.
    custom_language_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates the language of the audio output track. The ISO 639 language
    # specified in the 'Language Code' drop down will be used when 'Follow Input
    # Language Code' is not selected or when 'Follow Input Language Code' is
    # selected but there is no ISO 639 language code specified by the input.
    language_code: typing.Union[str, "LanguageCode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Choosing FOLLOW_INPUT will cause the ISO 639 language code of the output to
    # follow the ISO 639 language code of the input. The language specified for
    # languageCode' will be used when USE_CONFIGURED is selected or when
    # FOLLOW_INPUT is selected but there is no ISO 639 language code specified by
    # the input.
    language_code_control: typing.Union[str, "AudioLanguageCodeControl"
                                       ] = dataclasses.field(
                                           default=ShapeBase.NOT_SET,
                                       )

    # Advanced audio remixing settings.
    remix_settings: "RemixSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Used for MS Smooth and Apple HLS outputs. Indicates the name displayed by
    # the player (eg. English, or Director Commentary). Alphanumeric characters,
    # spaces, and underscore are legal.
    stream_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class AudioLanguageCodeControl(str):
    """
    Choosing FOLLOW_INPUT will cause the ISO 639 language code of the output to
    follow the ISO 639 language code of the input. The language specified for
    languageCode' will be used when USE_CONFIGURED is selected or when FOLLOW_INPUT
    is selected but there is no ISO 639 language code specified by the input.
    """
    FOLLOW_INPUT = "FOLLOW_INPUT"
    USE_CONFIGURED = "USE_CONFIGURED"


class AudioNormalizationAlgorithm(str):
    """
    Audio normalization algorithm to use. 1770-1 conforms to the CALM Act
    specification, 1770-2 conforms to the EBU R-128 specification.
    """
    ITU_BS_1770_1 = "ITU_BS_1770_1"
    ITU_BS_1770_2 = "ITU_BS_1770_2"


class AudioNormalizationAlgorithmControl(str):
    """
    When enabled the output audio is corrected using the chosen algorithm. If
    disabled, the audio will be measured but not adjusted.
    """
    CORRECT_AUDIO = "CORRECT_AUDIO"
    MEASURE_ONLY = "MEASURE_ONLY"


class AudioNormalizationLoudnessLogging(str):
    """
    If set to LOG, log each output's audio track loudness to a CSV file.
    """
    LOG = "LOG"
    DONT_LOG = "DONT_LOG"


class AudioNormalizationPeakCalculation(str):
    """
    If set to TRUE_PEAK, calculate and log the TruePeak for each output's audio
    track loudness.
    """
    TRUE_PEAK = "TRUE_PEAK"
    NONE = "NONE"


@dataclasses.dataclass
class AudioNormalizationSettings(ShapeBase):
    """
    Advanced audio normalization settings.
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
                "correction_gate_level",
                "CorrectionGateLevel",
                TypeInfo(int),
            ),
            (
                "loudness_logging",
                "LoudnessLogging",
                TypeInfo(typing.Union[str, AudioNormalizationLoudnessLogging]),
            ),
            (
                "peak_calculation",
                "PeakCalculation",
                TypeInfo(typing.Union[str, AudioNormalizationPeakCalculation]),
            ),
            (
                "target_lkfs",
                "TargetLkfs",
                TypeInfo(float),
            ),
        ]

    # Audio normalization algorithm to use. 1770-1 conforms to the CALM Act
    # specification, 1770-2 conforms to the EBU R-128 specification.
    algorithm: typing.Union[str, "AudioNormalizationAlgorithm"
                           ] = dataclasses.field(
                               default=ShapeBase.NOT_SET,
                           )

    # When enabled the output audio is corrected using the chosen algorithm. If
    # disabled, the audio will be measured but not adjusted.
    algorithm_control: typing.Union[str, "AudioNormalizationAlgorithmControl"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # Content measuring above this level will be corrected to the target level.
    # Content measuring below this level will not be corrected. Gating only
    # applies when not using real_time_correction.
    correction_gate_level: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If set to LOG, log each output's audio track loudness to a CSV file.
    loudness_logging: typing.Union[str, "AudioNormalizationLoudnessLogging"
                                  ] = dataclasses.field(
                                      default=ShapeBase.NOT_SET,
                                  )

    # If set to TRUE_PEAK, calculate and log the TruePeak for each output's audio
    # track loudness.
    peak_calculation: typing.Union[str, "AudioNormalizationPeakCalculation"
                                  ] = dataclasses.field(
                                      default=ShapeBase.NOT_SET,
                                  )

    # Target LKFS(loudness) to adjust volume to. If no value is entered, a
    # default value will be used according to the chosen algorithm. The CALM Act
    # (1770-1) recommends a target of -24 LKFS. The EBU R-128 specification
    # (1770-2) recommends a target of -23 LKFS.
    target_lkfs: float = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AudioSelector(ShapeBase):
    """
    Selector for Audio
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "custom_language_code",
                "CustomLanguageCode",
                TypeInfo(str),
            ),
            (
                "default_selection",
                "DefaultSelection",
                TypeInfo(typing.Union[str, AudioDefaultSelection]),
            ),
            (
                "external_audio_file_input",
                "ExternalAudioFileInput",
                TypeInfo(str),
            ),
            (
                "language_code",
                "LanguageCode",
                TypeInfo(typing.Union[str, LanguageCode]),
            ),
            (
                "offset",
                "Offset",
                TypeInfo(int),
            ),
            (
                "pids",
                "Pids",
                TypeInfo(typing.List[int]),
            ),
            (
                "program_selection",
                "ProgramSelection",
                TypeInfo(int),
            ),
            (
                "remix_settings",
                "RemixSettings",
                TypeInfo(RemixSettings),
            ),
            (
                "selector_type",
                "SelectorType",
                TypeInfo(typing.Union[str, AudioSelectorType]),
            ),
            (
                "tracks",
                "Tracks",
                TypeInfo(typing.List[int]),
            ),
        ]

    # Selects a specific language code from within an audio source, using the ISO
    # 639-2 or ISO 639-3 three-letter language code
    custom_language_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Enable this setting on one audio selector to set it as the default for the
    # job. The service uses this default for outputs where it can't find the
    # specified input audio. If you don't set a default, those outputs have no
    # audio.
    default_selection: typing.Union[str, "AudioDefaultSelection"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # Specifies audio data from an external file source.
    external_audio_file_input: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Selects a specific language code from within an audio source.
    language_code: typing.Union[str, "LanguageCode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies a time delta in milliseconds to offset the audio from the input
    # video.
    offset: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Selects a specific PID from within an audio source (e.g. 257 selects PID
    # 0x101).
    pids: typing.List[int] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use this setting for input streams that contain Dolby E, to have the
    # service extract specific program data from the track. To select multiple
    # programs, create multiple selectors with the same Track and different
    # Program numbers. In the console, this setting is visible when you set
    # Selector type to Track. Choose the program number from the dropdown list.
    # If you are sending a JSON file, provide the program ID, which is part of
    # the audio metadata. If your input file has incorrect metadata, you can
    # choose All channels instead of a program number to have the service ignore
    # the program IDs and include all the programs in the track.
    program_selection: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use these settings to reorder the audio channels of one input to match
    # those of another input. This allows you to combine the two files into a
    # single output, one after the other.
    remix_settings: "RemixSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the type of the audio selector.
    selector_type: typing.Union[str, "AudioSelectorType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Identify a track from the input audio to include in this selector by
    # entering the track index number. To include several tracks in a single
    # audio selector, specify multiple tracks as follows. Using the console,
    # enter a comma-separated list. For examle, type "1,2,3" to include tracks 1
    # through 3. Specifying directly in your JSON job file, provide the track
    # numbers in an array. For example, "tracks": [1,2,3].
    tracks: typing.List[int] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AudioSelectorGroup(ShapeBase):
    """
    Group of Audio Selectors
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "audio_selector_names",
                "AudioSelectorNames",
                TypeInfo(typing.List[str]),
            ),
        ]

    # Name of an Audio Selector within the same input to include in the group.
    # Audio selector names are standardized, based on their order within the
    # input (e.g., "Audio Selector 1"). The audio selector name parameter can be
    # repeated to add any number of audio selectors to the group.
    audio_selector_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class AudioSelectorType(str):
    """
    Specifies the type of the audio selector.
    """
    PID = "PID"
    TRACK = "TRACK"
    LANGUAGE_CODE = "LANGUAGE_CODE"


class AudioTypeControl(str):
    """
    When set to FOLLOW_INPUT, if the input contains an ISO 639 audio_type, then that
    value is passed through to the output. If the input contains no ISO 639
    audio_type, the value in Audio Type is included in the output. Otherwise the
    value in Audio Type is included in the output. Note that this field and
    audioType are both ignored if audioDescriptionBroadcasterMix is set to
    BROADCASTER_MIXED_AD.
    """
    FOLLOW_INPUT = "FOLLOW_INPUT"
    USE_CONFIGURED = "USE_CONFIGURED"


@dataclasses.dataclass
class AvailBlanking(ShapeBase):
    """
    Settings for Avail Blanking
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "avail_blanking_image",
                "AvailBlankingImage",
                TypeInfo(str),
            ),
        ]

    # Blanking image to be used. Leave empty for solid black. Only bmp and png
    # images are supported.
    avail_blanking_image: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BadRequestException(ShapeBase):
    """
    The service can't process your request because of a problem in the request.
    Please check your request form and syntax.
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

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class BillingTagsSource(str):
    """
    Optional. Choose a tag type that AWS Billing and Cost Management will use to
    sort your AWS Elemental MediaConvert costs on any billing report that you set
    up. Any transcoding outputs that don't have an associated tag will appear in
    your billing report unsorted. If you don't choose a valid value for this field,
    your job outputs will appear on the billing report unsorted.
    """
    QUEUE = "QUEUE"
    PRESET = "PRESET"
    JOB_TEMPLATE = "JOB_TEMPLATE"


@dataclasses.dataclass
class BurninDestinationSettings(ShapeBase):
    """
    Burn-In Destination Settings.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "alignment",
                "Alignment",
                TypeInfo(typing.Union[str, BurninSubtitleAlignment]),
            ),
            (
                "background_color",
                "BackgroundColor",
                TypeInfo(typing.Union[str, BurninSubtitleBackgroundColor]),
            ),
            (
                "background_opacity",
                "BackgroundOpacity",
                TypeInfo(int),
            ),
            (
                "font_color",
                "FontColor",
                TypeInfo(typing.Union[str, BurninSubtitleFontColor]),
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
                TypeInfo(int),
            ),
            (
                "outline_color",
                "OutlineColor",
                TypeInfo(typing.Union[str, BurninSubtitleOutlineColor]),
            ),
            (
                "outline_size",
                "OutlineSize",
                TypeInfo(int),
            ),
            (
                "shadow_color",
                "ShadowColor",
                TypeInfo(typing.Union[str, BurninSubtitleShadowColor]),
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
                "teletext_spacing",
                "TeletextSpacing",
                TypeInfo(typing.Union[str, BurninSubtitleTeletextSpacing]),
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

    # If no explicit x_position or y_position is provided, setting alignment to
    # centered will place the captions at the bottom center of the output.
    # Similarly, setting a left alignment will align captions to the bottom left
    # of the output. If x and y positions are given in conjunction with the
    # alignment parameter, the font will be justified (either left or centered)
    # relative to those coordinates. This option is not valid for source captions
    # that are STL, 608/embedded or teletext. These source settings are already
    # pre-defined by the caption stream. All burn-in and DVB-Sub font settings
    # must match.
    alignment: typing.Union[str, "BurninSubtitleAlignment"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the color of the rectangle behind the captions. All burn-in and
    # DVB-Sub font settings must match.
    background_color: typing.Union[str, "BurninSubtitleBackgroundColor"
                                  ] = dataclasses.field(
                                      default=ShapeBase.NOT_SET,
                                  )

    # Specifies the opacity of the background rectangle. 255 is opaque; 0 is
    # transparent. Leaving this parameter blank is equivalent to setting it to 0
    # (transparent). All burn-in and DVB-Sub font settings must match.
    background_opacity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the color of the burned-in captions. This option is not valid for
    # source captions that are STL, 608/embedded or teletext. These source
    # settings are already pre-defined by the caption stream. All burn-in and
    # DVB-Sub font settings must match.
    font_color: typing.Union[str, "BurninSubtitleFontColor"
                            ] = dataclasses.field(
                                default=ShapeBase.NOT_SET,
                            )

    # Specifies the opacity of the burned-in captions. 255 is opaque; 0 is
    # transparent. All burn-in and DVB-Sub font settings must match.
    font_opacity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Font resolution in DPI (dots per inch); default is 96 dpi. All burn-in and
    # DVB-Sub font settings must match.
    font_resolution: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A positive integer indicates the exact font size in points. Set to 0 for
    # automatic font size selection. All burn-in and DVB-Sub font settings must
    # match.
    font_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies font outline color. This option is not valid for source captions
    # that are either 608/embedded or teletext. These source settings are already
    # pre-defined by the caption stream. All burn-in and DVB-Sub font settings
    # must match.
    outline_color: typing.Union[str, "BurninSubtitleOutlineColor"
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
    shadow_color: typing.Union[str, "BurninSubtitleShadowColor"
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

    # Only applies to jobs with input captions in Teletext or STL formats.
    # Specify whether the spacing between letters in your captions is set by the
    # captions grid or varies depending on letter width. Choose fixed grid to
    # conform to the spacing specified in the captions file more accurately.
    # Choose proportional to make the text easier to read if the captions are
    # closed caption.
    teletext_spacing: typing.Union[str, "BurninSubtitleTeletextSpacing"
                                  ] = dataclasses.field(
                                      default=ShapeBase.NOT_SET,
                                  )

    # Specifies the horizontal position of the caption relative to the left side
    # of the output in pixels. A value of 10 would result in the captions
    # starting 10 pixels from the left of the output. If no explicit x_position
    # is provided, the horizontal caption position will be determined by the
    # alignment parameter. This option is not valid for source captions that are
    # STL, 608/embedded or teletext. These source settings are already pre-
    # defined by the caption stream. All burn-in and DVB-Sub font settings must
    # match.
    x_position: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the vertical position of the caption relative to the top of the
    # output in pixels. A value of 10 would result in the captions starting 10
    # pixels from the top of the output. If no explicit y_position is provided,
    # the caption will be positioned towards the bottom of the output. This
    # option is not valid for source captions that are STL, 608/embedded or
    # teletext. These source settings are already pre-defined by the caption
    # stream. All burn-in and DVB-Sub font settings must match.
    y_position: int = dataclasses.field(default=ShapeBase.NOT_SET, )


class BurninSubtitleAlignment(str):
    """
    If no explicit x_position or y_position is provided, setting alignment to
    centered will place the captions at the bottom center of the output. Similarly,
    setting a left alignment will align captions to the bottom left of the output.
    If x and y positions are given in conjunction with the alignment parameter, the
    font will be justified (either left or centered) relative to those coordinates.
    This option is not valid for source captions that are STL, 608/embedded or
    teletext. These source settings are already pre-defined by the caption stream.
    All burn-in and DVB-Sub font settings must match.
    """
    CENTERED = "CENTERED"
    LEFT = "LEFT"


class BurninSubtitleBackgroundColor(str):
    """
    Specifies the color of the rectangle behind the captions. All burn-in and DVB-
    Sub font settings must match.
    """
    NONE = "NONE"
    BLACK = "BLACK"
    WHITE = "WHITE"


class BurninSubtitleFontColor(str):
    """
    Specifies the color of the burned-in captions. This option is not valid for
    source captions that are STL, 608/embedded or teletext. These source settings
    are already pre-defined by the caption stream. All burn-in and DVB-Sub font
    settings must match.
    """
    WHITE = "WHITE"
    BLACK = "BLACK"
    YELLOW = "YELLOW"
    RED = "RED"
    GREEN = "GREEN"
    BLUE = "BLUE"


class BurninSubtitleOutlineColor(str):
    """
    Specifies font outline color. This option is not valid for source captions that
    are either 608/embedded or teletext. These source settings are already pre-
    defined by the caption stream. All burn-in and DVB-Sub font settings must match.
    """
    BLACK = "BLACK"
    WHITE = "WHITE"
    YELLOW = "YELLOW"
    RED = "RED"
    GREEN = "GREEN"
    BLUE = "BLUE"


class BurninSubtitleShadowColor(str):
    """
    Specifies the color of the shadow cast by the captions. All burn-in and DVB-Sub
    font settings must match.
    """
    NONE = "NONE"
    BLACK = "BLACK"
    WHITE = "WHITE"


class BurninSubtitleTeletextSpacing(str):
    """
    Only applies to jobs with input captions in Teletext or STL formats. Specify
    whether the spacing between letters in your captions is set by the captions grid
    or varies depending on letter width. Choose fixed grid to conform to the spacing
    specified in the captions file more accurately. Choose proportional to make the
    text easier to read if the captions are closed caption.
    """
    FIXED_GRID = "FIXED_GRID"
    PROPORTIONAL = "PROPORTIONAL"


@dataclasses.dataclass
class CancelJobRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
        ]

    # The Job ID of the job to be cancelled.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CancelJobResponse(OutputShapeBase):
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
class CaptionDescription(ShapeBase):
    """
    Description of Caption output
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
                "custom_language_code",
                "CustomLanguageCode",
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
                TypeInfo(typing.Union[str, LanguageCode]),
            ),
            (
                "language_description",
                "LanguageDescription",
                TypeInfo(str),
            ),
        ]

    # Specifies which "Caption Selector":#inputs-caption_selector to use from
    # each input when generating captions. The name should be of the format
    # "Caption Selector ", which denotes that the Nth Caption Selector will be
    # used from each input.
    caption_selector_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates the language of the caption output track, using the ISO 639-2 or
    # ISO 639-3 three-letter language code
    custom_language_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specific settings required by destination type. Note that
    # burnin_destination_settings are not available if the source of the caption
    # data is Embedded or Teletext.
    destination_settings: "CaptionDestinationSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates the language of the caption output track.
    language_code: typing.Union[str, "LanguageCode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Human readable information to indicate captions available for players (eg.
    # English, or Spanish). Alphanumeric characters, spaces, and underscore are
    # legal.
    language_description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CaptionDescriptionPreset(ShapeBase):
    """
    Caption Description for preset
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "custom_language_code",
                "CustomLanguageCode",
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
                TypeInfo(typing.Union[str, LanguageCode]),
            ),
            (
                "language_description",
                "LanguageDescription",
                TypeInfo(str),
            ),
        ]

    # Indicates the language of the caption output track, using the ISO 639-2 or
    # ISO 639-3 three-letter language code
    custom_language_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specific settings required by destination type. Note that
    # burnin_destination_settings are not available if the source of the caption
    # data is Embedded or Teletext.
    destination_settings: "CaptionDestinationSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates the language of the caption output track.
    language_code: typing.Union[str, "LanguageCode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Human readable information to indicate captions available for players (eg.
    # English, or Spanish). Alphanumeric characters, spaces, and underscore are
    # legal.
    language_description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CaptionDestinationSettings(ShapeBase):
    """
    Specific settings required by destination type. Note that
    burnin_destination_settings are not available if the source of the caption data
    is Embedded or Teletext.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "burnin_destination_settings",
                "BurninDestinationSettings",
                TypeInfo(BurninDestinationSettings),
            ),
            (
                "destination_type",
                "DestinationType",
                TypeInfo(typing.Union[str, CaptionDestinationType]),
            ),
            (
                "dvb_sub_destination_settings",
                "DvbSubDestinationSettings",
                TypeInfo(DvbSubDestinationSettings),
            ),
            (
                "scc_destination_settings",
                "SccDestinationSettings",
                TypeInfo(SccDestinationSettings),
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
        ]

    # Burn-In Destination Settings.
    burnin_destination_settings: "BurninDestinationSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Type of Caption output, including Burn-In, Embedded, SCC, SRT, TTML,
    # WebVTT, DVB-Sub, Teletext.
    destination_type: typing.Union[str, "CaptionDestinationType"
                                  ] = dataclasses.field(
                                      default=ShapeBase.NOT_SET,
                                  )

    # DVB-Sub Destination Settings
    dvb_sub_destination_settings: "DvbSubDestinationSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Settings for SCC caption output.
    scc_destination_settings: "SccDestinationSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Settings for Teletext caption output
    teletext_destination_settings: "TeletextDestinationSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Settings specific to TTML caption outputs, including Pass style information
    # (TtmlStylePassthrough).
    ttml_destination_settings: "TtmlDestinationSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class CaptionDestinationType(str):
    """
    Type of Caption output, including Burn-In, Embedded, SCC, SRT, TTML, WebVTT,
    DVB-Sub, Teletext.
    """
    BURN_IN = "BURN_IN"
    DVB_SUB = "DVB_SUB"
    EMBEDDED = "EMBEDDED"
    SCC = "SCC"
    SRT = "SRT"
    TELETEXT = "TELETEXT"
    TTML = "TTML"
    WEBVTT = "WEBVTT"


@dataclasses.dataclass
class CaptionSelector(ShapeBase):
    """
    Set up captions in your outputs by first selecting them from your input here.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "custom_language_code",
                "CustomLanguageCode",
                TypeInfo(str),
            ),
            (
                "language_code",
                "LanguageCode",
                TypeInfo(typing.Union[str, LanguageCode]),
            ),
            (
                "source_settings",
                "SourceSettings",
                TypeInfo(CaptionSourceSettings),
            ),
        ]

    # The specific language to extract from source, using the ISO 639-2 or ISO
    # 639-3 three-letter language code. If input is SCTE-27, complete this field
    # and/or PID to select the caption language to extract. If input is DVB-Sub
    # and output is Burn-in or SMPTE-TT, complete this field and/or PID to select
    # the caption language to extract. If input is DVB-Sub that is being passed
    # through, omit this field (and PID field); there is no way to extract a
    # specific language with pass-through captions.
    custom_language_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The specific language to extract from source. If input is SCTE-27, complete
    # this field and/or PID to select the caption language to extract. If input
    # is DVB-Sub and output is Burn-in or SMPTE-TT, complete this field and/or
    # PID to select the caption language to extract. If input is DVB-Sub that is
    # being passed through, omit this field (and PID field); there is no way to
    # extract a specific language with pass-through captions.
    language_code: typing.Union[str, "LanguageCode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Source settings (SourceSettings) contains the group of settings for
    # captions in the input.
    source_settings: "CaptionSourceSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CaptionSourceSettings(ShapeBase):
    """
    Source settings (SourceSettings) contains the group of settings for captions in
    the input.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ancillary_source_settings",
                "AncillarySourceSettings",
                TypeInfo(AncillarySourceSettings),
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
                "file_source_settings",
                "FileSourceSettings",
                TypeInfo(FileSourceSettings),
            ),
            (
                "source_type",
                "SourceType",
                TypeInfo(typing.Union[str, CaptionSourceType]),
            ),
            (
                "teletext_source_settings",
                "TeletextSourceSettings",
                TypeInfo(TeletextSourceSettings),
            ),
        ]

    # Settings for ancillary captions source.
    ancillary_source_settings: "AncillarySourceSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # DVB Sub Source Settings
    dvb_sub_source_settings: "DvbSubSourceSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Settings for embedded captions Source
    embedded_source_settings: "EmbeddedSourceSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Settings for File-based Captions in Source
    file_source_settings: "FileSourceSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Use Source (SourceType) to identify the format of your input captions. The
    # service cannot auto-detect caption format.
    source_type: typing.Union[str, "CaptionSourceType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Settings specific to Teletext caption sources, including Page number.
    teletext_source_settings: "TeletextSourceSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class CaptionSourceType(str):
    """
    Use Source (SourceType) to identify the format of your input captions. The
    service cannot auto-detect caption format.
    """
    ANCILLARY = "ANCILLARY"
    DVB_SUB = "DVB_SUB"
    EMBEDDED = "EMBEDDED"
    SCC = "SCC"
    TTML = "TTML"
    STL = "STL"
    SRT = "SRT"
    TELETEXT = "TELETEXT"
    NULL_SOURCE = "NULL_SOURCE"


@dataclasses.dataclass
class ChannelMapping(ShapeBase):
    """
    Channel mapping (ChannelMapping) contains the group of fields that hold the
    remixing value for each channel. Units are in dB. Acceptable values are within
    the range from -60 (mute) through 6. A setting of 0 passes the input channel
    unchanged to the output channel (no attenuation or amplification).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "output_channels",
                "OutputChannels",
                TypeInfo(typing.List[OutputChannelMapping]),
            ),
        ]

    # List of output channels
    output_channels: typing.List["OutputChannelMapping"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class CmafClientCache(str):
    """
    When set to ENABLED, sets #EXT-X-ALLOW-CACHE:no tag, which prevents client from
    saving media segments for later replay.
    """
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class CmafCodecSpecification(str):
    """
    Specification to use (RFC-6381 or the default RFC-4281) during m3u8 playlist
    generation.
    """
    RFC_6381 = "RFC_6381"
    RFC_4281 = "RFC_4281"


@dataclasses.dataclass
class CmafEncryptionSettings(ShapeBase):
    """
    Settings for CMAF encryption
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "constant_initialization_vector",
                "ConstantInitializationVector",
                TypeInfo(str),
            ),
            (
                "encryption_method",
                "EncryptionMethod",
                TypeInfo(typing.Union[str, CmafEncryptionType]),
            ),
            (
                "initialization_vector_in_manifest",
                "InitializationVectorInManifest",
                TypeInfo(typing.Union[str, CmafInitializationVectorInManifest]),
            ),
            (
                "static_key_provider",
                "StaticKeyProvider",
                TypeInfo(StaticKeyProvider),
            ),
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, CmafKeyProviderType]),
            ),
        ]

    # This is a 128-bit, 16-byte hex value represented by a 32-character text
    # string. If this parameter is not set then the Initialization Vector will
    # follow the segment number by default.
    constant_initialization_vector: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Encrypts the segments with the given encryption scheme. Leave blank to
    # disable. Selecting 'Disabled' in the web interface also disables
    # encryption.
    encryption_method: typing.Union[str, "CmafEncryptionType"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # The Initialization Vector is a 128-bit number used in conjunction with the
    # key for encrypting blocks. If set to INCLUDE, Initialization Vector is
    # listed in the manifest. Otherwise Initialization Vector is not in the
    # manifest.
    initialization_vector_in_manifest: typing.Union[
        str, "CmafInitializationVectorInManifest"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # Settings for use with a SPEKE key provider.
    static_key_provider: "StaticKeyProvider" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates which type of key provider is used for encryption.
    type: typing.Union[str, "CmafKeyProviderType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class CmafEncryptionType(str):
    """
    Encrypts the segments with the given encryption scheme. Leave blank to disable.
    Selecting 'Disabled' in the web interface also disables encryption.
    """
    SAMPLE_AES = "SAMPLE_AES"


@dataclasses.dataclass
class CmafGroupSettings(ShapeBase):
    """
    Required when you set (Type) under (OutputGroups)>(OutputGroupSettings) to
    CMAF_GROUP_SETTINGS. Each output in a CMAF Output Group may only contain a
    single video, audio, or caption output.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "base_url",
                "BaseUrl",
                TypeInfo(str),
            ),
            (
                "client_cache",
                "ClientCache",
                TypeInfo(typing.Union[str, CmafClientCache]),
            ),
            (
                "codec_specification",
                "CodecSpecification",
                TypeInfo(typing.Union[str, CmafCodecSpecification]),
            ),
            (
                "destination",
                "Destination",
                TypeInfo(str),
            ),
            (
                "encryption",
                "Encryption",
                TypeInfo(CmafEncryptionSettings),
            ),
            (
                "fragment_length",
                "FragmentLength",
                TypeInfo(int),
            ),
            (
                "manifest_compression",
                "ManifestCompression",
                TypeInfo(typing.Union[str, CmafManifestCompression]),
            ),
            (
                "manifest_duration_format",
                "ManifestDurationFormat",
                TypeInfo(typing.Union[str, CmafManifestDurationFormat]),
            ),
            (
                "min_buffer_time",
                "MinBufferTime",
                TypeInfo(int),
            ),
            (
                "min_final_segment_length",
                "MinFinalSegmentLength",
                TypeInfo(float),
            ),
            (
                "segment_control",
                "SegmentControl",
                TypeInfo(typing.Union[str, CmafSegmentControl]),
            ),
            (
                "segment_length",
                "SegmentLength",
                TypeInfo(int),
            ),
            (
                "stream_inf_resolution",
                "StreamInfResolution",
                TypeInfo(typing.Union[str, CmafStreamInfResolution]),
            ),
            (
                "write_dash_manifest",
                "WriteDashManifest",
                TypeInfo(typing.Union[str, CmafWriteDASHManifest]),
            ),
            (
                "write_hls_manifest",
                "WriteHlsManifest",
                TypeInfo(typing.Union[str, CmafWriteHLSManifest]),
            ),
        ]

    # A partial URI prefix that will be put in the manifest file at the top level
    # BaseURL element. Can be used if streams are delivered from a different URL
    # than the manifest file.
    base_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When set to ENABLED, sets #EXT-X-ALLOW-CACHE:no tag, which prevents client
    # from saving media segments for later replay.
    client_cache: typing.Union[str, "CmafClientCache"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specification to use (RFC-6381 or the default RFC-4281) during m3u8
    # playlist generation.
    codec_specification: typing.Union[str, "CmafCodecSpecification"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # Use Destination (Destination) to specify the S3 output location and the
    # output filename base. Destination accepts format identifiers. If you do not
    # specify the base filename in the URI, the service will use the filename of
    # the input file. If your job has multiple inputs, the service uses the
    # filename of the first input file.
    destination: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # DRM settings.
    encryption: "CmafEncryptionSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Length of fragments to generate (in seconds). Fragment length must be
    # compatible with GOP size and Framerate. Note that fragments will end on the
    # next keyframe after this number of seconds, so actual fragment length may
    # be longer. When Emit Single File is checked, the fragmentation is internal
    # to a single output file and it does not cause the creation of many output
    # files as in other output types.
    fragment_length: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When set to GZIP, compresses HLS playlist.
    manifest_compression: typing.Union[str, "CmafManifestCompression"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    # Indicates whether the output manifest should use floating point values for
    # segment duration.
    manifest_duration_format: typing.Union[str, "CmafManifestDurationFormat"
                                          ] = dataclasses.field(
                                              default=ShapeBase.NOT_SET,
                                          )

    # Minimum time of initially buffered media that is needed to ensure smooth
    # playout.
    min_buffer_time: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Keep this setting at the default value of 0, unless you are troubleshooting
    # a problem with how devices play back the end of your video asset. If you
    # know that player devices are hanging on the final segment of your video
    # because the length of your final segment is too short, use this setting to
    # specify a minimum final segment length, in seconds. Choose a value that is
    # greater than or equal to 1 and less than your segment length. When you
    # specify a value for this setting, the encoder will combine any final
    # segment that is shorter than the length that you specify with the previous
    # segment. For example, your segment length is 3 seconds and your final
    # segment is .5 seconds without a minimum final segment length; when you set
    # the minimum final segment length to 1, your final segment is 3.5 seconds.
    min_final_segment_length: float = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When set to SINGLE_FILE, a single output file is generated, which is
    # internally segmented using the Fragment Length and Segment Length. When set
    # to SEGMENTED_FILES, separate segment files will be created.
    segment_control: typing.Union[str, "CmafSegmentControl"
                                 ] = dataclasses.field(
                                     default=ShapeBase.NOT_SET,
                                 )

    # Use this setting to specify the length, in seconds, of each individual CMAF
    # segment. This value applies to the whole package; that is, to every output
    # in the output group. Note that segments end on the first keyframe after
    # this number of seconds, so the actual segment length might be slightly
    # longer. If you set Segment control (CmafSegmentControl) to single file, the
    # service puts the content of each output in a single file that has metadata
    # that marks these segments. If you set it to segmented files, the service
    # creates multiple files for each output, each with the content of one
    # segment.
    segment_length: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Include or exclude RESOLUTION attribute for video in EXT-X-STREAM-INF tag
    # of variant manifest.
    stream_inf_resolution: typing.Union[str, "CmafStreamInfResolution"
                                       ] = dataclasses.field(
                                           default=ShapeBase.NOT_SET,
                                       )

    # When set to ENABLED, a DASH MPD manifest will be generated for this output.
    write_dash_manifest: typing.Union[str, "CmafWriteDASHManifest"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # When set to ENABLED, an Apple HLS manifest will be generated for this
    # output.
    write_hls_manifest: typing.Union[str, "CmafWriteHLSManifest"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )


class CmafInitializationVectorInManifest(str):
    """
    The Initialization Vector is a 128-bit number used in conjunction with the key
    for encrypting blocks. If set to INCLUDE, Initialization Vector is listed in the
    manifest. Otherwise Initialization Vector is not in the manifest.
    """
    INCLUDE = "INCLUDE"
    EXCLUDE = "EXCLUDE"


class CmafKeyProviderType(str):
    """
    Indicates which type of key provider is used for encryption.
    """
    STATIC_KEY = "STATIC_KEY"


class CmafManifestCompression(str):
    """
    When set to GZIP, compresses HLS playlist.
    """
    GZIP = "GZIP"
    NONE = "NONE"


class CmafManifestDurationFormat(str):
    """
    Indicates whether the output manifest should use floating point values for
    segment duration.
    """
    FLOATING_POINT = "FLOATING_POINT"
    INTEGER = "INTEGER"


class CmafSegmentControl(str):
    """
    When set to SINGLE_FILE, a single output file is generated, which is internally
    segmented using the Fragment Length and Segment Length. When set to
    SEGMENTED_FILES, separate segment files will be created.
    """
    SINGLE_FILE = "SINGLE_FILE"
    SEGMENTED_FILES = "SEGMENTED_FILES"


class CmafStreamInfResolution(str):
    """
    Include or exclude RESOLUTION attribute for video in EXT-X-STREAM-INF tag of
    variant manifest.
    """
    INCLUDE = "INCLUDE"
    EXCLUDE = "EXCLUDE"


class CmafWriteDASHManifest(str):
    """
    When set to ENABLED, a DASH MPD manifest will be generated for this output.
    """
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class CmafWriteHLSManifest(str):
    """
    When set to ENABLED, an Apple HLS manifest will be generated for this output.
    """
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


@dataclasses.dataclass
class ColorCorrector(ShapeBase):
    """
    Settings for color correction.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "brightness",
                "Brightness",
                TypeInfo(int),
            ),
            (
                "color_space_conversion",
                "ColorSpaceConversion",
                TypeInfo(typing.Union[str, ColorSpaceConversion]),
            ),
            (
                "contrast",
                "Contrast",
                TypeInfo(int),
            ),
            (
                "hdr10_metadata",
                "Hdr10Metadata",
                TypeInfo(Hdr10Metadata),
            ),
            (
                "hue",
                "Hue",
                TypeInfo(int),
            ),
            (
                "saturation",
                "Saturation",
                TypeInfo(int),
            ),
        ]

    # Brightness level.
    brightness: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Determines if colorspace conversion will be performed. If set to _None_, no
    # conversion will be performed. If _Force 601_ or _Force 709_ are selected,
    # conversion will be performed for inputs with differing colorspaces. An
    # input's colorspace can be specified explicitly in the "Video
    # Selector":#inputs-video_selector if necessary.
    color_space_conversion: typing.Union[str, "ColorSpaceConversion"
                                        ] = dataclasses.field(
                                            default=ShapeBase.NOT_SET,
                                        )

    # Contrast level.
    contrast: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use the HDR master display (Hdr10Metadata) settings to correct HDR metadata
    # or to provide missing metadata. These values vary depending on the input
    # video and must be provided by a color grader. Range is 0 to 50,000, each
    # increment represents 0.00002 in CIE1931 color coordinate. Note that these
    # settings are not color correction. Note that if you are creating HDR
    # outputs inside of an HLS CMAF package, to comply with the Apple
    # specification, you must use the HVC1 for H.265 setting.
    hdr10_metadata: "Hdr10Metadata" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Hue in degrees.
    hue: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Saturation level.
    saturation: int = dataclasses.field(default=ShapeBase.NOT_SET, )


class ColorMetadata(str):
    """
    Enable Insert color metadata (ColorMetadata) to include color metadata in this
    output. This setting is enabled by default.
    """
    IGNORE = "IGNORE"
    INSERT = "INSERT"


class ColorSpace(str):
    """
    If your input video has accurate color space metadata, or if you don't know
    about color space, leave this set to the default value FOLLOW. The service will
    automatically detect your input color space. If your input video has metadata
    indicating the wrong color space, or if your input video is missing color space
    metadata that should be there, specify the accurate color space here. If you
    choose HDR10, you can also correct inaccurate color space coefficients, using
    the HDR master display information controls. You must also set Color space usage
    (ColorSpaceUsage) to FORCE for the service to use these values.
    """
    FOLLOW = "FOLLOW"
    REC_601 = "REC_601"
    REC_709 = "REC_709"
    HDR10 = "HDR10"
    HLG_2020 = "HLG_2020"


class ColorSpaceConversion(str):
    """
    Determines if colorspace conversion will be performed. If set to _None_, no
    conversion will be performed. If _Force 601_ or _Force 709_ are selected,
    conversion will be performed for inputs with differing colorspaces. An input's
    colorspace can be specified explicitly in the "Video Selector":#inputs-
    video_selector if necessary.
    """
    NONE = "NONE"
    FORCE_601 = "FORCE_601"
    FORCE_709 = "FORCE_709"
    FORCE_HDR10 = "FORCE_HDR10"
    FORCE_HLG_2020 = "FORCE_HLG_2020"


class ColorSpaceUsage(str):
    """
    There are two sources for color metadata, the input file and the job
    configuration (in the Color space and HDR master display informaiton settings).
    The Color space usage setting controls which takes precedence. FORCE: The system
    will use color metadata supplied by user, if any. If the user does not supply
    color metadata, the system will use data from the source. FALLBACK: The system
    will use color metadata from the source. If source has no color metadata, the
    system will use user-supplied color metadata values if available.
    """
    FORCE = "FORCE"
    FALLBACK = "FALLBACK"


@dataclasses.dataclass
class ConflictException(ShapeBase):
    """
    The service couldn't complete your request because there is a conflict with the
    current state of the resource.
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

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ContainerSettings(ShapeBase):
    """
    Container specific settings.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "container",
                "Container",
                TypeInfo(typing.Union[str, ContainerType]),
            ),
            (
                "f4v_settings",
                "F4vSettings",
                TypeInfo(F4vSettings),
            ),
            (
                "m2ts_settings",
                "M2tsSettings",
                TypeInfo(M2tsSettings),
            ),
            (
                "m3u8_settings",
                "M3u8Settings",
                TypeInfo(M3u8Settings),
            ),
            (
                "mov_settings",
                "MovSettings",
                TypeInfo(MovSettings),
            ),
            (
                "mp4_settings",
                "Mp4Settings",
                TypeInfo(Mp4Settings),
            ),
        ]

    # Container for this output. Some containers require a container settings
    # object. If not specified, the default object will be created.
    container: typing.Union[str, "ContainerType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Settings for F4v container
    f4v_settings: "F4vSettings" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Settings for M2TS Container.
    m2ts_settings: "M2tsSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Settings for TS segments in HLS
    m3u8_settings: "M3u8Settings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Settings for MOV Container.
    mov_settings: "MovSettings" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Settings for MP4 Container
    mp4_settings: "Mp4Settings" = dataclasses.field(default=ShapeBase.NOT_SET, )


class ContainerType(str):
    """
    Container for this output. Some containers require a container settings object.
    If not specified, the default object will be created.
    """
    F4V = "F4V"
    ISMV = "ISMV"
    M2TS = "M2TS"
    M3U8 = "M3U8"
    CMFC = "CMFC"
    MOV = "MOV"
    MP4 = "MP4"
    MPD = "MPD"
    MXF = "MXF"
    RAW = "RAW"


@dataclasses.dataclass
class CreateJobRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role",
                "Role",
                TypeInfo(str),
            ),
            (
                "settings",
                "Settings",
                TypeInfo(JobSettings),
            ),
            (
                "billing_tags_source",
                "BillingTagsSource",
                TypeInfo(typing.Union[str, BillingTagsSource]),
            ),
            (
                "client_request_token",
                "ClientRequestToken",
                TypeInfo(str),
            ),
            (
                "job_template",
                "JobTemplate",
                TypeInfo(str),
            ),
            (
                "queue",
                "Queue",
                TypeInfo(str),
            ),
            (
                "user_metadata",
                "UserMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # Required. The IAM role you use for creating this job. For details about
    # permissions, see the User Guide topic at the User Guide at
    # http://docs.aws.amazon.com/mediaconvert/latest/ug/iam-role.html.
    role: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # JobSettings contains all the transcode settings for a job.
    settings: "JobSettings" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Optional. Choose a tag type that AWS Billing and Cost Management will use
    # to sort your AWS Elemental MediaConvert costs on any billing report that
    # you set up. Any transcoding outputs that don't have an associated tag will
    # appear in your billing report unsorted. If you don't choose a valid value
    # for this field, your job outputs will appear on the billing report
    # unsorted.
    billing_tags_source: typing.Union[str, "BillingTagsSource"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # Idempotency token for CreateJob operation.
    client_request_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When you create a job, you can either specify a job template or specify the
    # transcoding settings individually
    job_template: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Optional. When you create a job, you can specify a queue to send it to. If
    # you don't specify, the job will go to the default queue. For more about
    # queues, see the User Guide topic at
    # http://docs.aws.amazon.com/mediaconvert/latest/ug/what-is.html.
    queue: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # User-defined metadata that you want to associate with an MediaConvert job.
    # You specify metadata in key/value pairs.
    user_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateJobResponse(OutputShapeBase):
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
                "Job",
                TypeInfo(Job),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Each job converts an input file into an output file or files. For more
    # information, see the User Guide at
    # http://docs.aws.amazon.com/mediaconvert/latest/ug/what-is.html
    job: "Job" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateJobTemplateRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "settings",
                "Settings",
                TypeInfo(JobTemplateSettings),
            ),
            (
                "category",
                "Category",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "queue",
                "Queue",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The name of the job template you are creating.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # JobTemplateSettings contains all the transcode settings saved in the
    # template that will be applied to jobs created from it.
    settings: "JobTemplateSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Optional. A category for the job template you are creating
    category: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Optional. A description of the job template you are creating.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Optional. The queue that jobs created from this template are assigned to.
    # If you don't specify this, jobs will go to the default queue.
    queue: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The tags that you want to add to the resource. You can tag resources with a
    # key-value pair or with only a key.
    tags: typing.Dict[str, str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateJobTemplateResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "job_template",
                "JobTemplate",
                TypeInfo(JobTemplate),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A job template is a pre-made set of encoding instructions that you can use
    # to quickly create a job.
    job_template: "JobTemplate" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreatePresetRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "settings",
                "Settings",
                TypeInfo(PresetSettings),
            ),
            (
                "category",
                "Category",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The name of the preset you are creating.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Settings for preset
    settings: "PresetSettings" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Optional. A category for the preset you are creating.
    category: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Optional. A description of the preset you are creating.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The tags that you want to add to the resource. You can tag resources with a
    # key-value pair or with only a key.
    tags: typing.Dict[str, str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreatePresetResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "preset",
                "Preset",
                TypeInfo(Preset),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A preset is a collection of preconfigured media conversion settings that
    # you want MediaConvert to apply to the output during the conversion process.
    preset: "Preset" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateQueueRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The name of the queue you are creating.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Optional. A description of the queue you are creating.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The tags that you want to add to the resource. You can tag resources with a
    # key-value pair or with only a key.
    tags: typing.Dict[str, str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateQueueResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "queue",
                "Queue",
                TypeInfo(Queue),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # MediaConvert jobs are submitted to a queue. Unless specified otherwise jobs
    # are submitted to a built-in default queue. User can create additional
    # queues to separate the jobs of different categories or priority.
    queue: "Queue" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DashIsoEncryptionSettings(ShapeBase):
    """
    Specifies DRM settings for DASH outputs.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "speke_key_provider",
                "SpekeKeyProvider",
                TypeInfo(SpekeKeyProvider),
            ),
        ]

    # Settings for use with a SPEKE key provider
    speke_key_provider: "SpekeKeyProvider" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DashIsoGroupSettings(ShapeBase):
    """
    Required when you set (Type) under (OutputGroups)>(OutputGroupSettings) to
    DASH_ISO_GROUP_SETTINGS.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "base_url",
                "BaseUrl",
                TypeInfo(str),
            ),
            (
                "destination",
                "Destination",
                TypeInfo(str),
            ),
            (
                "encryption",
                "Encryption",
                TypeInfo(DashIsoEncryptionSettings),
            ),
            (
                "fragment_length",
                "FragmentLength",
                TypeInfo(int),
            ),
            (
                "hbbtv_compliance",
                "HbbtvCompliance",
                TypeInfo(typing.Union[str, DashIsoHbbtvCompliance]),
            ),
            (
                "min_buffer_time",
                "MinBufferTime",
                TypeInfo(int),
            ),
            (
                "segment_control",
                "SegmentControl",
                TypeInfo(typing.Union[str, DashIsoSegmentControl]),
            ),
            (
                "segment_length",
                "SegmentLength",
                TypeInfo(int),
            ),
            (
                "write_segment_timeline_in_representation",
                "WriteSegmentTimelineInRepresentation",
                TypeInfo(
                    typing.
                    Union[str, DashIsoWriteSegmentTimelineInRepresentation]
                ),
            ),
        ]

    # A partial URI prefix that will be put in the manifest (.mpd) file at the
    # top level BaseURL element. Can be used if streams are delivered from a
    # different URL than the manifest file.
    base_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use Destination (Destination) to specify the S3 output location and the
    # output filename base. Destination accepts format identifiers. If you do not
    # specify the base filename in the URI, the service will use the filename of
    # the input file. If your job has multiple inputs, the service uses the
    # filename of the first input file.
    destination: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # DRM settings.
    encryption: "DashIsoEncryptionSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Length of fragments to generate (in seconds). Fragment length must be
    # compatible with GOP size and Framerate. Note that fragments will end on the
    # next keyframe after this number of seconds, so actual fragment length may
    # be longer. When Emit Single File is checked, the fragmentation is internal
    # to a single output file and it does not cause the creation of many output
    # files as in other output types.
    fragment_length: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Supports HbbTV specification as indicated
    hbbtv_compliance: typing.Union[str, "DashIsoHbbtvCompliance"
                                  ] = dataclasses.field(
                                      default=ShapeBase.NOT_SET,
                                  )

    # Minimum time of initially buffered media that is needed to ensure smooth
    # playout.
    min_buffer_time: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When set to SINGLE_FILE, a single output file is generated, which is
    # internally segmented using the Fragment Length and Segment Length. When set
    # to SEGMENTED_FILES, separate segment files will be created.
    segment_control: typing.Union[str, "DashIsoSegmentControl"
                                 ] = dataclasses.field(
                                     default=ShapeBase.NOT_SET,
                                 )

    # Length of mpd segments to create (in seconds). Note that segments will end
    # on the next keyframe after this number of seconds, so actual segment length
    # may be longer. When Emit Single File is checked, the segmentation is
    # internal to a single output file and it does not cause the creation of many
    # output files as in other output types.
    segment_length: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When ENABLED, segment durations are indicated in the manifest using
    # SegmentTimeline and SegmentTimeline will be promoted down into
    # Representation from AdaptationSet.
    write_segment_timeline_in_representation: typing.Union[
        str, "DashIsoWriteSegmentTimelineInRepresentation"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )


class DashIsoHbbtvCompliance(str):
    """
    Supports HbbTV specification as indicated
    """
    HBBTV_1_5 = "HBBTV_1_5"
    NONE = "NONE"


class DashIsoSegmentControl(str):
    """
    When set to SINGLE_FILE, a single output file is generated, which is internally
    segmented using the Fragment Length and Segment Length. When set to
    SEGMENTED_FILES, separate segment files will be created.
    """
    SINGLE_FILE = "SINGLE_FILE"
    SEGMENTED_FILES = "SEGMENTED_FILES"


class DashIsoWriteSegmentTimelineInRepresentation(str):
    """
    When ENABLED, segment durations are indicated in the manifest using
    SegmentTimeline and SegmentTimeline will be promoted down into Representation
    from AdaptationSet.
    """
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class DeinterlaceAlgorithm(str):
    """
    Only applies when you set Deinterlacer (DeinterlaceMode) to Deinterlace
    (DEINTERLACE) or Adaptive (ADAPTIVE). Motion adaptive interpolate (INTERPOLATE)
    produces sharper pictures, while blend (BLEND) produces smoother motion. Use
    (INTERPOLATE_TICKER) OR (BLEND_TICKER) if your source file includes a ticker,
    such as a scrolling headline at the bottom of the frame.
    """
    INTERPOLATE = "INTERPOLATE"
    INTERPOLATE_TICKER = "INTERPOLATE_TICKER"
    BLEND = "BLEND"
    BLEND_TICKER = "BLEND_TICKER"


@dataclasses.dataclass
class Deinterlacer(ShapeBase):
    """
    Settings for deinterlacer
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "algorithm",
                "Algorithm",
                TypeInfo(typing.Union[str, DeinterlaceAlgorithm]),
            ),
            (
                "control",
                "Control",
                TypeInfo(typing.Union[str, DeinterlacerControl]),
            ),
            (
                "mode",
                "Mode",
                TypeInfo(typing.Union[str, DeinterlacerMode]),
            ),
        ]

    # Only applies when you set Deinterlacer (DeinterlaceMode) to Deinterlace
    # (DEINTERLACE) or Adaptive (ADAPTIVE). Motion adaptive interpolate
    # (INTERPOLATE) produces sharper pictures, while blend (BLEND) produces
    # smoother motion. Use (INTERPOLATE_TICKER) OR (BLEND_TICKER) if your source
    # file includes a ticker, such as a scrolling headline at the bottom of the
    # frame.
    algorithm: typing.Union[str, "DeinterlaceAlgorithm"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # \- When set to NORMAL (default), the deinterlacer does not convert frames
    # that are tagged in metadata as progressive. It will only convert those that
    # are tagged as some other type. - When set to FORCE_ALL_FRAMES, the
    # deinterlacer converts every frame to progressive - even those that are
    # already tagged as progressive. Turn Force mode on only if there is a good
    # chance that the metadata has tagged frames as progressive when they are not
    # progressive. Do not turn on otherwise; processing frames that are already
    # progressive into progressive will probably result in lower quality video.
    control: typing.Union[str, "DeinterlacerControl"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Use Deinterlacer (DeinterlaceMode) to choose how the service will do
    # deinterlacing. Default is Deinterlace. - Deinterlace converts interlaced to
    # progressive. - Inverse telecine converts Hard Telecine 29.97i to
    # progressive 23.976p. - Adaptive auto-detects and converts to progressive.
    mode: typing.Union[str, "DeinterlacerMode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class DeinterlacerControl(str):
    """
    \- When set to NORMAL (default), the deinterlacer does not convert frames that
    are tagged in metadata as progressive. It will only convert those that are
    tagged as some other type. - When set to FORCE_ALL_FRAMES, the deinterlacer
    converts every frame to progressive - even those that are already tagged as
    progressive. Turn Force mode on only if there is a good chance that the metadata
    has tagged frames as progressive when they are not progressive. Do not turn on
    otherwise; processing frames that are already progressive into progressive will
    probably result in lower quality video.
    """
    FORCE_ALL_FRAMES = "FORCE_ALL_FRAMES"
    NORMAL = "NORMAL"


class DeinterlacerMode(str):
    """
    Use Deinterlacer (DeinterlaceMode) to choose how the service will do
    deinterlacing. Default is Deinterlace. - Deinterlace converts interlaced to
    progressive. - Inverse telecine converts Hard Telecine 29.97i to progressive
    23.976p. - Adaptive auto-detects and converts to progressive.
    """
    DEINTERLACE = "DEINTERLACE"
    INVERSE_TELECINE = "INVERSE_TELECINE"
    ADAPTIVE = "ADAPTIVE"


@dataclasses.dataclass
class DeleteJobTemplateRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The name of the job template to be deleted.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteJobTemplateResponse(OutputShapeBase):
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
class DeletePresetRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The name of the preset to be deleted.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeletePresetResponse(OutputShapeBase):
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
class DeleteQueueRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The name of the queue to be deleted.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteQueueResponse(OutputShapeBase):
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


class DescribeEndpointsMode(str):
    """
    Optional field, defaults to DEFAULT. Specify DEFAULT for this operation to
    return your endpoints if any exist, or to create an endpoint for you and return
    it if one doesn't already exist. Specify GET_ONLY to return your endpoints if
    any exist, or an empty list if none exist.
    """
    DEFAULT = "DEFAULT"
    GET_ONLY = "GET_ONLY"


@dataclasses.dataclass
class DescribeEndpointsRequest(ShapeBase):
    """
    DescribeEndpointsRequest
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
                "mode",
                "Mode",
                TypeInfo(typing.Union[str, DescribeEndpointsMode]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # Optional. Max number of endpoints, up to twenty, that will be returned at
    # one time.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Optional field, defaults to DEFAULT. Specify DEFAULT for this operation to
    # return your endpoints if any exist, or to create an endpoint for you and
    # return it if one doesn't already exist. Specify GET_ONLY to return your
    # endpoints if any exist, or an empty list if none exist.
    mode: typing.Union[str, "DescribeEndpointsMode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Use this string, provided with the response to a previous request, to
    # request the next batch of endpoints.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeEndpointsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "endpoints",
                "Endpoints",
                TypeInfo(typing.List[Endpoint]),
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

    # List of endpoints
    endpoints: typing.List["Endpoint"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Use this string to request the next batch of endpoints.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class DropFrameTimecode(str):
    """
    Applies only to 29.97 fps outputs. When this feature is enabled, the service
    will use drop-frame timecode on outputs. If it is not possible to use drop-frame
    timecode, the system will fall back to non-drop-frame. This setting is enabled
    by default when Timecode insertion (TimecodeInsertion) is enabled.
    """
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


@dataclasses.dataclass
class DvbNitSettings(ShapeBase):
    """
    Inserts DVB Network Information Table (NIT) at the specified table repetition
    interval.
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
                "nit_interval",
                "NitInterval",
                TypeInfo(int),
            ),
        ]

    # The numeric value placed in the Network Information Table (NIT).
    network_id: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The network name text placed in the network_name_descriptor inside the
    # Network Information Table. Maximum length is 256 characters.
    network_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of milliseconds between instances of this table in the output
    # transport stream.
    nit_interval: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DvbSdtSettings(ShapeBase):
    """
    Inserts DVB Service Description Table (NIT) at the specified table repetition
    interval.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "output_sdt",
                "OutputSdt",
                TypeInfo(typing.Union[str, OutputSdt]),
            ),
            (
                "sdt_interval",
                "SdtInterval",
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

    # Selects method of inserting SDT information into output stream. "Follow
    # input SDT" copies SDT information from input stream to output stream.
    # "Follow input SDT if present" copies SDT information from input stream to
    # output stream if SDT information is present in the input, otherwise it will
    # fall back on the user-defined values. Enter "SDT Manually" means user will
    # enter the SDT information. "No SDT" means output stream will not contain
    # SDT information.
    output_sdt: typing.Union[str, "OutputSdt"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of milliseconds between instances of this table in the output
    # transport stream.
    sdt_interval: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The service name placed in the service_descriptor in the Service
    # Description Table. Maximum length is 256 characters.
    service_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The service provider name placed in the service_descriptor in the Service
    # Description Table. Maximum length is 256 characters.
    service_provider_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DvbSubDestinationSettings(ShapeBase):
    """
    DVB-Sub Destination Settings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "alignment",
                "Alignment",
                TypeInfo(typing.Union[str, DvbSubtitleAlignment]),
            ),
            (
                "background_color",
                "BackgroundColor",
                TypeInfo(typing.Union[str, DvbSubtitleBackgroundColor]),
            ),
            (
                "background_opacity",
                "BackgroundOpacity",
                TypeInfo(int),
            ),
            (
                "font_color",
                "FontColor",
                TypeInfo(typing.Union[str, DvbSubtitleFontColor]),
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
                TypeInfo(int),
            ),
            (
                "outline_color",
                "OutlineColor",
                TypeInfo(typing.Union[str, DvbSubtitleOutlineColor]),
            ),
            (
                "outline_size",
                "OutlineSize",
                TypeInfo(int),
            ),
            (
                "shadow_color",
                "ShadowColor",
                TypeInfo(typing.Union[str, DvbSubtitleShadowColor]),
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
                "teletext_spacing",
                "TeletextSpacing",
                TypeInfo(typing.Union[str, DvbSubtitleTeletextSpacing]),
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

    # If no explicit x_position or y_position is provided, setting alignment to
    # centered will place the captions at the bottom center of the output.
    # Similarly, setting a left alignment will align captions to the bottom left
    # of the output. If x and y positions are given in conjunction with the
    # alignment parameter, the font will be justified (either left or centered)
    # relative to those coordinates. This option is not valid for source captions
    # that are STL, 608/embedded or teletext. These source settings are already
    # pre-defined by the caption stream. All burn-in and DVB-Sub font settings
    # must match.
    alignment: typing.Union[str, "DvbSubtitleAlignment"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the color of the rectangle behind the captions. All burn-in and
    # DVB-Sub font settings must match.
    background_color: typing.Union[str, "DvbSubtitleBackgroundColor"
                                  ] = dataclasses.field(
                                      default=ShapeBase.NOT_SET,
                                  )

    # Specifies the opacity of the background rectangle. 255 is opaque; 0 is
    # transparent. Leaving this parameter blank is equivalent to setting it to 0
    # (transparent). All burn-in and DVB-Sub font settings must match.
    background_opacity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the color of the burned-in captions. This option is not valid for
    # source captions that are STL, 608/embedded or teletext. These source
    # settings are already pre-defined by the caption stream. All burn-in and
    # DVB-Sub font settings must match.
    font_color: typing.Union[str, "DvbSubtitleFontColor"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the opacity of the burned-in captions. 255 is opaque; 0 is
    # transparent. All burn-in and DVB-Sub font settings must match.
    font_opacity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Font resolution in DPI (dots per inch); default is 96 dpi. All burn-in and
    # DVB-Sub font settings must match.
    font_resolution: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A positive integer indicates the exact font size in points. Set to 0 for
    # automatic font size selection. All burn-in and DVB-Sub font settings must
    # match.
    font_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies font outline color. This option is not valid for source captions
    # that are either 608/embedded or teletext. These source settings are already
    # pre-defined by the caption stream. All burn-in and DVB-Sub font settings
    # must match.
    outline_color: typing.Union[str, "DvbSubtitleOutlineColor"
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
    shadow_color: typing.Union[str, "DvbSubtitleShadowColor"
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

    # Only applies to jobs with input captions in Teletext or STL formats.
    # Specify whether the spacing between letters in your captions is set by the
    # captions grid or varies depending on letter width. Choose fixed grid to
    # conform to the spacing specified in the captions file more accurately.
    # Choose proportional to make the text easier to read if the captions are
    # closed caption.
    teletext_spacing: typing.Union[str, "DvbSubtitleTeletextSpacing"
                                  ] = dataclasses.field(
                                      default=ShapeBase.NOT_SET,
                                  )

    # Specifies the horizontal position of the caption relative to the left side
    # of the output in pixels. A value of 10 would result in the captions
    # starting 10 pixels from the left of the output. If no explicit x_position
    # is provided, the horizontal caption position will be determined by the
    # alignment parameter. This option is not valid for source captions that are
    # STL, 608/embedded or teletext. These source settings are already pre-
    # defined by the caption stream. All burn-in and DVB-Sub font settings must
    # match.
    x_position: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the vertical position of the caption relative to the top of the
    # output in pixels. A value of 10 would result in the captions starting 10
    # pixels from the top of the output. If no explicit y_position is provided,
    # the caption will be positioned towards the bottom of the output. This
    # option is not valid for source captions that are STL, 608/embedded or
    # teletext. These source settings are already pre-defined by the caption
    # stream. All burn-in and DVB-Sub font settings must match.
    y_position: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DvbSubSourceSettings(ShapeBase):
    """
    DVB Sub Source Settings
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


class DvbSubtitleAlignment(str):
    """
    If no explicit x_position or y_position is provided, setting alignment to
    centered will place the captions at the bottom center of the output. Similarly,
    setting a left alignment will align captions to the bottom left of the output.
    If x and y positions are given in conjunction with the alignment parameter, the
    font will be justified (either left or centered) relative to those coordinates.
    This option is not valid for source captions that are STL, 608/embedded or
    teletext. These source settings are already pre-defined by the caption stream.
    All burn-in and DVB-Sub font settings must match.
    """
    CENTERED = "CENTERED"
    LEFT = "LEFT"


class DvbSubtitleBackgroundColor(str):
    """
    Specifies the color of the rectangle behind the captions. All burn-in and DVB-
    Sub font settings must match.
    """
    NONE = "NONE"
    BLACK = "BLACK"
    WHITE = "WHITE"


class DvbSubtitleFontColor(str):
    """
    Specifies the color of the burned-in captions. This option is not valid for
    source captions that are STL, 608/embedded or teletext. These source settings
    are already pre-defined by the caption stream. All burn-in and DVB-Sub font
    settings must match.
    """
    WHITE = "WHITE"
    BLACK = "BLACK"
    YELLOW = "YELLOW"
    RED = "RED"
    GREEN = "GREEN"
    BLUE = "BLUE"


class DvbSubtitleOutlineColor(str):
    """
    Specifies font outline color. This option is not valid for source captions that
    are either 608/embedded or teletext. These source settings are already pre-
    defined by the caption stream. All burn-in and DVB-Sub font settings must match.
    """
    BLACK = "BLACK"
    WHITE = "WHITE"
    YELLOW = "YELLOW"
    RED = "RED"
    GREEN = "GREEN"
    BLUE = "BLUE"


class DvbSubtitleShadowColor(str):
    """
    Specifies the color of the shadow cast by the captions. All burn-in and DVB-Sub
    font settings must match.
    """
    NONE = "NONE"
    BLACK = "BLACK"
    WHITE = "WHITE"


class DvbSubtitleTeletextSpacing(str):
    """
    Only applies to jobs with input captions in Teletext or STL formats. Specify
    whether the spacing between letters in your captions is set by the captions grid
    or varies depending on letter width. Choose fixed grid to conform to the spacing
    specified in the captions file more accurately. Choose proportional to make the
    text easier to read if the captions are closed caption.
    """
    FIXED_GRID = "FIXED_GRID"
    PROPORTIONAL = "PROPORTIONAL"


@dataclasses.dataclass
class DvbTdtSettings(ShapeBase):
    """
    Inserts DVB Time and Date Table (TDT) at the specified table repetition
    interval.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "tdt_interval",
                "TdtInterval",
                TypeInfo(int),
            ),
        ]

    # The number of milliseconds between instances of this table in the output
    # transport stream.
    tdt_interval: int = dataclasses.field(default=ShapeBase.NOT_SET, )


class Eac3AttenuationControl(str):
    """
    If set to ATTENUATE_3_DB, applies a 3 dB attenuation to the surround channels.
    Only used for 3/2 coding mode.
    """
    ATTENUATE_3_DB = "ATTENUATE_3_DB"
    NONE = "NONE"


class Eac3BitstreamMode(str):
    """
    Specifies the "Bitstream Mode" (bsmod) for the emitted E-AC-3 stream. See ATSC
    A/52-2012 (Annex E) for background on these values.
    """
    COMPLETE_MAIN = "COMPLETE_MAIN"
    COMMENTARY = "COMMENTARY"
    EMERGENCY = "EMERGENCY"
    HEARING_IMPAIRED = "HEARING_IMPAIRED"
    VISUALLY_IMPAIRED = "VISUALLY_IMPAIRED"


class Eac3CodingMode(str):
    """
    Dolby Digital Plus coding mode. Determines number of channels.
    """
    CODING_MODE_1_0 = "CODING_MODE_1_0"
    CODING_MODE_2_0 = "CODING_MODE_2_0"
    CODING_MODE_3_2 = "CODING_MODE_3_2"


class Eac3DcFilter(str):
    """
    Activates a DC highpass filter for all input channels.
    """
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class Eac3DynamicRangeCompressionLine(str):
    """
    Enables Dynamic Range Compression that restricts the absolute peak level for a
    signal.
    """
    NONE = "NONE"
    FILM_STANDARD = "FILM_STANDARD"
    FILM_LIGHT = "FILM_LIGHT"
    MUSIC_STANDARD = "MUSIC_STANDARD"
    MUSIC_LIGHT = "MUSIC_LIGHT"
    SPEECH = "SPEECH"


class Eac3DynamicRangeCompressionRf(str):
    """
    Enables Heavy Dynamic Range Compression, ensures that the instantaneous signal
    peaks do not exceed specified levels.
    """
    NONE = "NONE"
    FILM_STANDARD = "FILM_STANDARD"
    FILM_LIGHT = "FILM_LIGHT"
    MUSIC_STANDARD = "MUSIC_STANDARD"
    MUSIC_LIGHT = "MUSIC_LIGHT"
    SPEECH = "SPEECH"


class Eac3LfeControl(str):
    """
    When encoding 3/2 audio, controls whether the LFE channel is enabled
    """
    LFE = "LFE"
    NO_LFE = "NO_LFE"


class Eac3LfeFilter(str):
    """
    Applies a 120Hz lowpass filter to the LFE channel prior to encoding. Only valid
    with 3_2_LFE coding mode.
    """
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class Eac3MetadataControl(str):
    """
    When set to FOLLOW_INPUT, encoder metadata will be sourced from the DD, DD+, or
    DolbyE decoder that supplied this audio data. If audio was not supplied from one
    of these streams, then the static metadata settings will be used.
    """
    FOLLOW_INPUT = "FOLLOW_INPUT"
    USE_CONFIGURED = "USE_CONFIGURED"


class Eac3PassthroughControl(str):
    """
    When set to WHEN_POSSIBLE, input DD+ audio will be passed through if it is
    present on the input. this detection is dynamic over the life of the transcode.
    Inputs that alternate between DD+ and non-DD+ content will have a consistent DD+
    output as the system alternates between passthrough and encoding.
    """
    WHEN_POSSIBLE = "WHEN_POSSIBLE"
    NO_PASSTHROUGH = "NO_PASSTHROUGH"


class Eac3PhaseControl(str):
    """
    Controls the amount of phase-shift applied to the surround channels. Only used
    for 3/2 coding mode.
    """
    SHIFT_90_DEGREES = "SHIFT_90_DEGREES"
    NO_SHIFT = "NO_SHIFT"


@dataclasses.dataclass
class Eac3Settings(ShapeBase):
    """
    Required when you set (Codec) under (AudioDescriptions)>(CodecSettings) to the
    value EAC3.
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
                TypeInfo(int),
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
                "dynamic_range_compression_line",
                "DynamicRangeCompressionLine",
                TypeInfo(typing.Union[str, Eac3DynamicRangeCompressionLine]),
            ),
            (
                "dynamic_range_compression_rf",
                "DynamicRangeCompressionRf",
                TypeInfo(typing.Union[str, Eac3DynamicRangeCompressionRf]),
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
                "sample_rate",
                "SampleRate",
                TypeInfo(int),
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

    # If set to ATTENUATE_3_DB, applies a 3 dB attenuation to the surround
    # channels. Only used for 3/2 coding mode.
    attenuation_control: typing.Union[str, "Eac3AttenuationControl"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # Average bitrate in bits/second. Valid bitrates depend on the coding mode.
    bitrate: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the "Bitstream Mode" (bsmod) for the emitted E-AC-3 stream. See
    # ATSC A/52-2012 (Annex E) for background on these values.
    bitstream_mode: typing.Union[str, "Eac3BitstreamMode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Dolby Digital Plus coding mode. Determines number of channels.
    coding_mode: typing.Union[str, "Eac3CodingMode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Activates a DC highpass filter for all input channels.
    dc_filter: typing.Union[str, "Eac3DcFilter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Sets the dialnorm for the output. If blank and input audio is Dolby Digital
    # Plus, dialnorm will be passed through.
    dialnorm: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Enables Dynamic Range Compression that restricts the absolute peak level
    # for a signal.
    dynamic_range_compression_line: typing.Union[
        str, "Eac3DynamicRangeCompressionLine"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # Enables Heavy Dynamic Range Compression, ensures that the instantaneous
    # signal peaks do not exceed specified levels.
    dynamic_range_compression_rf: typing.Union[
        str, "Eac3DynamicRangeCompressionRf"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # When encoding 3/2 audio, controls whether the LFE channel is enabled
    lfe_control: typing.Union[str, "Eac3LfeControl"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Applies a 120Hz lowpass filter to the LFE channel prior to encoding. Only
    # valid with 3_2_LFE coding mode.
    lfe_filter: typing.Union[str, "Eac3LfeFilter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Left only/Right only center mix level. Only used for 3/2 coding mode. Valid
    # values: 3.0, 1.5, 0.0, -1.5 -3.0 -4.5 -6.0 -60
    lo_ro_center_mix_level: float = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Left only/Right only surround mix level. Only used for 3/2 coding mode.
    # Valid values: -1.5 -3.0 -4.5 -6.0 -60
    lo_ro_surround_mix_level: float = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Left total/Right total center mix level. Only used for 3/2 coding mode.
    # Valid values: 3.0, 1.5, 0.0, -1.5 -3.0 -4.5 -6.0 -60
    lt_rt_center_mix_level: float = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Left total/Right total surround mix level. Only used for 3/2 coding mode.
    # Valid values: -1.5 -3.0 -4.5 -6.0 -60
    lt_rt_surround_mix_level: float = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When set to FOLLOW_INPUT, encoder metadata will be sourced from the DD,
    # DD+, or DolbyE decoder that supplied this audio data. If audio was not
    # supplied from one of these streams, then the static metadata settings will
    # be used.
    metadata_control: typing.Union[str, "Eac3MetadataControl"
                                  ] = dataclasses.field(
                                      default=ShapeBase.NOT_SET,
                                  )

    # When set to WHEN_POSSIBLE, input DD+ audio will be passed through if it is
    # present on the input. this detection is dynamic over the life of the
    # transcode. Inputs that alternate between DD+ and non-DD+ content will have
    # a consistent DD+ output as the system alternates between passthrough and
    # encoding.
    passthrough_control: typing.Union[str, "Eac3PassthroughControl"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # Controls the amount of phase-shift applied to the surround channels. Only
    # used for 3/2 coding mode.
    phase_control: typing.Union[str, "Eac3PhaseControl"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Sample rate in hz. Sample rate is always 48000.
    sample_rate: int = dataclasses.field(default=ShapeBase.NOT_SET, )

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
    Stereo downmix preference. Only used for 3/2 coding mode.
    """
    NOT_INDICATED = "NOT_INDICATED"
    LO_RO = "LO_RO"
    LT_RT = "LT_RT"
    DPL2 = "DPL2"


class Eac3SurroundExMode(str):
    """
    When encoding 3/2 audio, sets whether an extra center back surround channel is
    matrix encoded into the left and right surround channels.
    """
    NOT_INDICATED = "NOT_INDICATED"
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class Eac3SurroundMode(str):
    """
    When encoding 2/0 audio, sets whether Dolby Surround is matrix encoded into the
    two channels.
    """
    NOT_INDICATED = "NOT_INDICATED"
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class EmbeddedConvert608To708(str):
    """
    When set to UPCONVERT, 608 data is both passed through via the "608
    compatibility bytes" fields of the 708 wrapper as well as translated into 708.
    708 data present in the source content will be discarded.
    """
    UPCONVERT = "UPCONVERT"
    DISABLED = "DISABLED"


@dataclasses.dataclass
class EmbeddedSourceSettings(ShapeBase):
    """
    Settings for embedded captions Source
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

    # When set to UPCONVERT, 608 data is both passed through via the "608
    # compatibility bytes" fields of the 708 wrapper as well as translated into
    # 708. 708 data present in the source content will be discarded.
    convert608_to708: typing.Union[str, "EmbeddedConvert608To708"
                                  ] = dataclasses.field(
                                      default=ShapeBase.NOT_SET,
                                  )

    # Specifies the 608/708 channel number within the video track from which to
    # extract captions. Unused for passthrough.
    source608_channel_number: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the video track index used for extracting captions. The system
    # only supports one input video track, so this should always be set to '1'.
    source608_track_number: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Endpoint(ShapeBase):
    """
    Describes an account-specific API endpoint.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "url",
                "Url",
                TypeInfo(str),
            ),
        ]

    # URL of endpoint
    url: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ExceptionBody(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class F4vMoovPlacement(str):
    """
    If set to PROGRESSIVE_DOWNLOAD, the MOOV atom is relocated to the beginning of
    the archive as required for progressive downloading. Otherwise it is placed
    normally at the end.
    """
    PROGRESSIVE_DOWNLOAD = "PROGRESSIVE_DOWNLOAD"
    NORMAL = "NORMAL"


@dataclasses.dataclass
class F4vSettings(ShapeBase):
    """
    Settings for F4v container
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "moov_placement",
                "MoovPlacement",
                TypeInfo(typing.Union[str, F4vMoovPlacement]),
            ),
        ]

    # If set to PROGRESSIVE_DOWNLOAD, the MOOV atom is relocated to the beginning
    # of the archive as required for progressive downloading. Otherwise it is
    # placed normally at the end.
    moov_placement: typing.Union[str, "F4vMoovPlacement"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class FileGroupSettings(ShapeBase):
    """
    Required when you set (Type) under (OutputGroups)>(OutputGroupSettings) to
    FILE_GROUP_SETTINGS.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "destination",
                "Destination",
                TypeInfo(str),
            ),
        ]

    # Use Destination (Destination) to specify the S3 output location and the
    # output filename base. Destination accepts format identifiers. If you do not
    # specify the base filename in the URI, the service will use the filename of
    # the input file. If your job has multiple inputs, the service uses the
    # filename of the first input file.
    destination: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class FileSourceConvert608To708(str):
    """
    If set to UPCONVERT, 608 caption data is both passed through via the "608
    compatibility bytes" fields of the 708 wrapper as well as translated into 708.
    708 data present in the source content will be discarded.
    """
    UPCONVERT = "UPCONVERT"
    DISABLED = "DISABLED"


@dataclasses.dataclass
class FileSourceSettings(ShapeBase):
    """
    Settings for File-based Captions in Source
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "convert608_to708",
                "Convert608To708",
                TypeInfo(typing.Union[str, FileSourceConvert608To708]),
            ),
            (
                "source_file",
                "SourceFile",
                TypeInfo(str),
            ),
            (
                "time_delta",
                "TimeDelta",
                TypeInfo(int),
            ),
        ]

    # If set to UPCONVERT, 608 caption data is both passed through via the "608
    # compatibility bytes" fields of the 708 wrapper as well as translated into
    # 708. 708 data present in the source content will be discarded.
    convert608_to708: typing.Union[str, "FileSourceConvert608To708"
                                  ] = dataclasses.field(
                                      default=ShapeBase.NOT_SET,
                                  )

    # External caption file used for loading captions. Accepted file extensions
    # are 'scc', 'ttml', 'dfxp', 'stl', 'srt', and 'smi'.
    source_file: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies a time delta in seconds to offset the captions from the source
    # file.
    time_delta: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ForbiddenException(ShapeBase):
    """
    You don't have permissions for this action with the credentials you sent.
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

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class FrameCaptureSettings(ShapeBase):
    """
    Required when you set (Codec) under (VideoDescription)>(CodecSettings) to the
    value FRAME_CAPTURE.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
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
                "max_captures",
                "MaxCaptures",
                TypeInfo(int),
            ),
            (
                "quality",
                "Quality",
                TypeInfo(int),
            ),
        ]

    # Frame capture will encode the first frame of the output stream, then one
    # frame every framerateDenominator/framerateNumerator seconds. For example,
    # settings of framerateNumerator = 1 and framerateDenominator = 3 (a rate of
    # 1/3 frame per second) will capture the first frame, then 1 frame every 3s.
    # Files will be named as filename.n.jpg where n is the 0-based sequence
    # number of each Capture.
    framerate_denominator: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Frame capture will encode the first frame of the output stream, then one
    # frame every framerateDenominator/framerateNumerator seconds. For example,
    # settings of framerateNumerator = 1 and framerateDenominator = 3 (a rate of
    # 1/3 frame per second) will capture the first frame, then 1 frame every 3s.
    # Files will be named as filename.NNNNNNN.jpg where N is the 0-based frame
    # sequence number zero padded to 7 decimal places.
    framerate_numerator: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Maximum number of captures (encoded jpg output files).
    max_captures: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # JPEG Quality - a higher value equals higher quality.
    quality: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetJobRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
        ]

    # the job ID of the job.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetJobResponse(OutputShapeBase):
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
                "Job",
                TypeInfo(Job),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Each job converts an input file into an output file or files. For more
    # information, see the User Guide at
    # http://docs.aws.amazon.com/mediaconvert/latest/ug/what-is.html
    job: "Job" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetJobTemplateRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The name of the job template.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetJobTemplateResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "job_template",
                "JobTemplate",
                TypeInfo(JobTemplate),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A job template is a pre-made set of encoding instructions that you can use
    # to quickly create a job.
    job_template: "JobTemplate" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetPresetRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The name of the preset.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetPresetResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "preset",
                "Preset",
                TypeInfo(Preset),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A preset is a collection of preconfigured media conversion settings that
    # you want MediaConvert to apply to the output during the conversion process.
    preset: "Preset" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetQueueRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The name of the queue.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetQueueResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "queue",
                "Queue",
                TypeInfo(Queue),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # MediaConvert jobs are submitted to a queue. Unless specified otherwise jobs
    # are submitted to a built-in default queue. User can create additional
    # queues to separate the jobs of different categories or priority.
    queue: "Queue" = dataclasses.field(default=ShapeBase.NOT_SET, )


class H264AdaptiveQuantization(str):
    """
    Adaptive quantization. Allows intra-frame quantizers to vary to improve visual
    quality.
    """
    OFF = "OFF"
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    HIGHER = "HIGHER"
    MAX = "MAX"


class H264CodecLevel(str):
    """
    H.264 Level.
    """
    AUTO = "AUTO"
    LEVEL_1 = "LEVEL_1"
    LEVEL_1_1 = "LEVEL_1_1"
    LEVEL_1_2 = "LEVEL_1_2"
    LEVEL_1_3 = "LEVEL_1_3"
    LEVEL_2 = "LEVEL_2"
    LEVEL_2_1 = "LEVEL_2_1"
    LEVEL_2_2 = "LEVEL_2_2"
    LEVEL_3 = "LEVEL_3"
    LEVEL_3_1 = "LEVEL_3_1"
    LEVEL_3_2 = "LEVEL_3_2"
    LEVEL_4 = "LEVEL_4"
    LEVEL_4_1 = "LEVEL_4_1"
    LEVEL_4_2 = "LEVEL_4_2"
    LEVEL_5 = "LEVEL_5"
    LEVEL_5_1 = "LEVEL_5_1"
    LEVEL_5_2 = "LEVEL_5_2"


class H264CodecProfile(str):
    """
    H.264 Profile. High 4:2:2 and 10-bit profiles are only available with the AVC-I
    License.
    """
    BASELINE = "BASELINE"
    HIGH = "HIGH"
    HIGH_10BIT = "HIGH_10BIT"
    HIGH_422 = "HIGH_422"
    HIGH_422_10BIT = "HIGH_422_10BIT"
    MAIN = "MAIN"


class H264DynamicSubGop(str):
    """
    Choose Adaptive to improve subjective video quality for high-motion content.
    This will cause the service to use fewer B-frames (which infer information based
    on other frames) for high-motion portions of the video and more B-frames for
    low-motion portions. The maximum number of B-frames is limited by the value you
    provide for the setting B frames between reference frames
    (numberBFramesBetweenReferenceFrames).
    """
    ADAPTIVE = "ADAPTIVE"
    STATIC = "STATIC"


class H264EntropyEncoding(str):
    """
    Entropy encoding mode. Use CABAC (must be in Main or High profile) or CAVLC.
    """
    CABAC = "CABAC"
    CAVLC = "CAVLC"


class H264FieldEncoding(str):
    """
    Choosing FORCE_FIELD disables PAFF encoding for interlaced outputs.
    """
    PAFF = "PAFF"
    FORCE_FIELD = "FORCE_FIELD"


class H264FlickerAdaptiveQuantization(str):
    """
    Adjust quantization within each frame to reduce flicker or 'pop' on I-frames.
    """
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H264FramerateControl(str):
    """
    If you are using the console, use the Framerate setting to specify the framerate
    for this output. If you want to keep the same framerate as the input video,
    choose Follow source. If you want to do framerate conversion, choose a framerate
    from the dropdown list or choose Custom. The framerates shown in the dropdown
    list are decimal approximations of fractions. If you choose Custom, specify your
    framerate as a fraction. If you are creating your transcoding job specification
    as a JSON file without the console, use FramerateControl to specify which value
    the service uses for the framerate for this output. Choose
    INITIALIZE_FROM_SOURCE if you want the service to use the framerate from the
    input. Choose SPECIFIED if you want the service to use the framerate you specify
    in the settings FramerateNumerator and FramerateDenominator.
    """
    INITIALIZE_FROM_SOURCE = "INITIALIZE_FROM_SOURCE"
    SPECIFIED = "SPECIFIED"


class H264FramerateConversionAlgorithm(str):
    """
    When set to INTERPOLATE, produces smoother motion during framerate conversion.
    """
    DUPLICATE_DROP = "DUPLICATE_DROP"
    INTERPOLATE = "INTERPOLATE"


class H264GopBReference(str):
    """
    If enable, use reference B frames for GOP structures that have B frames > 1.
    """
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H264GopSizeUnits(str):
    """
    Indicates if the GOP Size in H264 is specified in frames or seconds. If seconds
    the system will convert the GOP Size into a frame count at run time.
    """
    FRAMES = "FRAMES"
    SECONDS = "SECONDS"


class H264InterlaceMode(str):
    """
    Use Interlace mode (InterlaceMode) to choose the scan line type for the output.
    * Top Field First (TOP_FIELD) and Bottom Field First (BOTTOM_FIELD) produce
    interlaced output with the entire output having the same field polarity (top or
    bottom first). * Follow, Default Top (FOLLOW_TOP_FIELD) and Follow, Default
    Bottom (FOLLOW_BOTTOM_FIELD) use the same field polarity as the source.
    Therefore, behavior depends on the input scan type, as follows. \- If the source
    is interlaced, the output will be interlaced with the same polarity as the
    source (it will follow the source). The output could therefore be a mix of "top
    field first" and "bottom field first". \- If the source is progressive, the
    output will be interlaced with "top field first" or "bottom field first"
    polarity, depending on which of the Follow options you chose.
    """
    PROGRESSIVE = "PROGRESSIVE"
    TOP_FIELD = "TOP_FIELD"
    BOTTOM_FIELD = "BOTTOM_FIELD"
    FOLLOW_TOP_FIELD = "FOLLOW_TOP_FIELD"
    FOLLOW_BOTTOM_FIELD = "FOLLOW_BOTTOM_FIELD"


class H264ParControl(str):
    """
    Using the API, enable ParFollowSource if you want the service to use the pixel
    aspect ratio from the input. Using the console, do this by choosing Follow
    source for Pixel aspect ratio.
    """
    INITIALIZE_FROM_SOURCE = "INITIALIZE_FROM_SOURCE"
    SPECIFIED = "SPECIFIED"


class H264QualityTuningLevel(str):
    """
    Use Quality tuning level (H264QualityTuningLevel) to specifiy whether to use
    fast single-pass, high-quality singlepass, or high-quality multipass video
    encoding.
    """
    SINGLE_PASS = "SINGLE_PASS"
    SINGLE_PASS_HQ = "SINGLE_PASS_HQ"
    MULTI_PASS_HQ = "MULTI_PASS_HQ"


@dataclasses.dataclass
class H264QvbrSettings(ShapeBase):
    """
    Settings for quality-defined variable bitrate encoding with the H.264 codec.
    Required when you set Rate control mode to QVBR. Not valid when you set Rate
    control mode to a value other than QVBR, or when you don't define Rate control
    mode.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "max_average_bitrate",
                "MaxAverageBitrate",
                TypeInfo(int),
            ),
            (
                "qvbr_quality_level",
                "QvbrQualityLevel",
                TypeInfo(int),
            ),
        ]

    # Use this setting only when Rate control mode is QVBR and Quality tuning
    # level is Multi-pass HQ. For Max average bitrate values suited to the
    # complexity of your input video, the service limits the average bitrate of
    # the video part of this output to the value you choose. That is, the total
    # size of the video element is less than or equal to the value you set
    # multiplied by the number of seconds of encoded output.
    max_average_bitrate: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Required when you use QVBR rate control mode. That is, when you specify
    # qvbrSettings within h264Settings. Specify the target quality level for this
    # output, from 1 to 10. Use higher numbers for greater quality. Level 10
    # results in nearly lossless compression. The quality level for most
    # broadcast-quality transcodes is between 6 and 9.
    qvbr_quality_level: int = dataclasses.field(default=ShapeBase.NOT_SET, )


class H264RateControlMode(str):
    """
    Use this setting to specify whether this output has a variable bitrate (VBR),
    constant bitrate (CBR) or quality-defined variable bitrate (QVBR).
    """
    VBR = "VBR"
    CBR = "CBR"
    QVBR = "QVBR"


class H264RepeatPps(str):
    """
    Places a PPS header on each encoded picture, even if repeated.
    """
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H264SceneChangeDetect(str):
    """
    Scene change detection (inserts I-frames on scene changes).
    """
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


@dataclasses.dataclass
class H264Settings(ShapeBase):
    """
    Required when you set (Codec) under (VideoDescription)>(CodecSettings) to the
    value H_264.
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
                "bitrate",
                "Bitrate",
                TypeInfo(int),
            ),
            (
                "codec_level",
                "CodecLevel",
                TypeInfo(typing.Union[str, H264CodecLevel]),
            ),
            (
                "codec_profile",
                "CodecProfile",
                TypeInfo(typing.Union[str, H264CodecProfile]),
            ),
            (
                "dynamic_sub_gop",
                "DynamicSubGop",
                TypeInfo(typing.Union[str, H264DynamicSubGop]),
            ),
            (
                "entropy_encoding",
                "EntropyEncoding",
                TypeInfo(typing.Union[str, H264EntropyEncoding]),
            ),
            (
                "field_encoding",
                "FieldEncoding",
                TypeInfo(typing.Union[str, H264FieldEncoding]),
            ),
            (
                "flicker_adaptive_quantization",
                "FlickerAdaptiveQuantization",
                TypeInfo(typing.Union[str, H264FlickerAdaptiveQuantization]),
            ),
            (
                "framerate_control",
                "FramerateControl",
                TypeInfo(typing.Union[str, H264FramerateControl]),
            ),
            (
                "framerate_conversion_algorithm",
                "FramerateConversionAlgorithm",
                TypeInfo(typing.Union[str, H264FramerateConversionAlgorithm]),
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
                "hrd_buffer_initial_fill_percentage",
                "HrdBufferInitialFillPercentage",
                TypeInfo(int),
            ),
            (
                "hrd_buffer_size",
                "HrdBufferSize",
                TypeInfo(int),
            ),
            (
                "interlace_mode",
                "InterlaceMode",
                TypeInfo(typing.Union[str, H264InterlaceMode]),
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
                "number_b_frames_between_reference_frames",
                "NumberBFramesBetweenReferenceFrames",
                TypeInfo(int),
            ),
            (
                "number_reference_frames",
                "NumberReferenceFrames",
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
                "quality_tuning_level",
                "QualityTuningLevel",
                TypeInfo(typing.Union[str, H264QualityTuningLevel]),
            ),
            (
                "qvbr_settings",
                "QvbrSettings",
                TypeInfo(H264QvbrSettings),
            ),
            (
                "rate_control_mode",
                "RateControlMode",
                TypeInfo(typing.Union[str, H264RateControlMode]),
            ),
            (
                "repeat_pps",
                "RepeatPps",
                TypeInfo(typing.Union[str, H264RepeatPps]),
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
                "slow_pal",
                "SlowPal",
                TypeInfo(typing.Union[str, H264SlowPal]),
            ),
            (
                "softness",
                "Softness",
                TypeInfo(int),
            ),
            (
                "spatial_adaptive_quantization",
                "SpatialAdaptiveQuantization",
                TypeInfo(typing.Union[str, H264SpatialAdaptiveQuantization]),
            ),
            (
                "syntax",
                "Syntax",
                TypeInfo(typing.Union[str, H264Syntax]),
            ),
            (
                "telecine",
                "Telecine",
                TypeInfo(typing.Union[str, H264Telecine]),
            ),
            (
                "temporal_adaptive_quantization",
                "TemporalAdaptiveQuantization",
                TypeInfo(typing.Union[str, H264TemporalAdaptiveQuantization]),
            ),
            (
                "unregistered_sei_timecode",
                "UnregisteredSeiTimecode",
                TypeInfo(typing.Union[str, H264UnregisteredSeiTimecode]),
            ),
        ]

    # Adaptive quantization. Allows intra-frame quantizers to vary to improve
    # visual quality.
    adaptive_quantization: typing.Union[str, "H264AdaptiveQuantization"
                                       ] = dataclasses.field(
                                           default=ShapeBase.NOT_SET,
                                       )

    # Average bitrate in bits/second. Required for VBR and CBR. For MS Smooth
    # outputs, bitrates must be unique when rounded down to the nearest multiple
    # of 1000.
    bitrate: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # H.264 Level.
    codec_level: typing.Union[str, "H264CodecLevel"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # H.264 Profile. High 4:2:2 and 10-bit profiles are only available with the
    # AVC-I License.
    codec_profile: typing.Union[str, "H264CodecProfile"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Choose Adaptive to improve subjective video quality for high-motion
    # content. This will cause the service to use fewer B-frames (which infer
    # information based on other frames) for high-motion portions of the video
    # and more B-frames for low-motion portions. The maximum number of B-frames
    # is limited by the value you provide for the setting B frames between
    # reference frames (numberBFramesBetweenReferenceFrames).
    dynamic_sub_gop: typing.Union[str, "H264DynamicSubGop"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Entropy encoding mode. Use CABAC (must be in Main or High profile) or
    # CAVLC.
    entropy_encoding: typing.Union[str, "H264EntropyEncoding"
                                  ] = dataclasses.field(
                                      default=ShapeBase.NOT_SET,
                                  )

    # Choosing FORCE_FIELD disables PAFF encoding for interlaced outputs.
    field_encoding: typing.Union[str, "H264FieldEncoding"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Adjust quantization within each frame to reduce flicker or 'pop' on
    # I-frames.
    flicker_adaptive_quantization: typing.Union[
        str, "H264FlickerAdaptiveQuantization"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # If you are using the console, use the Framerate setting to specify the
    # framerate for this output. If you want to keep the same framerate as the
    # input video, choose Follow source. If you want to do framerate conversion,
    # choose a framerate from the dropdown list or choose Custom. The framerates
    # shown in the dropdown list are decimal approximations of fractions. If you
    # choose Custom, specify your framerate as a fraction. If you are creating
    # your transcoding job specification as a JSON file without the console, use
    # FramerateControl to specify which value the service uses for the framerate
    # for this output. Choose INITIALIZE_FROM_SOURCE if you want the service to
    # use the framerate from the input. Choose SPECIFIED if you want the service
    # to use the framerate you specify in the settings FramerateNumerator and
    # FramerateDenominator.
    framerate_control: typing.Union[str, "H264FramerateControl"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # When set to INTERPOLATE, produces smoother motion during framerate
    # conversion.
    framerate_conversion_algorithm: typing.Union[
        str, "H264FramerateConversionAlgorithm"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # When you use the API for transcode jobs that use framerate conversion,
    # specify the framerate as a fraction. For example, 24000 / 1001 = 23.976
    # fps. Use FramerateDenominator to specify the denominator of this fraction.
    # In this example, use 1001 for the value of FramerateDenominator. When you
    # use the console for transcode jobs that use framerate conversion, provide
    # the value as a decimal number for Framerate. In this example, specify
    # 23.976.
    framerate_denominator: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Framerate numerator - framerate is a fraction, e.g. 24000 / 1001 = 23.976
    # fps.
    framerate_numerator: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If enable, use reference B frames for GOP structures that have B frames >
    # 1.
    gop_b_reference: typing.Union[str, "H264GopBReference"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Frequency of closed GOPs. In streaming applications, it is recommended that
    # this be set to 1 so a decoder joining mid-stream will receive an IDR frame
    # as quickly as possible. Setting this value to 0 will break output
    # segmenting.
    gop_closed_cadence: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # GOP Length (keyframe interval) in frames or seconds. Must be greater than
    # zero.
    gop_size: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates if the GOP Size in H264 is specified in frames or seconds. If
    # seconds the system will convert the GOP Size into a frame count at run
    # time.
    gop_size_units: typing.Union[str, "H264GopSizeUnits"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Percentage of the buffer that should initially be filled (HRD buffer
    # model).
    hrd_buffer_initial_fill_percentage: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Size of buffer (HRD buffer model) in bits. For example, enter five megabits
    # as 5000000.
    hrd_buffer_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use Interlace mode (InterlaceMode) to choose the scan line type for the
    # output. * Top Field First (TOP_FIELD) and Bottom Field First (BOTTOM_FIELD)
    # produce interlaced output with the entire output having the same field
    # polarity (top or bottom first). * Follow, Default Top (FOLLOW_TOP_FIELD)
    # and Follow, Default Bottom (FOLLOW_BOTTOM_FIELD) use the same field
    # polarity as the source. Therefore, behavior depends on the input scan type,
    # as follows. \- If the source is interlaced, the output will be interlaced
    # with the same polarity as the source (it will follow the source). The
    # output could therefore be a mix of "top field first" and "bottom field
    # first". \- If the source is progressive, the output will be interlaced with
    # "top field first" or "bottom field first" polarity, depending on which of
    # the Follow options you chose.
    interlace_mode: typing.Union[str, "H264InterlaceMode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Maximum bitrate in bits/second. For example, enter five megabits per second
    # as 5000000. Required when Rate control mode is QVBR.
    max_bitrate: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Enforces separation between repeated (cadence) I-frames and I-frames
    # inserted by Scene Change Detection. If a scene change I-frame is within
    # I-interval frames of a cadence I-frame, the GOP is shrunk and/or stretched
    # to the scene change I-frame. GOP stretch requires enabling lookahead as
    # well as setting I-interval. The normal cadence resumes for the next GOP.
    # This setting is only used when Scene Change Detect is enabled. Note:
    # Maximum GOP stretch = GOP size + Min-I-interval - 1
    min_i_interval: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Number of B-frames between reference frames.
    number_b_frames_between_reference_frames: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Number of reference frames to use. The encoder may use more than requested
    # if using B-frames and/or interlaced encoding.
    number_reference_frames: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Using the API, enable ParFollowSource if you want the service to use the
    # pixel aspect ratio from the input. Using the console, do this by choosing
    # Follow source for Pixel aspect ratio.
    par_control: typing.Union[str, "H264ParControl"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Pixel Aspect Ratio denominator.
    par_denominator: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Pixel Aspect Ratio numerator.
    par_numerator: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use Quality tuning level (H264QualityTuningLevel) to specifiy whether to
    # use fast single-pass, high-quality singlepass, or high-quality multipass
    # video encoding.
    quality_tuning_level: typing.Union[str, "H264QualityTuningLevel"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    # Settings for quality-defined variable bitrate encoding with the H.264
    # codec. Required when you set Rate control mode to QVBR. Not valid when you
    # set Rate control mode to a value other than QVBR, or when you don't define
    # Rate control mode.
    qvbr_settings: "H264QvbrSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Use this setting to specify whether this output has a variable bitrate
    # (VBR), constant bitrate (CBR) or quality-defined variable bitrate (QVBR).
    rate_control_mode: typing.Union[str, "H264RateControlMode"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # Places a PPS header on each encoded picture, even if repeated.
    repeat_pps: typing.Union[str, "H264RepeatPps"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Scene change detection (inserts I-frames on scene changes).
    scene_change_detect: typing.Union[str, "H264SceneChangeDetect"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # Number of slices per picture. Must be less than or equal to the number of
    # macroblock rows for progressive pictures, and less than or equal to half
    # the number of macroblock rows for interlaced pictures.
    slices: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Enables Slow PAL rate conversion. 23.976fps and 24fps input is relabeled as
    # 25fps, and audio is sped up correspondingly.
    slow_pal: typing.Union[str, "H264SlowPal"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Softness. Selects quantizer matrix, larger values reduce high-frequency
    # content in the encoded image.
    softness: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Adjust quantization within each frame based on spatial variation of content
    # complexity.
    spatial_adaptive_quantization: typing.Union[
        str, "H264SpatialAdaptiveQuantization"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # Produces a bitstream compliant with SMPTE RP-2027.
    syntax: typing.Union[str, "H264Syntax"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # This field applies only if the Streams > Advanced > Framerate (framerate)
    # field is set to 29.970. This field works with the Streams > Advanced >
    # Preprocessors > Deinterlacer field (deinterlace_mode) and the Streams >
    # Advanced > Interlaced Mode field (interlace_mode) to identify the scan type
    # for the output: Progressive, Interlaced, Hard Telecine or Soft Telecine. -
    # Hard: produces 29.97i output from 23.976 input. - Soft: produces 23.976;
    # the player converts this output to 29.97i.
    telecine: typing.Union[str, "H264Telecine"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Adjust quantization within each frame based on temporal variation of
    # content complexity.
    temporal_adaptive_quantization: typing.Union[
        str, "H264TemporalAdaptiveQuantization"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # Inserts timecode for each frame as 4 bytes of an unregistered SEI message.
    unregistered_sei_timecode: typing.Union[str, "H264UnregisteredSeiTimecode"
                                           ] = dataclasses.field(
                                               default=ShapeBase.NOT_SET,
                                           )


class H264SlowPal(str):
    """
    Enables Slow PAL rate conversion. 23.976fps and 24fps input is relabeled as
    25fps, and audio is sped up correspondingly.
    """
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H264SpatialAdaptiveQuantization(str):
    """
    Adjust quantization within each frame based on spatial variation of content
    complexity.
    """
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H264Syntax(str):
    """
    Produces a bitstream compliant with SMPTE RP-2027.
    """
    DEFAULT = "DEFAULT"
    RP2027 = "RP2027"


class H264Telecine(str):
    """
    This field applies only if the Streams > Advanced > Framerate (framerate) field
    is set to 29.970. This field works with the Streams > Advanced > Preprocessors >
    Deinterlacer field (deinterlace_mode) and the Streams > Advanced > Interlaced
    Mode field (interlace_mode) to identify the scan type for the output:
    Progressive, Interlaced, Hard Telecine or Soft Telecine. - Hard: produces 29.97i
    output from 23.976 input. - Soft: produces 23.976; the player converts this
    output to 29.97i.
    """
    NONE = "NONE"
    SOFT = "SOFT"
    HARD = "HARD"


class H264TemporalAdaptiveQuantization(str):
    """
    Adjust quantization within each frame based on temporal variation of content
    complexity.
    """
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H264UnregisteredSeiTimecode(str):
    """
    Inserts timecode for each frame as 4 bytes of an unregistered SEI message.
    """
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H265AdaptiveQuantization(str):
    """
    Adaptive quantization. Allows intra-frame quantizers to vary to improve visual
    quality.
    """
    OFF = "OFF"
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    HIGHER = "HIGHER"
    MAX = "MAX"


class H265AlternateTransferFunctionSei(str):
    """
    Enables Alternate Transfer Function SEI message for outputs using Hybrid Log
    Gamma (HLG) Electro-Optical Transfer Function (EOTF).
    """
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H265CodecLevel(str):
    """
    H.265 Level.
    """
    AUTO = "AUTO"
    LEVEL_1 = "LEVEL_1"
    LEVEL_2 = "LEVEL_2"
    LEVEL_2_1 = "LEVEL_2_1"
    LEVEL_3 = "LEVEL_3"
    LEVEL_3_1 = "LEVEL_3_1"
    LEVEL_4 = "LEVEL_4"
    LEVEL_4_1 = "LEVEL_4_1"
    LEVEL_5 = "LEVEL_5"
    LEVEL_5_1 = "LEVEL_5_1"
    LEVEL_5_2 = "LEVEL_5_2"
    LEVEL_6 = "LEVEL_6"
    LEVEL_6_1 = "LEVEL_6_1"
    LEVEL_6_2 = "LEVEL_6_2"


class H265CodecProfile(str):
    """
    Represents the Profile and Tier, per the HEVC (H.265) specification. Selections
    are grouped as [Profile] / [Tier], so "Main/High" represents Main Profile with
    High Tier. 4:2:2 profiles are only available with the HEVC 4:2:2 License.
    """
    MAIN_MAIN = "MAIN_MAIN"
    MAIN_HIGH = "MAIN_HIGH"
    MAIN10_MAIN = "MAIN10_MAIN"
    MAIN10_HIGH = "MAIN10_HIGH"
    MAIN_422_8BIT_MAIN = "MAIN_422_8BIT_MAIN"
    MAIN_422_8BIT_HIGH = "MAIN_422_8BIT_HIGH"
    MAIN_422_10BIT_MAIN = "MAIN_422_10BIT_MAIN"
    MAIN_422_10BIT_HIGH = "MAIN_422_10BIT_HIGH"


class H265DynamicSubGop(str):
    """
    Choose Adaptive to improve subjective video quality for high-motion content.
    This will cause the service to use fewer B-frames (which infer information based
    on other frames) for high-motion portions of the video and more B-frames for
    low-motion portions. The maximum number of B-frames is limited by the value you
    provide for the setting B frames between reference frames
    (numberBFramesBetweenReferenceFrames).
    """
    ADAPTIVE = "ADAPTIVE"
    STATIC = "STATIC"


class H265FlickerAdaptiveQuantization(str):
    """
    Adjust quantization within each frame to reduce flicker or 'pop' on I-frames.
    """
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H265FramerateControl(str):
    """
    If you are using the console, use the Framerate setting to specify the framerate
    for this output. If you want to keep the same framerate as the input video,
    choose Follow source. If you want to do framerate conversion, choose a framerate
    from the dropdown list or choose Custom. The framerates shown in the dropdown
    list are decimal approximations of fractions. If you choose Custom, specify your
    framerate as a fraction. If you are creating your transcoding job sepecification
    as a JSON file without the console, use FramerateControl to specify which value
    the service uses for the framerate for this output. Choose
    INITIALIZE_FROM_SOURCE if you want the service to use the framerate from the
    input. Choose SPECIFIED if you want the service to use the framerate you specify
    in the settings FramerateNumerator and FramerateDenominator.
    """
    INITIALIZE_FROM_SOURCE = "INITIALIZE_FROM_SOURCE"
    SPECIFIED = "SPECIFIED"


class H265FramerateConversionAlgorithm(str):
    """
    When set to INTERPOLATE, produces smoother motion during framerate conversion.
    """
    DUPLICATE_DROP = "DUPLICATE_DROP"
    INTERPOLATE = "INTERPOLATE"


class H265GopBReference(str):
    """
    If enable, use reference B frames for GOP structures that have B frames > 1.
    """
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H265GopSizeUnits(str):
    """
    Indicates if the GOP Size in H265 is specified in frames or seconds. If seconds
    the system will convert the GOP Size into a frame count at run time.
    """
    FRAMES = "FRAMES"
    SECONDS = "SECONDS"


class H265InterlaceMode(str):
    """
    Use Interlace mode (InterlaceMode) to choose the scan line type for the output.
    * Top Field First (TOP_FIELD) and Bottom Field First (BOTTOM_FIELD) produce
    interlaced output with the entire output having the same field polarity (top or
    bottom first). * Follow, Default Top (FOLLOW_TOP_FIELD) and Follow, Default
    Bottom (FOLLOW_BOTTOM_FIELD) use the same field polarity as the source.
    Therefore, behavior depends on the input scan type. \- If the source is
    interlaced, the output will be interlaced with the same polarity as the source
    (it will follow the source). The output could therefore be a mix of "top field
    first" and "bottom field first". \- If the source is progressive, the output
    will be interlaced with "top field first" or "bottom field first" polarity,
    depending on which of the Follow options you chose.
    """
    PROGRESSIVE = "PROGRESSIVE"
    TOP_FIELD = "TOP_FIELD"
    BOTTOM_FIELD = "BOTTOM_FIELD"
    FOLLOW_TOP_FIELD = "FOLLOW_TOP_FIELD"
    FOLLOW_BOTTOM_FIELD = "FOLLOW_BOTTOM_FIELD"


class H265ParControl(str):
    """
    Using the API, enable ParFollowSource if you want the service to use the pixel
    aspect ratio from the input. Using the console, do this by choosing Follow
    source for Pixel aspect ratio.
    """
    INITIALIZE_FROM_SOURCE = "INITIALIZE_FROM_SOURCE"
    SPECIFIED = "SPECIFIED"


class H265QualityTuningLevel(str):
    """
    Use Quality tuning level (H265QualityTuningLevel) to specifiy whether to use
    fast single-pass, high-quality singlepass, or high-quality multipass video
    encoding.
    """
    SINGLE_PASS = "SINGLE_PASS"
    SINGLE_PASS_HQ = "SINGLE_PASS_HQ"
    MULTI_PASS_HQ = "MULTI_PASS_HQ"


@dataclasses.dataclass
class H265QvbrSettings(ShapeBase):
    """
    Settings for quality-defined variable bitrate encoding with the H.265 codec.
    Required when you set Rate control mode to QVBR. Not valid when you set Rate
    control mode to a value other than QVBR, or when you don't define Rate control
    mode.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "max_average_bitrate",
                "MaxAverageBitrate",
                TypeInfo(int),
            ),
            (
                "qvbr_quality_level",
                "QvbrQualityLevel",
                TypeInfo(int),
            ),
        ]

    # Use this setting only when Rate control mode is QVBR and Quality tuning
    # level is Multi-pass HQ. For Max average bitrate values suited to the
    # complexity of your input video, the service limits the average bitrate of
    # the video part of this output to the value you choose. That is, the total
    # size of the video element is less than or equal to the value you set
    # multiplied by the number of seconds of encoded output.
    max_average_bitrate: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Required when you use QVBR rate control mode. That is, when you specify
    # qvbrSettings within h265Settings. Specify the target quality level for this
    # output, from 1 to 10. Use higher numbers for greater quality. Level 10
    # results in nearly lossless compression. The quality level for most
    # broadcast-quality transcodes is between 6 and 9.
    qvbr_quality_level: int = dataclasses.field(default=ShapeBase.NOT_SET, )


class H265RateControlMode(str):
    """
    Use this setting to specify whether this output has a variable bitrate (VBR),
    constant bitrate (CBR) or quality-defined variable bitrate (QVBR).
    """
    VBR = "VBR"
    CBR = "CBR"
    QVBR = "QVBR"


class H265SampleAdaptiveOffsetFilterMode(str):
    """
    Specify Sample Adaptive Offset (SAO) filter strength. Adaptive mode dynamically
    selects best strength based on content
    """
    DEFAULT = "DEFAULT"
    ADAPTIVE = "ADAPTIVE"
    OFF = "OFF"


class H265SceneChangeDetect(str):
    """
    Scene change detection (inserts I-frames on scene changes).
    """
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


@dataclasses.dataclass
class H265Settings(ShapeBase):
    """
    Settings for H265 codec
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "adaptive_quantization",
                "AdaptiveQuantization",
                TypeInfo(typing.Union[str, H265AdaptiveQuantization]),
            ),
            (
                "alternate_transfer_function_sei",
                "AlternateTransferFunctionSei",
                TypeInfo(typing.Union[str, H265AlternateTransferFunctionSei]),
            ),
            (
                "bitrate",
                "Bitrate",
                TypeInfo(int),
            ),
            (
                "codec_level",
                "CodecLevel",
                TypeInfo(typing.Union[str, H265CodecLevel]),
            ),
            (
                "codec_profile",
                "CodecProfile",
                TypeInfo(typing.Union[str, H265CodecProfile]),
            ),
            (
                "dynamic_sub_gop",
                "DynamicSubGop",
                TypeInfo(typing.Union[str, H265DynamicSubGop]),
            ),
            (
                "flicker_adaptive_quantization",
                "FlickerAdaptiveQuantization",
                TypeInfo(typing.Union[str, H265FlickerAdaptiveQuantization]),
            ),
            (
                "framerate_control",
                "FramerateControl",
                TypeInfo(typing.Union[str, H265FramerateControl]),
            ),
            (
                "framerate_conversion_algorithm",
                "FramerateConversionAlgorithm",
                TypeInfo(typing.Union[str, H265FramerateConversionAlgorithm]),
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
                TypeInfo(typing.Union[str, H265GopBReference]),
            ),
            (
                "gop_closed_cadence",
                "GopClosedCadence",
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
                TypeInfo(typing.Union[str, H265GopSizeUnits]),
            ),
            (
                "hrd_buffer_initial_fill_percentage",
                "HrdBufferInitialFillPercentage",
                TypeInfo(int),
            ),
            (
                "hrd_buffer_size",
                "HrdBufferSize",
                TypeInfo(int),
            ),
            (
                "interlace_mode",
                "InterlaceMode",
                TypeInfo(typing.Union[str, H265InterlaceMode]),
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
                "number_b_frames_between_reference_frames",
                "NumberBFramesBetweenReferenceFrames",
                TypeInfo(int),
            ),
            (
                "number_reference_frames",
                "NumberReferenceFrames",
                TypeInfo(int),
            ),
            (
                "par_control",
                "ParControl",
                TypeInfo(typing.Union[str, H265ParControl]),
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
                "quality_tuning_level",
                "QualityTuningLevel",
                TypeInfo(typing.Union[str, H265QualityTuningLevel]),
            ),
            (
                "qvbr_settings",
                "QvbrSettings",
                TypeInfo(H265QvbrSettings),
            ),
            (
                "rate_control_mode",
                "RateControlMode",
                TypeInfo(typing.Union[str, H265RateControlMode]),
            ),
            (
                "sample_adaptive_offset_filter_mode",
                "SampleAdaptiveOffsetFilterMode",
                TypeInfo(typing.Union[str, H265SampleAdaptiveOffsetFilterMode]),
            ),
            (
                "scene_change_detect",
                "SceneChangeDetect",
                TypeInfo(typing.Union[str, H265SceneChangeDetect]),
            ),
            (
                "slices",
                "Slices",
                TypeInfo(int),
            ),
            (
                "slow_pal",
                "SlowPal",
                TypeInfo(typing.Union[str, H265SlowPal]),
            ),
            (
                "spatial_adaptive_quantization",
                "SpatialAdaptiveQuantization",
                TypeInfo(typing.Union[str, H265SpatialAdaptiveQuantization]),
            ),
            (
                "telecine",
                "Telecine",
                TypeInfo(typing.Union[str, H265Telecine]),
            ),
            (
                "temporal_adaptive_quantization",
                "TemporalAdaptiveQuantization",
                TypeInfo(typing.Union[str, H265TemporalAdaptiveQuantization]),
            ),
            (
                "temporal_ids",
                "TemporalIds",
                TypeInfo(typing.Union[str, H265TemporalIds]),
            ),
            (
                "tiles",
                "Tiles",
                TypeInfo(typing.Union[str, H265Tiles]),
            ),
            (
                "unregistered_sei_timecode",
                "UnregisteredSeiTimecode",
                TypeInfo(typing.Union[str, H265UnregisteredSeiTimecode]),
            ),
            (
                "write_mp4_packaging_type",
                "WriteMp4PackagingType",
                TypeInfo(typing.Union[str, H265WriteMp4PackagingType]),
            ),
        ]

    # Adaptive quantization. Allows intra-frame quantizers to vary to improve
    # visual quality.
    adaptive_quantization: typing.Union[str, "H265AdaptiveQuantization"
                                       ] = dataclasses.field(
                                           default=ShapeBase.NOT_SET,
                                       )

    # Enables Alternate Transfer Function SEI message for outputs using Hybrid
    # Log Gamma (HLG) Electro-Optical Transfer Function (EOTF).
    alternate_transfer_function_sei: typing.Union[
        str, "H265AlternateTransferFunctionSei"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # Average bitrate in bits/second. Required for VBR and CBR. For MS Smooth
    # outputs, bitrates must be unique when rounded down to the nearest multiple
    # of 1000.
    bitrate: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # H.265 Level.
    codec_level: typing.Union[str, "H265CodecLevel"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Represents the Profile and Tier, per the HEVC (H.265) specification.
    # Selections are grouped as [Profile] / [Tier], so "Main/High" represents
    # Main Profile with High Tier. 4:2:2 profiles are only available with the
    # HEVC 4:2:2 License.
    codec_profile: typing.Union[str, "H265CodecProfile"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Choose Adaptive to improve subjective video quality for high-motion
    # content. This will cause the service to use fewer B-frames (which infer
    # information based on other frames) for high-motion portions of the video
    # and more B-frames for low-motion portions. The maximum number of B-frames
    # is limited by the value you provide for the setting B frames between
    # reference frames (numberBFramesBetweenReferenceFrames).
    dynamic_sub_gop: typing.Union[str, "H265DynamicSubGop"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Adjust quantization within each frame to reduce flicker or 'pop' on
    # I-frames.
    flicker_adaptive_quantization: typing.Union[
        str, "H265FlickerAdaptiveQuantization"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # If you are using the console, use the Framerate setting to specify the
    # framerate for this output. If you want to keep the same framerate as the
    # input video, choose Follow source. If you want to do framerate conversion,
    # choose a framerate from the dropdown list or choose Custom. The framerates
    # shown in the dropdown list are decimal approximations of fractions. If you
    # choose Custom, specify your framerate as a fraction. If you are creating
    # your transcoding job sepecification as a JSON file without the console, use
    # FramerateControl to specify which value the service uses for the framerate
    # for this output. Choose INITIALIZE_FROM_SOURCE if you want the service to
    # use the framerate from the input. Choose SPECIFIED if you want the service
    # to use the framerate you specify in the settings FramerateNumerator and
    # FramerateDenominator.
    framerate_control: typing.Union[str, "H265FramerateControl"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # When set to INTERPOLATE, produces smoother motion during framerate
    # conversion.
    framerate_conversion_algorithm: typing.Union[
        str, "H265FramerateConversionAlgorithm"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # Framerate denominator.
    framerate_denominator: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Framerate numerator - framerate is a fraction, e.g. 24000 / 1001 = 23.976
    # fps.
    framerate_numerator: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If enable, use reference B frames for GOP structures that have B frames >
    # 1.
    gop_b_reference: typing.Union[str, "H265GopBReference"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Frequency of closed GOPs. In streaming applications, it is recommended that
    # this be set to 1 so a decoder joining mid-stream will receive an IDR frame
    # as quickly as possible. Setting this value to 0 will break output
    # segmenting.
    gop_closed_cadence: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # GOP Length (keyframe interval) in frames or seconds. Must be greater than
    # zero.
    gop_size: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates if the GOP Size in H265 is specified in frames or seconds. If
    # seconds the system will convert the GOP Size into a frame count at run
    # time.
    gop_size_units: typing.Union[str, "H265GopSizeUnits"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Percentage of the buffer that should initially be filled (HRD buffer
    # model).
    hrd_buffer_initial_fill_percentage: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Size of buffer (HRD buffer model) in bits. For example, enter five megabits
    # as 5000000.
    hrd_buffer_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use Interlace mode (InterlaceMode) to choose the scan line type for the
    # output. * Top Field First (TOP_FIELD) and Bottom Field First (BOTTOM_FIELD)
    # produce interlaced output with the entire output having the same field
    # polarity (top or bottom first). * Follow, Default Top (FOLLOW_TOP_FIELD)
    # and Follow, Default Bottom (FOLLOW_BOTTOM_FIELD) use the same field
    # polarity as the source. Therefore, behavior depends on the input scan type.
    # \- If the source is interlaced, the output will be interlaced with the same
    # polarity as the source (it will follow the source). The output could
    # therefore be a mix of "top field first" and "bottom field first". \- If the
    # source is progressive, the output will be interlaced with "top field first"
    # or "bottom field first" polarity, depending on which of the Follow options
    # you chose.
    interlace_mode: typing.Union[str, "H265InterlaceMode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Maximum bitrate in bits/second. For example, enter five megabits per second
    # as 5000000. Required when Rate control mode is QVBR.
    max_bitrate: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Enforces separation between repeated (cadence) I-frames and I-frames
    # inserted by Scene Change Detection. If a scene change I-frame is within
    # I-interval frames of a cadence I-frame, the GOP is shrunk and/or stretched
    # to the scene change I-frame. GOP stretch requires enabling lookahead as
    # well as setting I-interval. The normal cadence resumes for the next GOP.
    # This setting is only used when Scene Change Detect is enabled. Note:
    # Maximum GOP stretch = GOP size + Min-I-interval - 1
    min_i_interval: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Number of B-frames between reference frames.
    number_b_frames_between_reference_frames: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Number of reference frames to use. The encoder may use more than requested
    # if using B-frames and/or interlaced encoding.
    number_reference_frames: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Using the API, enable ParFollowSource if you want the service to use the
    # pixel aspect ratio from the input. Using the console, do this by choosing
    # Follow source for Pixel aspect ratio.
    par_control: typing.Union[str, "H265ParControl"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Pixel Aspect Ratio denominator.
    par_denominator: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Pixel Aspect Ratio numerator.
    par_numerator: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use Quality tuning level (H265QualityTuningLevel) to specifiy whether to
    # use fast single-pass, high-quality singlepass, or high-quality multipass
    # video encoding.
    quality_tuning_level: typing.Union[str, "H265QualityTuningLevel"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    # Settings for quality-defined variable bitrate encoding with the H.265
    # codec. Required when you set Rate control mode to QVBR. Not valid when you
    # set Rate control mode to a value other than QVBR, or when you don't define
    # Rate control mode.
    qvbr_settings: "H265QvbrSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Use this setting to specify whether this output has a variable bitrate
    # (VBR), constant bitrate (CBR) or quality-defined variable bitrate (QVBR).
    rate_control_mode: typing.Union[str, "H265RateControlMode"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # Specify Sample Adaptive Offset (SAO) filter strength. Adaptive mode
    # dynamically selects best strength based on content
    sample_adaptive_offset_filter_mode: typing.Union[
        str, "H265SampleAdaptiveOffsetFilterMode"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # Scene change detection (inserts I-frames on scene changes).
    scene_change_detect: typing.Union[str, "H265SceneChangeDetect"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # Number of slices per picture. Must be less than or equal to the number of
    # macroblock rows for progressive pictures, and less than or equal to half
    # the number of macroblock rows for interlaced pictures.
    slices: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Enables Slow PAL rate conversion. 23.976fps and 24fps input is relabeled as
    # 25fps, and audio is sped up correspondingly.
    slow_pal: typing.Union[str, "H265SlowPal"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Adjust quantization within each frame based on spatial variation of content
    # complexity.
    spatial_adaptive_quantization: typing.Union[
        str, "H265SpatialAdaptiveQuantization"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # This field applies only if the Streams > Advanced > Framerate (framerate)
    # field is set to 29.970. This field works with the Streams > Advanced >
    # Preprocessors > Deinterlacer field (deinterlace_mode) and the Streams >
    # Advanced > Interlaced Mode field (interlace_mode) to identify the scan type
    # for the output: Progressive, Interlaced, Hard Telecine or Soft Telecine. -
    # Hard: produces 29.97i output from 23.976 input. - Soft: produces 23.976;
    # the player converts this output to 29.97i.
    telecine: typing.Union[str, "H265Telecine"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Adjust quantization within each frame based on temporal variation of
    # content complexity.
    temporal_adaptive_quantization: typing.Union[
        str, "H265TemporalAdaptiveQuantization"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # Enables temporal layer identifiers in the encoded bitstream. Up to 3 layers
    # are supported depending on GOP structure: I- and P-frames form one layer,
    # reference B-frames can form a second layer and non-reference b-frames can
    # form a third layer. Decoders can optionally decode only the lower temporal
    # layers to generate a lower frame rate output. For example, given a
    # bitstream with temporal IDs and with b-frames = 1 (i.e. IbPbPb display
    # order), a decoder could decode all the frames for full frame rate output or
    # only the I and P frames (lowest temporal layer) for a half frame rate
    # output.
    temporal_ids: typing.Union[str, "H265TemporalIds"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Enable use of tiles, allowing horizontal as well as vertical subdivision of
    # the encoded pictures.
    tiles: typing.Union[str, "H265Tiles"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Inserts timecode for each frame as 4 bytes of an unregistered SEI message.
    unregistered_sei_timecode: typing.Union[str, "H265UnregisteredSeiTimecode"
                                           ] = dataclasses.field(
                                               default=ShapeBase.NOT_SET,
                                           )

    # If HVC1, output that is H.265 will be marked as HVC1 and adhere to the ISO-
    # IECJTC1-SC29_N13798_Text_ISOIEC_FDIS_14496-15_3rd_E spec which states that
    # parameter set NAL units will be stored in the sample headers but not in the
    # samples directly. If HEV1, then H.265 will be marked as HEV1 and parameter
    # set NAL units will be written into the samples.
    write_mp4_packaging_type: typing.Union[str, "H265WriteMp4PackagingType"
                                          ] = dataclasses.field(
                                              default=ShapeBase.NOT_SET,
                                          )


class H265SlowPal(str):
    """
    Enables Slow PAL rate conversion. 23.976fps and 24fps input is relabeled as
    25fps, and audio is sped up correspondingly.
    """
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H265SpatialAdaptiveQuantization(str):
    """
    Adjust quantization within each frame based on spatial variation of content
    complexity.
    """
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H265Telecine(str):
    """
    This field applies only if the Streams > Advanced > Framerate (framerate) field
    is set to 29.970. This field works with the Streams > Advanced > Preprocessors >
    Deinterlacer field (deinterlace_mode) and the Streams > Advanced > Interlaced
    Mode field (interlace_mode) to identify the scan type for the output:
    Progressive, Interlaced, Hard Telecine or Soft Telecine. - Hard: produces 29.97i
    output from 23.976 input. - Soft: produces 23.976; the player converts this
    output to 29.97i.
    """
    NONE = "NONE"
    SOFT = "SOFT"
    HARD = "HARD"


class H265TemporalAdaptiveQuantization(str):
    """
    Adjust quantization within each frame based on temporal variation of content
    complexity.
    """
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H265TemporalIds(str):
    """
    Enables temporal layer identifiers in the encoded bitstream. Up to 3 layers are
    supported depending on GOP structure: I- and P-frames form one layer, reference
    B-frames can form a second layer and non-reference b-frames can form a third
    layer. Decoders can optionally decode only the lower temporal layers to generate
    a lower frame rate output. For example, given a bitstream with temporal IDs and
    with b-frames = 1 (i.e. IbPbPb display order), a decoder could decode all the
    frames for full frame rate output or only the I and P frames (lowest temporal
    layer) for a half frame rate output.
    """
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H265Tiles(str):
    """
    Enable use of tiles, allowing horizontal as well as vertical subdivision of the
    encoded pictures.
    """
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H265UnregisteredSeiTimecode(str):
    """
    Inserts timecode for each frame as 4 bytes of an unregistered SEI message.
    """
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class H265WriteMp4PackagingType(str):
    """
    If HVC1, output that is H.265 will be marked as HVC1 and adhere to the ISO-
    IECJTC1-SC29_N13798_Text_ISOIEC_FDIS_14496-15_3rd_E spec which states that
    parameter set NAL units will be stored in the sample headers but not in the
    samples directly. If HEV1, then H.265 will be marked as HEV1 and parameter set
    NAL units will be written into the samples.
    """
    HVC1 = "HVC1"
    HEV1 = "HEV1"


@dataclasses.dataclass
class Hdr10Metadata(ShapeBase):
    """
    Use the HDR master display (Hdr10Metadata) settings to correct HDR metadata or
    to provide missing metadata. These values vary depending on the input video and
    must be provided by a color grader. Range is 0 to 50,000, each increment
    represents 0.00002 in CIE1931 color coordinate. Note that these settings are not
    color correction. Note that if you are creating HDR outputs inside of an HLS
    CMAF package, to comply with the Apple specification, you must use the HVC1 for
    H.265 setting.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "blue_primary_x",
                "BluePrimaryX",
                TypeInfo(int),
            ),
            (
                "blue_primary_y",
                "BluePrimaryY",
                TypeInfo(int),
            ),
            (
                "green_primary_x",
                "GreenPrimaryX",
                TypeInfo(int),
            ),
            (
                "green_primary_y",
                "GreenPrimaryY",
                TypeInfo(int),
            ),
            (
                "max_content_light_level",
                "MaxContentLightLevel",
                TypeInfo(int),
            ),
            (
                "max_frame_average_light_level",
                "MaxFrameAverageLightLevel",
                TypeInfo(int),
            ),
            (
                "max_luminance",
                "MaxLuminance",
                TypeInfo(int),
            ),
            (
                "min_luminance",
                "MinLuminance",
                TypeInfo(int),
            ),
            (
                "red_primary_x",
                "RedPrimaryX",
                TypeInfo(int),
            ),
            (
                "red_primary_y",
                "RedPrimaryY",
                TypeInfo(int),
            ),
            (
                "white_point_x",
                "WhitePointX",
                TypeInfo(int),
            ),
            (
                "white_point_y",
                "WhitePointY",
                TypeInfo(int),
            ),
        ]

    # HDR Master Display Information must be provided by a color grader, using
    # color grading tools. Range is 0 to 50,000, each increment represents
    # 0.00002 in CIE1931 color coordinate. Note that this setting is not for
    # color correction.
    blue_primary_x: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # HDR Master Display Information must be provided by a color grader, using
    # color grading tools. Range is 0 to 50,000, each increment represents
    # 0.00002 in CIE1931 color coordinate. Note that this setting is not for
    # color correction.
    blue_primary_y: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # HDR Master Display Information must be provided by a color grader, using
    # color grading tools. Range is 0 to 50,000, each increment represents
    # 0.00002 in CIE1931 color coordinate. Note that this setting is not for
    # color correction.
    green_primary_x: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # HDR Master Display Information must be provided by a color grader, using
    # color grading tools. Range is 0 to 50,000, each increment represents
    # 0.00002 in CIE1931 color coordinate. Note that this setting is not for
    # color correction.
    green_primary_y: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Maximum light level among all samples in the coded video sequence, in units
    # of candelas per square meter.
    max_content_light_level: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Maximum average light level of any frame in the coded video sequence, in
    # units of candelas per square meter.
    max_frame_average_light_level: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Nominal maximum mastering display luminance in units of of 0.0001 candelas
    # per square meter.
    max_luminance: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Nominal minimum mastering display luminance in units of of 0.0001 candelas
    # per square meter
    min_luminance: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # HDR Master Display Information must be provided by a color grader, using
    # color grading tools. Range is 0 to 50,000, each increment represents
    # 0.00002 in CIE1931 color coordinate. Note that this setting is not for
    # color correction.
    red_primary_x: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # HDR Master Display Information must be provided by a color grader, using
    # color grading tools. Range is 0 to 50,000, each increment represents
    # 0.00002 in CIE1931 color coordinate. Note that this setting is not for
    # color correction.
    red_primary_y: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # HDR Master Display Information must be provided by a color grader, using
    # color grading tools. Range is 0 to 50,000, each increment represents
    # 0.00002 in CIE1931 color coordinate. Note that this setting is not for
    # color correction.
    white_point_x: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # HDR Master Display Information must be provided by a color grader, using
    # color grading tools. Range is 0 to 50,000, each increment represents
    # 0.00002 in CIE1931 color coordinate. Note that this setting is not for
    # color correction.
    white_point_y: int = dataclasses.field(default=ShapeBase.NOT_SET, )


class HlsAdMarkers(str):
    ELEMENTAL = "ELEMENTAL"
    ELEMENTAL_SCTE35 = "ELEMENTAL_SCTE35"


class HlsAudioTrackType(str):
    """
    Four types of audio-only tracks are supported: Audio-Only Variant Stream The
    client can play back this audio-only stream instead of video in low-bandwidth
    scenarios. Represented as an EXT-X-STREAM-INF in the HLS manifest. Alternate
    Audio, Auto Select, Default Alternate rendition that the client should try to
    play back by default. Represented as an EXT-X-MEDIA in the HLS manifest with
    DEFAULT=YES, AUTOSELECT=YES Alternate Audio, Auto Select, Not Default Alternate
    rendition that the client may try to play back by default. Represented as an
    EXT-X-MEDIA in the HLS manifest with DEFAULT=NO, AUTOSELECT=YES Alternate Audio,
    not Auto Select Alternate rendition that the client will not try to play back by
    default. Represented as an EXT-X-MEDIA in the HLS manifest with DEFAULT=NO,
    AUTOSELECT=NO
    """
    ALTERNATE_AUDIO_AUTO_SELECT_DEFAULT = "ALTERNATE_AUDIO_AUTO_SELECT_DEFAULT"
    ALTERNATE_AUDIO_AUTO_SELECT = "ALTERNATE_AUDIO_AUTO_SELECT"
    ALTERNATE_AUDIO_NOT_AUTO_SELECT = "ALTERNATE_AUDIO_NOT_AUTO_SELECT"
    AUDIO_ONLY_VARIANT_STREAM = "AUDIO_ONLY_VARIANT_STREAM"


@dataclasses.dataclass
class HlsCaptionLanguageMapping(ShapeBase):
    """
    Caption Language Mapping
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
                "custom_language_code",
                "CustomLanguageCode",
                TypeInfo(str),
            ),
            (
                "language_code",
                "LanguageCode",
                TypeInfo(typing.Union[str, LanguageCode]),
            ),
            (
                "language_description",
                "LanguageDescription",
                TypeInfo(str),
            ),
        ]

    # Caption channel.
    caption_channel: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specify the language for this caption channel, using the ISO 639-2 or ISO
    # 639-3 three-letter language code
    custom_language_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specify the language, using the ISO 639-2 three-letter code listed at
    # https://www.loc.gov/standards/iso639-2/php/code_list.php.
    language_code: typing.Union[str, "LanguageCode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Caption language description.
    language_description: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class HlsCaptionLanguageSetting(str):
    """
    Applies only to 608 Embedded output captions. Insert: Include CLOSED-CAPTIONS
    lines in the manifest. Specify at least one language in the CC1 Language Code
    field. One CLOSED-CAPTION line is added for each Language Code you specify. Make
    sure to specify the languages in the order in which they appear in the original
    source (if the source is embedded format) or the order of the caption selectors
    (if the source is other than embedded). Otherwise, languages in the manifest
    will not match up properly with the output captions. None: Include CLOSED-
    CAPTIONS=NONE line in the manifest. Omit: Omit any CLOSED-CAPTIONS line from the
    manifest.
    """
    INSERT = "INSERT"
    OMIT = "OMIT"
    NONE = "NONE"


class HlsClientCache(str):
    """
    When set to ENABLED, sets #EXT-X-ALLOW-CACHE:no tag, which prevents client from
    saving media segments for later replay.
    """
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class HlsCodecSpecification(str):
    """
    Specification to use (RFC-6381 or the default RFC-4281) during m3u8 playlist
    generation.
    """
    RFC_6381 = "RFC_6381"
    RFC_4281 = "RFC_4281"


class HlsDirectoryStructure(str):
    """
    Indicates whether segments should be placed in subdirectories.
    """
    SINGLE_DIRECTORY = "SINGLE_DIRECTORY"
    SUBDIRECTORY_PER_STREAM = "SUBDIRECTORY_PER_STREAM"


@dataclasses.dataclass
class HlsEncryptionSettings(ShapeBase):
    """
    Settings for HLS encryption
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "constant_initialization_vector",
                "ConstantInitializationVector",
                TypeInfo(str),
            ),
            (
                "encryption_method",
                "EncryptionMethod",
                TypeInfo(typing.Union[str, HlsEncryptionType]),
            ),
            (
                "initialization_vector_in_manifest",
                "InitializationVectorInManifest",
                TypeInfo(typing.Union[str, HlsInitializationVectorInManifest]),
            ),
            (
                "speke_key_provider",
                "SpekeKeyProvider",
                TypeInfo(SpekeKeyProvider),
            ),
            (
                "static_key_provider",
                "StaticKeyProvider",
                TypeInfo(StaticKeyProvider),
            ),
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, HlsKeyProviderType]),
            ),
        ]

    # This is a 128-bit, 16-byte hex value represented by a 32-character text
    # string. If this parameter is not set then the Initialization Vector will
    # follow the segment number by default.
    constant_initialization_vector: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Encrypts the segments with the given encryption scheme. Leave blank to
    # disable. Selecting 'Disabled' in the web interface also disables
    # encryption.
    encryption_method: typing.Union[str, "HlsEncryptionType"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # The Initialization Vector is a 128-bit number used in conjunction with the
    # key for encrypting blocks. If set to INCLUDE, Initialization Vector is
    # listed in the manifest. Otherwise Initialization Vector is not in the
    # manifest.
    initialization_vector_in_manifest: typing.Union[
        str, "HlsInitializationVectorInManifest"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # Settings for use with a SPEKE key provider
    speke_key_provider: "SpekeKeyProvider" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Settings for use with a SPEKE key provider.
    static_key_provider: "StaticKeyProvider" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates which type of key provider is used for encryption.
    type: typing.Union[str, "HlsKeyProviderType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class HlsEncryptionType(str):
    """
    Encrypts the segments with the given encryption scheme. Leave blank to disable.
    Selecting 'Disabled' in the web interface also disables encryption.
    """
    AES128 = "AES128"
    SAMPLE_AES = "SAMPLE_AES"


@dataclasses.dataclass
class HlsGroupSettings(ShapeBase):
    """
    Required when you set (Type) under (OutputGroups)>(OutputGroupSettings) to
    HLS_GROUP_SETTINGS.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ad_markers",
                "AdMarkers",
                TypeInfo(typing.List[typing.Union[str, HlsAdMarkers]]),
            ),
            (
                "base_url",
                "BaseUrl",
                TypeInfo(str),
            ),
            (
                "caption_language_mappings",
                "CaptionLanguageMappings",
                TypeInfo(typing.List[HlsCaptionLanguageMapping]),
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
                "destination",
                "Destination",
                TypeInfo(str),
            ),
            (
                "directory_structure",
                "DirectoryStructure",
                TypeInfo(typing.Union[str, HlsDirectoryStructure]),
            ),
            (
                "encryption",
                "Encryption",
                TypeInfo(HlsEncryptionSettings),
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
                "min_final_segment_length",
                "MinFinalSegmentLength",
                TypeInfo(float),
            ),
            (
                "min_segment_length",
                "MinSegmentLength",
                TypeInfo(int),
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
                "segment_control",
                "SegmentControl",
                TypeInfo(typing.Union[str, HlsSegmentControl]),
            ),
            (
                "segment_length",
                "SegmentLength",
                TypeInfo(int),
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
        ]

    # Choose one or more ad marker types to pass SCTE35 signals through to this
    # group of Apple HLS outputs.
    ad_markers: typing.List[typing.Union[str, "HlsAdMarkers"]
                           ] = dataclasses.field(
                               default=ShapeBase.NOT_SET,
                           )

    # A partial URI prefix that will be prepended to each output in the media
    # .m3u8 file. Can be used if base manifest is delivered from a different URL
    # than the main .m3u8 file.
    base_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Language to be used on Caption outputs
    caption_language_mappings: typing.List["HlsCaptionLanguageMapping"
                                          ] = dataclasses.field(
                                              default=ShapeBase.NOT_SET,
                                          )

    # Applies only to 608 Embedded output captions. Insert: Include CLOSED-
    # CAPTIONS lines in the manifest. Specify at least one language in the CC1
    # Language Code field. One CLOSED-CAPTION line is added for each Language
    # Code you specify. Make sure to specify the languages in the order in which
    # they appear in the original source (if the source is embedded format) or
    # the order of the caption selectors (if the source is other than embedded).
    # Otherwise, languages in the manifest will not match up properly with the
    # output captions. None: Include CLOSED-CAPTIONS=NONE line in the manifest.
    # Omit: Omit any CLOSED-CAPTIONS line from the manifest.
    caption_language_setting: typing.Union[str, "HlsCaptionLanguageSetting"
                                          ] = dataclasses.field(
                                              default=ShapeBase.NOT_SET,
                                          )

    # When set to ENABLED, sets #EXT-X-ALLOW-CACHE:no tag, which prevents client
    # from saving media segments for later replay.
    client_cache: typing.Union[str, "HlsClientCache"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specification to use (RFC-6381 or the default RFC-4281) during m3u8
    # playlist generation.
    codec_specification: typing.Union[str, "HlsCodecSpecification"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # Use Destination (Destination) to specify the S3 output location and the
    # output filename base. Destination accepts format identifiers. If you do not
    # specify the base filename in the URI, the service will use the filename of
    # the input file. If your job has multiple inputs, the service uses the
    # filename of the first input file.
    destination: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether segments should be placed in subdirectories.
    directory_structure: typing.Union[str, "HlsDirectoryStructure"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # DRM settings.
    encryption: "HlsEncryptionSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When set to GZIP, compresses HLS playlist.
    manifest_compression: typing.Union[str, "HlsManifestCompression"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    # Indicates whether the output manifest should use floating point values for
    # segment duration.
    manifest_duration_format: typing.Union[str, "HlsManifestDurationFormat"
                                          ] = dataclasses.field(
                                              default=ShapeBase.NOT_SET,
                                          )

    # Keep this setting at the default value of 0, unless you are troubleshooting
    # a problem with how devices play back the end of your video asset. If you
    # know that player devices are hanging on the final segment of your video
    # because the length of your final segment is too short, use this setting to
    # specify a minimum final segment length, in seconds. Choose a value that is
    # greater than or equal to 1 and less than your segment length. When you
    # specify a value for this setting, the encoder will combine any final
    # segment that is shorter than the length that you specify with the previous
    # segment. For example, your segment length is 3 seconds and your final
    # segment is .5 seconds without a minimum final segment length; when you set
    # the minimum final segment length to 1, your final segment is 3.5 seconds.
    min_final_segment_length: float = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When set, Minimum Segment Size is enforced by looking ahead and back within
    # the specified range for a nearby avail and extending the segment size if
    # needed.
    min_segment_length: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether the .m3u8 manifest file should be generated for this HLS
    # output group.
    output_selection: typing.Union[str, "HlsOutputSelection"
                                  ] = dataclasses.field(
                                      default=ShapeBase.NOT_SET,
                                  )

    # Includes or excludes EXT-X-PROGRAM-DATE-TIME tag in .m3u8 manifest files.
    # The value is calculated as follows: either the program date and time are
    # initialized using the input timecode source, or the time is initialized
    # using the input timecode source and the date is initialized using the
    # timestamp_offset.
    program_date_time: typing.Union[str, "HlsProgramDateTime"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # Period of insertion of EXT-X-PROGRAM-DATE-TIME entry, in seconds.
    program_date_time_period: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When set to SINGLE_FILE, emits program as a single media resource (.ts)
    # file, uses #EXT-X-BYTERANGE tags to index segment for playback.
    segment_control: typing.Union[str, "HlsSegmentControl"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Length of MPEG-2 Transport Stream segments to create (in seconds). Note
    # that segments will end on the next keyframe after this number of seconds,
    # so actual segment length may be longer.
    segment_length: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Number of segments to write to a subdirectory before starting a new one.
    # directoryStructure must be SINGLE_DIRECTORY for this setting to have an
    # effect.
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


class HlsIFrameOnlyManifest(str):
    """
    When set to INCLUDE, writes I-Frame Only Manifest in addition to the HLS
    manifest
    """
    INCLUDE = "INCLUDE"
    EXCLUDE = "EXCLUDE"


class HlsInitializationVectorInManifest(str):
    """
    The Initialization Vector is a 128-bit number used in conjunction with the key
    for encrypting blocks. If set to INCLUDE, Initialization Vector is listed in the
    manifest. Otherwise Initialization Vector is not in the manifest.
    """
    INCLUDE = "INCLUDE"
    EXCLUDE = "EXCLUDE"


class HlsKeyProviderType(str):
    """
    Indicates which type of key provider is used for encryption.
    """
    SPEKE = "SPEKE"
    STATIC_KEY = "STATIC_KEY"


class HlsManifestCompression(str):
    """
    When set to GZIP, compresses HLS playlist.
    """
    GZIP = "GZIP"
    NONE = "NONE"


class HlsManifestDurationFormat(str):
    """
    Indicates whether the output manifest should use floating point values for
    segment duration.
    """
    FLOATING_POINT = "FLOATING_POINT"
    INTEGER = "INTEGER"


class HlsOutputSelection(str):
    """
    Indicates whether the .m3u8 manifest file should be generated for this HLS
    output group.
    """
    MANIFESTS_AND_SEGMENTS = "MANIFESTS_AND_SEGMENTS"
    SEGMENTS_ONLY = "SEGMENTS_ONLY"


class HlsProgramDateTime(str):
    """
    Includes or excludes EXT-X-PROGRAM-DATE-TIME tag in .m3u8 manifest files. The
    value is calculated as follows: either the program date and time are initialized
    using the input timecode source, or the time is initialized using the input
    timecode source and the date is initialized using the timestamp_offset.
    """
    INCLUDE = "INCLUDE"
    EXCLUDE = "EXCLUDE"


class HlsSegmentControl(str):
    """
    When set to SINGLE_FILE, emits program as a single media resource (.ts) file,
    uses #EXT-X-BYTERANGE tags to index segment for playback.
    """
    SINGLE_FILE = "SINGLE_FILE"
    SEGMENTED_FILES = "SEGMENTED_FILES"


@dataclasses.dataclass
class HlsSettings(ShapeBase):
    """
    Settings for HLS output groups
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
                "audio_rendition_sets",
                "AudioRenditionSets",
                TypeInfo(str),
            ),
            (
                "audio_track_type",
                "AudioTrackType",
                TypeInfo(typing.Union[str, HlsAudioTrackType]),
            ),
            (
                "i_frame_only_manifest",
                "IFrameOnlyManifest",
                TypeInfo(typing.Union[str, HlsIFrameOnlyManifest]),
            ),
            (
                "segment_modifier",
                "SegmentModifier",
                TypeInfo(str),
            ),
        ]

    # Specifies the group to which the audio Rendition belongs.
    audio_group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # List all the audio groups that are used with the video output stream. Input
    # all the audio GROUP-IDs that are associated to the video, separate by ','.
    audio_rendition_sets: str = dataclasses.field(default=ShapeBase.NOT_SET, )

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
    audio_track_type: typing.Union[str, "HlsAudioTrackType"
                                  ] = dataclasses.field(
                                      default=ShapeBase.NOT_SET,
                                  )

    # When set to INCLUDE, writes I-Frame Only Manifest in addition to the HLS
    # manifest
    i_frame_only_manifest: typing.Union[str, "HlsIFrameOnlyManifest"
                                       ] = dataclasses.field(
                                           default=ShapeBase.NOT_SET,
                                       )

    # String concatenated to end of segment filenames. Accepts "Format
    # Identifiers":#format_identifier_parameters.
    segment_modifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class HlsStreamInfResolution(str):
    """
    Include or exclude RESOLUTION attribute for video in EXT-X-STREAM-INF tag of
    variant manifest.
    """
    INCLUDE = "INCLUDE"
    EXCLUDE = "EXCLUDE"


class HlsTimedMetadataId3Frame(str):
    """
    Indicates ID3 frame that has the timecode.
    """
    NONE = "NONE"
    PRIV = "PRIV"
    TDRL = "TDRL"


@dataclasses.dataclass
class Id3Insertion(ShapeBase):
    """
    To insert ID3 tags in your output, specify two values. Use ID3 tag (Id3) to
    specify the base 64 encoded string and use Timecode (TimeCode) to specify the
    time when the tag should be inserted. To insert multiple ID3 tags in your
    output, create multiple instances of ID3 insertion (Id3Insertion).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id3",
                "Id3",
                TypeInfo(str),
            ),
            (
                "timecode",
                "Timecode",
                TypeInfo(str),
            ),
        ]

    # Use ID3 tag (Id3) to provide a tag value in base64-encode format.
    id3: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Provide a Timecode (TimeCode) in HH:MM:SS:FF or HH:MM:SS;FF format.
    timecode: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ImageInserter(ShapeBase):
    """
    Enable the Image inserter (ImageInserter) feature to include a graphic overlay
    on your video. Enable or disable this feature for each output individually. This
    setting is disabled by default.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "insertable_images",
                "InsertableImages",
                TypeInfo(typing.List[InsertableImage]),
            ),
        ]

    # Image to insert. Must be 32 bit windows BMP, PNG, or TGA file. Must not be
    # larger than the output frames.
    insertable_images: typing.List["InsertableImage"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Input(ShapeBase):
    """
    Specifies media input
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "audio_selector_groups",
                "AudioSelectorGroups",
                TypeInfo(typing.Dict[str, AudioSelectorGroup]),
            ),
            (
                "audio_selectors",
                "AudioSelectors",
                TypeInfo(typing.Dict[str, AudioSelector]),
            ),
            (
                "caption_selectors",
                "CaptionSelectors",
                TypeInfo(typing.Dict[str, CaptionSelector]),
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
                "file_input",
                "FileInput",
                TypeInfo(str),
            ),
            (
                "filter_enable",
                "FilterEnable",
                TypeInfo(typing.Union[str, InputFilterEnable]),
            ),
            (
                "filter_strength",
                "FilterStrength",
                TypeInfo(int),
            ),
            (
                "input_clippings",
                "InputClippings",
                TypeInfo(typing.List[InputClipping]),
            ),
            (
                "program_number",
                "ProgramNumber",
                TypeInfo(int),
            ),
            (
                "psi_control",
                "PsiControl",
                TypeInfo(typing.Union[str, InputPsiControl]),
            ),
            (
                "timecode_source",
                "TimecodeSource",
                TypeInfo(typing.Union[str, InputTimecodeSource]),
            ),
            (
                "video_selector",
                "VideoSelector",
                TypeInfo(VideoSelector),
            ),
        ]

    # Specifies set of audio selectors within an input to combine. An input may
    # have multiple audio selector groups. See "Audio Selector Group":#inputs-
    # audio_selector_group for more information.
    audio_selector_groups: typing.Dict[str, "AudioSelectorGroup"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    # Use Audio selectors (AudioSelectors) to specify a track or set of tracks
    # from the input that you will use in your outputs. You can use mutiple Audio
    # selectors per input.
    audio_selectors: typing.Dict[str, "AudioSelector"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Use Captions selectors (CaptionSelectors) to specify the captions data from
    # the input that you will use in your outputs. You can use mutiple captions
    # selectors per input.
    caption_selectors: typing.Dict[str, "CaptionSelector"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Enable Deblock (InputDeblockFilter) to produce smoother motion in the
    # output. Default is disabled. Only manaully controllable for MPEG2 and
    # uncompressed video inputs.
    deblock_filter: typing.Union[str, "InputDeblockFilter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Enable Denoise (InputDenoiseFilter) to filter noise from the input. Default
    # is disabled. Only applicable to MPEG2, H.264, H.265, and uncompressed video
    # inputs.
    denoise_filter: typing.Union[str, "InputDenoiseFilter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Use Input (fileInput) to define the source file used in the transcode job.
    # There can be multiple inputs in a job. These inputs are concantenated, in
    # the order they are specified in the job, to create the output.
    file_input: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use Filter enable (InputFilterEnable) to specify how the transcoding
    # service applies the denoise and deblock filters. You must also enable the
    # filters separately, with Denoise (InputDenoiseFilter) and Deblock
    # (InputDeblockFilter). * Auto - The transcoding service determines whether
    # to apply filtering, depending on input type and quality. * Disable - The
    # input is not filtered. This is true even if you use the API to enable them
    # in (InputDeblockFilter) and (InputDeblockFilter). * Force - The in put is
    # filtered regardless of input type.
    filter_enable: typing.Union[str, "InputFilterEnable"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Use Filter strength (FilterStrength) to adjust the magnitude the input
    # filter settings (Deblock and Denoise). The range is -5 to 5. Default is 0.
    filter_strength: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (InputClippings) contains sets of start and end times that together specify
    # a portion of the input to be used in the outputs. If you provide only a
    # start time, the clip will be the entire input from that point to the end.
    # If you provide only an end time, it will be the entire input up to that
    # point. When you specify more than one input clip, the transcoding service
    # creates the job outputs by stringing the clips together in the order you
    # specify them.
    input_clippings: typing.List["InputClipping"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Use Program (programNumber) to select a specific program from within a
    # multi-program transport stream. Note that Quad 4K is not currently
    # supported. Default is the first program within the transport stream. If the
    # program you specify doesn't exist, the transcoding service will use this
    # default.
    program_number: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Set PSI control (InputPsiControl) for transport stream inputs to specify
    # which data the demux process to scans. * Ignore PSI - Scan all PIDs for
    # audio and video. * Use PSI - Scan only PSI data.
    psi_control: typing.Union[str, "InputPsiControl"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Timecode source under input settings (InputTimecodeSource) only affects the
    # behavior of features that apply to a single input at a time, such as input
    # clipping and synchronizing some captions formats. Use this setting to
    # specify whether the service counts frames by timecodes embedded in the
    # video (EMBEDDED) or by starting the first frame at zero (ZEROBASED). In
    # both cases, the timecode format is HH:MM:SS:FF or HH:MM:SS;FF, where FF is
    # the frame number. Only set this to EMBEDDED if your source video has
    # embedded timecodes.
    timecode_source: typing.Union[str, "InputTimecodeSource"
                                 ] = dataclasses.field(
                                     default=ShapeBase.NOT_SET,
                                 )

    # Selector for video.
    video_selector: "VideoSelector" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InputClipping(ShapeBase):
    """
    To transcode only portions of your input (clips), include one Input clipping
    (one instance of InputClipping in the JSON job file) for each input clip. All
    input clips you specify will be included in every output of the job.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "end_timecode",
                "EndTimecode",
                TypeInfo(str),
            ),
            (
                "start_timecode",
                "StartTimecode",
                TypeInfo(str),
            ),
        ]

    # Set End timecode (EndTimecode) to the end of the portion of the input you
    # are clipping. The frame corresponding to the End timecode value is included
    # in the clip. Start timecode or End timecode may be left blank, but not
    # both. Use the format HH:MM:SS:FF or HH:MM:SS;FF, where HH is the hour, MM
    # is the minute, SS is the second, and FF is the frame number. When choosing
    # this value, take into account your setting for timecode source under input
    # settings (InputTimecodeSource). For example, if you have embedded timecodes
    # that start at 01:00:00:00 and you want your clip to end six minutes into
    # the video, use 01:06:00:00.
    end_timecode: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Set Start timecode (StartTimecode) to the beginning of the portion of the
    # input you are clipping. The frame corresponding to the Start timecode value
    # is included in the clip. Start timecode or End timecode may be left blank,
    # but not both. Use the format HH:MM:SS:FF or HH:MM:SS;FF, where HH is the
    # hour, MM is the minute, SS is the second, and FF is the frame number. When
    # choosing this value, take into account your setting for Input timecode
    # source. For example, if you have embedded timecodes that start at
    # 01:00:00:00 and you want your clip to begin five minutes into the video,
    # use 01:05:00:00.
    start_timecode: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class InputDeblockFilter(str):
    """
    Enable Deblock (InputDeblockFilter) to produce smoother motion in the output.
    Default is disabled. Only manaully controllable for MPEG2 and uncompressed video
    inputs.
    """
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class InputDenoiseFilter(str):
    """
    Enable Denoise (InputDenoiseFilter) to filter noise from the input. Default is
    disabled. Only applicable to MPEG2, H.264, H.265, and uncompressed video inputs.
    """
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class InputFilterEnable(str):
    """
    Use Filter enable (InputFilterEnable) to specify how the transcoding service
    applies the denoise and deblock filters. You must also enable the filters
    separately, with Denoise (InputDenoiseFilter) and Deblock (InputDeblockFilter).
    * Auto - The transcoding service determines whether to apply filtering,
    depending on input type and quality. * Disable - The input is not filtered. This
    is true even if you use the API to enable them in (InputDeblockFilter) and
    (InputDeblockFilter). * Force - The in put is filtered regardless of input type.
    """
    AUTO = "AUTO"
    DISABLE = "DISABLE"
    FORCE = "FORCE"


class InputPsiControl(str):
    """
    Set PSI control (InputPsiControl) for transport stream inputs to specify which
    data the demux process to scans. * Ignore PSI - Scan all PIDs for audio and
    video. * Use PSI - Scan only PSI data.
    """
    IGNORE_PSI = "IGNORE_PSI"
    USE_PSI = "USE_PSI"


@dataclasses.dataclass
class InputTemplate(ShapeBase):
    """
    Specified video input in a template.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "audio_selector_groups",
                "AudioSelectorGroups",
                TypeInfo(typing.Dict[str, AudioSelectorGroup]),
            ),
            (
                "audio_selectors",
                "AudioSelectors",
                TypeInfo(typing.Dict[str, AudioSelector]),
            ),
            (
                "caption_selectors",
                "CaptionSelectors",
                TypeInfo(typing.Dict[str, CaptionSelector]),
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
                "filter_enable",
                "FilterEnable",
                TypeInfo(typing.Union[str, InputFilterEnable]),
            ),
            (
                "filter_strength",
                "FilterStrength",
                TypeInfo(int),
            ),
            (
                "input_clippings",
                "InputClippings",
                TypeInfo(typing.List[InputClipping]),
            ),
            (
                "program_number",
                "ProgramNumber",
                TypeInfo(int),
            ),
            (
                "psi_control",
                "PsiControl",
                TypeInfo(typing.Union[str, InputPsiControl]),
            ),
            (
                "timecode_source",
                "TimecodeSource",
                TypeInfo(typing.Union[str, InputTimecodeSource]),
            ),
            (
                "video_selector",
                "VideoSelector",
                TypeInfo(VideoSelector),
            ),
        ]

    # Specifies set of audio selectors within an input to combine. An input may
    # have multiple audio selector groups. See "Audio Selector Group":#inputs-
    # audio_selector_group for more information.
    audio_selector_groups: typing.Dict[str, "AudioSelectorGroup"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    # Use Audio selectors (AudioSelectors) to specify a track or set of tracks
    # from the input that you will use in your outputs. You can use mutiple Audio
    # selectors per input.
    audio_selectors: typing.Dict[str, "AudioSelector"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Use Captions selectors (CaptionSelectors) to specify the captions data from
    # the input that you will use in your outputs. You can use mutiple captions
    # selectors per input.
    caption_selectors: typing.Dict[str, "CaptionSelector"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Enable Deblock (InputDeblockFilter) to produce smoother motion in the
    # output. Default is disabled. Only manaully controllable for MPEG2 and
    # uncompressed video inputs.
    deblock_filter: typing.Union[str, "InputDeblockFilter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Enable Denoise (InputDenoiseFilter) to filter noise from the input. Default
    # is disabled. Only applicable to MPEG2, H.264, H.265, and uncompressed video
    # inputs.
    denoise_filter: typing.Union[str, "InputDenoiseFilter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Use Filter enable (InputFilterEnable) to specify how the transcoding
    # service applies the denoise and deblock filters. You must also enable the
    # filters separately, with Denoise (InputDenoiseFilter) and Deblock
    # (InputDeblockFilter). * Auto - The transcoding service determines whether
    # to apply filtering, depending on input type and quality. * Disable - The
    # input is not filtered. This is true even if you use the API to enable them
    # in (InputDeblockFilter) and (InputDeblockFilter). * Force - The in put is
    # filtered regardless of input type.
    filter_enable: typing.Union[str, "InputFilterEnable"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Use Filter strength (FilterStrength) to adjust the magnitude the input
    # filter settings (Deblock and Denoise). The range is -5 to 5. Default is 0.
    filter_strength: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (InputClippings) contains sets of start and end times that together specify
    # a portion of the input to be used in the outputs. If you provide only a
    # start time, the clip will be the entire input from that point to the end.
    # If you provide only an end time, it will be the entire input up to that
    # point. When you specify more than one input clip, the transcoding service
    # creates the job outputs by stringing the clips together in the order you
    # specify them.
    input_clippings: typing.List["InputClipping"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Use Program (programNumber) to select a specific program from within a
    # multi-program transport stream. Note that Quad 4K is not currently
    # supported. Default is the first program within the transport stream. If the
    # program you specify doesn't exist, the transcoding service will use this
    # default.
    program_number: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Set PSI control (InputPsiControl) for transport stream inputs to specify
    # which data the demux process to scans. * Ignore PSI - Scan all PIDs for
    # audio and video. * Use PSI - Scan only PSI data.
    psi_control: typing.Union[str, "InputPsiControl"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Timecode source under input settings (InputTimecodeSource) only affects the
    # behavior of features that apply to a single input at a time, such as input
    # clipping and synchronizing some captions formats. Use this setting to
    # specify whether the service counts frames by timecodes embedded in the
    # video (EMBEDDED) or by starting the first frame at zero (ZEROBASED). In
    # both cases, the timecode format is HH:MM:SS:FF or HH:MM:SS;FF, where FF is
    # the frame number. Only set this to EMBEDDED if your source video has
    # embedded timecodes.
    timecode_source: typing.Union[str, "InputTimecodeSource"
                                 ] = dataclasses.field(
                                     default=ShapeBase.NOT_SET,
                                 )

    # Selector for video.
    video_selector: "VideoSelector" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class InputTimecodeSource(str):
    """
    Timecode source under input settings (InputTimecodeSource) only affects the
    behavior of features that apply to a single input at a time, such as input
    clipping and synchronizing some captions formats. Use this setting to specify
    whether the service counts frames by timecodes embedded in the video (EMBEDDED)
    or by starting the first frame at zero (ZEROBASED). In both cases, the timecode
    format is HH:MM:SS:FF or HH:MM:SS;FF, where FF is the frame number. Only set
    this to EMBEDDED if your source video has embedded timecodes.
    """
    EMBEDDED = "EMBEDDED"
    ZEROBASED = "ZEROBASED"
    SPECIFIEDSTART = "SPECIFIEDSTART"


@dataclasses.dataclass
class InsertableImage(ShapeBase):
    """
    Settings for Insertable Image
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
                "image_inserter_input",
                "ImageInserterInput",
                TypeInfo(str),
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
                "start_time",
                "StartTime",
                TypeInfo(str),
            ),
            (
                "width",
                "Width",
                TypeInfo(int),
            ),
        ]

    # Use Duration (Duration) to set the time, in milliseconds, for the image to
    # remain on the output video.
    duration: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use Fade in (FadeIut) to set the length, in milliseconds, of the inserted
    # image fade in. If you don't specify a value for Fade in, the image will
    # appear abruptly at the Start time.
    fade_in: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use Fade out (FadeOut) to set the length, in milliseconds, of the inserted
    # image fade out. If you don't specify a value for Fade out, the image will
    # disappear abruptly at the end of the inserted image duration.
    fade_out: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specify the Height (Height) of the inserted image. Use a value that is less
    # than or equal to the video resolution height. Leave this setting blank to
    # use the native height of the image.
    height: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use Image location (imageInserterInput) to specify the Amazon S3 location
    # of the image to be inserted into the output. Use a 32 bit BMP, PNG, or TGA
    # file that fits inside the video frame.
    image_inserter_input: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use Left (ImageX) to set the distance, in pixels, between the inserted
    # image and the left edge of the frame. Required for BMP, PNG and TGA input.
    image_x: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use Top (ImageY) to set the distance, in pixels, between the inserted image
    # and the top edge of the video frame. Required for BMP, PNG and TGA input.
    image_y: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use Layer (Layer) to specify how overlapping inserted images appear. Images
    # with higher values of layer appear on top of images with lower values of
    # layer.
    layer: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use Opacity (Opacity) to specify how much of the underlying video shows
    # through the inserted image. 0 is transparent and 100 is fully opaque.
    # Default is 50.
    opacity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use Start time (StartTime) to specify the video timecode when the image is
    # inserted in the output. This must be in timecode (HH:MM:SS:FF or
    # HH:MM:SS;FF) format.
    start_time: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specify the Width (Width) of the inserted image. Use a value that is less
    # than or equal to the video resolution width. Leave this setting blank to
    # use the native width of the image.
    width: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InternalServerErrorException(ShapeBase):
    """
    The service encountered an unexpected condition and can't fulfill your request.
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

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Job(ShapeBase):
    """
    Each job converts an input file into an output file or files. For more
    information, see the User Guide at
    http://docs.aws.amazon.com/mediaconvert/latest/ug/what-is.html
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "role",
                "Role",
                TypeInfo(str),
            ),
            (
                "settings",
                "Settings",
                TypeInfo(JobSettings),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "billing_tags_source",
                "BillingTagsSource",
                TypeInfo(typing.Union[str, BillingTagsSource]),
            ),
            (
                "created_at",
                "CreatedAt",
                TypeInfo(datetime.datetime),
            ),
            (
                "error_code",
                "ErrorCode",
                TypeInfo(int),
            ),
            (
                "error_message",
                "ErrorMessage",
                TypeInfo(str),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "job_template",
                "JobTemplate",
                TypeInfo(str),
            ),
            (
                "output_group_details",
                "OutputGroupDetails",
                TypeInfo(typing.List[OutputGroupDetail]),
            ),
            (
                "queue",
                "Queue",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, JobStatus]),
            ),
            (
                "timing",
                "Timing",
                TypeInfo(Timing),
            ),
            (
                "user_metadata",
                "UserMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The IAM role you use for creating this job. For details about permissions,
    # see the User Guide topic at the User Guide at
    # http://docs.aws.amazon.com/mediaconvert/latest/ug/iam-role.html
    role: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # JobSettings contains all the transcode settings for a job.
    settings: "JobSettings" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An identifier for this resource that is unique within all of AWS.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Optional. Choose a tag type that AWS Billing and Cost Management will use
    # to sort your AWS Elemental MediaConvert costs on any billing report that
    # you set up. Any transcoding outputs that don't have an associated tag will
    # appear in your billing report unsorted. If you don't choose a valid value
    # for this field, your job outputs will appear on the billing report
    # unsorted.
    billing_tags_source: typing.Union[str, "BillingTagsSource"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # The time, in Unix epoch format in seconds, when the job got created.
    created_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Error code for the job
    error_code: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Error message of Job
    error_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A portion of the job's ARN, unique within your AWS Elemental MediaConvert
    # resources
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The job template that the job is created from, if it is created from a job
    # template.
    job_template: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # List of output group details
    output_group_details: typing.List["OutputGroupDetail"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Optional. When you create a job, you can specify a queue to send it to. If
    # you don't specify, the job will go to the default queue. For more about
    # queues, see the User Guide topic at
    # http://docs.aws.amazon.com/mediaconvert/latest/ug/what-is.html
    queue: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A job's status can be SUBMITTED, PROGRESSING, COMPLETE, CANCELED, or ERROR.
    status: typing.Union[str, "JobStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about when jobs are submitted, started, and finished is
    # specified in Unix epoch format in seconds.
    timing: "Timing" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # User-defined metadata that you want to associate with an MediaConvert job.
    # You specify metadata in key/value pairs.
    user_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class JobSettings(ShapeBase):
    """
    JobSettings contains all the transcode settings for a job.
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
                "avail_blanking",
                "AvailBlanking",
                TypeInfo(AvailBlanking),
            ),
            (
                "inputs",
                "Inputs",
                TypeInfo(typing.List[Input]),
            ),
            (
                "nielsen_configuration",
                "NielsenConfiguration",
                TypeInfo(NielsenConfiguration),
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
                "timed_metadata_insertion",
                "TimedMetadataInsertion",
                TypeInfo(TimedMetadataInsertion),
            ),
        ]

    # When specified, this offset (in milliseconds) is added to the input Ad
    # Avail PTS time.
    ad_avail_offset: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Settings for ad avail blanking. Video can be blanked or overlaid with an
    # image, and audio muted during SCTE-35 triggered ad avails.
    avail_blanking: "AvailBlanking" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Use Inputs (inputs) to define source file used in the transcode job. There
    # can be multiple inputs add in a job. These inputs will be concantenated
    # together to create the output.
    inputs: typing.List["Input"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Settings for Nielsen Configuration
    nielsen_configuration: "NielsenConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # (OutputGroups) contains one group of settings for each set of outputs that
    # share a common package type. All unpackaged files (MPEG-4, MPEG-2 TS,
    # Quicktime, MXF, and no container) are grouped in a single output group as
    # well. Required in (OutputGroups) is a group of settings that apply to the
    # whole group. This required object depends on the value you set for (Type)
    # under (OutputGroups)>(OutputGroupSettings). Type, settings object pairs are
    # as follows. * FILE_GROUP_SETTINGS, FileGroupSettings * HLS_GROUP_SETTINGS,
    # HlsGroupSettings * DASH_ISO_GROUP_SETTINGS, DashIsoGroupSettings *
    # MS_SMOOTH_GROUP_SETTINGS, MsSmoothGroupSettings * CMAF_GROUP_SETTINGS,
    # CmafGroupSettings
    output_groups: typing.List["OutputGroup"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains settings used to acquire and adjust timecode information from
    # inputs.
    timecode_config: "TimecodeConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Enable Timed metadata insertion (TimedMetadataInsertion) to include ID3
    # tags in your job. To include timed metadata, you must enable it here,
    # enable it in each output container, and specify tags and timecodes in ID3
    # insertion (Id3Insertion) objects.
    timed_metadata_insertion: "TimedMetadataInsertion" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class JobStatus(str):
    """
    A job's status can be SUBMITTED, PROGRESSING, COMPLETE, CANCELED, or ERROR.
    """
    SUBMITTED = "SUBMITTED"
    PROGRESSING = "PROGRESSING"
    COMPLETE = "COMPLETE"
    CANCELED = "CANCELED"
    ERROR = "ERROR"


@dataclasses.dataclass
class JobTemplate(ShapeBase):
    """
    A job template is a pre-made set of encoding instructions that you can use to
    quickly create a job.
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
                "settings",
                "Settings",
                TypeInfo(JobTemplateSettings),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "category",
                "Category",
                TypeInfo(str),
            ),
            (
                "created_at",
                "CreatedAt",
                TypeInfo(datetime.datetime),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "last_updated",
                "LastUpdated",
                TypeInfo(datetime.datetime),
            ),
            (
                "queue",
                "Queue",
                TypeInfo(str),
            ),
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, Type]),
            ),
        ]

    # A name you create for each job template. Each name must be unique within
    # your account.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # JobTemplateSettings contains all the transcode settings saved in the
    # template that will be applied to jobs created from it.
    settings: "JobTemplateSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An identifier for this resource that is unique within all of AWS.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional category you create to organize your job templates.
    category: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The timestamp in epoch seconds for Job template creation.
    created_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An optional description you create for each job template.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The timestamp in epoch seconds when the Job template was last updated.
    last_updated: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Optional. The queue that jobs created from this template are assigned to.
    # If you don't specify this, jobs will go to the default queue.
    queue: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A job template can be of two types: system or custom. System or built-in
    # job templates can't be modified or deleted by the user.
    type: typing.Union[str, "Type"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class JobTemplateListBy(str):
    """
    Optional. When you request a list of job templates, you can choose to list them
    alphabetically by NAME or chronologically by CREATION_DATE. If you don't
    specify, the service will list them by name.
    """
    NAME = "NAME"
    CREATION_DATE = "CREATION_DATE"
    SYSTEM = "SYSTEM"


@dataclasses.dataclass
class JobTemplateSettings(ShapeBase):
    """
    JobTemplateSettings contains all the transcode settings saved in the template
    that will be applied to jobs created from it.
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
                "avail_blanking",
                "AvailBlanking",
                TypeInfo(AvailBlanking),
            ),
            (
                "inputs",
                "Inputs",
                TypeInfo(typing.List[InputTemplate]),
            ),
            (
                "nielsen_configuration",
                "NielsenConfiguration",
                TypeInfo(NielsenConfiguration),
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
                "timed_metadata_insertion",
                "TimedMetadataInsertion",
                TypeInfo(TimedMetadataInsertion),
            ),
        ]

    # When specified, this offset (in milliseconds) is added to the input Ad
    # Avail PTS time.
    ad_avail_offset: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Settings for ad avail blanking. Video can be blanked or overlaid with an
    # image, and audio muted during SCTE-35 triggered ad avails.
    avail_blanking: "AvailBlanking" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Use Inputs (inputs) to define the source file used in the transcode job.
    # There can only be one input in a job template. Using the API, you can
    # include multiple inputs when referencing a job template.
    inputs: typing.List["InputTemplate"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Settings for Nielsen Configuration
    nielsen_configuration: "NielsenConfiguration" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # (OutputGroups) contains one group of settings for each set of outputs that
    # share a common package type. All unpackaged files (MPEG-4, MPEG-2 TS,
    # Quicktime, MXF, and no container) are grouped in a single output group as
    # well. Required in (OutputGroups) is a group of settings that apply to the
    # whole group. This required object depends on the value you set for (Type)
    # under (OutputGroups)>(OutputGroupSettings). Type, settings object pairs are
    # as follows. * FILE_GROUP_SETTINGS, FileGroupSettings * HLS_GROUP_SETTINGS,
    # HlsGroupSettings * DASH_ISO_GROUP_SETTINGS, DashIsoGroupSettings *
    # MS_SMOOTH_GROUP_SETTINGS, MsSmoothGroupSettings * CMAF_GROUP_SETTINGS,
    # CmafGroupSettings
    output_groups: typing.List["OutputGroup"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains settings used to acquire and adjust timecode information from
    # inputs.
    timecode_config: "TimecodeConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Enable Timed metadata insertion (TimedMetadataInsertion) to include ID3
    # tags in your job. To include timed metadata, you must enable it here,
    # enable it in each output container, and specify tags and timecodes in ID3
    # insertion (Id3Insertion) objects.
    timed_metadata_insertion: "TimedMetadataInsertion" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class LanguageCode(str):
    """
    Specify the language, using the ISO 639-2 three-letter code listed at
    https://www.loc.gov/standards/iso639-2/php/code_list.php.
    """
    ENG = "ENG"
    SPA = "SPA"
    FRA = "FRA"
    DEU = "DEU"
    GER = "GER"
    ZHO = "ZHO"
    ARA = "ARA"
    HIN = "HIN"
    JPN = "JPN"
    RUS = "RUS"
    POR = "POR"
    ITA = "ITA"
    URD = "URD"
    VIE = "VIE"
    KOR = "KOR"
    PAN = "PAN"
    ABK = "ABK"
    AAR = "AAR"
    AFR = "AFR"
    AKA = "AKA"
    SQI = "SQI"
    AMH = "AMH"
    ARG = "ARG"
    HYE = "HYE"
    ASM = "ASM"
    AVA = "AVA"
    AVE = "AVE"
    AYM = "AYM"
    AZE = "AZE"
    BAM = "BAM"
    BAK = "BAK"
    EUS = "EUS"
    BEL = "BEL"
    BEN = "BEN"
    BIH = "BIH"
    BIS = "BIS"
    BOS = "BOS"
    BRE = "BRE"
    BUL = "BUL"
    MYA = "MYA"
    CAT = "CAT"
    KHM = "KHM"
    CHA = "CHA"
    CHE = "CHE"
    NYA = "NYA"
    CHU = "CHU"
    CHV = "CHV"
    COR = "COR"
    COS = "COS"
    CRE = "CRE"
    HRV = "HRV"
    CES = "CES"
    DAN = "DAN"
    DIV = "DIV"
    NLD = "NLD"
    DZO = "DZO"
    ENM = "ENM"
    EPO = "EPO"
    EST = "EST"
    EWE = "EWE"
    FAO = "FAO"
    FIJ = "FIJ"
    FIN = "FIN"
    FRM = "FRM"
    FUL = "FUL"
    GLA = "GLA"
    GLG = "GLG"
    LUG = "LUG"
    KAT = "KAT"
    ELL = "ELL"
    GRN = "GRN"
    GUJ = "GUJ"
    HAT = "HAT"
    HAU = "HAU"
    HEB = "HEB"
    HER = "HER"
    HMO = "HMO"
    HUN = "HUN"
    ISL = "ISL"
    IDO = "IDO"
    IBO = "IBO"
    IND = "IND"
    INA = "INA"
    ILE = "ILE"
    IKU = "IKU"
    IPK = "IPK"
    GLE = "GLE"
    JAV = "JAV"
    KAL = "KAL"
    KAN = "KAN"
    KAU = "KAU"
    KAS = "KAS"
    KAZ = "KAZ"
    KIK = "KIK"
    KIN = "KIN"
    KIR = "KIR"
    KOM = "KOM"
    KON = "KON"
    KUA = "KUA"
    KUR = "KUR"
    LAO = "LAO"
    LAT = "LAT"
    LAV = "LAV"
    LIM = "LIM"
    LIN = "LIN"
    LIT = "LIT"
    LUB = "LUB"
    LTZ = "LTZ"
    MKD = "MKD"
    MLG = "MLG"
    MSA = "MSA"
    MAL = "MAL"
    MLT = "MLT"
    GLV = "GLV"
    MRI = "MRI"
    MAR = "MAR"
    MAH = "MAH"
    MON = "MON"
    NAU = "NAU"
    NAV = "NAV"
    NDE = "NDE"
    NBL = "NBL"
    NDO = "NDO"
    NEP = "NEP"
    SME = "SME"
    NOR = "NOR"
    NOB = "NOB"
    NNO = "NNO"
    OCI = "OCI"
    OJI = "OJI"
    ORI = "ORI"
    ORM = "ORM"
    OSS = "OSS"
    PLI = "PLI"
    FAS = "FAS"
    POL = "POL"
    PUS = "PUS"
    QUE = "QUE"
    QAA = "QAA"
    RON = "RON"
    ROH = "ROH"
    RUN = "RUN"
    SMO = "SMO"
    SAG = "SAG"
    SAN = "SAN"
    SRD = "SRD"
    SRB = "SRB"
    SNA = "SNA"
    III = "III"
    SND = "SND"
    SIN = "SIN"
    SLK = "SLK"
    SLV = "SLV"
    SOM = "SOM"
    SOT = "SOT"
    SUN = "SUN"
    SWA = "SWA"
    SSW = "SSW"
    SWE = "SWE"
    TGL = "TGL"
    TAH = "TAH"
    TGK = "TGK"
    TAM = "TAM"
    TAT = "TAT"
    TEL = "TEL"
    THA = "THA"
    BOD = "BOD"
    TIR = "TIR"
    TON = "TON"
    TSO = "TSO"
    TSN = "TSN"
    TUR = "TUR"
    TUK = "TUK"
    TWI = "TWI"
    UIG = "UIG"
    UKR = "UKR"
    UZB = "UZB"
    VEN = "VEN"
    VOL = "VOL"
    WLN = "WLN"
    CYM = "CYM"
    FRY = "FRY"
    WOL = "WOL"
    XHO = "XHO"
    YID = "YID"
    YOR = "YOR"
    ZHA = "ZHA"
    ZUL = "ZUL"
    ORJ = "ORJ"
    QPC = "QPC"
    TNG = "TNG"


@dataclasses.dataclass
class ListJobTemplatesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "category",
                "Category",
                TypeInfo(str),
            ),
            (
                "list_by",
                "ListBy",
                TypeInfo(typing.Union[str, JobTemplateListBy]),
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
            (
                "order",
                "Order",
                TypeInfo(typing.Union[str, Order]),
            ),
        ]

    # Optionally, specify a job template category to limit responses to only job
    # templates from that category.
    category: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Optional. When you request a list of job templates, you can choose to list
    # them alphabetically by NAME or chronologically by CREATION_DATE. If you
    # don't specify, the service will list them by name.
    list_by: typing.Union[str, "JobTemplateListBy"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Optional. Number of job templates, up to twenty, that will be returned at
    # one time.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use this string, provided with the response to a previous request, to
    # request the next batch of job templates.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When you request lists of resources, you can optionally specify whether
    # they are sorted in ASCENDING or DESCENDING order. Default varies by
    # resource.
    order: typing.Union[str, "Order"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListJobTemplatesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "job_templates",
                "JobTemplates",
                TypeInfo(typing.List[JobTemplate]),
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

    # List of Job templates.
    job_templates: typing.List["JobTemplate"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Use this string to request the next batch of job templates.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListJobsRequest(ShapeBase):
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
            (
                "order",
                "Order",
                TypeInfo(typing.Union[str, Order]),
            ),
            (
                "queue",
                "Queue",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, JobStatus]),
            ),
        ]

    # Optional. Number of jobs, up to twenty, that will be returned at one time.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use this string, provided with the response to a previous request, to
    # request the next batch of jobs.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When you request lists of resources, you can optionally specify whether
    # they are sorted in ASCENDING or DESCENDING order. Default varies by
    # resource.
    order: typing.Union[str, "Order"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Provide a queue name to get back only jobs from that queue.
    queue: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A job's status can be SUBMITTED, PROGRESSING, COMPLETE, CANCELED, or ERROR.
    status: typing.Union[str, "JobStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListJobsResponse(OutputShapeBase):
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
                "Jobs",
                TypeInfo(typing.List[Job]),
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

    # List of jobs
    jobs: typing.List["Job"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use this string to request the next batch of jobs.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListPresetsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "category",
                "Category",
                TypeInfo(str),
            ),
            (
                "list_by",
                "ListBy",
                TypeInfo(typing.Union[str, PresetListBy]),
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
            (
                "order",
                "Order",
                TypeInfo(typing.Union[str, Order]),
            ),
        ]

    # Optionally, specify a preset category to limit responses to only presets
    # from that category.
    category: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Optional. When you request a list of presets, you can choose to list them
    # alphabetically by NAME or chronologically by CREATION_DATE. If you don't
    # specify, the service will list them by name.
    list_by: typing.Union[str, "PresetListBy"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Optional. Number of presets, up to twenty, that will be returned at one
    # time
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use this string, provided with the response to a previous request, to
    # request the next batch of presets.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When you request lists of resources, you can optionally specify whether
    # they are sorted in ASCENDING or DESCENDING order. Default varies by
    # resource.
    order: typing.Union[str, "Order"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListPresetsResponse(OutputShapeBase):
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
                "presets",
                "Presets",
                TypeInfo(typing.List[Preset]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Use this string to request the next batch of presets.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # List of presets
    presets: typing.List["Preset"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListQueuesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "list_by",
                "ListBy",
                TypeInfo(typing.Union[str, QueueListBy]),
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
            (
                "order",
                "Order",
                TypeInfo(typing.Union[str, Order]),
            ),
        ]

    # Optional. When you request a list of queues, you can choose to list them
    # alphabetically by NAME or chronologically by CREATION_DATE. If you don't
    # specify, the service will list them by creation date.
    list_by: typing.Union[str, "QueueListBy"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Optional. Number of queues, up to twenty, that will be returned at one
    # time.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use this string, provided with the response to a previous request, to
    # request the next batch of queues.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When you request lists of resources, you can optionally specify whether
    # they are sorted in ASCENDING or DESCENDING order. Default varies by
    # resource.
    order: typing.Union[str, "Order"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListQueuesResponse(OutputShapeBase):
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
                "queues",
                "Queues",
                TypeInfo(typing.List[Queue]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Use this string to request the next batch of queues.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # List of queues
    queues: typing.List["Queue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListTagsForResourceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the resource that you want to list tags
    # for. To get the ARN, send a GET request with the resource name.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTagsForResourceResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "resource_tags",
                "ResourceTags",
                TypeInfo(ResourceTags),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) and tags for an AWS Elemental MediaConvert
    # resource.
    resource_tags: "ResourceTags" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class M2tsAudioBufferModel(str):
    """
    Selects between the DVB and ATSC buffer models for Dolby Digital audio.
    """
    DVB = "DVB"
    ATSC = "ATSC"


class M2tsBufferModel(str):
    """
    Controls what buffer model to use for accurate interleaving. If set to
    MULTIPLEX, use multiplex buffer model. If set to NONE, this can lead to lower
    latency, but low-memory devices may not be able to play back the stream without
    interruptions.
    """
    MULTIPLEX = "MULTIPLEX"
    NONE = "NONE"


class M2tsEbpAudioInterval(str):
    """
    When set to VIDEO_AND_FIXED_INTERVALS, audio EBP markers will be added to
    partitions 3 and 4. The interval between these additional markers will be fixed,
    and will be slightly shorter than the video EBP marker interval. When set to
    VIDEO_INTERVAL, these additional markers will not be inserted. Only applicable
    when EBP segmentation markers are is selected (segmentationMarkers is EBP or
    EBP_LEGACY).
    """
    VIDEO_AND_FIXED_INTERVALS = "VIDEO_AND_FIXED_INTERVALS"
    VIDEO_INTERVAL = "VIDEO_INTERVAL"


class M2tsEbpPlacement(str):
    """
    Selects which PIDs to place EBP markers on. They can either be placed only on
    the video PID, or on both the video PID and all audio PIDs. Only applicable when
    EBP segmentation markers are is selected (segmentationMarkers is EBP or
    EBP_LEGACY).
    """
    VIDEO_AND_AUDIO_PIDS = "VIDEO_AND_AUDIO_PIDS"
    VIDEO_PID = "VIDEO_PID"


class M2tsEsRateInPes(str):
    """
    Controls whether to include the ES Rate field in the PES header.
    """
    INCLUDE = "INCLUDE"
    EXCLUDE = "EXCLUDE"


class M2tsNielsenId3(str):
    """
    If INSERT, Nielsen inaudible tones for media tracking will be detected in the
    input audio and an equivalent ID3 tag will be inserted in the output.
    """
    INSERT = "INSERT"
    NONE = "NONE"


class M2tsPcrControl(str):
    """
    When set to PCR_EVERY_PES_PACKET, a Program Clock Reference value is inserted
    for every Packetized Elementary Stream (PES) header. This is effective only when
    the PCR PID is the same as the video or audio elementary stream.
    """
    PCR_EVERY_PES_PACKET = "PCR_EVERY_PES_PACKET"
    CONFIGURED_PCR_PERIOD = "CONFIGURED_PCR_PERIOD"


class M2tsRateMode(str):
    """
    When set to CBR, inserts null packets into transport stream to fill specified
    bitrate. When set to VBR, the bitrate setting acts as the maximum bitrate, but
    the output will not be padded up to that bitrate.
    """
    VBR = "VBR"
    CBR = "CBR"


class M2tsScte35Source(str):
    """
    Enables SCTE-35 passthrough (scte35Source) to pass any SCTE-35 signals from
    input to output.
    """
    PASSTHROUGH = "PASSTHROUGH"
    NONE = "NONE"


class M2tsSegmentationMarkers(str):
    """
    Inserts segmentation markers at each segmentation_time period. rai_segstart sets
    the Random Access Indicator bit in the adaptation field. rai_adapt sets the RAI
    bit and adds the current timecode in the private data bytes. psi_segstart
    inserts PAT and PMT tables at the start of segments. ebp adds Encoder Boundary
    Point information to the adaptation field as per OpenCable specification OC-SP-
    EBP-I01-130118. ebp_legacy adds Encoder Boundary Point information to the
    adaptation field using a legacy proprietary format.
    """
    NONE = "NONE"
    RAI_SEGSTART = "RAI_SEGSTART"
    RAI_ADAPT = "RAI_ADAPT"
    PSI_SEGSTART = "PSI_SEGSTART"
    EBP = "EBP"
    EBP_LEGACY = "EBP_LEGACY"


class M2tsSegmentationStyle(str):
    """
    The segmentation style parameter controls how segmentation markers are inserted
    into the transport stream. With avails, it is possible that segments may be
    truncated, which can influence where future segmentation markers are inserted.
    When a segmentation style of "reset_cadence" is selected and a segment is
    truncated due to an avail, we will reset the segmentation cadence. This means
    the subsequent segment will have a duration of of $segmentation_time seconds.
    When a segmentation style of "maintain_cadence" is selected and a segment is
    truncated due to an avail, we will not reset the segmentation cadence. This
    means the subsequent segment will likely be truncated as well. However, all
    segments after that will have a duration of $segmentation_time seconds. Note
    that EBP lookahead is a slight exception to this rule.
    """
    MAINTAIN_CADENCE = "MAINTAIN_CADENCE"
    RESET_CADENCE = "RESET_CADENCE"


@dataclasses.dataclass
class M2tsSettings(ShapeBase):
    """
    Settings for M2TS Container.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
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
                TypeInfo(typing.List[int]),
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
                TypeInfo(typing.List[int]),
            ),
            (
                "dvb_tdt_settings",
                "DvbTdtSettings",
                TypeInfo(DvbTdtSettings),
            ),
            (
                "dvb_teletext_pid",
                "DvbTeletextPid",
                TypeInfo(int),
            ),
            (
                "ebp_audio_interval",
                "EbpAudioInterval",
                TypeInfo(typing.Union[str, M2tsEbpAudioInterval]),
            ),
            (
                "ebp_placement",
                "EbpPlacement",
                TypeInfo(typing.Union[str, M2tsEbpPlacement]),
            ),
            (
                "es_rate_in_pes",
                "EsRateInPes",
                TypeInfo(typing.Union[str, M2tsEsRateInPes]),
            ),
            (
                "fragment_time",
                "FragmentTime",
                TypeInfo(float),
            ),
            (
                "max_pcr_interval",
                "MaxPcrInterval",
                TypeInfo(int),
            ),
            (
                "min_ebp_interval",
                "MinEbpInterval",
                TypeInfo(int),
            ),
            (
                "nielsen_id3",
                "NielsenId3",
                TypeInfo(typing.Union[str, M2tsNielsenId3]),
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
                "pcr_pid",
                "PcrPid",
                TypeInfo(int),
            ),
            (
                "pmt_interval",
                "PmtInterval",
                TypeInfo(int),
            ),
            (
                "pmt_pid",
                "PmtPid",
                TypeInfo(int),
            ),
            (
                "private_metadata_pid",
                "PrivateMetadataPid",
                TypeInfo(int),
            ),
            (
                "program_number",
                "ProgramNumber",
                TypeInfo(int),
            ),
            (
                "rate_mode",
                "RateMode",
                TypeInfo(typing.Union[str, M2tsRateMode]),
            ),
            (
                "scte35_pid",
                "Scte35Pid",
                TypeInfo(int),
            ),
            (
                "scte35_source",
                "Scte35Source",
                TypeInfo(typing.Union[str, M2tsScte35Source]),
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
                "timed_metadata_pid",
                "TimedMetadataPid",
                TypeInfo(int),
            ),
            (
                "transport_stream_id",
                "TransportStreamId",
                TypeInfo(int),
            ),
            (
                "video_pid",
                "VideoPid",
                TypeInfo(int),
            ),
        ]

    # Selects between the DVB and ATSC buffer models for Dolby Digital audio.
    audio_buffer_model: typing.Union[str, "M2tsAudioBufferModel"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )

    # The number of audio frames to insert for each PES packet.
    audio_frames_per_pes: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Packet Identifier (PID) of the elementary audio stream(s) in the transport
    # stream. Multiple values are accepted, and can be entered in ranges and/or
    # by comma separation.
    audio_pids: typing.List[int] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The output bitrate of the transport stream in bits per second. Setting to 0
    # lets the muxer automatically determine the appropriate bitrate. Other
    # common values are 3750000, 7500000, and 15000000.
    bitrate: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Controls what buffer model to use for accurate interleaving. If set to
    # MULTIPLEX, use multiplex buffer model. If set to NONE, this can lead to
    # lower latency, but low-memory devices may not be able to play back the
    # stream without interruptions.
    buffer_model: typing.Union[str, "M2tsBufferModel"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Inserts DVB Network Information Table (NIT) at the specified table
    # repetition interval.
    dvb_nit_settings: "DvbNitSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Inserts DVB Service Description Table (NIT) at the specified table
    # repetition interval.
    dvb_sdt_settings: "DvbSdtSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Packet Identifier (PID) for input source DVB Subtitle data to this output.
    # Multiple values are accepted, and can be entered in ranges and/or by comma
    # separation.
    dvb_sub_pids: typing.List[int] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Inserts DVB Time and Date Table (TDT) at the specified table repetition
    # interval.
    dvb_tdt_settings: "DvbTdtSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Packet Identifier (PID) for input source DVB Teletext data to this output.
    dvb_teletext_pid: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When set to VIDEO_AND_FIXED_INTERVALS, audio EBP markers will be added to
    # partitions 3 and 4. The interval between these additional markers will be
    # fixed, and will be slightly shorter than the video EBP marker interval.
    # When set to VIDEO_INTERVAL, these additional markers will not be inserted.
    # Only applicable when EBP segmentation markers are is selected
    # (segmentationMarkers is EBP or EBP_LEGACY).
    ebp_audio_interval: typing.Union[str, "M2tsEbpAudioInterval"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )

    # Selects which PIDs to place EBP markers on. They can either be placed only
    # on the video PID, or on both the video PID and all audio PIDs. Only
    # applicable when EBP segmentation markers are is selected
    # (segmentationMarkers is EBP or EBP_LEGACY).
    ebp_placement: typing.Union[str, "M2tsEbpPlacement"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Controls whether to include the ES Rate field in the PES header.
    es_rate_in_pes: typing.Union[str, "M2tsEsRateInPes"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The length in seconds of each fragment. Only used with EBP markers.
    fragment_time: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Maximum time in milliseconds between Program Clock References (PCRs)
    # inserted into the transport stream.
    max_pcr_interval: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When set, enforces that Encoder Boundary Points do not come within the
    # specified time interval of each other by looking ahead at input video. If
    # another EBP is going to come in within the specified time interval, the
    # current EBP is not emitted, and the segment is "stretched" to the next
    # marker. The lookahead value does not add latency to the system. The Live
    # Event must be configured elsewhere to create sufficient latency to make the
    # lookahead accurate.
    min_ebp_interval: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If INSERT, Nielsen inaudible tones for media tracking will be detected in
    # the input audio and an equivalent ID3 tag will be inserted in the output.
    nielsen_id3: typing.Union[str, "M2tsNielsenId3"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Value in bits per second of extra null packets to insert into the transport
    # stream. This can be used if a downstream encryption system requires
    # periodic null packets.
    null_packet_bitrate: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of milliseconds between instances of this table in the output
    # transport stream.
    pat_interval: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When set to PCR_EVERY_PES_PACKET, a Program Clock Reference value is
    # inserted for every Packetized Elementary Stream (PES) header. This is
    # effective only when the PCR PID is the same as the video or audio
    # elementary stream.
    pcr_control: typing.Union[str, "M2tsPcrControl"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Packet Identifier (PID) of the Program Clock Reference (PCR) in the
    # transport stream. When no value is given, the encoder will assign the same
    # value as the Video PID.
    pcr_pid: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of milliseconds between instances of this table in the output
    # transport stream.
    pmt_interval: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Packet Identifier (PID) for the Program Map Table (PMT) in the transport
    # stream.
    pmt_pid: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Packet Identifier (PID) of the private metadata stream in the transport
    # stream.
    private_metadata_pid: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of the program number field in the Program Map Table.
    program_number: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When set to CBR, inserts null packets into transport stream to fill
    # specified bitrate. When set to VBR, the bitrate setting acts as the maximum
    # bitrate, but the output will not be padded up to that bitrate.
    rate_mode: typing.Union[str, "M2tsRateMode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Packet Identifier (PID) of the SCTE-35 stream in the transport stream.
    scte35_pid: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Enables SCTE-35 passthrough (scte35Source) to pass any SCTE-35 signals from
    # input to output.
    scte35_source: typing.Union[str, "M2tsScte35Source"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Inserts segmentation markers at each segmentation_time period. rai_segstart
    # sets the Random Access Indicator bit in the adaptation field. rai_adapt
    # sets the RAI bit and adds the current timecode in the private data bytes.
    # psi_segstart inserts PAT and PMT tables at the start of segments. ebp adds
    # Encoder Boundary Point information to the adaptation field as per OpenCable
    # specification OC-SP-EBP-I01-130118. ebp_legacy adds Encoder Boundary Point
    # information to the adaptation field using a legacy proprietary format.
    segmentation_markers: typing.Union[str, "M2tsSegmentationMarkers"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    # The segmentation style parameter controls how segmentation markers are
    # inserted into the transport stream. With avails, it is possible that
    # segments may be truncated, which can influence where future segmentation
    # markers are inserted. When a segmentation style of "reset_cadence" is
    # selected and a segment is truncated due to an avail, we will reset the
    # segmentation cadence. This means the subsequent segment will have a
    # duration of of $segmentation_time seconds. When a segmentation style of
    # "maintain_cadence" is selected and a segment is truncated due to an avail,
    # we will not reset the segmentation cadence. This means the subsequent
    # segment will likely be truncated as well. However, all segments after that
    # will have a duration of $segmentation_time seconds. Note that EBP lookahead
    # is a slight exception to this rule.
    segmentation_style: typing.Union[str, "M2tsSegmentationStyle"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )

    # The length in seconds of each segment. Required unless markers is set to
    # _none_.
    segmentation_time: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Packet Identifier (PID) of the timed metadata stream in the transport
    # stream.
    timed_metadata_pid: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of the transport stream ID field in the Program Map Table.
    transport_stream_id: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Packet Identifier (PID) of the elementary video stream in the transport
    # stream.
    video_pid: int = dataclasses.field(default=ShapeBase.NOT_SET, )


class M3u8NielsenId3(str):
    """
    If INSERT, Nielsen inaudible tones for media tracking will be detected in the
    input audio and an equivalent ID3 tag will be inserted in the output.
    """
    INSERT = "INSERT"
    NONE = "NONE"


class M3u8PcrControl(str):
    """
    When set to PCR_EVERY_PES_PACKET a Program Clock Reference value is inserted for
    every Packetized Elementary Stream (PES) header. This parameter is effective
    only when the PCR PID is the same as the video or audio elementary stream.
    """
    PCR_EVERY_PES_PACKET = "PCR_EVERY_PES_PACKET"
    CONFIGURED_PCR_PERIOD = "CONFIGURED_PCR_PERIOD"


class M3u8Scte35Source(str):
    """
    Enables SCTE-35 passthrough (scte35Source) to pass any SCTE-35 signals from
    input to output.
    """
    PASSTHROUGH = "PASSTHROUGH"
    NONE = "NONE"


@dataclasses.dataclass
class M3u8Settings(ShapeBase):
    """
    Settings for TS segments in HLS
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
                TypeInfo(typing.List[int]),
            ),
            (
                "nielsen_id3",
                "NielsenId3",
                TypeInfo(typing.Union[str, M3u8NielsenId3]),
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
                "pcr_pid",
                "PcrPid",
                TypeInfo(int),
            ),
            (
                "pmt_interval",
                "PmtInterval",
                TypeInfo(int),
            ),
            (
                "pmt_pid",
                "PmtPid",
                TypeInfo(int),
            ),
            (
                "private_metadata_pid",
                "PrivateMetadataPid",
                TypeInfo(int),
            ),
            (
                "program_number",
                "ProgramNumber",
                TypeInfo(int),
            ),
            (
                "scte35_pid",
                "Scte35Pid",
                TypeInfo(int),
            ),
            (
                "scte35_source",
                "Scte35Source",
                TypeInfo(typing.Union[str, M3u8Scte35Source]),
            ),
            (
                "timed_metadata",
                "TimedMetadata",
                TypeInfo(typing.Union[str, TimedMetadata]),
            ),
            (
                "timed_metadata_pid",
                "TimedMetadataPid",
                TypeInfo(int),
            ),
            (
                "transport_stream_id",
                "TransportStreamId",
                TypeInfo(int),
            ),
            (
                "video_pid",
                "VideoPid",
                TypeInfo(int),
            ),
        ]

    # The number of audio frames to insert for each PES packet.
    audio_frames_per_pes: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Packet Identifier (PID) of the elementary audio stream(s) in the transport
    # stream. Multiple values are accepted, and can be entered in ranges and/or
    # by comma separation.
    audio_pids: typing.List[int] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If INSERT, Nielsen inaudible tones for media tracking will be detected in
    # the input audio and an equivalent ID3 tag will be inserted in the output.
    nielsen_id3: typing.Union[str, "M3u8NielsenId3"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of milliseconds between instances of this table in the output
    # transport stream.
    pat_interval: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When set to PCR_EVERY_PES_PACKET a Program Clock Reference value is
    # inserted for every Packetized Elementary Stream (PES) header. This
    # parameter is effective only when the PCR PID is the same as the video or
    # audio elementary stream.
    pcr_control: typing.Union[str, "M3u8PcrControl"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Packet Identifier (PID) of the Program Clock Reference (PCR) in the
    # transport stream. When no value is given, the encoder will assign the same
    # value as the Video PID.
    pcr_pid: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of milliseconds between instances of this table in the output
    # transport stream.
    pmt_interval: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Packet Identifier (PID) for the Program Map Table (PMT) in the transport
    # stream.
    pmt_pid: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Packet Identifier (PID) of the private metadata stream in the transport
    # stream.
    private_metadata_pid: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of the program number field in the Program Map Table.
    program_number: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Packet Identifier (PID) of the SCTE-35 stream in the transport stream.
    scte35_pid: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Enables SCTE-35 passthrough (scte35Source) to pass any SCTE-35 signals from
    # input to output.
    scte35_source: typing.Union[str, "M3u8Scte35Source"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Applies only to HLS outputs. Use this setting to specify whether the
    # service inserts the ID3 timed metadata from the input in this output.
    timed_metadata: typing.Union[str, "TimedMetadata"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Packet Identifier (PID) of the timed metadata stream in the transport
    # stream.
    timed_metadata_pid: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of the transport stream ID field in the Program Map Table.
    transport_stream_id: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Packet Identifier (PID) of the elementary video stream in the transport
    # stream.
    video_pid: int = dataclasses.field(default=ShapeBase.NOT_SET, )


class MovClapAtom(str):
    """
    When enabled, include 'clap' atom if appropriate for the video output settings.
    """
    INCLUDE = "INCLUDE"
    EXCLUDE = "EXCLUDE"


class MovCslgAtom(str):
    """
    When enabled, file composition times will start at zero, composition times in
    the 'ctts' (composition time to sample) box for B-frames will be negative, and a
    'cslg' (composition shift least greatest) box will be included per 14496-1
    amendment 1. This improves compatibility with Apple players and tools.
    """
    INCLUDE = "INCLUDE"
    EXCLUDE = "EXCLUDE"


class MovMpeg2FourCCControl(str):
    """
    When set to XDCAM, writes MPEG2 video streams into the QuickTime file using
    XDCAM fourcc codes. This increases compatibility with Apple editors and players,
    but may decrease compatibility with other players. Only applicable when the
    video codec is MPEG2.
    """
    XDCAM = "XDCAM"
    MPEG = "MPEG"


class MovPaddingControl(str):
    """
    If set to OMNEON, inserts Omneon-compatible padding
    """
    OMNEON = "OMNEON"
    NONE = "NONE"


class MovReference(str):
    """
    A value of 'external' creates separate media files and the wrapper file (.mov)
    contains references to these media files. A value of 'self_contained' creates
    only a wrapper (.mov) file and this file contains all of the media.
    """
    SELF_CONTAINED = "SELF_CONTAINED"
    EXTERNAL = "EXTERNAL"


@dataclasses.dataclass
class MovSettings(ShapeBase):
    """
    Settings for MOV Container.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "clap_atom",
                "ClapAtom",
                TypeInfo(typing.Union[str, MovClapAtom]),
            ),
            (
                "cslg_atom",
                "CslgAtom",
                TypeInfo(typing.Union[str, MovCslgAtom]),
            ),
            (
                "mpeg2_four_cc_control",
                "Mpeg2FourCCControl",
                TypeInfo(typing.Union[str, MovMpeg2FourCCControl]),
            ),
            (
                "padding_control",
                "PaddingControl",
                TypeInfo(typing.Union[str, MovPaddingControl]),
            ),
            (
                "reference",
                "Reference",
                TypeInfo(typing.Union[str, MovReference]),
            ),
        ]

    # When enabled, include 'clap' atom if appropriate for the video output
    # settings.
    clap_atom: typing.Union[str, "MovClapAtom"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When enabled, file composition times will start at zero, composition times
    # in the 'ctts' (composition time to sample) box for B-frames will be
    # negative, and a 'cslg' (composition shift least greatest) box will be
    # included per 14496-1 amendment 1. This improves compatibility with Apple
    # players and tools.
    cslg_atom: typing.Union[str, "MovCslgAtom"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # When set to XDCAM, writes MPEG2 video streams into the QuickTime file using
    # XDCAM fourcc codes. This increases compatibility with Apple editors and
    # players, but may decrease compatibility with other players. Only applicable
    # when the video codec is MPEG2.
    mpeg2_four_cc_control: typing.Union[str, "MovMpeg2FourCCControl"
                                       ] = dataclasses.field(
                                           default=ShapeBase.NOT_SET,
                                       )

    # If set to OMNEON, inserts Omneon-compatible padding
    padding_control: typing.Union[str, "MovPaddingControl"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A value of 'external' creates separate media files and the wrapper file
    # (.mov) contains references to these media files. A value of
    # 'self_contained' creates only a wrapper (.mov) file and this file contains
    # all of the media.
    reference: typing.Union[str, "MovReference"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Mp2Settings(ShapeBase):
    """
    Required when you set (Codec) under (AudioDescriptions)>(CodecSettings) to the
    value MP2.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bitrate",
                "Bitrate",
                TypeInfo(int),
            ),
            (
                "channels",
                "Channels",
                TypeInfo(int),
            ),
            (
                "sample_rate",
                "SampleRate",
                TypeInfo(int),
            ),
        ]

    # Average bitrate in bits/second.
    bitrate: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Set Channels to specify the number of channels in this output audio track.
    # Choosing Mono in the console will give you 1 output channel; choosing
    # Stereo will give you 2. In the API, valid values are 1 and 2.
    channels: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Sample rate in hz.
    sample_rate: int = dataclasses.field(default=ShapeBase.NOT_SET, )


class Mp4CslgAtom(str):
    """
    When enabled, file composition times will start at zero, composition times in
    the 'ctts' (composition time to sample) box for B-frames will be negative, and a
    'cslg' (composition shift least greatest) box will be included per 14496-1
    amendment 1. This improves compatibility with Apple players and tools.
    """
    INCLUDE = "INCLUDE"
    EXCLUDE = "EXCLUDE"


class Mp4FreeSpaceBox(str):
    """
    Inserts a free-space box immediately after the moov box.
    """
    INCLUDE = "INCLUDE"
    EXCLUDE = "EXCLUDE"


class Mp4MoovPlacement(str):
    """
    If set to PROGRESSIVE_DOWNLOAD, the MOOV atom is relocated to the beginning of
    the archive as required for progressive downloading. Otherwise it is placed
    normally at the end.
    """
    PROGRESSIVE_DOWNLOAD = "PROGRESSIVE_DOWNLOAD"
    NORMAL = "NORMAL"


@dataclasses.dataclass
class Mp4Settings(ShapeBase):
    """
    Settings for MP4 Container
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cslg_atom",
                "CslgAtom",
                TypeInfo(typing.Union[str, Mp4CslgAtom]),
            ),
            (
                "free_space_box",
                "FreeSpaceBox",
                TypeInfo(typing.Union[str, Mp4FreeSpaceBox]),
            ),
            (
                "moov_placement",
                "MoovPlacement",
                TypeInfo(typing.Union[str, Mp4MoovPlacement]),
            ),
            (
                "mp4_major_brand",
                "Mp4MajorBrand",
                TypeInfo(str),
            ),
        ]

    # When enabled, file composition times will start at zero, composition times
    # in the 'ctts' (composition time to sample) box for B-frames will be
    # negative, and a 'cslg' (composition shift least greatest) box will be
    # included per 14496-1 amendment 1. This improves compatibility with Apple
    # players and tools.
    cslg_atom: typing.Union[str, "Mp4CslgAtom"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Inserts a free-space box immediately after the moov box.
    free_space_box: typing.Union[str, "Mp4FreeSpaceBox"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If set to PROGRESSIVE_DOWNLOAD, the MOOV atom is relocated to the beginning
    # of the archive as required for progressive downloading. Otherwise it is
    # placed normally at the end.
    moov_placement: typing.Union[str, "Mp4MoovPlacement"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Overrides the "Major Brand" field in the output file. Usually not necessary
    # to specify.
    mp4_major_brand: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class Mpeg2AdaptiveQuantization(str):
    """
    Adaptive quantization. Allows intra-frame quantizers to vary to improve visual
    quality.
    """
    OFF = "OFF"
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


class Mpeg2CodecLevel(str):
    """
    Use Level (Mpeg2CodecLevel) to set the MPEG-2 level for the video output.
    """
    AUTO = "AUTO"
    LOW = "LOW"
    MAIN = "MAIN"
    HIGH1440 = "HIGH1440"
    HIGH = "HIGH"


class Mpeg2CodecProfile(str):
    """
    Use Profile (Mpeg2CodecProfile) to set the MPEG-2 profile for the video output.
    """
    MAIN = "MAIN"
    PROFILE_422 = "PROFILE_422"


class Mpeg2DynamicSubGop(str):
    """
    Choose Adaptive to improve subjective video quality for high-motion content.
    This will cause the service to use fewer B-frames (which infer information based
    on other frames) for high-motion portions of the video and more B-frames for
    low-motion portions. The maximum number of B-frames is limited by the value you
    provide for the setting B frames between reference frames
    (numberBFramesBetweenReferenceFrames).
    """
    ADAPTIVE = "ADAPTIVE"
    STATIC = "STATIC"


class Mpeg2FramerateControl(str):
    """
    If you are using the console, use the Framerate setting to specify the framerate
    for this output. If you want to keep the same framerate as the input video,
    choose Follow source. If you want to do framerate conversion, choose a framerate
    from the dropdown list or choose Custom. The framerates shown in the dropdown
    list are decimal approximations of fractions. If you choose Custom, specify your
    framerate as a fraction. If you are creating your transcoding job sepecification
    as a JSON file without the console, use FramerateControl to specify which value
    the service uses for the framerate for this output. Choose
    INITIALIZE_FROM_SOURCE if you want the service to use the framerate from the
    input. Choose SPECIFIED if you want the service to use the framerate you specify
    in the settings FramerateNumerator and FramerateDenominator.
    """
    INITIALIZE_FROM_SOURCE = "INITIALIZE_FROM_SOURCE"
    SPECIFIED = "SPECIFIED"


class Mpeg2FramerateConversionAlgorithm(str):
    """
    When set to INTERPOLATE, produces smoother motion during framerate conversion.
    """
    DUPLICATE_DROP = "DUPLICATE_DROP"
    INTERPOLATE = "INTERPOLATE"


class Mpeg2GopSizeUnits(str):
    """
    Indicates if the GOP Size in MPEG2 is specified in frames or seconds. If seconds
    the system will convert the GOP Size into a frame count at run time.
    """
    FRAMES = "FRAMES"
    SECONDS = "SECONDS"


class Mpeg2InterlaceMode(str):
    """
    Use Interlace mode (InterlaceMode) to choose the scan line type for the output.
    * Top Field First (TOP_FIELD) and Bottom Field First (BOTTOM_FIELD) produce
    interlaced output with the entire output having the same field polarity (top or
    bottom first). * Follow, Default Top (FOLLOW_TOP_FIELD) and Follow, Default
    Bottom (FOLLOW_BOTTOM_FIELD) use the same field polarity as the source.
    Therefore, behavior depends on the input scan type. \- If the source is
    interlaced, the output will be interlaced with the same polarity as the source
    (it will follow the source). The output could therefore be a mix of "top field
    first" and "bottom field first". \- If the source is progressive, the output
    will be interlaced with "top field first" or "bottom field first" polarity,
    depending on which of the Follow options you chose.
    """
    PROGRESSIVE = "PROGRESSIVE"
    TOP_FIELD = "TOP_FIELD"
    BOTTOM_FIELD = "BOTTOM_FIELD"
    FOLLOW_TOP_FIELD = "FOLLOW_TOP_FIELD"
    FOLLOW_BOTTOM_FIELD = "FOLLOW_BOTTOM_FIELD"


class Mpeg2IntraDcPrecision(str):
    """
    Use Intra DC precision (Mpeg2IntraDcPrecision) to set quantization precision for
    intra-block DC coefficients. If you choose the value auto, the service will
    automatically select the precision based on the per-frame compression ratio.
    """
    AUTO = "AUTO"
    INTRA_DC_PRECISION_8 = "INTRA_DC_PRECISION_8"
    INTRA_DC_PRECISION_9 = "INTRA_DC_PRECISION_9"
    INTRA_DC_PRECISION_10 = "INTRA_DC_PRECISION_10"
    INTRA_DC_PRECISION_11 = "INTRA_DC_PRECISION_11"


class Mpeg2ParControl(str):
    """
    Using the API, enable ParFollowSource if you want the service to use the pixel
    aspect ratio from the input. Using the console, do this by choosing Follow
    source for Pixel aspect ratio.
    """
    INITIALIZE_FROM_SOURCE = "INITIALIZE_FROM_SOURCE"
    SPECIFIED = "SPECIFIED"


class Mpeg2QualityTuningLevel(str):
    """
    Use Quality tuning level (Mpeg2QualityTuningLevel) to specifiy whether to use
    single-pass or multipass video encoding.
    """
    SINGLE_PASS = "SINGLE_PASS"
    MULTI_PASS = "MULTI_PASS"


class Mpeg2RateControlMode(str):
    """
    Use Rate control mode (Mpeg2RateControlMode) to specifiy whether the bitrate is
    variable (vbr) or constant (cbr).
    """
    VBR = "VBR"
    CBR = "CBR"


class Mpeg2SceneChangeDetect(str):
    """
    Scene change detection (inserts I-frames on scene changes).
    """
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


@dataclasses.dataclass
class Mpeg2Settings(ShapeBase):
    """
    Required when you set (Codec) under (VideoDescription)>(CodecSettings) to the
    value MPEG2.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "adaptive_quantization",
                "AdaptiveQuantization",
                TypeInfo(typing.Union[str, Mpeg2AdaptiveQuantization]),
            ),
            (
                "bitrate",
                "Bitrate",
                TypeInfo(int),
            ),
            (
                "codec_level",
                "CodecLevel",
                TypeInfo(typing.Union[str, Mpeg2CodecLevel]),
            ),
            (
                "codec_profile",
                "CodecProfile",
                TypeInfo(typing.Union[str, Mpeg2CodecProfile]),
            ),
            (
                "dynamic_sub_gop",
                "DynamicSubGop",
                TypeInfo(typing.Union[str, Mpeg2DynamicSubGop]),
            ),
            (
                "framerate_control",
                "FramerateControl",
                TypeInfo(typing.Union[str, Mpeg2FramerateControl]),
            ),
            (
                "framerate_conversion_algorithm",
                "FramerateConversionAlgorithm",
                TypeInfo(typing.Union[str, Mpeg2FramerateConversionAlgorithm]),
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
                "gop_closed_cadence",
                "GopClosedCadence",
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
                TypeInfo(typing.Union[str, Mpeg2GopSizeUnits]),
            ),
            (
                "hrd_buffer_initial_fill_percentage",
                "HrdBufferInitialFillPercentage",
                TypeInfo(int),
            ),
            (
                "hrd_buffer_size",
                "HrdBufferSize",
                TypeInfo(int),
            ),
            (
                "interlace_mode",
                "InterlaceMode",
                TypeInfo(typing.Union[str, Mpeg2InterlaceMode]),
            ),
            (
                "intra_dc_precision",
                "IntraDcPrecision",
                TypeInfo(typing.Union[str, Mpeg2IntraDcPrecision]),
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
                "number_b_frames_between_reference_frames",
                "NumberBFramesBetweenReferenceFrames",
                TypeInfo(int),
            ),
            (
                "par_control",
                "ParControl",
                TypeInfo(typing.Union[str, Mpeg2ParControl]),
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
                "quality_tuning_level",
                "QualityTuningLevel",
                TypeInfo(typing.Union[str, Mpeg2QualityTuningLevel]),
            ),
            (
                "rate_control_mode",
                "RateControlMode",
                TypeInfo(typing.Union[str, Mpeg2RateControlMode]),
            ),
            (
                "scene_change_detect",
                "SceneChangeDetect",
                TypeInfo(typing.Union[str, Mpeg2SceneChangeDetect]),
            ),
            (
                "slow_pal",
                "SlowPal",
                TypeInfo(typing.Union[str, Mpeg2SlowPal]),
            ),
            (
                "softness",
                "Softness",
                TypeInfo(int),
            ),
            (
                "spatial_adaptive_quantization",
                "SpatialAdaptiveQuantization",
                TypeInfo(typing.Union[str, Mpeg2SpatialAdaptiveQuantization]),
            ),
            (
                "syntax",
                "Syntax",
                TypeInfo(typing.Union[str, Mpeg2Syntax]),
            ),
            (
                "telecine",
                "Telecine",
                TypeInfo(typing.Union[str, Mpeg2Telecine]),
            ),
            (
                "temporal_adaptive_quantization",
                "TemporalAdaptiveQuantization",
                TypeInfo(typing.Union[str, Mpeg2TemporalAdaptiveQuantization]),
            ),
        ]

    # Adaptive quantization. Allows intra-frame quantizers to vary to improve
    # visual quality.
    adaptive_quantization: typing.Union[str, "Mpeg2AdaptiveQuantization"
                                       ] = dataclasses.field(
                                           default=ShapeBase.NOT_SET,
                                       )

    # Average bitrate in bits/second. Required for VBR and CBR. For MS Smooth
    # outputs, bitrates must be unique when rounded down to the nearest multiple
    # of 1000.
    bitrate: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use Level (Mpeg2CodecLevel) to set the MPEG-2 level for the video output.
    codec_level: typing.Union[str, "Mpeg2CodecLevel"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Use Profile (Mpeg2CodecProfile) to set the MPEG-2 profile for the video
    # output.
    codec_profile: typing.Union[str, "Mpeg2CodecProfile"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Choose Adaptive to improve subjective video quality for high-motion
    # content. This will cause the service to use fewer B-frames (which infer
    # information based on other frames) for high-motion portions of the video
    # and more B-frames for low-motion portions. The maximum number of B-frames
    # is limited by the value you provide for the setting B frames between
    # reference frames (numberBFramesBetweenReferenceFrames).
    dynamic_sub_gop: typing.Union[str, "Mpeg2DynamicSubGop"
                                 ] = dataclasses.field(
                                     default=ShapeBase.NOT_SET,
                                 )

    # If you are using the console, use the Framerate setting to specify the
    # framerate for this output. If you want to keep the same framerate as the
    # input video, choose Follow source. If you want to do framerate conversion,
    # choose a framerate from the dropdown list or choose Custom. The framerates
    # shown in the dropdown list are decimal approximations of fractions. If you
    # choose Custom, specify your framerate as a fraction. If you are creating
    # your transcoding job sepecification as a JSON file without the console, use
    # FramerateControl to specify which value the service uses for the framerate
    # for this output. Choose INITIALIZE_FROM_SOURCE if you want the service to
    # use the framerate from the input. Choose SPECIFIED if you want the service
    # to use the framerate you specify in the settings FramerateNumerator and
    # FramerateDenominator.
    framerate_control: typing.Union[str, "Mpeg2FramerateControl"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # When set to INTERPOLATE, produces smoother motion during framerate
    # conversion.
    framerate_conversion_algorithm: typing.Union[
        str, "Mpeg2FramerateConversionAlgorithm"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # Framerate denominator.
    framerate_denominator: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Framerate numerator - framerate is a fraction, e.g. 24000 / 1001 = 23.976
    # fps.
    framerate_numerator: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Frequency of closed GOPs. In streaming applications, it is recommended that
    # this be set to 1 so a decoder joining mid-stream will receive an IDR frame
    # as quickly as possible. Setting this value to 0 will break output
    # segmenting.
    gop_closed_cadence: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # GOP Length (keyframe interval) in frames or seconds. Must be greater than
    # zero.
    gop_size: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates if the GOP Size in MPEG2 is specified in frames or seconds. If
    # seconds the system will convert the GOP Size into a frame count at run
    # time.
    gop_size_units: typing.Union[str, "Mpeg2GopSizeUnits"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Percentage of the buffer that should initially be filled (HRD buffer
    # model).
    hrd_buffer_initial_fill_percentage: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Size of buffer (HRD buffer model) in bits. For example, enter five megabits
    # as 5000000.
    hrd_buffer_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use Interlace mode (InterlaceMode) to choose the scan line type for the
    # output. * Top Field First (TOP_FIELD) and Bottom Field First (BOTTOM_FIELD)
    # produce interlaced output with the entire output having the same field
    # polarity (top or bottom first). * Follow, Default Top (FOLLOW_TOP_FIELD)
    # and Follow, Default Bottom (FOLLOW_BOTTOM_FIELD) use the same field
    # polarity as the source. Therefore, behavior depends on the input scan type.
    # \- If the source is interlaced, the output will be interlaced with the same
    # polarity as the source (it will follow the source). The output could
    # therefore be a mix of "top field first" and "bottom field first". \- If the
    # source is progressive, the output will be interlaced with "top field first"
    # or "bottom field first" polarity, depending on which of the Follow options
    # you chose.
    interlace_mode: typing.Union[str, "Mpeg2InterlaceMode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Use Intra DC precision (Mpeg2IntraDcPrecision) to set quantization
    # precision for intra-block DC coefficients. If you choose the value auto,
    # the service will automatically select the precision based on the per-frame
    # compression ratio.
    intra_dc_precision: typing.Union[str, "Mpeg2IntraDcPrecision"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )

    # Maximum bitrate in bits/second. For example, enter five megabits per second
    # as 5000000.
    max_bitrate: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Enforces separation between repeated (cadence) I-frames and I-frames
    # inserted by Scene Change Detection. If a scene change I-frame is within
    # I-interval frames of a cadence I-frame, the GOP is shrunk and/or stretched
    # to the scene change I-frame. GOP stretch requires enabling lookahead as
    # well as setting I-interval. The normal cadence resumes for the next GOP.
    # This setting is only used when Scene Change Detect is enabled. Note:
    # Maximum GOP stretch = GOP size + Min-I-interval - 1
    min_i_interval: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Number of B-frames between reference frames.
    number_b_frames_between_reference_frames: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Using the API, enable ParFollowSource if you want the service to use the
    # pixel aspect ratio from the input. Using the console, do this by choosing
    # Follow source for Pixel aspect ratio.
    par_control: typing.Union[str, "Mpeg2ParControl"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Pixel Aspect Ratio denominator.
    par_denominator: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Pixel Aspect Ratio numerator.
    par_numerator: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use Quality tuning level (Mpeg2QualityTuningLevel) to specifiy whether to
    # use single-pass or multipass video encoding.
    quality_tuning_level: typing.Union[str, "Mpeg2QualityTuningLevel"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    # Use Rate control mode (Mpeg2RateControlMode) to specifiy whether the
    # bitrate is variable (vbr) or constant (cbr).
    rate_control_mode: typing.Union[str, "Mpeg2RateControlMode"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # Scene change detection (inserts I-frames on scene changes).
    scene_change_detect: typing.Union[str, "Mpeg2SceneChangeDetect"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # Enables Slow PAL rate conversion. 23.976fps and 24fps input is relabeled as
    # 25fps, and audio is sped up correspondingly.
    slow_pal: typing.Union[str, "Mpeg2SlowPal"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Softness. Selects quantizer matrix, larger values reduce high-frequency
    # content in the encoded image.
    softness: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Adjust quantization within each frame based on spatial variation of content
    # complexity.
    spatial_adaptive_quantization: typing.Union[
        str, "Mpeg2SpatialAdaptiveQuantization"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # Produces a Type D-10 compatible bitstream (SMPTE 356M-2001).
    syntax: typing.Union[str, "Mpeg2Syntax"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Only use Telecine (Mpeg2Telecine) when you set Framerate (Framerate) to
    # 29.970. Set Telecine (Mpeg2Telecine) to Hard (hard) to produce a 29.97i
    # output from a 23.976 input. Set it to Soft (soft) to produce 23.976 output
    # and leave converstion to the player.
    telecine: typing.Union[str, "Mpeg2Telecine"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Adjust quantization within each frame based on temporal variation of
    # content complexity.
    temporal_adaptive_quantization: typing.Union[
        str, "Mpeg2TemporalAdaptiveQuantization"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )


class Mpeg2SlowPal(str):
    """
    Enables Slow PAL rate conversion. 23.976fps and 24fps input is relabeled as
    25fps, and audio is sped up correspondingly.
    """
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class Mpeg2SpatialAdaptiveQuantization(str):
    """
    Adjust quantization within each frame based on spatial variation of content
    complexity.
    """
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class Mpeg2Syntax(str):
    """
    Produces a Type D-10 compatible bitstream (SMPTE 356M-2001).
    """
    DEFAULT = "DEFAULT"
    D_10 = "D_10"


class Mpeg2Telecine(str):
    """
    Only use Telecine (Mpeg2Telecine) when you set Framerate (Framerate) to 29.970.
    Set Telecine (Mpeg2Telecine) to Hard (hard) to produce a 29.97i output from a
    23.976 input. Set it to Soft (soft) to produce 23.976 output and leave
    converstion to the player.
    """
    NONE = "NONE"
    SOFT = "SOFT"
    HARD = "HARD"


class Mpeg2TemporalAdaptiveQuantization(str):
    """
    Adjust quantization within each frame based on temporal variation of content
    complexity.
    """
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class MsSmoothAudioDeduplication(str):
    """
    COMBINE_DUPLICATE_STREAMS combines identical audio encoding settings across a
    Microsoft Smooth output group into a single audio stream.
    """
    COMBINE_DUPLICATE_STREAMS = "COMBINE_DUPLICATE_STREAMS"
    NONE = "NONE"


@dataclasses.dataclass
class MsSmoothEncryptionSettings(ShapeBase):
    """
    If you are using DRM, set DRM System (MsSmoothEncryptionSettings) to specify the
    value SpekeKeyProvider.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "speke_key_provider",
                "SpekeKeyProvider",
                TypeInfo(SpekeKeyProvider),
            ),
        ]

    # Settings for use with a SPEKE key provider
    speke_key_provider: "SpekeKeyProvider" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class MsSmoothGroupSettings(ShapeBase):
    """
    Required when you set (Type) under (OutputGroups)>(OutputGroupSettings) to
    MS_SMOOTH_GROUP_SETTINGS.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "audio_deduplication",
                "AudioDeduplication",
                TypeInfo(typing.Union[str, MsSmoothAudioDeduplication]),
            ),
            (
                "destination",
                "Destination",
                TypeInfo(str),
            ),
            (
                "encryption",
                "Encryption",
                TypeInfo(MsSmoothEncryptionSettings),
            ),
            (
                "fragment_length",
                "FragmentLength",
                TypeInfo(int),
            ),
            (
                "manifest_encoding",
                "ManifestEncoding",
                TypeInfo(typing.Union[str, MsSmoothManifestEncoding]),
            ),
        ]

    # COMBINE_DUPLICATE_STREAMS combines identical audio encoding settings across
    # a Microsoft Smooth output group into a single audio stream.
    audio_deduplication: typing.Union[str, "MsSmoothAudioDeduplication"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # Use Destination (Destination) to specify the S3 output location and the
    # output filename base. Destination accepts format identifiers. If you do not
    # specify the base filename in the URI, the service will use the filename of
    # the input file. If your job has multiple inputs, the service uses the
    # filename of the first input file.
    destination: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If you are using DRM, set DRM System (MsSmoothEncryptionSettings) to
    # specify the value SpekeKeyProvider.
    encryption: "MsSmoothEncryptionSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Use Fragment length (FragmentLength) to specify the mp4 fragment sizes in
    # seconds. Fragment length must be compatible with GOP size and framerate.
    fragment_length: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use Manifest encoding (MsSmoothManifestEncoding) to specify the encoding
    # format for the server and client manifest. Valid options are utf8 and
    # utf16.
    manifest_encoding: typing.Union[str, "MsSmoothManifestEncoding"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )


class MsSmoothManifestEncoding(str):
    """
    Use Manifest encoding (MsSmoothManifestEncoding) to specify the encoding format
    for the server and client manifest. Valid options are utf8 and utf16.
    """
    UTF8 = "UTF8"
    UTF16 = "UTF16"


@dataclasses.dataclass
class NielsenConfiguration(ShapeBase):
    """
    Settings for Nielsen Configuration
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "breakout_code",
                "BreakoutCode",
                TypeInfo(int),
            ),
            (
                "distributor_id",
                "DistributorId",
                TypeInfo(str),
            ),
        ]

    # Use Nielsen Configuration (NielsenConfiguration) to set the Nielsen
    # measurement system breakout code. Supported values are 0, 3, 7, and 9.
    breakout_code: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use Distributor ID (DistributorID) to specify the distributor ID that is
    # assigned to your organization by Neilsen.
    distributor_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class NoiseReducer(ShapeBase):
    """
    Enable the Noise reducer (NoiseReducer) feature to remove noise from your video
    output if necessary. Enable or disable this feature for each output
    individually. This setting is disabled by default. When you enable Noise reducer
    (NoiseReducer), you must also select a value for Noise reducer filter
    (NoiseReducerFilter).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "filter",
                "Filter",
                TypeInfo(typing.Union[str, NoiseReducerFilter]),
            ),
            (
                "filter_settings",
                "FilterSettings",
                TypeInfo(NoiseReducerFilterSettings),
            ),
            (
                "spatial_filter_settings",
                "SpatialFilterSettings",
                TypeInfo(NoiseReducerSpatialFilterSettings),
            ),
        ]

    # Use Noise reducer filter (NoiseReducerFilter) to select one of the
    # following spatial image filtering functions. To use this setting, you must
    # also enable Noise reducer (NoiseReducer). * Bilateral is an edge preserving
    # noise reduction filter. * Mean (softest), Gaussian, Lanczos, and Sharpen
    # (sharpest) are convolution filters. * Conserve is a min/max noise reduction
    # filter. * Spatial is a frequency-domain filter based on JND principles.
    filter: typing.Union[str, "NoiseReducerFilter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Settings for a noise reducer filter
    filter_settings: "NoiseReducerFilterSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Noise reducer filter settings for spatial filter.
    spatial_filter_settings: "NoiseReducerSpatialFilterSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class NoiseReducerFilter(str):
    """
    Use Noise reducer filter (NoiseReducerFilter) to select one of the following
    spatial image filtering functions. To use this setting, you must also enable
    Noise reducer (NoiseReducer). * Bilateral is an edge preserving noise reduction
    filter. * Mean (softest), Gaussian, Lanczos, and Sharpen (sharpest) are
    convolution filters. * Conserve is a min/max noise reduction filter. * Spatial
    is a frequency-domain filter based on JND principles.
    """
    BILATERAL = "BILATERAL"
    MEAN = "MEAN"
    GAUSSIAN = "GAUSSIAN"
    LANCZOS = "LANCZOS"
    SHARPEN = "SHARPEN"
    CONSERVE = "CONSERVE"
    SPATIAL = "SPATIAL"


@dataclasses.dataclass
class NoiseReducerFilterSettings(ShapeBase):
    """
    Settings for a noise reducer filter
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "strength",
                "Strength",
                TypeInfo(int),
            ),
        ]

    # Relative strength of noise reducing filter. Higher values produce stronger
    # filtering.
    strength: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class NoiseReducerSpatialFilterSettings(ShapeBase):
    """
    Noise reducer filter settings for spatial filter.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "post_filter_sharpen_strength",
                "PostFilterSharpenStrength",
                TypeInfo(int),
            ),
            (
                "speed",
                "Speed",
                TypeInfo(int),
            ),
            (
                "strength",
                "Strength",
                TypeInfo(int),
            ),
        ]

    # Specify strength of post noise reduction sharpening filter, with 0
    # disabling the filter and 3 enabling it at maximum strength.
    post_filter_sharpen_strength: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The speed of the filter, from -2 (lower speed) to 3 (higher speed), with 0
    # being the nominal value.
    speed: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Relative strength of noise reducing filter. Higher values produce stronger
    # filtering.
    strength: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class NotFoundException(ShapeBase):
    """
    The resource you requested doesn't exist.
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

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class Order(str):
    """
    When you request lists of resources, you can optionally specify whether they are
    sorted in ASCENDING or DESCENDING order. Default varies by resource.
    """
    ASCENDING = "ASCENDING"
    DESCENDING = "DESCENDING"


@dataclasses.dataclass
class Output(ShapeBase):
    """
    An output object describes the settings for a single output file or stream in an
    output group.
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
                "caption_descriptions",
                "CaptionDescriptions",
                TypeInfo(typing.List[CaptionDescription]),
            ),
            (
                "container_settings",
                "ContainerSettings",
                TypeInfo(ContainerSettings),
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
            (
                "output_settings",
                "OutputSettings",
                TypeInfo(OutputSettings),
            ),
            (
                "preset",
                "Preset",
                TypeInfo(str),
            ),
            (
                "video_description",
                "VideoDescription",
                TypeInfo(VideoDescription),
            ),
        ]

    # (AudioDescriptions) contains groups of audio encoding settings organized by
    # audio codec. Include one instance of (AudioDescriptions) per output.
    # (AudioDescriptions) can contain multiple groups of encoding settings.
    audio_descriptions: typing.List["AudioDescription"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # (CaptionDescriptions) contains groups of captions settings. For each output
    # that has captions, include one instance of (CaptionDescriptions).
    # (CaptionDescriptions) can contain multiple groups of captions settings.
    caption_descriptions: typing.List["CaptionDescription"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Container specific settings.
    container_settings: "ContainerSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Use Extension (Extension) to specify the file extension for outputs in File
    # output groups. If you do not specify a value, the service will use default
    # extensions by container type as follows * MPEG-2 transport stream, m2ts *
    # Quicktime, mov * MXF container, mxf * MPEG-4 container, mp4 * No Container,
    # the service will use codec extensions (e.g. AAC, H265, H265, AC3)
    extension: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use Name modifier (NameModifier) to have the service add a string to the
    # end of each output filename. You specify the base filename as part of your
    # destination URI. When you create multiple outputs in the same output group,
    # Name modifier (NameModifier) is required. Name modifier also accepts format
    # identifiers. For DASH ISO outputs, if you use the format identifiers
    # $Number$ or $Time$ in one output, you must use them in the same way in all
    # outputs of the output group.
    name_modifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specific settings for this type of output.
    output_settings: "OutputSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Use Preset (Preset) to specifiy a preset for your transcoding settings.
    # Provide the system or custom preset name. You can specify either Preset
    # (Preset) or Container settings (ContainerSettings), but not both.
    preset: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (VideoDescription) contains a group of video encoding settings. The
    # specific video settings depend on the video codec you choose when you
    # specify a value for Video codec (codec). Include one instance of
    # (VideoDescription) per output.
    video_description: "VideoDescription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class OutputChannelMapping(ShapeBase):
    """
    OutputChannel mapping settings.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "input_channels",
                "InputChannels",
                TypeInfo(typing.List[int]),
            ),
        ]

    # List of input channels
    input_channels: typing.List[int] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class OutputDetail(ShapeBase):
    """
    Details regarding output
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "duration_in_ms",
                "DurationInMs",
                TypeInfo(int),
            ),
            (
                "video_details",
                "VideoDetails",
                TypeInfo(VideoDetail),
            ),
        ]

    # Duration in milliseconds
    duration_in_ms: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Contains details about the output's video stream
    video_details: "VideoDetail" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class OutputGroup(ShapeBase):
    """
    Group of outputs
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "custom_name",
                "CustomName",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
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
        ]

    # Use Custom Group Name (CustomName) to specify a name for the output group.
    # This value is displayed on the console and can make your job settings JSON
    # more human-readable. It does not affect your outputs. Use up to twelve
    # characters that are either letters, numbers, spaces, or underscores.
    custom_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Name of the output group
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Output Group settings, including type
    output_group_settings: "OutputGroupSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # This object holds groups of encoding settings, one group of settings per
    # output.
    outputs: typing.List["Output"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class OutputGroupDetail(ShapeBase):
    """
    Contains details about the output groups specified in the job settings.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "output_details",
                "OutputDetails",
                TypeInfo(typing.List[OutputDetail]),
            ),
        ]

    # Details about the output
    output_details: typing.List["OutputDetail"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class OutputGroupSettings(ShapeBase):
    """
    Output Group settings, including type
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cmaf_group_settings",
                "CmafGroupSettings",
                TypeInfo(CmafGroupSettings),
            ),
            (
                "dash_iso_group_settings",
                "DashIsoGroupSettings",
                TypeInfo(DashIsoGroupSettings),
            ),
            (
                "file_group_settings",
                "FileGroupSettings",
                TypeInfo(FileGroupSettings),
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
                "type",
                "Type",
                TypeInfo(typing.Union[str, OutputGroupType]),
            ),
        ]

    # Required when you set (Type) under (OutputGroups)>(OutputGroupSettings) to
    # CMAF_GROUP_SETTINGS. Each output in a CMAF Output Group may only contain a
    # single video, audio, or caption output.
    cmaf_group_settings: "CmafGroupSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Required when you set (Type) under (OutputGroups)>(OutputGroupSettings) to
    # DASH_ISO_GROUP_SETTINGS.
    dash_iso_group_settings: "DashIsoGroupSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Required when you set (Type) under (OutputGroups)>(OutputGroupSettings) to
    # FILE_GROUP_SETTINGS.
    file_group_settings: "FileGroupSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Required when you set (Type) under (OutputGroups)>(OutputGroupSettings) to
    # HLS_GROUP_SETTINGS.
    hls_group_settings: "HlsGroupSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Required when you set (Type) under (OutputGroups)>(OutputGroupSettings) to
    # MS_SMOOTH_GROUP_SETTINGS.
    ms_smooth_group_settings: "MsSmoothGroupSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Type of output group (File group, Apple HLS, DASH ISO, Microsoft Smooth
    # Streaming, CMAF)
    type: typing.Union[str, "OutputGroupType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class OutputGroupType(str):
    """
    Type of output group (File group, Apple HLS, DASH ISO, Microsoft Smooth
    Streaming, CMAF)
    """
    HLS_GROUP_SETTINGS = "HLS_GROUP_SETTINGS"
    DASH_ISO_GROUP_SETTINGS = "DASH_ISO_GROUP_SETTINGS"
    FILE_GROUP_SETTINGS = "FILE_GROUP_SETTINGS"
    MS_SMOOTH_GROUP_SETTINGS = "MS_SMOOTH_GROUP_SETTINGS"
    CMAF_GROUP_SETTINGS = "CMAF_GROUP_SETTINGS"


class OutputSdt(str):
    """
    Selects method of inserting SDT information into output stream. "Follow input
    SDT" copies SDT information from input stream to output stream. "Follow input
    SDT if present" copies SDT information from input stream to output stream if SDT
    information is present in the input, otherwise it will fall back on the user-
    defined values. Enter "SDT Manually" means user will enter the SDT information.
    "No SDT" means output stream will not contain SDT information.
    """
    SDT_FOLLOW = "SDT_FOLLOW"
    SDT_FOLLOW_IF_PRESENT = "SDT_FOLLOW_IF_PRESENT"
    SDT_MANUAL = "SDT_MANUAL"
    SDT_NONE = "SDT_NONE"


@dataclasses.dataclass
class OutputSettings(ShapeBase):
    """
    Specific settings for this type of output.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "hls_settings",
                "HlsSettings",
                TypeInfo(HlsSettings),
            ),
        ]

    # Settings for HLS output groups
    hls_settings: "HlsSettings" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Preset(ShapeBase):
    """
    A preset is a collection of preconfigured media conversion settings that you
    want MediaConvert to apply to the output during the conversion process.
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
                "settings",
                "Settings",
                TypeInfo(PresetSettings),
            ),
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "category",
                "Category",
                TypeInfo(str),
            ),
            (
                "created_at",
                "CreatedAt",
                TypeInfo(datetime.datetime),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "last_updated",
                "LastUpdated",
                TypeInfo(datetime.datetime),
            ),
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, Type]),
            ),
        ]

    # A name you create for each preset. Each name must be unique within your
    # account.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Settings for preset
    settings: "PresetSettings" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An identifier for this resource that is unique within all of AWS.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional category you create to organize your presets.
    category: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The timestamp in epoch seconds for preset creation.
    created_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An optional description you create for each preset.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The timestamp in epoch seconds when the preset was last updated.
    last_updated: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A preset can be of two types: system or custom. System or built-in preset
    # can't be modified or deleted by the user.
    type: typing.Union[str, "Type"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class PresetListBy(str):
    """
    Optional. When you request a list of presets, you can choose to list them
    alphabetically by NAME or chronologically by CREATION_DATE. If you don't
    specify, the service will list them by name.
    """
    NAME = "NAME"
    CREATION_DATE = "CREATION_DATE"
    SYSTEM = "SYSTEM"


@dataclasses.dataclass
class PresetSettings(ShapeBase):
    """
    Settings for preset
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
                "caption_descriptions",
                "CaptionDescriptions",
                TypeInfo(typing.List[CaptionDescriptionPreset]),
            ),
            (
                "container_settings",
                "ContainerSettings",
                TypeInfo(ContainerSettings),
            ),
            (
                "video_description",
                "VideoDescription",
                TypeInfo(VideoDescription),
            ),
        ]

    # (AudioDescriptions) contains groups of audio encoding settings organized by
    # audio codec. Include one instance of (AudioDescriptions) per output.
    # (AudioDescriptions) can contain multiple groups of encoding settings.
    audio_descriptions: typing.List["AudioDescription"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Caption settings for this preset. There can be multiple caption settings in
    # a single output.
    caption_descriptions: typing.List["CaptionDescriptionPreset"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # Container specific settings.
    container_settings: "ContainerSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # (VideoDescription) contains a group of video encoding settings. The
    # specific video settings depend on the video codec you choose when you
    # specify a value for Video codec (codec). Include one instance of
    # (VideoDescription) per output.
    video_description: "VideoDescription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class ProresCodecProfile(str):
    """
    Use Profile (ProResCodecProfile) to specifiy the type of Apple ProRes codec to
    use for this output.
    """
    APPLE_PRORES_422 = "APPLE_PRORES_422"
    APPLE_PRORES_422_HQ = "APPLE_PRORES_422_HQ"
    APPLE_PRORES_422_LT = "APPLE_PRORES_422_LT"
    APPLE_PRORES_422_PROXY = "APPLE_PRORES_422_PROXY"


class ProresFramerateControl(str):
    """
    If you are using the console, use the Framerate setting to specify the framerate
    for this output. If you want to keep the same framerate as the input video,
    choose Follow source. If you want to do framerate conversion, choose a framerate
    from the dropdown list or choose Custom. The framerates shown in the dropdown
    list are decimal approximations of fractions. If you choose Custom, specify your
    framerate as a fraction. If you are creating your transcoding job sepecification
    as a JSON file without the console, use FramerateControl to specify which value
    the service uses for the framerate for this output. Choose
    INITIALIZE_FROM_SOURCE if you want the service to use the framerate from the
    input. Choose SPECIFIED if you want the service to use the framerate you specify
    in the settings FramerateNumerator and FramerateDenominator.
    """
    INITIALIZE_FROM_SOURCE = "INITIALIZE_FROM_SOURCE"
    SPECIFIED = "SPECIFIED"


class ProresFramerateConversionAlgorithm(str):
    """
    When set to INTERPOLATE, produces smoother motion during framerate conversion.
    """
    DUPLICATE_DROP = "DUPLICATE_DROP"
    INTERPOLATE = "INTERPOLATE"


class ProresInterlaceMode(str):
    """
    Use Interlace mode (InterlaceMode) to choose the scan line type for the output.
    * Top Field First (TOP_FIELD) and Bottom Field First (BOTTOM_FIELD) produce
    interlaced output with the entire output having the same field polarity (top or
    bottom first). * Follow, Default Top (FOLLOW_TOP_FIELD) and Follow, Default
    Bottom (FOLLOW_BOTTOM_FIELD) use the same field polarity as the source.
    Therefore, behavior depends on the input scan type. \- If the source is
    interlaced, the output will be interlaced with the same polarity as the source
    (it will follow the source). The output could therefore be a mix of "top field
    first" and "bottom field first". \- If the source is progressive, the output
    will be interlaced with "top field first" or "bottom field first" polarity,
    depending on which of the Follow options you chose.
    """
    PROGRESSIVE = "PROGRESSIVE"
    TOP_FIELD = "TOP_FIELD"
    BOTTOM_FIELD = "BOTTOM_FIELD"
    FOLLOW_TOP_FIELD = "FOLLOW_TOP_FIELD"
    FOLLOW_BOTTOM_FIELD = "FOLLOW_BOTTOM_FIELD"


class ProresParControl(str):
    """
    Use (ProresParControl) to specify how the service determines the pixel aspect
    ratio. Set to Follow source (INITIALIZE_FROM_SOURCE) to use the pixel aspect
    ratio from the input. To specify a different pixel aspect ratio: Using the
    console, choose it from the dropdown menu. Using the API, set ProresParControl
    to (SPECIFIED) and provide for (ParNumerator) and (ParDenominator).
    """
    INITIALIZE_FROM_SOURCE = "INITIALIZE_FROM_SOURCE"
    SPECIFIED = "SPECIFIED"


@dataclasses.dataclass
class ProresSettings(ShapeBase):
    """
    Required when you set (Codec) under (VideoDescription)>(CodecSettings) to the
    value PRORES.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "codec_profile",
                "CodecProfile",
                TypeInfo(typing.Union[str, ProresCodecProfile]),
            ),
            (
                "framerate_control",
                "FramerateControl",
                TypeInfo(typing.Union[str, ProresFramerateControl]),
            ),
            (
                "framerate_conversion_algorithm",
                "FramerateConversionAlgorithm",
                TypeInfo(typing.Union[str, ProresFramerateConversionAlgorithm]),
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
                "interlace_mode",
                "InterlaceMode",
                TypeInfo(typing.Union[str, ProresInterlaceMode]),
            ),
            (
                "par_control",
                "ParControl",
                TypeInfo(typing.Union[str, ProresParControl]),
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
                "slow_pal",
                "SlowPal",
                TypeInfo(typing.Union[str, ProresSlowPal]),
            ),
            (
                "telecine",
                "Telecine",
                TypeInfo(typing.Union[str, ProresTelecine]),
            ),
        ]

    # Use Profile (ProResCodecProfile) to specifiy the type of Apple ProRes codec
    # to use for this output.
    codec_profile: typing.Union[str, "ProresCodecProfile"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If you are using the console, use the Framerate setting to specify the
    # framerate for this output. If you want to keep the same framerate as the
    # input video, choose Follow source. If you want to do framerate conversion,
    # choose a framerate from the dropdown list or choose Custom. The framerates
    # shown in the dropdown list are decimal approximations of fractions. If you
    # choose Custom, specify your framerate as a fraction. If you are creating
    # your transcoding job sepecification as a JSON file without the console, use
    # FramerateControl to specify which value the service uses for the framerate
    # for this output. Choose INITIALIZE_FROM_SOURCE if you want the service to
    # use the framerate from the input. Choose SPECIFIED if you want the service
    # to use the framerate you specify in the settings FramerateNumerator and
    # FramerateDenominator.
    framerate_control: typing.Union[str, "ProresFramerateControl"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # When set to INTERPOLATE, produces smoother motion during framerate
    # conversion.
    framerate_conversion_algorithm: typing.Union[
        str, "ProresFramerateConversionAlgorithm"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # Framerate denominator.
    framerate_denominator: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When you use the API for transcode jobs that use framerate conversion,
    # specify the framerate as a fraction. For example, 24000 / 1001 = 23.976
    # fps. Use FramerateNumerator to specify the numerator of this fraction. In
    # this example, use 24000 for the value of FramerateNumerator.
    framerate_numerator: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use Interlace mode (InterlaceMode) to choose the scan line type for the
    # output. * Top Field First (TOP_FIELD) and Bottom Field First (BOTTOM_FIELD)
    # produce interlaced output with the entire output having the same field
    # polarity (top or bottom first). * Follow, Default Top (FOLLOW_TOP_FIELD)
    # and Follow, Default Bottom (FOLLOW_BOTTOM_FIELD) use the same field
    # polarity as the source. Therefore, behavior depends on the input scan type.
    # \- If the source is interlaced, the output will be interlaced with the same
    # polarity as the source (it will follow the source). The output could
    # therefore be a mix of "top field first" and "bottom field first". \- If the
    # source is progressive, the output will be interlaced with "top field first"
    # or "bottom field first" polarity, depending on which of the Follow options
    # you chose.
    interlace_mode: typing.Union[str, "ProresInterlaceMode"
                                ] = dataclasses.field(
                                    default=ShapeBase.NOT_SET,
                                )

    # Use (ProresParControl) to specify how the service determines the pixel
    # aspect ratio. Set to Follow source (INITIALIZE_FROM_SOURCE) to use the
    # pixel aspect ratio from the input. To specify a different pixel aspect
    # ratio: Using the console, choose it from the dropdown menu. Using the API,
    # set ProresParControl to (SPECIFIED) and provide for (ParNumerator) and
    # (ParDenominator).
    par_control: typing.Union[str, "ProresParControl"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Pixel Aspect Ratio denominator.
    par_denominator: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Pixel Aspect Ratio numerator.
    par_numerator: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Enables Slow PAL rate conversion. 23.976fps and 24fps input is relabeled as
    # 25fps, and audio is sped up correspondingly.
    slow_pal: typing.Union[str, "ProresSlowPal"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Only use Telecine (ProresTelecine) when you set Framerate (Framerate) to
    # 29.970. Set Telecine (ProresTelecine) to Hard (hard) to produce a 29.97i
    # output from a 23.976 input. Set it to Soft (soft) to produce 23.976 output
    # and leave converstion to the player.
    telecine: typing.Union[str, "ProresTelecine"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class ProresSlowPal(str):
    """
    Enables Slow PAL rate conversion. 23.976fps and 24fps input is relabeled as
    25fps, and audio is sped up correspondingly.
    """
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class ProresTelecine(str):
    """
    Only use Telecine (ProresTelecine) when you set Framerate (Framerate) to 29.970.
    Set Telecine (ProresTelecine) to Hard (hard) to produce a 29.97i output from a
    23.976 input. Set it to Soft (soft) to produce 23.976 output and leave
    converstion to the player.
    """
    NONE = "NONE"
    HARD = "HARD"


@dataclasses.dataclass
class Queue(ShapeBase):
    """
    MediaConvert jobs are submitted to a queue. Unless specified otherwise jobs are
    submitted to a built-in default queue. User can create additional queues to
    separate the jobs of different categories or priority.
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
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "created_at",
                "CreatedAt",
                TypeInfo(datetime.datetime),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "last_updated",
                "LastUpdated",
                TypeInfo(datetime.datetime),
            ),
            (
                "progressing_jobs_count",
                "ProgressingJobsCount",
                TypeInfo(int),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, QueueStatus]),
            ),
            (
                "submitted_jobs_count",
                "SubmittedJobsCount",
                TypeInfo(int),
            ),
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, Type]),
            ),
        ]

    # A name you create for each queue. Each name must be unique within your
    # account.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An identifier for this resource that is unique within all of AWS.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The timestamp in epoch seconds for queue creation.
    created_at: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An optional description you create for each queue.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The timestamp in epoch seconds when the queue was last updated.
    last_updated: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Estimated number of jobs in PROGRESSING status.
    progressing_jobs_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Queues can be ACTIVE or PAUSED. If you pause a queue, jobs in that queue
    # won't begin. Jobs running when a queue is paused continue to run until they
    # finish or error out.
    status: typing.Union[str, "QueueStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Estimated number of jobs in SUBMITTED status.
    submitted_jobs_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A queue can be of two types: system or custom. System or built-in queues
    # can't be modified or deleted by the user.
    type: typing.Union[str, "Type"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class QueueListBy(str):
    """
    Optional. When you request a list of queues, you can choose to list them
    alphabetically by NAME or chronologically by CREATION_DATE. If you don't
    specify, the service will list them by creation date.
    """
    NAME = "NAME"
    CREATION_DATE = "CREATION_DATE"


class QueueStatus(str):
    """
    Queues can be ACTIVE or PAUSED. If you pause a queue, jobs in that queue won't
    begin. Jobs running when a queue is paused continue to run until they finish or
    error out.
    """
    ACTIVE = "ACTIVE"
    PAUSED = "PAUSED"


@dataclasses.dataclass
class Rectangle(ShapeBase):
    """
    Use Rectangle to identify a specific area of the video frame.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "height",
                "Height",
                TypeInfo(int),
            ),
            (
                "width",
                "Width",
                TypeInfo(int),
            ),
            (
                "x",
                "X",
                TypeInfo(int),
            ),
            (
                "y",
                "Y",
                TypeInfo(int),
            ),
        ]

    # Height of rectangle in pixels. Specify only even numbers.
    height: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Width of rectangle in pixels. Specify only even numbers.
    width: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The distance, in pixels, between the rectangle and the left edge of the
    # video frame. Specify only even numbers.
    x: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The distance, in pixels, between the rectangle and the top edge of the
    # video frame. Specify only even numbers.
    y: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RemixSettings(ShapeBase):
    """
    Use Manual audio remixing (RemixSettings) to adjust audio levels for each audio
    channel in each output of your job. With audio remixing, you can output more or
    fewer audio channels than your input audio source provides.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "channel_mapping",
                "ChannelMapping",
                TypeInfo(ChannelMapping),
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

    # Channel mapping (ChannelMapping) contains the group of fields that hold the
    # remixing value for each channel. Units are in dB. Acceptable values are
    # within the range from -60 (mute) through 6. A setting of 0 passes the input
    # channel unchanged to the output channel (no attenuation or amplification).
    channel_mapping: "ChannelMapping" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specify the number of audio channels from your input that you want to use
    # in your output. With remixing, you might combine or split the data in these
    # channels, so the number of channels in your final output might be
    # different.
    channels_in: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specify the number of channels in this output after remixing. Valid values:
    # 1, 2, 4, 6, 8
    channels_out: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceTags(ShapeBase):
    """
    The Amazon Resource Name (ARN) and tags for an AWS Elemental MediaConvert
    resource.
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
                "tags",
                "Tags",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The Amazon Resource Name (ARN) of the resource.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The tags for the resource.
    tags: typing.Dict[str, str] = dataclasses.field(default=ShapeBase.NOT_SET, )


class RespondToAfd(str):
    """
    Use Respond to AFD (RespondToAfd) to specify how the service changes the video
    itself in response to AFD values in the input. * Choose Respond to clip the
    input video frame according to the AFD value, input display aspect ratio, and
    output display aspect ratio. * Choose Passthrough to include the input AFD
    values. Do not choose this when AfdSignaling is set to (NONE). A preferred
    implementation of this workflow is to set RespondToAfd to (NONE) and set
    AfdSignaling to (AUTO). * Choose None to remove all input AFD values from this
    output.
    """
    NONE = "NONE"
    RESPOND = "RESPOND"
    PASSTHROUGH = "PASSTHROUGH"


class ScalingBehavior(str):
    """
    Applies only if your input aspect ratio is different from your output aspect
    ratio. Enable Stretch to output (StretchToOutput) to have the service stretch
    your video image to fit. Leave this setting disabled to allow the service to
    letterbox your video instead. This setting overrides any positioning value you
    specify elsewhere in the job.
    """
    DEFAULT = "DEFAULT"
    STRETCH_TO_OUTPUT = "STRETCH_TO_OUTPUT"


class SccDestinationFramerate(str):
    """
    Set Framerate (SccDestinationFramerate) to make sure that the captions and the
    video are synchronized in the output. Specify a framerate that matches the
    framerate of the associated video. If the video framerate is 29.97, choose 29.97
    dropframe (FRAMERATE_29_97_DROPFRAME) only if the video has video_insertion=true
    and drop_frame_timecode=true; otherwise, choose 29.97 non-dropframe
    (FRAMERATE_29_97_NON_DROPFRAME).
    """
    FRAMERATE_23_97 = "FRAMERATE_23_97"
    FRAMERATE_24 = "FRAMERATE_24"
    FRAMERATE_29_97_DROPFRAME = "FRAMERATE_29_97_DROPFRAME"
    FRAMERATE_29_97_NON_DROPFRAME = "FRAMERATE_29_97_NON_DROPFRAME"


@dataclasses.dataclass
class SccDestinationSettings(ShapeBase):
    """
    Settings for SCC caption output.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "framerate",
                "Framerate",
                TypeInfo(typing.Union[str, SccDestinationFramerate]),
            ),
        ]

    # Set Framerate (SccDestinationFramerate) to make sure that the captions and
    # the video are synchronized in the output. Specify a framerate that matches
    # the framerate of the associated video. If the video framerate is 29.97,
    # choose 29.97 dropframe (FRAMERATE_29_97_DROPFRAME) only if the video has
    # video_insertion=true and drop_frame_timecode=true; otherwise, choose 29.97
    # non-dropframe (FRAMERATE_29_97_NON_DROPFRAME).
    framerate: typing.Union[str, "SccDestinationFramerate"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SpekeKeyProvider(ShapeBase):
    """
    Settings for use with a SPEKE key provider
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_id",
                "ResourceId",
                TypeInfo(str),
            ),
            (
                "system_ids",
                "SystemIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "url",
                "Url",
                TypeInfo(str),
            ),
        ]

    # The SPEKE-compliant server uses Resource ID (ResourceId) to identify
    # content.
    resource_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Relates to SPEKE implementation. DRM system identifiers. DASH output groups
    # support a max of two system ids. Other group types support one system id.
    system_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Use URL (Url) to specify the SPEKE-compliant server that will provide keys
    # for content.
    url: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StaticKeyProvider(ShapeBase):
    """
    Settings for use with a SPEKE key provider.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
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
                "static_key_value",
                "StaticKeyValue",
                TypeInfo(str),
            ),
            (
                "url",
                "Url",
                TypeInfo(str),
            ),
        ]

    # Relates to DRM implementation. Sets the value of the KEYFORMAT attribute.
    # Must be 'identity' or a reverse DNS string. May be omitted to indicate an
    # implicit value of 'identity'.
    key_format: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Relates to DRM implementation. Either a single positive integer version
    # value or a slash delimited list of version values (1/2/3).
    key_format_versions: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Relates to DRM implementation. Use a 32-character hexidecimal string to
    # specify Key Value (StaticKeyValue).
    static_key_value: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Relates to DRM implementation. The location of the license server used for
    # protecting content.
    url: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TagResourceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The Amazon Resource Name (ARN) of the resource that you want to tag. To get
    # the ARN, send a GET request with the resource name.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The tags that you want to add to the resource. You can tag resources with a
    # key-value pair or with only a key.
    tags: typing.Dict[str, str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TagResourceResponse(OutputShapeBase):
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
class TeletextDestinationSettings(ShapeBase):
    """
    Settings for Teletext caption output
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

    # Set pageNumber to the Teletext page number for the destination captions for
    # this output. This value must be a three-digit hexadecimal string; strings
    # ending in -FF are invalid. If you are passing through the entire set of
    # Teletext data, do not use this field.
    page_number: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TeletextSourceSettings(ShapeBase):
    """
    Settings specific to Teletext caption sources, including Page number.
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

    # Use Page Number (PageNumber) to specify the three-digit hexadecimal page
    # number that will be used for Teletext captions. Do not use this setting if
    # you are passing through teletext from the input source to output.
    page_number: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TimecodeBurnin(ShapeBase):
    """
    Timecode burn-in (TimecodeBurnIn)--Burns the output timecode and specified
    prefix into the output.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "font_size",
                "FontSize",
                TypeInfo(int),
            ),
            (
                "position",
                "Position",
                TypeInfo(typing.Union[str, TimecodeBurninPosition]),
            ),
            (
                "prefix",
                "Prefix",
                TypeInfo(str),
            ),
        ]

    # Use Font Size (FontSize) to set the font size of any burned-in timecode.
    # Valid values are 10, 16, 32, 48.
    font_size: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use Position (Position) under under Timecode burn-in (TimecodeBurnIn) to
    # specify the location the burned-in timecode on output video.
    position: typing.Union[str, "TimecodeBurninPosition"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Use Prefix (Prefix) to place ASCII characters before any burned-in
    # timecode. For example, a prefix of "EZ-" will result in the timecode
    # "EZ-00:00:00:00". Provide either the characters themselves or the ASCII
    # code equivalents. The supported range of characters is 0x20 through 0x7e.
    # This includes letters, numbers, and all special characters represented on a
    # standard English keyboard.
    prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class TimecodeBurninPosition(str):
    """
    Use Position (Position) under under Timecode burn-in (TimecodeBurnIn) to specify
    the location the burned-in timecode on output video.
    """
    TOP_CENTER = "TOP_CENTER"
    TOP_LEFT = "TOP_LEFT"
    TOP_RIGHT = "TOP_RIGHT"
    MIDDLE_LEFT = "MIDDLE_LEFT"
    MIDDLE_CENTER = "MIDDLE_CENTER"
    MIDDLE_RIGHT = "MIDDLE_RIGHT"
    BOTTOM_LEFT = "BOTTOM_LEFT"
    BOTTOM_CENTER = "BOTTOM_CENTER"
    BOTTOM_RIGHT = "BOTTOM_RIGHT"


@dataclasses.dataclass
class TimecodeConfig(ShapeBase):
    """
    These settings control how the service handles timecodes throughout the job.
    These settings don't affect input clipping.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "anchor",
                "Anchor",
                TypeInfo(str),
            ),
            (
                "source",
                "Source",
                TypeInfo(typing.Union[str, TimecodeSource]),
            ),
            (
                "start",
                "Start",
                TypeInfo(str),
            ),
            (
                "timestamp_offset",
                "TimestampOffset",
                TypeInfo(str),
            ),
        ]

    # If you use an editing platform that relies on an anchor timecode, use
    # Anchor Timecode (Anchor) to specify a timecode that will match the input
    # video frame to the output video frame. Use 24-hour format with frame
    # number, (HH:MM:SS:FF) or (HH:MM:SS;FF). This setting ignores framerate
    # conversion. System behavior for Anchor Timecode varies depending on your
    # setting for Source (TimecodeSource). * If Source (TimecodeSource) is set to
    # Specified Start (SPECIFIEDSTART), the first input frame is the specified
    # value in Start Timecode (Start). Anchor Timecode (Anchor) and Start
    # Timecode (Start) are used calculate output timecode. * If Source
    # (TimecodeSource) is set to Start at 0 (ZEROBASED) the first frame is
    # 00:00:00:00. * If Source (TimecodeSource) is set to Embedded (EMBEDDED),
    # the first frame is the timecode value on the first input frame of the
    # input.
    anchor: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use Source (TimecodeSource) to set how timecodes are handled within this
    # job. To make sure that your video, audio, captions, and markers are
    # synchronized and that time-based features, such as image inserter, work
    # correctly, choose the Timecode source option that matches your assets. All
    # timecodes are in a 24-hour format with frame number (HH:MM:SS:FF). *
    # Embedded (EMBEDDED) - Use the timecode that is in the input video. If no
    # embedded timecode is in the source, the service will use Start at 0
    # (ZEROBASED) instead. * Start at 0 (ZEROBASED) - Set the timecode of the
    # initial frame to 00:00:00:00. * Specified Start (SPECIFIEDSTART) - Set the
    # timecode of the initial frame to a value other than zero. You use Start
    # timecode (Start) to provide this value.
    source: typing.Union[str, "TimecodeSource"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Only use when you set Source (TimecodeSource) to Specified start
    # (SPECIFIEDSTART). Use Start timecode (Start) to specify the timecode for
    # the initial frame. Use 24-hour format with frame number, (HH:MM:SS:FF) or
    # (HH:MM:SS;FF).
    start: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Only applies to outputs that support program-date-time stamp. Use Timestamp
    # offset (TimestampOffset) to overwrite the timecode date without affecting
    # the time and frame number. Provide the new date as a string in the format
    # "yyyy-mm-dd". To use Time stamp offset, you must also enable Insert
    # program-date-time (InsertProgramDateTime) in the output settings. For
    # example, if the date part of your timecodes is 2002-1-25 and you want to
    # change it to one year later, set Timestamp offset (TimestampOffset) to
    # 2003-1-25.
    timestamp_offset: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class TimecodeSource(str):
    """
    Use Source (TimecodeSource) to set how timecodes are handled within this job. To
    make sure that your video, audio, captions, and markers are synchronized and
    that time-based features, such as image inserter, work correctly, choose the
    Timecode source option that matches your assets. All timecodes are in a 24-hour
    format with frame number (HH:MM:SS:FF). * Embedded (EMBEDDED) - Use the timecode
    that is in the input video. If no embedded timecode is in the source, the
    service will use Start at 0 (ZEROBASED) instead. * Start at 0 (ZEROBASED) - Set
    the timecode of the initial frame to 00:00:00:00. * Specified Start
    (SPECIFIEDSTART) - Set the timecode of the initial frame to a value other than
    zero. You use Start timecode (Start) to provide this value.
    """
    EMBEDDED = "EMBEDDED"
    ZEROBASED = "ZEROBASED"
    SPECIFIEDSTART = "SPECIFIEDSTART"


class TimedMetadata(str):
    """
    Applies only to HLS outputs. Use this setting to specify whether the service
    inserts the ID3 timed metadata from the input in this output.
    """
    PASSTHROUGH = "PASSTHROUGH"
    NONE = "NONE"


@dataclasses.dataclass
class TimedMetadataInsertion(ShapeBase):
    """
    Enable Timed metadata insertion (TimedMetadataInsertion) to include ID3 tags in
    your job. To include timed metadata, you must enable it here, enable it in each
    output container, and specify tags and timecodes in ID3 insertion (Id3Insertion)
    objects.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id3_insertions",
                "Id3Insertions",
                TypeInfo(typing.List[Id3Insertion]),
            ),
        ]

    # Id3Insertions contains the array of Id3Insertion instances.
    id3_insertions: typing.List["Id3Insertion"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Timing(ShapeBase):
    """
    Information about when jobs are submitted, started, and finished is specified in
    Unix epoch format in seconds.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "finish_time",
                "FinishTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "start_time",
                "StartTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "submit_time",
                "SubmitTime",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The time, in Unix epoch format, that the transcoding job finished
    finish_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time, in Unix epoch format, that transcoding for the job began.
    start_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time, in Unix epoch format, that you submitted the job.
    submit_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class TooManyRequestsException(ShapeBase):
    """
    Too many requests have been sent in too short of a time. The service limits the
    rate at which it will accept requests.
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

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TtmlDestinationSettings(ShapeBase):
    """
    Settings specific to TTML caption outputs, including Pass style information
    (TtmlStylePassthrough).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "style_passthrough",
                "StylePassthrough",
                TypeInfo(typing.Union[str, TtmlStylePassthrough]),
            ),
        ]

    # Pass through style and position information from a TTML-like input source
    # (TTML, SMPTE-TT, CFF-TT) to the CFF-TT output or TTML output.
    style_passthrough: typing.Union[str, "TtmlStylePassthrough"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )


class TtmlStylePassthrough(str):
    """
    Pass through style and position information from a TTML-like input source (TTML,
    SMPTE-TT, CFF-TT) to the CFF-TT output or TTML output.
    """
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class Type(str):
    SYSTEM = "SYSTEM"
    CUSTOM = "CUSTOM"


@dataclasses.dataclass
class UntagResourceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
            (
                "tag_keys",
                "TagKeys",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The Amazon Resource Name (ARN) of the resource that you want to remove tags
    # from. To get the ARN, send a GET request with the resource name.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The keys of the tags that you want to remove from the resource.
    tag_keys: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UntagResourceResponse(OutputShapeBase):
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
class UpdateJobTemplateRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "category",
                "Category",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "queue",
                "Queue",
                TypeInfo(str),
            ),
            (
                "settings",
                "Settings",
                TypeInfo(JobTemplateSettings),
            ),
        ]

    # The name of the job template you are modifying
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new category for the job template, if you are changing it.
    category: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new description for the job template, if you are changing it.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new queue for the job template, if you are changing it.
    queue: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # JobTemplateSettings contains all the transcode settings saved in the
    # template that will be applied to jobs created from it.
    settings: "JobTemplateSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateJobTemplateResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "job_template",
                "JobTemplate",
                TypeInfo(JobTemplate),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A job template is a pre-made set of encoding instructions that you can use
    # to quickly create a job.
    job_template: "JobTemplate" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdatePresetRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "category",
                "Category",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "settings",
                "Settings",
                TypeInfo(PresetSettings),
            ),
        ]

    # The name of the preset you are modifying.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new category for the preset, if you are changing it.
    category: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new description for the preset, if you are changing it.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Settings for preset
    settings: "PresetSettings" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdatePresetResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "preset",
                "Preset",
                TypeInfo(Preset),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A preset is a collection of preconfigured media conversion settings that
    # you want MediaConvert to apply to the output during the conversion process.
    preset: "Preset" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateQueueRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "description",
                "Description",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, QueueStatus]),
            ),
        ]

    # The name of the queue you are modifying.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new description for the queue, if you are changing it.
    description: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Queues can be ACTIVE or PAUSED. If you pause a queue, jobs in that queue
    # won't begin. Jobs running when a queue is paused continue to run until they
    # finish or error out.
    status: typing.Union[str, "QueueStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateQueueResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "queue",
                "Queue",
                TypeInfo(Queue),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # MediaConvert jobs are submitted to a queue. Unless specified otherwise jobs
    # are submitted to a built-in default queue. User can create additional
    # queues to separate the jobs of different categories or priority.
    queue: "Queue" = dataclasses.field(default=ShapeBase.NOT_SET, )


class VideoCodec(str):
    """
    Type of video codec
    """
    FRAME_CAPTURE = "FRAME_CAPTURE"
    H_264 = "H_264"
    H_265 = "H_265"
    MPEG2 = "MPEG2"
    PRORES = "PRORES"


@dataclasses.dataclass
class VideoCodecSettings(ShapeBase):
    """
    Video codec settings, (CodecSettings) under (VideoDescription), contains the
    group of settings related to video encoding. The settings in this group vary
    depending on the value you choose for Video codec (Codec). For each codec enum
    you choose, define the corresponding settings object. The following lists the
    codec enum, settings object pairs. * H_264, H264Settings * H_265, H265Settings *
    MPEG2, Mpeg2Settings * PRORES, ProresSettings * FRAME_CAPTURE,
    FrameCaptureSettings
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "codec",
                "Codec",
                TypeInfo(typing.Union[str, VideoCodec]),
            ),
            (
                "frame_capture_settings",
                "FrameCaptureSettings",
                TypeInfo(FrameCaptureSettings),
            ),
            (
                "h264_settings",
                "H264Settings",
                TypeInfo(H264Settings),
            ),
            (
                "h265_settings",
                "H265Settings",
                TypeInfo(H265Settings),
            ),
            (
                "mpeg2_settings",
                "Mpeg2Settings",
                TypeInfo(Mpeg2Settings),
            ),
            (
                "prores_settings",
                "ProresSettings",
                TypeInfo(ProresSettings),
            ),
        ]

    # Type of video codec
    codec: typing.Union[str, "VideoCodec"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Required when you set (Codec) under (VideoDescription)>(CodecSettings) to
    # the value FRAME_CAPTURE.
    frame_capture_settings: "FrameCaptureSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Required when you set (Codec) under (VideoDescription)>(CodecSettings) to
    # the value H_264.
    h264_settings: "H264Settings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Settings for H265 codec
    h265_settings: "H265Settings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Required when you set (Codec) under (VideoDescription)>(CodecSettings) to
    # the value MPEG2.
    mpeg2_settings: "Mpeg2Settings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Required when you set (Codec) under (VideoDescription)>(CodecSettings) to
    # the value PRORES.
    prores_settings: "ProresSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class VideoDescription(ShapeBase):
    """
    Settings for video outputs
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "afd_signaling",
                "AfdSignaling",
                TypeInfo(typing.Union[str, AfdSignaling]),
            ),
            (
                "anti_alias",
                "AntiAlias",
                TypeInfo(typing.Union[str, AntiAlias]),
            ),
            (
                "codec_settings",
                "CodecSettings",
                TypeInfo(VideoCodecSettings),
            ),
            (
                "color_metadata",
                "ColorMetadata",
                TypeInfo(typing.Union[str, ColorMetadata]),
            ),
            (
                "crop",
                "Crop",
                TypeInfo(Rectangle),
            ),
            (
                "drop_frame_timecode",
                "DropFrameTimecode",
                TypeInfo(typing.Union[str, DropFrameTimecode]),
            ),
            (
                "fixed_afd",
                "FixedAfd",
                TypeInfo(int),
            ),
            (
                "height",
                "Height",
                TypeInfo(int),
            ),
            (
                "position",
                "Position",
                TypeInfo(Rectangle),
            ),
            (
                "respond_to_afd",
                "RespondToAfd",
                TypeInfo(typing.Union[str, RespondToAfd]),
            ),
            (
                "scaling_behavior",
                "ScalingBehavior",
                TypeInfo(typing.Union[str, ScalingBehavior]),
            ),
            (
                "sharpness",
                "Sharpness",
                TypeInfo(int),
            ),
            (
                "timecode_insertion",
                "TimecodeInsertion",
                TypeInfo(typing.Union[str, VideoTimecodeInsertion]),
            ),
            (
                "video_preprocessors",
                "VideoPreprocessors",
                TypeInfo(VideoPreprocessor),
            ),
            (
                "width",
                "Width",
                TypeInfo(int),
            ),
        ]

    # This setting only applies to H.264 and MPEG2 outputs. Use Insert AFD
    # signaling (AfdSignaling) to specify whether the service includes AFD values
    # in the output video data and what those values are. * Choose None to remove
    # all AFD values from this output. * Choose Fixed to ignore input AFD values
    # and instead encode the value specified in the job. * Choose Auto to
    # calculate output AFD values based on the input AFD scaler data.
    afd_signaling: typing.Union[str, "AfdSignaling"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Enable Anti-alias (AntiAlias) to enhance sharp edges in video output when
    # your input resolution is much larger than your output resolution. Default
    # is enabled.
    anti_alias: typing.Union[str, "AntiAlias"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Video codec settings, (CodecSettings) under (VideoDescription), contains
    # the group of settings related to video encoding. The settings in this group
    # vary depending on the value you choose for Video codec (Codec). For each
    # codec enum you choose, define the corresponding settings object. The
    # following lists the codec enum, settings object pairs. * H_264,
    # H264Settings * H_265, H265Settings * MPEG2, Mpeg2Settings * PRORES,
    # ProresSettings * FRAME_CAPTURE, FrameCaptureSettings
    codec_settings: "VideoCodecSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Enable Insert color metadata (ColorMetadata) to include color metadata in
    # this output. This setting is enabled by default.
    color_metadata: typing.Union[str, "ColorMetadata"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Applies only if your input aspect ratio is different from your output
    # aspect ratio. Use Input cropping rectangle (Crop) to specify the video area
    # the service will include in the output. This will crop the input source,
    # causing video pixels to be removed on encode. Do not use this setting if
    # you have enabled Stretch to output (stretchToOutput) in your output
    # settings.
    crop: "Rectangle" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Applies only to 29.97 fps outputs. When this feature is enabled, the
    # service will use drop-frame timecode on outputs. If it is not possible to
    # use drop-frame timecode, the system will fall back to non-drop-frame. This
    # setting is enabled by default when Timecode insertion (TimecodeInsertion)
    # is enabled.
    drop_frame_timecode: typing.Union[str, "DropFrameTimecode"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # Applies only if you set AFD Signaling(AfdSignaling) to Fixed (FIXED). Use
    # Fixed (FixedAfd) to specify a four-bit AFD value which the service will
    # write on all frames of this video output.
    fixed_afd: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use the Height (Height) setting to define the video resolution height for
    # this output. Specify in pixels. If you don't provide a value here, the
    # service will use the input height.
    height: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use Position (Position) to point to a rectangle object to define your
    # position. This setting overrides any other aspect ratio.
    position: "Rectangle" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use Respond to AFD (RespondToAfd) to specify how the service changes the
    # video itself in response to AFD values in the input. * Choose Respond to
    # clip the input video frame according to the AFD value, input display aspect
    # ratio, and output display aspect ratio. * Choose Passthrough to include the
    # input AFD values. Do not choose this when AfdSignaling is set to (NONE). A
    # preferred implementation of this workflow is to set RespondToAfd to (NONE)
    # and set AfdSignaling to (AUTO). * Choose None to remove all input AFD
    # values from this output.
    respond_to_afd: typing.Union[str, "RespondToAfd"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Applies only if your input aspect ratio is different from your output
    # aspect ratio. Enable Stretch to output (StretchToOutput) to have the
    # service stretch your video image to fit. Leave this setting disabled to
    # allow the service to letterbox your video instead. This setting overrides
    # any positioning value you specify elsewhere in the job.
    scaling_behavior: typing.Union[str, "ScalingBehavior"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Use Sharpness (Sharpness)setting to specify the strength of anti-aliasing.
    # This setting changes the width of the anti-alias filter kernel used for
    # scaling. Sharpness only applies if your output resolution is different from
    # your input resolution, and if you set Anti-alias (AntiAlias) to ENABLED. 0
    # is the softest setting, 100 the sharpest, and 50 recommended for most
    # content.
    sharpness: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Applies only to H.264, H.265, MPEG2, and ProRes outputs. Only enable
    # Timecode insertion when the input framerate is identical to the output
    # framerate. To include timecodes in this output, set Timecode insertion
    # (VideoTimecodeInsertion) to PIC_TIMING_SEI. To leave them out, set it to
    # DISABLED. Default is DISABLED. When the service inserts timecodes in an
    # output, by default, it uses any embedded timecodes from the input. If none
    # are present, the service will set the timecode for the first output frame
    # to zero. To change this default behavior, adjust the settings under
    # Timecode configuration (TimecodeConfig). In the console, these settings are
    # located under Job > Job settings > Timecode configuration. Note - Timecode
    # source under input settings (InputTimecodeSource) does not affect the
    # timecodes that are inserted in the output. Source under Job settings >
    # Timecode configuration (TimecodeSource) does.
    timecode_insertion: typing.Union[str, "VideoTimecodeInsertion"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )

    # Find additional transcoding features under Preprocessors
    # (VideoPreprocessors). Enable the features at each output individually.
    # These features are disabled by default.
    video_preprocessors: "VideoPreprocessor" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Use Width (Width) to define the video resolution width, in pixels, for this
    # output. If you don't provide a value here, the service will use the input
    # width.
    width: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class VideoDetail(ShapeBase):
    """
    Contains details about the output's video stream
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "height_in_px",
                "HeightInPx",
                TypeInfo(int),
            ),
            (
                "width_in_px",
                "WidthInPx",
                TypeInfo(int),
            ),
        ]

    # Height in pixels for the output
    height_in_px: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Width in pixels for the output
    width_in_px: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class VideoPreprocessor(ShapeBase):
    """
    Find additional transcoding features under Preprocessors (VideoPreprocessors).
    Enable the features at each output individually. These features are disabled by
    default.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "color_corrector",
                "ColorCorrector",
                TypeInfo(ColorCorrector),
            ),
            (
                "deinterlacer",
                "Deinterlacer",
                TypeInfo(Deinterlacer),
            ),
            (
                "image_inserter",
                "ImageInserter",
                TypeInfo(ImageInserter),
            ),
            (
                "noise_reducer",
                "NoiseReducer",
                TypeInfo(NoiseReducer),
            ),
            (
                "timecode_burnin",
                "TimecodeBurnin",
                TypeInfo(TimecodeBurnin),
            ),
        ]

    # Enable the Color corrector (ColorCorrector) feature if necessary. Enable or
    # disable this feature for each output individually. This setting is disabled
    # by default.
    color_corrector: "ColorCorrector" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Use Deinterlacer (Deinterlacer) to produce smoother motion and a clearer
    # picture.
    deinterlacer: "Deinterlacer" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Enable the Image inserter (ImageInserter) feature to include a graphic
    # overlay on your video. Enable or disable this feature for each output
    # individually. This setting is disabled by default.
    image_inserter: "ImageInserter" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Enable the Noise reducer (NoiseReducer) feature to remove noise from your
    # video output if necessary. Enable or disable this feature for each output
    # individually. This setting is disabled by default.
    noise_reducer: "NoiseReducer" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Timecode burn-in (TimecodeBurnIn)--Burns the output timecode and specified
    # prefix into the output.
    timecode_burnin: "TimecodeBurnin" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class VideoSelector(ShapeBase):
    """
    Selector for video.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "color_space",
                "ColorSpace",
                TypeInfo(typing.Union[str, ColorSpace]),
            ),
            (
                "color_space_usage",
                "ColorSpaceUsage",
                TypeInfo(typing.Union[str, ColorSpaceUsage]),
            ),
            (
                "hdr10_metadata",
                "Hdr10Metadata",
                TypeInfo(Hdr10Metadata),
            ),
            (
                "pid",
                "Pid",
                TypeInfo(int),
            ),
            (
                "program_number",
                "ProgramNumber",
                TypeInfo(int),
            ),
        ]

    # If your input video has accurate color space metadata, or if you don't know
    # about color space, leave this set to the default value FOLLOW. The service
    # will automatically detect your input color space. If your input video has
    # metadata indicating the wrong color space, or if your input video is
    # missing color space metadata that should be there, specify the accurate
    # color space here. If you choose HDR10, you can also correct inaccurate
    # color space coefficients, using the HDR master display information
    # controls. You must also set Color space usage (ColorSpaceUsage) to FORCE
    # for the service to use these values.
    color_space: typing.Union[str, "ColorSpace"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # There are two sources for color metadata, the input file and the job
    # configuration (in the Color space and HDR master display informaiton
    # settings). The Color space usage setting controls which takes precedence.
    # FORCE: The system will use color metadata supplied by user, if any. If the
    # user does not supply color metadata, the system will use data from the
    # source. FALLBACK: The system will use color metadata from the source. If
    # source has no color metadata, the system will use user-supplied color
    # metadata values if available.
    color_space_usage: typing.Union[str, "ColorSpaceUsage"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Use the HDR master display (Hdr10Metadata) settings to correct HDR metadata
    # or to provide missing metadata. These values vary depending on the input
    # video and must be provided by a color grader. Range is 0 to 50,000, each
    # increment represents 0.00002 in CIE1931 color coordinate. Note that these
    # settings are not color correction. Note that if you are creating HDR
    # outputs inside of an HLS CMAF package, to comply with the Apple
    # specification, you must use the HVC1 for H.265 setting.
    hdr10_metadata: "Hdr10Metadata" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Use PID (Pid) to select specific video data from an input file. Specify
    # this value as an integer; the system automatically converts it to the
    # hexidecimal value. For example, 257 selects PID 0x101. A PID, or packet
    # identifier, is an identifier for a set of data in an MPEG-2 transport
    # stream container.
    pid: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Selects a specific program from within a multi-program transport stream.
    # Note that Quad 4K is not currently supported.
    program_number: int = dataclasses.field(default=ShapeBase.NOT_SET, )


class VideoTimecodeInsertion(str):
    """
    Applies only to H.264, H.265, MPEG2, and ProRes outputs. Only enable Timecode
    insertion when the input framerate is identical to the output framerate. To
    include timecodes in this output, set Timecode insertion
    (VideoTimecodeInsertion) to PIC_TIMING_SEI. To leave them out, set it to
    DISABLED. Default is DISABLED. When the service inserts timecodes in an output,
    by default, it uses any embedded timecodes from the input. If none are present,
    the service will set the timecode for the first output frame to zero. To change
    this default behavior, adjust the settings under Timecode configuration
    (TimecodeConfig). In the console, these settings are located under Job > Job
    settings > Timecode configuration. Note - Timecode source under input settings
    (InputTimecodeSource) does not affect the timecodes that are inserted in the
    output. Source under Job settings > Timecode configuration (TimecodeSource)
    does.
    """
    DISABLED = "DISABLED"
    PIC_TIMING_SEI = "PIC_TIMING_SEI"


class WavFormat(str):
    """
    The service defaults to using RIFF for WAV outputs. If your output audio is
    likely to exceed 4 GB in file size, or if you otherwise need the extended
    support of the RF64 format, set your output WAV file format to RF64.
    """
    RIFF = "RIFF"
    RF64 = "RF64"


@dataclasses.dataclass
class WavSettings(ShapeBase):
    """
    Required when you set (Codec) under (AudioDescriptions)>(CodecSettings) to the
    value WAV.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bit_depth",
                "BitDepth",
                TypeInfo(int),
            ),
            (
                "channels",
                "Channels",
                TypeInfo(int),
            ),
            (
                "format",
                "Format",
                TypeInfo(typing.Union[str, WavFormat]),
            ),
            (
                "sample_rate",
                "SampleRate",
                TypeInfo(int),
            ),
        ]

    # Specify Bit depth (BitDepth), in bits per sample, to choose the encoding
    # quality for this audio track.
    bit_depth: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Set Channels to specify the number of channels in this output audio track.
    # With WAV, valid values 1, 2, 4, and 8. In the console, these values are
    # Mono, Stereo, 4-Channel, and 8-Channel, respectively.
    channels: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The service defaults to using RIFF for WAV outputs. If your output audio is
    # likely to exceed 4 GB in file size, or if you otherwise need the extended
    # support of the RF64 format, set your output WAV file format to RF64.
    format: typing.Union[str, "WavFormat"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Sample rate in Hz.
    sample_rate: int = dataclasses.field(default=ShapeBase.NOT_SET, )
