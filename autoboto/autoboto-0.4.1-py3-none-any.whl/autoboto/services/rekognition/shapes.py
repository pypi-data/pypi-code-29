import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import botocore.response
import dataclasses


@dataclasses.dataclass
class AccessDeniedException(ShapeBase):
    """
    You are not authorized to perform the action.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class AgeRange(ShapeBase):
    """
    Structure containing the estimated age range, in years, for a face.

    Rekognition estimates an age-range for faces detected in the input image.
    Estimated age ranges can overlap; a face of a 5 year old may have an estimated
    range of 4-6 whilst the face of a 6 year old may have an estimated range of 4-8.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "low",
                "Low",
                TypeInfo(int),
            ),
            (
                "high",
                "High",
                TypeInfo(int),
            ),
        ]

    # The lowest estimated age.
    low: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The highest estimated age.
    high: int = dataclasses.field(default=ShapeBase.NOT_SET, )


class Attribute(str):
    DEFAULT = "DEFAULT"
    ALL = "ALL"


@dataclasses.dataclass
class Beard(ShapeBase):
    """
    Indicates whether or not the face has a beard, and the confidence level in the
    determination.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "value",
                "Value",
                TypeInfo(bool),
            ),
            (
                "confidence",
                "Confidence",
                TypeInfo(float),
            ),
        ]

    # Boolean value that indicates whether the face has beard or not.
    value: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Level of confidence in the determination.
    confidence: float = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BoundingBox(ShapeBase):
    """
    Identifies the bounding box around the face or text. The `left` (x-coordinate)
    and `top` (y-coordinate) are coordinates representing the top and left sides of
    the bounding box. Note that the upper-left corner of the image is the origin
    (0,0).

    The `top` and `left` values returned are ratios of the overall image size. For
    example, if the input image is 700x200 pixels, and the top-left coordinate of
    the bounding box is 350x50 pixels, the API returns a `left` value of 0.5
    (350/700) and a `top` value of 0.25 (50/200).

    The `width` and `height` values represent the dimensions of the bounding box as
    a ratio of the overall image dimension. For example, if the input image is
    700x200 pixels, and the bounding box width is 70 pixels, the width returned is
    0.1.

    The bounding box coordinates can have negative values. For example, if Amazon
    Rekognition is able to detect a face that is at the image edge and is only
    partially visible, the service can return coordinates that are outside the image
    bounds and, depending on the image edge, you might get negative values or values
    greater than 1 for the `left` or `top` values.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "width",
                "Width",
                TypeInfo(float),
            ),
            (
                "height",
                "Height",
                TypeInfo(float),
            ),
            (
                "left",
                "Left",
                TypeInfo(float),
            ),
            (
                "top",
                "Top",
                TypeInfo(float),
            ),
        ]

    # Width of the bounding box as a ratio of the overall image width.
    width: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Height of the bounding box as a ratio of the overall image height.
    height: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Left coordinate of the bounding box as a ratio of overall image width.
    left: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Top coordinate of the bounding box as a ratio of overall image height.
    top: float = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Celebrity(ShapeBase):
    """
    Provides information about a celebrity recognized by the operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "urls",
                "Urls",
                TypeInfo(typing.List[str]),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "face",
                "Face",
                TypeInfo(ComparedFace),
            ),
            (
                "match_confidence",
                "MatchConfidence",
                TypeInfo(float),
            ),
        ]

    # An array of URLs pointing to additional information about the celebrity. If
    # there is no additional information about the celebrity, this list is empty.
    urls: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the celebrity.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A unique identifier for the celebrity.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Provides information about the celebrity's face, such as its location on
    # the image.
    face: "ComparedFace" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The confidence, in percentage, that Rekognition has that the recognized
    # face is the celebrity.
    match_confidence: float = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CelebrityDetail(ShapeBase):
    """
    Information about a recognized celebrity.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "urls",
                "Urls",
                TypeInfo(typing.List[str]),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "confidence",
                "Confidence",
                TypeInfo(float),
            ),
            (
                "bounding_box",
                "BoundingBox",
                TypeInfo(BoundingBox),
            ),
            (
                "face",
                "Face",
                TypeInfo(FaceDetail),
            ),
        ]

    # An array of URLs pointing to additional celebrity information.
    urls: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the celebrity.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique identifier for the celebrity.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The confidence, in percentage, that Amazon Rekognition has that the
    # recognized face is the celebrity.
    confidence: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Bounding box around the body of a celebrity.
    bounding_box: "BoundingBox" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Face details for the recognized celebrity.
    face: "FaceDetail" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CelebrityRecognition(ShapeBase):
    """
    Information about a detected celebrity and the time the celebrity was detected
    in a stored video. For more information, see GetCelebrityRecognition in the
    Amazon Rekognition Developer Guide.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "timestamp",
                "Timestamp",
                TypeInfo(int),
            ),
            (
                "celebrity",
                "Celebrity",
                TypeInfo(CelebrityDetail),
            ),
        ]

    # The time, in milliseconds from the start of the video, that the celebrity
    # was recognized.
    timestamp: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about a recognized celebrity.
    celebrity: "CelebrityDetail" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class CelebrityRecognitionSortBy(str):
    ID = "ID"
    TIMESTAMP = "TIMESTAMP"


@dataclasses.dataclass
class CompareFacesMatch(ShapeBase):
    """
    Provides information about a face in a target image that matches the source
    image face analysed by `CompareFaces`. The `Face` property contains the bounding
    box of the face in the target image. The `Similarity` property is the confidence
    that the source image face matches the face in the bounding box.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "similarity",
                "Similarity",
                TypeInfo(float),
            ),
            (
                "face",
                "Face",
                TypeInfo(ComparedFace),
            ),
        ]

    # Level of confidence that the faces match.
    similarity: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Provides face metadata (bounding box and confidence that the bounding box
    # actually contains a face).
    face: "ComparedFace" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CompareFacesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "source_image",
                "SourceImage",
                TypeInfo(Image),
            ),
            (
                "target_image",
                "TargetImage",
                TypeInfo(Image),
            ),
            (
                "similarity_threshold",
                "SimilarityThreshold",
                TypeInfo(float),
            ),
        ]

    # The input image as base64-encoded bytes or an S3 object. If you use the AWS
    # CLI to call Amazon Rekognition operations, passing base64-encoded image
    # bytes is not supported.
    source_image: "Image" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The target image as base64-encoded bytes or an S3 object. If you use the
    # AWS CLI to call Amazon Rekognition operations, passing base64-encoded image
    # bytes is not supported.
    target_image: "Image" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The minimum level of confidence in the face matches that a match must meet
    # to be included in the `FaceMatches` array.
    similarity_threshold: float = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CompareFacesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "source_image_face",
                "SourceImageFace",
                TypeInfo(ComparedSourceImageFace),
            ),
            (
                "face_matches",
                "FaceMatches",
                TypeInfo(typing.List[CompareFacesMatch]),
            ),
            (
                "unmatched_faces",
                "UnmatchedFaces",
                TypeInfo(typing.List[ComparedFace]),
            ),
            (
                "source_image_orientation_correction",
                "SourceImageOrientationCorrection",
                TypeInfo(typing.Union[str, OrientationCorrection]),
            ),
            (
                "target_image_orientation_correction",
                "TargetImageOrientationCorrection",
                TypeInfo(typing.Union[str, OrientationCorrection]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The face in the source image that was used for comparison.
    source_image_face: "ComparedSourceImageFace" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of faces in the target image that match the source image face.
    # Each `CompareFacesMatch` object provides the bounding box, the confidence
    # level that the bounding box contains a face, and the similarity score for
    # the face in the bounding box and the face in the source image.
    face_matches: typing.List["CompareFacesMatch"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of faces in the target image that did not match the source image
    # face.
    unmatched_faces: typing.List["ComparedFace"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The orientation of the source image (counterclockwise direction). If your
    # application displays the source image, you can use this value to correct
    # image orientation. The bounding box coordinates returned in
    # `SourceImageFace` represent the location of the face before the image
    # orientation is corrected.

    # If the source image is in .jpeg format, it might contain exchangeable image
    # (Exif) metadata that includes the image's orientation. If the Exif metadata
    # for the source image populates the orientation field, the value of
    # `OrientationCorrection` is null and the `SourceImageFace` bounding box
    # coordinates represent the location of the face after Exif metadata is used
    # to correct the orientation. Images in .png format don't contain Exif
    # metadata.
    source_image_orientation_correction: typing.Union[
        str, "OrientationCorrection"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # The orientation of the target image (in counterclockwise direction). If
    # your application displays the target image, you can use this value to
    # correct the orientation of the image. The bounding box coordinates returned
    # in `FaceMatches` and `UnmatchedFaces` represent face locations before the
    # image orientation is corrected.

    # If the target image is in .jpg format, it might contain Exif metadata that
    # includes the orientation of the image. If the Exif metadata for the target
    # image populates the orientation field, the value of `OrientationCorrection`
    # is null and the bounding box coordinates in `FaceMatches` and
    # `UnmatchedFaces` represent the location of the face after Exif metadata is
    # used to correct the orientation. Images in .png format don't contain Exif
    # metadata.
    target_image_orientation_correction: typing.Union[
        str, "OrientationCorrection"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )


@dataclasses.dataclass
class ComparedFace(ShapeBase):
    """
    Provides face metadata for target image faces that are analysed by
    `CompareFaces` and `RecognizeCelebrities`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bounding_box",
                "BoundingBox",
                TypeInfo(BoundingBox),
            ),
            (
                "confidence",
                "Confidence",
                TypeInfo(float),
            ),
            (
                "landmarks",
                "Landmarks",
                TypeInfo(typing.List[Landmark]),
            ),
            (
                "pose",
                "Pose",
                TypeInfo(Pose),
            ),
            (
                "quality",
                "Quality",
                TypeInfo(ImageQuality),
            ),
        ]

    # Bounding box of the face.
    bounding_box: "BoundingBox" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Level of confidence that what the bounding box contains is a face.
    confidence: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of facial landmarks.
    landmarks: typing.List["Landmark"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates the pose of the face as determined by its pitch, roll, and yaw.
    pose: "Pose" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Identifies face image brightness and sharpness.
    quality: "ImageQuality" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ComparedSourceImageFace(ShapeBase):
    """
    Type that describes the face Amazon Rekognition chose to compare with the faces
    in the target. This contains a bounding box for the selected face and confidence
    level that the bounding box contains a face. Note that Amazon Rekognition
    selects the largest face in the source image for this comparison.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bounding_box",
                "BoundingBox",
                TypeInfo(BoundingBox),
            ),
            (
                "confidence",
                "Confidence",
                TypeInfo(float),
            ),
        ]

    # Bounding box of the face.
    bounding_box: "BoundingBox" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Confidence level that the selected bounding box contains a face.
    confidence: float = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ContentModerationDetection(ShapeBase):
    """
    Information about a moderation label detection in a stored video.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "timestamp",
                "Timestamp",
                TypeInfo(int),
            ),
            (
                "moderation_label",
                "ModerationLabel",
                TypeInfo(ModerationLabel),
            ),
        ]

    # Time, in milliseconds from the beginning of the video, that the moderation
    # label was detected.
    timestamp: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The moderation label detected by in the stored video.
    moderation_label: "ModerationLabel" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class ContentModerationSortBy(str):
    NAME = "NAME"
    TIMESTAMP = "TIMESTAMP"


@dataclasses.dataclass
class CreateCollectionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "collection_id",
                "CollectionId",
                TypeInfo(str),
            ),
        ]

    # ID for the collection that you are creating.
    collection_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateCollectionResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "status_code",
                "StatusCode",
                TypeInfo(int),
            ),
            (
                "collection_arn",
                "CollectionArn",
                TypeInfo(str),
            ),
            (
                "face_model_version",
                "FaceModelVersion",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # HTTP status code indicating the result of the operation.
    status_code: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Amazon Resource Name (ARN) of the collection. You can use this to manage
    # permissions on your resources.
    collection_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Version number of the face detection model associated with the collection
    # you are creating.
    face_model_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateStreamProcessorRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "input",
                "Input",
                TypeInfo(StreamProcessorInput),
            ),
            (
                "output",
                "Output",
                TypeInfo(StreamProcessorOutput),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "settings",
                "Settings",
                TypeInfo(StreamProcessorSettings),
            ),
            (
                "role_arn",
                "RoleArn",
                TypeInfo(str),
            ),
        ]

    # Kinesis video stream stream that provides the source streaming video. If
    # you are using the AWS CLI, the parameter name is `StreamProcessorInput`.
    input: "StreamProcessorInput" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Kinesis data stream stream to which Amazon Rekognition Video puts the
    # analysis results. If you are using the AWS CLI, the parameter name is
    # `StreamProcessorOutput`.
    output: "StreamProcessorOutput" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An identifier you assign to the stream processor. You can use `Name` to
    # manage the stream processor. For example, you can get the current status of
    # the stream processor by calling . `Name` is idempotent.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Face recognition input parameters to be used by the stream processor.
    # Includes the collection to use for face recognition and the face attributes
    # to detect.
    settings: "StreamProcessorSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # ARN of the IAM role that allows access to the stream processor.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateStreamProcessorResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "stream_processor_arn",
                "StreamProcessorArn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # ARN for the newly create stream processor.
    stream_processor_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteCollectionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "collection_id",
                "CollectionId",
                TypeInfo(str),
            ),
        ]

    # ID of the collection to delete.
    collection_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteCollectionResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "status_code",
                "StatusCode",
                TypeInfo(int),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # HTTP status code that indicates the result of the operation.
    status_code: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteFacesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "collection_id",
                "CollectionId",
                TypeInfo(str),
            ),
            (
                "face_ids",
                "FaceIds",
                TypeInfo(typing.List[str]),
            ),
        ]

    # Collection from which to remove the specific faces.
    collection_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of face IDs to delete.
    face_ids: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteFacesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "deleted_faces",
                "DeletedFaces",
                TypeInfo(typing.List[str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of strings (face IDs) of the faces that were deleted.
    deleted_faces: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteStreamProcessorRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The name of the stream processor you want to delete.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteStreamProcessorResponse(OutputShapeBase):
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
class DescribeCollectionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "collection_id",
                "CollectionId",
                TypeInfo(str),
            ),
        ]

    # The ID of the collection to describe.
    collection_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeCollectionResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "face_count",
                "FaceCount",
                TypeInfo(int),
            ),
            (
                "face_model_version",
                "FaceModelVersion",
                TypeInfo(str),
            ),
            (
                "collection_arn",
                "CollectionARN",
                TypeInfo(str),
            ),
            (
                "creation_timestamp",
                "CreationTimestamp",
                TypeInfo(datetime.datetime),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of faces that are indexed into the collection. To index faces
    # into a collection, use .
    face_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The version of the face model that's used by the collection for face
    # detection.

    # For more information, see Model Versioning in the Amazon Rekognition
    # Developer Guide.
    face_model_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the collection.
    collection_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of milliseconds since the Unix epoch time until the creation of
    # the collection. The Unix epoch time is 00:00:00 Coordinated Universal Time
    # (UTC), Thursday, 1 January 1970.
    creation_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeStreamProcessorRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # Name of the stream processor for which you want information.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeStreamProcessorResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "stream_processor_arn",
                "StreamProcessorArn",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, StreamProcessorStatus]),
            ),
            (
                "status_message",
                "StatusMessage",
                TypeInfo(str),
            ),
            (
                "creation_timestamp",
                "CreationTimestamp",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_update_timestamp",
                "LastUpdateTimestamp",
                TypeInfo(datetime.datetime),
            ),
            (
                "input",
                "Input",
                TypeInfo(StreamProcessorInput),
            ),
            (
                "output",
                "Output",
                TypeInfo(StreamProcessorOutput),
            ),
            (
                "role_arn",
                "RoleArn",
                TypeInfo(str),
            ),
            (
                "settings",
                "Settings",
                TypeInfo(StreamProcessorSettings),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Name of the stream processor.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # ARN of the stream processor.
    stream_processor_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Current status of the stream processor.
    status: typing.Union[str, "StreamProcessorStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Detailed status message about the stream processor.
    status_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Date and time the stream processor was created
    creation_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The time, in Unix format, the stream processor was last updated. For
    # example, when the stream processor moves from a running state to a failed
    # state, or when the user starts or stops the stream processor.
    last_update_timestamp: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Kinesis video stream that provides the source streaming video.
    input: "StreamProcessorInput" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Kinesis data stream to which Amazon Rekognition Video puts the analysis
    # results.
    output: "StreamProcessorOutput" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # ARN of the IAM role that allows access to the stream processor.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Face recognition input parameters that are being used by the stream
    # processor. Includes the collection to use for face recognition and the face
    # attributes to detect.
    settings: "StreamProcessorSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DetectFacesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "image",
                "Image",
                TypeInfo(Image),
            ),
            (
                "attributes",
                "Attributes",
                TypeInfo(typing.List[typing.Union[str, Attribute]]),
            ),
        ]

    # The input image as base64-encoded bytes or an S3 object. If you use the AWS
    # CLI to call Amazon Rekognition operations, passing base64-encoded image
    # bytes is not supported.
    image: "Image" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of facial attributes you want to be returned. This can be the
    # default list of attributes or all attributes. If you don't specify a value
    # for `Attributes` or if you specify `["DEFAULT"]`, the API returns the
    # following subset of facial attributes: `BoundingBox`, `Confidence`, `Pose`,
    # `Quality` and `Landmarks`. If you provide `["ALL"]`, all facial attributes
    # are returned but the operation will take longer to complete.

    # If you provide both, `["ALL", "DEFAULT"]`, the service uses a logical AND
    # operator to determine which attributes to return (in this case, all
    # attributes).
    attributes: typing.List[typing.Union[str, "Attribute"]] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DetectFacesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "face_details",
                "FaceDetails",
                TypeInfo(typing.List[FaceDetail]),
            ),
            (
                "orientation_correction",
                "OrientationCorrection",
                TypeInfo(typing.Union[str, OrientationCorrection]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Details of each face found in the image.
    face_details: typing.List["FaceDetail"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The orientation of the input image (counter-clockwise direction). If your
    # application displays the image, you can use this value to correct image
    # orientation. The bounding box coordinates returned in `FaceDetails`
    # represent face locations before the image orientation is corrected.

    # If the input image is in .jpeg format, it might contain exchangeable image
    # (Exif) metadata that includes the image's orientation. If so, and the Exif
    # metadata for the input image populates the orientation field, the value of
    # `OrientationCorrection` is null and the `FaceDetails` bounding box
    # coordinates represent face locations after Exif metadata is used to correct
    # the image orientation. Images in .png format don't contain Exif metadata.
    orientation_correction: typing.Union[str, "OrientationCorrection"
                                        ] = dataclasses.field(
                                            default=ShapeBase.NOT_SET,
                                        )


@dataclasses.dataclass
class DetectLabelsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "image",
                "Image",
                TypeInfo(Image),
            ),
            (
                "max_labels",
                "MaxLabels",
                TypeInfo(int),
            ),
            (
                "min_confidence",
                "MinConfidence",
                TypeInfo(float),
            ),
        ]

    # The input image as base64-encoded bytes or an S3 object. If you use the AWS
    # CLI to call Amazon Rekognition operations, passing base64-encoded image
    # bytes is not supported.
    image: "Image" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Maximum number of labels you want the service to return in the response.
    # The service returns the specified number of highest confidence labels.
    max_labels: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the minimum confidence level for the labels to return. Amazon
    # Rekognition doesn't return any labels with confidence lower than this
    # specified value.

    # If `MinConfidence` is not specified, the operation returns labels with a
    # confidence values greater than or equal to 50 percent.
    min_confidence: float = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DetectLabelsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "labels",
                "Labels",
                TypeInfo(typing.List[Label]),
            ),
            (
                "orientation_correction",
                "OrientationCorrection",
                TypeInfo(typing.Union[str, OrientationCorrection]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of labels for the real-world objects detected.
    labels: typing.List["Label"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The orientation of the input image (counter-clockwise direction). If your
    # application displays the image, you can use this value to correct the
    # orientation. If Amazon Rekognition detects that the input image was rotated
    # (for example, by 90 degrees), it first corrects the orientation before
    # detecting the labels.

    # If the input image Exif metadata populates the orientation field, Amazon
    # Rekognition does not perform orientation correction and the value of
    # OrientationCorrection will be null.
    orientation_correction: typing.Union[str, "OrientationCorrection"
                                        ] = dataclasses.field(
                                            default=ShapeBase.NOT_SET,
                                        )


@dataclasses.dataclass
class DetectModerationLabelsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "image",
                "Image",
                TypeInfo(Image),
            ),
            (
                "min_confidence",
                "MinConfidence",
                TypeInfo(float),
            ),
        ]

    # The input image as base64-encoded bytes or an S3 object. If you use the AWS
    # CLI to call Amazon Rekognition operations, passing base64-encoded image
    # bytes is not supported.
    image: "Image" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the minimum confidence level for the labels to return. Amazon
    # Rekognition doesn't return any labels with a confidence level lower than
    # this specified value.

    # If you don't specify `MinConfidence`, the operation returns labels with
    # confidence values greater than or equal to 50 percent.
    min_confidence: float = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DetectModerationLabelsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "moderation_labels",
                "ModerationLabels",
                TypeInfo(typing.List[ModerationLabel]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Array of detected Moderation labels and the time, in millseconds from the
    # start of the video, they were detected.
    moderation_labels: typing.List["ModerationLabel"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DetectTextRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "image",
                "Image",
                TypeInfo(Image),
            ),
        ]

    # The input image as base64-encoded bytes or an Amazon S3 object. If you use
    # the AWS CLI to call Amazon Rekognition operations, you can't pass image
    # bytes.
    image: "Image" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DetectTextResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "text_detections",
                "TextDetections",
                TypeInfo(typing.List[TextDetection]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of text that was detected in the input image.
    text_detections: typing.List["TextDetection"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Emotion(ShapeBase):
    """
    The emotions detected on the face, and the confidence level in the
    determination. For example, HAPPY, SAD, and ANGRY.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, EmotionName]),
            ),
            (
                "confidence",
                "Confidence",
                TypeInfo(float),
            ),
        ]

    # Type of emotion detected.
    type: typing.Union[str, "EmotionName"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Level of confidence in the determination.
    confidence: float = dataclasses.field(default=ShapeBase.NOT_SET, )


class EmotionName(str):
    HAPPY = "HAPPY"
    SAD = "SAD"
    ANGRY = "ANGRY"
    CONFUSED = "CONFUSED"
    DISGUSTED = "DISGUSTED"
    SURPRISED = "SURPRISED"
    CALM = "CALM"
    UNKNOWN = "UNKNOWN"


@dataclasses.dataclass
class EyeOpen(ShapeBase):
    """
    Indicates whether or not the eyes on the face are open, and the confidence level
    in the determination.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "value",
                "Value",
                TypeInfo(bool),
            ),
            (
                "confidence",
                "Confidence",
                TypeInfo(float),
            ),
        ]

    # Boolean value that indicates whether the eyes on the face are open.
    value: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Level of confidence in the determination.
    confidence: float = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Eyeglasses(ShapeBase):
    """
    Indicates whether or not the face is wearing eye glasses, and the confidence
    level in the determination.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "value",
                "Value",
                TypeInfo(bool),
            ),
            (
                "confidence",
                "Confidence",
                TypeInfo(float),
            ),
        ]

    # Boolean value that indicates whether the face is wearing eye glasses or
    # not.
    value: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Level of confidence in the determination.
    confidence: float = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Face(ShapeBase):
    """
    Describes the face properties such as the bounding box, face ID, image ID of the
    input image, and external image ID that you assigned.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "face_id",
                "FaceId",
                TypeInfo(str),
            ),
            (
                "bounding_box",
                "BoundingBox",
                TypeInfo(BoundingBox),
            ),
            (
                "image_id",
                "ImageId",
                TypeInfo(str),
            ),
            (
                "external_image_id",
                "ExternalImageId",
                TypeInfo(str),
            ),
            (
                "confidence",
                "Confidence",
                TypeInfo(float),
            ),
        ]

    # Unique identifier that Amazon Rekognition assigns to the face.
    face_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Bounding box of the face.
    bounding_box: "BoundingBox" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique identifier that Amazon Rekognition assigns to the input image.
    image_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Identifier that you assign to all the faces in the input image.
    external_image_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Confidence level that the bounding box contains a face (and not a different
    # object such as a tree).
    confidence: float = dataclasses.field(default=ShapeBase.NOT_SET, )


class FaceAttributes(str):
    DEFAULT = "DEFAULT"
    ALL = "ALL"


@dataclasses.dataclass
class FaceDetail(ShapeBase):
    """
    Structure containing attributes of the face that the algorithm detected.

    A `FaceDetail` object contains either the default facial attributes or all
    facial attributes. The default attributes are `BoundingBox`, `Confidence`,
    `Landmarks`, `Pose`, and `Quality`.

    is the only Amazon Rekognition Video stored video operation that can return a
    `FaceDetail` object with all attributes. To specify which attributes to return,
    use the `FaceAttributes` input parameter for . The following Amazon Rekognition
    Video operations return only the default attributes. The corresponding Start
    operations don't have a `FaceAttributes` input parameter.

      * GetCelebrityRecognition

      * GetPersonTracking

      * GetFaceSearch

    The Amazon Rekognition Image and operations can return all facial attributes. To
    specify which attributes to return, use the `Attributes` input parameter for
    `DetectFaces`. For `IndexFaces`, use the `DetectAttributes` input parameter.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bounding_box",
                "BoundingBox",
                TypeInfo(BoundingBox),
            ),
            (
                "age_range",
                "AgeRange",
                TypeInfo(AgeRange),
            ),
            (
                "smile",
                "Smile",
                TypeInfo(Smile),
            ),
            (
                "eyeglasses",
                "Eyeglasses",
                TypeInfo(Eyeglasses),
            ),
            (
                "sunglasses",
                "Sunglasses",
                TypeInfo(Sunglasses),
            ),
            (
                "gender",
                "Gender",
                TypeInfo(Gender),
            ),
            (
                "beard",
                "Beard",
                TypeInfo(Beard),
            ),
            (
                "mustache",
                "Mustache",
                TypeInfo(Mustache),
            ),
            (
                "eyes_open",
                "EyesOpen",
                TypeInfo(EyeOpen),
            ),
            (
                "mouth_open",
                "MouthOpen",
                TypeInfo(MouthOpen),
            ),
            (
                "emotions",
                "Emotions",
                TypeInfo(typing.List[Emotion]),
            ),
            (
                "landmarks",
                "Landmarks",
                TypeInfo(typing.List[Landmark]),
            ),
            (
                "pose",
                "Pose",
                TypeInfo(Pose),
            ),
            (
                "quality",
                "Quality",
                TypeInfo(ImageQuality),
            ),
            (
                "confidence",
                "Confidence",
                TypeInfo(float),
            ),
        ]

    # Bounding box of the face. Default attribute.
    bounding_box: "BoundingBox" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The estimated age range, in years, for the face. Low represents the lowest
    # estimated age and High represents the highest estimated age.
    age_range: "AgeRange" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether or not the face is smiling, and the confidence level in
    # the determination.
    smile: "Smile" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether or not the face is wearing eye glasses, and the
    # confidence level in the determination.
    eyeglasses: "Eyeglasses" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether or not the face is wearing sunglasses, and the confidence
    # level in the determination.
    sunglasses: "Sunglasses" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Gender of the face and the confidence level in the determination.
    gender: "Gender" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether or not the face has a beard, and the confidence level in
    # the determination.
    beard: "Beard" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether or not the face has a mustache, and the confidence level
    # in the determination.
    mustache: "Mustache" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether or not the eyes on the face are open, and the confidence
    # level in the determination.
    eyes_open: "EyeOpen" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether or not the mouth on the face is open, and the confidence
    # level in the determination.
    mouth_open: "MouthOpen" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The emotions detected on the face, and the confidence level in the
    # determination. For example, HAPPY, SAD, and ANGRY.
    emotions: typing.List["Emotion"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates the location of landmarks on the face. Default attribute.
    landmarks: typing.List["Landmark"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates the pose of the face as determined by its pitch, roll, and yaw.
    # Default attribute.
    pose: "Pose" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Identifies image brightness and sharpness. Default attribute.
    quality: "ImageQuality" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Confidence level that the bounding box contains a face (and not a different
    # object such as a tree). Default attribute.
    confidence: float = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class FaceDetection(ShapeBase):
    """
    Information about a face detected in a video analysis request and the time the
    face was detected in the video.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "timestamp",
                "Timestamp",
                TypeInfo(int),
            ),
            (
                "face",
                "Face",
                TypeInfo(FaceDetail),
            ),
        ]

    # Time, in milliseconds from the start of the video, that the face was
    # detected.
    timestamp: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The face properties for the detected face.
    face: "FaceDetail" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class FaceMatch(ShapeBase):
    """
    Provides face metadata. In addition, it also provides the confidence in the
    match of this face with the input face.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "similarity",
                "Similarity",
                TypeInfo(float),
            ),
            (
                "face",
                "Face",
                TypeInfo(Face),
            ),
        ]

    # Confidence in the match of this face with the input face.
    similarity: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Describes the face properties such as the bounding box, face ID, image ID
    # of the source image, and external image ID that you assigned.
    face: "Face" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class FaceRecord(ShapeBase):
    """
    Object containing both the face metadata (stored in the back-end database) and
    facial attributes that are detected but aren't stored in the database.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "face",
                "Face",
                TypeInfo(Face),
            ),
            (
                "face_detail",
                "FaceDetail",
                TypeInfo(FaceDetail),
            ),
        ]

    # Describes the face properties such as the bounding box, face ID, image ID
    # of the input image, and external image ID that you assigned.
    face: "Face" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Structure containing attributes of the face that the algorithm detected.
    face_detail: "FaceDetail" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class FaceSearchSettings(ShapeBase):
    """
    Input face recognition parameters for an Amazon Rekognition stream processor.
    `FaceRecognitionSettings` is a request parameter for .
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "collection_id",
                "CollectionId",
                TypeInfo(str),
            ),
            (
                "face_match_threshold",
                "FaceMatchThreshold",
                TypeInfo(float),
            ),
        ]

    # The ID of a collection that contains faces that you want to search for.
    collection_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Minimum face match confidence score that must be met to return a result for
    # a recognized face. Default is 70. 0 is the lowest confidence. 100 is the
    # highest confidence.
    face_match_threshold: float = dataclasses.field(default=ShapeBase.NOT_SET, )


class FaceSearchSortBy(str):
    INDEX = "INDEX"
    TIMESTAMP = "TIMESTAMP"


@dataclasses.dataclass
class Gender(ShapeBase):
    """
    Gender of the face and the confidence level in the determination.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "value",
                "Value",
                TypeInfo(typing.Union[str, GenderType]),
            ),
            (
                "confidence",
                "Confidence",
                TypeInfo(float),
            ),
        ]

    # Gender of the face.
    value: typing.Union[str, "GenderType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Level of confidence in the determination.
    confidence: float = dataclasses.field(default=ShapeBase.NOT_SET, )


class GenderType(str):
    Male = "Male"
    Female = "Female"


@dataclasses.dataclass
class Geometry(ShapeBase):
    """
    Information about where text detected by is located on an image.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bounding_box",
                "BoundingBox",
                TypeInfo(BoundingBox),
            ),
            (
                "polygon",
                "Polygon",
                TypeInfo(typing.List[Point]),
            ),
        ]

    # An axis-aligned coarse representation of the detected text's location on
    # the image.
    bounding_box: "BoundingBox" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Within the bounding box, a fine-grained polygon around the detected text.
    polygon: typing.List["Point"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetCelebrityInfoRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
        ]

    # The ID for the celebrity. You get the celebrity ID from a call to the
    # operation, which recognizes celebrities in an image.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetCelebrityInfoResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "urls",
                "Urls",
                TypeInfo(typing.List[str]),
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

    # An array of URLs pointing to additional celebrity information.
    urls: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the celebrity.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetCelebrityRecognitionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_id",
                "JobId",
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
            (
                "sort_by",
                "SortBy",
                TypeInfo(typing.Union[str, CelebrityRecognitionSortBy]),
            ),
        ]

    # Job identifier for the required celebrity recognition analysis. You can get
    # the job identifer from a call to `StartCelebrityRecognition`.
    job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Maximum number of results to return per paginated call. The largest value
    # you can specify is 1000. If you specify a value greater than 1000, a
    # maximum of 1000 results is returned. The default value is 1000.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If the previous response was incomplete (because there is more recognized
    # celebrities to retrieve), Amazon Rekognition Video returns a pagination
    # token in the response. You can use this pagination token to retrieve the
    # next set of celebrities.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Sort to use for celebrities returned in `Celebrities` field. Specify `ID`
    # to sort by the celebrity identifier, specify `TIMESTAMP` to sort by the
    # time the celebrity was recognized.
    sort_by: typing.Union[str, "CelebrityRecognitionSortBy"
                         ] = dataclasses.field(
                             default=ShapeBase.NOT_SET,
                         )


@dataclasses.dataclass
class GetCelebrityRecognitionResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "job_status",
                "JobStatus",
                TypeInfo(typing.Union[str, VideoJobStatus]),
            ),
            (
                "status_message",
                "StatusMessage",
                TypeInfo(str),
            ),
            (
                "video_metadata",
                "VideoMetadata",
                TypeInfo(VideoMetadata),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "celebrities",
                "Celebrities",
                TypeInfo(typing.List[CelebrityRecognition]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The current status of the celebrity recognition job.
    job_status: typing.Union[str, "VideoJobStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the job fails, `StatusMessage` provides a descriptive error message.
    status_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about a video that Amazon Rekognition Video analyzed.
    # `Videometadata` is returned in every page of paginated responses from a
    # Amazon Rekognition Video operation.
    video_metadata: "VideoMetadata" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the response is truncated, Amazon Rekognition Video returns this token
    # that you can use in the subsequent request to retrieve the next set of
    # celebrities.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Array of celebrities recognized in the video.
    celebrities: typing.List["CelebrityRecognition"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetContentModerationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_id",
                "JobId",
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
            (
                "sort_by",
                "SortBy",
                TypeInfo(typing.Union[str, ContentModerationSortBy]),
            ),
        ]

    # The identifier for the content moderation job. Use `JobId` to identify the
    # job in a subsequent call to `GetContentModeration`.
    job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Maximum number of results to return per paginated call. The largest value
    # you can specify is 1000. If you specify a value greater than 1000, a
    # maximum of 1000 results is returned. The default value is 1000.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If the previous response was incomplete (because there is more data to
    # retrieve), Amazon Rekognition returns a pagination token in the response.
    # You can use this pagination token to retrieve the next set of content
    # moderation labels.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Sort to use for elements in the `ModerationLabelDetections` array. Use
    # `TIMESTAMP` to sort array elements by the time labels are detected. Use
    # `NAME` to alphabetically group elements for a label together. Within each
    # label group, the array element are sorted by detection confidence. The
    # default sort is by `TIMESTAMP`.
    sort_by: typing.Union[str, "ContentModerationSortBy"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetContentModerationResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "job_status",
                "JobStatus",
                TypeInfo(typing.Union[str, VideoJobStatus]),
            ),
            (
                "status_message",
                "StatusMessage",
                TypeInfo(str),
            ),
            (
                "video_metadata",
                "VideoMetadata",
                TypeInfo(VideoMetadata),
            ),
            (
                "moderation_labels",
                "ModerationLabels",
                TypeInfo(typing.List[ContentModerationDetection]),
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

    # The current status of the content moderation job.
    job_status: typing.Union[str, "VideoJobStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the job fails, `StatusMessage` provides a descriptive error message.
    status_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about a video that Amazon Rekognition analyzed. `Videometadata`
    # is returned in every page of paginated responses from
    # `GetContentModeration`.
    video_metadata: "VideoMetadata" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The detected moderation labels and the time(s) they were detected.
    moderation_labels: typing.List["ContentModerationDetection"
                                  ] = dataclasses.field(
                                      default=ShapeBase.NOT_SET,
                                  )

    # If the response is truncated, Amazon Rekognition Video returns this token
    # that you can use in the subsequent request to retrieve the next set of
    # moderation labels.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetFaceDetectionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_id",
                "JobId",
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

    # Unique identifier for the face detection job. The `JobId` is returned from
    # `StartFaceDetection`.
    job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Maximum number of results to return per paginated call. The largest value
    # you can specify is 1000. If you specify a value greater than 1000, a
    # maximum of 1000 results is returned. The default value is 1000.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If the previous response was incomplete (because there are more faces to
    # retrieve), Amazon Rekognition Video returns a pagination token in the
    # response. You can use this pagination token to retrieve the next set of
    # faces.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetFaceDetectionResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "job_status",
                "JobStatus",
                TypeInfo(typing.Union[str, VideoJobStatus]),
            ),
            (
                "status_message",
                "StatusMessage",
                TypeInfo(str),
            ),
            (
                "video_metadata",
                "VideoMetadata",
                TypeInfo(VideoMetadata),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "faces",
                "Faces",
                TypeInfo(typing.List[FaceDetection]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The current status of the face detection job.
    job_status: typing.Union[str, "VideoJobStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the job fails, `StatusMessage` provides a descriptive error message.
    status_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about a video that Amazon Rekognition Video analyzed.
    # `Videometadata` is returned in every page of paginated responses from a
    # Amazon Rekognition video operation.
    video_metadata: "VideoMetadata" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the response is truncated, Amazon Rekognition returns this token that
    # you can use in the subsequent request to retrieve the next set of faces.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of faces detected in the video. Each element contains a detected
    # face's details and the time, in milliseconds from the start of the video,
    # the face was detected.
    faces: typing.List["FaceDetection"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetFaceSearchRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_id",
                "JobId",
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
            (
                "sort_by",
                "SortBy",
                TypeInfo(typing.Union[str, FaceSearchSortBy]),
            ),
        ]

    # The job identifer for the search request. You get the job identifier from
    # an initial call to `StartFaceSearch`.
    job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Maximum number of results to return per paginated call. The largest value
    # you can specify is 1000. If you specify a value greater than 1000, a
    # maximum of 1000 results is returned. The default value is 1000.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If the previous response was incomplete (because there is more search
    # results to retrieve), Amazon Rekognition Video returns a pagination token
    # in the response. You can use this pagination token to retrieve the next set
    # of search results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Sort to use for grouping faces in the response. Use `TIMESTAMP` to group
    # faces by the time that they are recognized. Use `INDEX` to sort by
    # recognized faces.
    sort_by: typing.Union[str, "FaceSearchSortBy"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetFaceSearchResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "job_status",
                "JobStatus",
                TypeInfo(typing.Union[str, VideoJobStatus]),
            ),
            (
                "status_message",
                "StatusMessage",
                TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "video_metadata",
                "VideoMetadata",
                TypeInfo(VideoMetadata),
            ),
            (
                "persons",
                "Persons",
                TypeInfo(typing.List[PersonMatch]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The current status of the face search job.
    job_status: typing.Union[str, "VideoJobStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the job fails, `StatusMessage` provides a descriptive error message.
    status_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If the response is truncated, Amazon Rekognition Video returns this token
    # that you can use in the subsequent request to retrieve the next set of
    # search results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about a video that Amazon Rekognition analyzed. `Videometadata`
    # is returned in every page of paginated responses from a Amazon Rekognition
    # Video operation.
    video_metadata: "VideoMetadata" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of persons, , in the video whose face(s) match the face(s) in an
    # Amazon Rekognition collection. It also includes time information for when
    # persons are matched in the video. You specify the input collection in an
    # initial call to `StartFaceSearch`. Each `Persons` element includes a time
    # the person was matched, face match details (`FaceMatches`) for matching
    # faces in the collection, and person information (`Person`) for the matched
    # person.
    persons: typing.List["PersonMatch"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetLabelDetectionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_id",
                "JobId",
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
            (
                "sort_by",
                "SortBy",
                TypeInfo(typing.Union[str, LabelDetectionSortBy]),
            ),
        ]

    # Job identifier for the label detection operation for which you want results
    # returned. You get the job identifer from an initial call to
    # `StartlabelDetection`.
    job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Maximum number of results to return per paginated call. The largest value
    # you can specify is 1000. If you specify a value greater than 1000, a
    # maximum of 1000 results is returned. The default value is 1000.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If the previous response was incomplete (because there are more labels to
    # retrieve), Amazon Rekognition Video returns a pagination token in the
    # response. You can use this pagination token to retrieve the next set of
    # labels.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Sort to use for elements in the `Labels` array. Use `TIMESTAMP` to sort
    # array elements by the time labels are detected. Use `NAME` to
    # alphabetically group elements for a label together. Within each label
    # group, the array element are sorted by detection confidence. The default
    # sort is by `TIMESTAMP`.
    sort_by: typing.Union[str, "LabelDetectionSortBy"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetLabelDetectionResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "job_status",
                "JobStatus",
                TypeInfo(typing.Union[str, VideoJobStatus]),
            ),
            (
                "status_message",
                "StatusMessage",
                TypeInfo(str),
            ),
            (
                "video_metadata",
                "VideoMetadata",
                TypeInfo(VideoMetadata),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "labels",
                "Labels",
                TypeInfo(typing.List[LabelDetection]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The current status of the label detection job.
    job_status: typing.Union[str, "VideoJobStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the job fails, `StatusMessage` provides a descriptive error message.
    status_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about a video that Amazon Rekognition Video analyzed.
    # `Videometadata` is returned in every page of paginated responses from a
    # Amazon Rekognition video operation.
    video_metadata: "VideoMetadata" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the response is truncated, Amazon Rekognition Video returns this token
    # that you can use in the subsequent request to retrieve the next set of
    # labels.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of labels detected in the video. Each element contains the
    # detected label and the time, in milliseconds from the start of the video,
    # that the label was detected.
    labels: typing.List["LabelDetection"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetPersonTrackingRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "job_id",
                "JobId",
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
            (
                "sort_by",
                "SortBy",
                TypeInfo(typing.Union[str, PersonTrackingSortBy]),
            ),
        ]

    # The identifier for a job that tracks persons in a video. You get the
    # `JobId` from a call to `StartPersonTracking`.
    job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Maximum number of results to return per paginated call. The largest value
    # you can specify is 1000. If you specify a value greater than 1000, a
    # maximum of 1000 results is returned. The default value is 1000.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If the previous response was incomplete (because there are more persons to
    # retrieve), Amazon Rekognition Video returns a pagination token in the
    # response. You can use this pagination token to retrieve the next set of
    # persons.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Sort to use for elements in the `Persons` array. Use `TIMESTAMP` to sort
    # array elements by the time persons are detected. Use `INDEX` to sort by the
    # tracked persons. If you sort by `INDEX`, the array elements for each person
    # are sorted by detection confidence. The default sort is by `TIMESTAMP`.
    sort_by: typing.Union[str, "PersonTrackingSortBy"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetPersonTrackingResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "job_status",
                "JobStatus",
                TypeInfo(typing.Union[str, VideoJobStatus]),
            ),
            (
                "status_message",
                "StatusMessage",
                TypeInfo(str),
            ),
            (
                "video_metadata",
                "VideoMetadata",
                TypeInfo(VideoMetadata),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "persons",
                "Persons",
                TypeInfo(typing.List[PersonDetection]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The current status of the person tracking job.
    job_status: typing.Union[str, "VideoJobStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the job fails, `StatusMessage` provides a descriptive error message.
    status_message: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about a video that Amazon Rekognition Video analyzed.
    # `Videometadata` is returned in every page of paginated responses from a
    # Amazon Rekognition Video operation.
    video_metadata: "VideoMetadata" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the response is truncated, Amazon Rekognition Video returns this token
    # that you can use in the subsequent request to retrieve the next set of
    # persons.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of the persons detected in the video and the times they are
    # tracked throughout the video. An array element will exist for each time the
    # person is tracked.
    persons: typing.List["PersonDetection"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class IdempotentParameterMismatchException(ShapeBase):
    """
    A `ClientRequestToken` input parameter was reused with an operation, but at
    least one of the other input parameters is different from the previous call to
    the operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class Image(ShapeBase):
    """
    Provides the input image either as bytes or an S3 object.

    You pass image bytes to a Rekognition API operation by using the `Bytes`
    property. For example, you would use the `Bytes` property to pass an image
    loaded from a local file system. Image bytes passed by using the `Bytes`
    property must be base64-encoded. Your code may not need to encode image bytes if
    you are using an AWS SDK to call Rekognition API operations.

    For more information, see Analyzing an Image Loaded from a Local File System in
    the Amazon Rekognition Developer Guide.

    You pass images stored in an S3 bucket to a Rekognition API operation by using
    the `S3Object` property. Images stored in an S3 bucket do not need to be
    base64-encoded.

    The region for the S3 bucket containing the S3 object must match the region you
    use for Amazon Rekognition operations.

    If you use the Amazon CLI to call Amazon Rekognition operations, passing image
    bytes using the Bytes property is not supported. You must first upload the image
    to an Amazon S3 bucket and then call the operation using the S3Object property.

    For Amazon Rekognition to process an S3 object, the user must have permission to
    access the S3 object. For more information, see Resource Based Policies in the
    Amazon Rekognition Developer Guide.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bytes",
                "Bytes",
                TypeInfo(typing.Any),
            ),
            (
                "s3_object",
                "S3Object",
                TypeInfo(S3Object),
            ),
        ]

    # Blob of image bytes up to 5 MBs.
    bytes: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Identifies an S3 object as the image source.
    s3_object: "S3Object" = dataclasses.field(default=ShapeBase.NOT_SET, )


class ImageBlob(botocore.response.StreamingBody):
    pass


@dataclasses.dataclass
class ImageQuality(ShapeBase):
    """
    Identifies face image brightness and sharpness.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "brightness",
                "Brightness",
                TypeInfo(float),
            ),
            (
                "sharpness",
                "Sharpness",
                TypeInfo(float),
            ),
        ]

    # Value representing brightness of the face. The service returns a value
    # between 0 and 100 (inclusive). A higher value indicates a brighter face
    # image.
    brightness: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Value representing sharpness of the face. The service returns a value
    # between 0 and 100 (inclusive). A higher value indicates a sharper face
    # image.
    sharpness: float = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ImageTooLargeException(ShapeBase):
    """
    The input image size exceeds the allowed limit. For more information, see Limits
    in Amazon Rekognition in the Amazon Rekognition Developer Guide.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class IndexFacesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "collection_id",
                "CollectionId",
                TypeInfo(str),
            ),
            (
                "image",
                "Image",
                TypeInfo(Image),
            ),
            (
                "external_image_id",
                "ExternalImageId",
                TypeInfo(str),
            ),
            (
                "detection_attributes",
                "DetectionAttributes",
                TypeInfo(typing.List[typing.Union[str, Attribute]]),
            ),
        ]

    # The ID of an existing collection to which you want to add the faces that
    # are detected in the input images.
    collection_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The input image as base64-encoded bytes or an S3 object. If you use the AWS
    # CLI to call Amazon Rekognition operations, passing base64-encoded image
    # bytes is not supported.
    image: "Image" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # ID you want to assign to all the faces detected in the image.
    external_image_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of facial attributes that you want to be returned. This can be the
    # default list of attributes or all attributes. If you don't specify a value
    # for `Attributes` or if you specify `["DEFAULT"]`, the API returns the
    # following subset of facial attributes: `BoundingBox`, `Confidence`, `Pose`,
    # `Quality` and `Landmarks`. If you provide `["ALL"]`, all facial attributes
    # are returned but the operation will take longer to complete.

    # If you provide both, `["ALL", "DEFAULT"]`, the service uses a logical AND
    # operator to determine which attributes to return (in this case, all
    # attributes).
    detection_attributes: typing.List[typing.Union[str, "Attribute"]
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )


@dataclasses.dataclass
class IndexFacesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "face_records",
                "FaceRecords",
                TypeInfo(typing.List[FaceRecord]),
            ),
            (
                "orientation_correction",
                "OrientationCorrection",
                TypeInfo(typing.Union[str, OrientationCorrection]),
            ),
            (
                "face_model_version",
                "FaceModelVersion",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of faces detected and added to the collection. For more
    # information, see Searching Faces in a Collection in the Amazon Rekognition
    # Developer Guide.
    face_records: typing.List["FaceRecord"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The orientation of the input image (counterclockwise direction). If your
    # application displays the image, you can use this value to correct image
    # orientation. The bounding box coordinates returned in `FaceRecords`
    # represent face locations before the image orientation is corrected.

    # If the input image is in jpeg format, it might contain exchangeable image
    # (Exif) metadata. If so, and the Exif metadata populates the orientation
    # field, the value of `OrientationCorrection` is null and the bounding box
    # coordinates in `FaceRecords` represent face locations after Exif metadata
    # is used to correct the image orientation. Images in .png format don't
    # contain Exif metadata.
    orientation_correction: typing.Union[str, "OrientationCorrection"
                                        ] = dataclasses.field(
                                            default=ShapeBase.NOT_SET,
                                        )

    # Version number of the face detection model associated with the input
    # collection (`CollectionId`).
    face_model_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InternalServerError(ShapeBase):
    """
    Amazon Rekognition experienced a service issue. Try your call again.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidImageFormatException(ShapeBase):
    """
    The provided image format is not supported.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidPaginationTokenException(ShapeBase):
    """
    Pagination token in the request is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidParameterException(ShapeBase):
    """
    Input parameter violated a constraint. Validate your parameter before calling
    the API operation again.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidS3ObjectException(ShapeBase):
    """
    Amazon Rekognition is unable to access the S3 object specified in the request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class KinesisDataStream(ShapeBase):
    """
    The Kinesis data stream Amazon Rekognition to which the analysis results of a
    Amazon Rekognition stream processor are streamed. For more information, see
    CreateStreamProcessor in the Amazon Rekognition Developer Guide.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
        ]

    # ARN of the output Amazon Kinesis Data Streams stream.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class KinesisVideoStream(ShapeBase):
    """
    Kinesis video stream stream that provides the source streaming video for a
    Amazon Rekognition Video stream processor. For more information, see
    CreateStreamProcessor in the Amazon Rekognition Developer Guide.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "Arn",
                TypeInfo(str),
            ),
        ]

    # ARN of the Kinesis video stream stream that streams the source video.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Label(ShapeBase):
    """
    Structure containing details about the detected label, including name, and level
    of confidence.
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
                "confidence",
                "Confidence",
                TypeInfo(float),
            ),
        ]

    # The name (label) of the object.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Level of confidence.
    confidence: float = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LabelDetection(ShapeBase):
    """
    Information about a label detected in a video analysis request and the time the
    label was detected in the video.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "timestamp",
                "Timestamp",
                TypeInfo(int),
            ),
            (
                "label",
                "Label",
                TypeInfo(Label),
            ),
        ]

    # Time, in milliseconds from the start of the video, that the label was
    # detected.
    timestamp: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Details about the detected label.
    label: "Label" = dataclasses.field(default=ShapeBase.NOT_SET, )


class LabelDetectionSortBy(str):
    NAME = "NAME"
    TIMESTAMP = "TIMESTAMP"


@dataclasses.dataclass
class Landmark(ShapeBase):
    """
    Indicates the location of the landmark on the face.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, LandmarkType]),
            ),
            (
                "x",
                "X",
                TypeInfo(float),
            ),
            (
                "y",
                "Y",
                TypeInfo(float),
            ),
        ]

    # Type of the landmark.
    type: typing.Union[str, "LandmarkType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # x-coordinate from the top left of the landmark expressed as the ratio of
    # the width of the image. For example, if the images is 700x200 and the
    # x-coordinate of the landmark is at 350 pixels, this value is 0.5.
    x: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # y-coordinate from the top left of the landmark expressed as the ratio of
    # the height of the image. For example, if the images is 700x200 and the
    # y-coordinate of the landmark is at 100 pixels, this value is 0.5.
    y: float = dataclasses.field(default=ShapeBase.NOT_SET, )


class LandmarkType(str):
    eyeLeft = "eyeLeft"
    eyeRight = "eyeRight"
    nose = "nose"
    mouthLeft = "mouthLeft"
    mouthRight = "mouthRight"
    leftEyeBrowLeft = "leftEyeBrowLeft"
    leftEyeBrowRight = "leftEyeBrowRight"
    leftEyeBrowUp = "leftEyeBrowUp"
    rightEyeBrowLeft = "rightEyeBrowLeft"
    rightEyeBrowRight = "rightEyeBrowRight"
    rightEyeBrowUp = "rightEyeBrowUp"
    leftEyeLeft = "leftEyeLeft"
    leftEyeRight = "leftEyeRight"
    leftEyeUp = "leftEyeUp"
    leftEyeDown = "leftEyeDown"
    rightEyeLeft = "rightEyeLeft"
    rightEyeRight = "rightEyeRight"
    rightEyeUp = "rightEyeUp"
    rightEyeDown = "rightEyeDown"
    noseLeft = "noseLeft"
    noseRight = "noseRight"
    mouthUp = "mouthUp"
    mouthDown = "mouthDown"
    leftPupil = "leftPupil"
    rightPupil = "rightPupil"


@dataclasses.dataclass
class LimitExceededException(ShapeBase):
    """
    An Amazon Rekognition service limit was exceeded. For example, if you start too
    many Amazon Rekognition Video jobs concurrently, calls to start operations
    (`StartLabelDetection`, for example) will raise a `LimitExceededException`
    exception (HTTP status code: 400) until the number of concurrently running jobs
    is below the Amazon Rekognition service limit.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ListCollectionsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                TypeInfo(int),
            ),
        ]

    # Pagination token from the previous response.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Maximum number of collection IDs to return.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListCollectionsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "collection_ids",
                "CollectionIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "face_model_versions",
                "FaceModelVersions",
                TypeInfo(typing.List[str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of collection IDs.
    collection_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the result is truncated, the response provides a `NextToken` that you
    # can use in the subsequent request to fetch the next set of collection IDs.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Version numbers of the face detection models associated with the
    # collections in the array `CollectionIds`. For example, the value of
    # `FaceModelVersions[2]` is the version number for the face detection model
    # used by the collection in `CollectionId[2]`.
    face_model_versions: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(self,
                ) -> typing.Generator["ListCollectionsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListFacesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "collection_id",
                "CollectionId",
                TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                TypeInfo(int),
            ),
        ]

    # ID of the collection from which to list the faces.
    collection_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If the previous response was incomplete (because there is more data to
    # retrieve), Amazon Rekognition returns a pagination token in the response.
    # You can use this pagination token to retrieve the next set of faces.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Maximum number of faces to return.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListFacesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "faces",
                "Faces",
                TypeInfo(typing.List[Face]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "face_model_version",
                "FaceModelVersion",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of `Face` objects.
    faces: typing.List["Face"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If the response is truncated, Amazon Rekognition returns this token that
    # you can use in the subsequent request to retrieve the next set of faces.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Version number of the face detection model associated with the input
    # collection (`CollectionId`).
    face_model_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["ListFacesResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListStreamProcessorsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
            (
                "max_results",
                "MaxResults",
                TypeInfo(int),
            ),
        ]

    # If the previous response was incomplete (because there are more stream
    # processors to retrieve), Amazon Rekognition Video returns a pagination
    # token in the response. You can use this pagination token to retrieve the
    # next set of stream processors.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Maximum number of stream processors you want Amazon Rekognition Video to
    # return in the response. The default is 1000.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListStreamProcessorsResponse(OutputShapeBase):
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
                "stream_processors",
                "StreamProcessors",
                TypeInfo(typing.List[StreamProcessor]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If the response is truncated, Amazon Rekognition Video returns this token
    # that you can use in the subsequent request to retrieve the next set of
    # stream processors.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # List of stream processors that you have created.
    stream_processors: typing.List["StreamProcessor"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(
        self,
    ) -> typing.Generator["ListStreamProcessorsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ModerationLabel(ShapeBase):
    """
    Provides information about a single type of moderated content found in an image
    or video. Each type of moderated content has a label within a hierarchical
    taxonomy. For more information, see Detecting Unsafe Content in the Amazon
    Rekognition Developer Guide.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "confidence",
                "Confidence",
                TypeInfo(float),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "parent_name",
                "ParentName",
                TypeInfo(str),
            ),
        ]

    # Specifies the confidence that Amazon Rekognition has that the label has
    # been correctly identified.

    # If you don't specify the `MinConfidence` parameter in the call to
    # `DetectModerationLabels`, the operation returns labels with a confidence
    # value greater than or equal to 50 percent.
    confidence: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The label name for the type of content detected in the image.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name for the parent label. Labels at the top-level of the hierarchy
    # have the parent label `""`.
    parent_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MouthOpen(ShapeBase):
    """
    Indicates whether or not the mouth on the face is open, and the confidence level
    in the determination.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "value",
                "Value",
                TypeInfo(bool),
            ),
            (
                "confidence",
                "Confidence",
                TypeInfo(float),
            ),
        ]

    # Boolean value that indicates whether the mouth on the face is open or not.
    value: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Level of confidence in the determination.
    confidence: float = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Mustache(ShapeBase):
    """
    Indicates whether or not the face has a mustache, and the confidence level in
    the determination.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "value",
                "Value",
                TypeInfo(bool),
            ),
            (
                "confidence",
                "Confidence",
                TypeInfo(float),
            ),
        ]

    # Boolean value that indicates whether the face has mustache or not.
    value: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Level of confidence in the determination.
    confidence: float = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class NotificationChannel(ShapeBase):
    """
    The Amazon Simple Notification Service topic to which Amazon Rekognition
    publishes the completion status of a video analysis operation. For more
    information, see api-video.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "sns_topic_arn",
                "SNSTopicArn",
                TypeInfo(str),
            ),
            (
                "role_arn",
                "RoleArn",
                TypeInfo(str),
            ),
        ]

    # The Amazon SNS topic to which Amazon Rekognition to posts the completion
    # status.
    sns_topic_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of an IAM role that gives Amazon Rekognition publishing permissions
    # to the Amazon SNS topic.
    role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class OrientationCorrection(str):
    ROTATE_0 = "ROTATE_0"
    ROTATE_90 = "ROTATE_90"
    ROTATE_180 = "ROTATE_180"
    ROTATE_270 = "ROTATE_270"


@dataclasses.dataclass
class PersonDetail(ShapeBase):
    """
    Details about a person detected in a video analysis request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "index",
                "Index",
                TypeInfo(int),
            ),
            (
                "bounding_box",
                "BoundingBox",
                TypeInfo(BoundingBox),
            ),
            (
                "face",
                "Face",
                TypeInfo(FaceDetail),
            ),
        ]

    # Identifier for the person detected person within a video. Use to keep track
    # of the person throughout the video. The identifier is not stored by Amazon
    # Rekognition.
    index: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Bounding box around the detected person.
    bounding_box: "BoundingBox" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Face details for the detected person.
    face: "FaceDetail" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PersonDetection(ShapeBase):
    """
    Details and tracking information for a single time a person is tracked in a
    video. Amazon Rekognition operations that track persons return an array of
    `PersonDetection` objects with elements for each time a person is tracked in a
    video.

    For more information, see API_GetPersonTracking in the Amazon Rekognition
    Developer Guide.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "timestamp",
                "Timestamp",
                TypeInfo(int),
            ),
            (
                "person",
                "Person",
                TypeInfo(PersonDetail),
            ),
        ]

    # The time, in milliseconds from the start of the video, that the person was
    # tracked.
    timestamp: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Details about a person tracked in a video.
    person: "PersonDetail" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PersonMatch(ShapeBase):
    """
    Information about a person whose face matches a face(s) in a Amazon Rekognition
    collection. Includes information about the faces in the Amazon Rekognition
    collection (), information about the person (PersonDetail) and the timestamp for
    when the person was detected in a video. An array of `PersonMatch` objects is
    returned by .
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "timestamp",
                "Timestamp",
                TypeInfo(int),
            ),
            (
                "person",
                "Person",
                TypeInfo(PersonDetail),
            ),
            (
                "face_matches",
                "FaceMatches",
                TypeInfo(typing.List[FaceMatch]),
            ),
        ]

    # The time, in milliseconds from the beginning of the video, that the person
    # was matched in the video.
    timestamp: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the matched person.
    person: "PersonDetail" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the faces in the input collection that match the face of
    # a person in the video.
    face_matches: typing.List["FaceMatch"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class PersonTrackingSortBy(str):
    INDEX = "INDEX"
    TIMESTAMP = "TIMESTAMP"


@dataclasses.dataclass
class Point(ShapeBase):
    """
    The X and Y coordinates of a point on an image. The X and Y values returned are
    ratios of the overall image size. For example, if the input image is 700x200 and
    the operation returns X=0.5 and Y=0.25, then the point is at the (350,50) pixel
    coordinate on the image.

    An array of `Point` objects, `Polygon`, is returned by . `Polygon` represents a
    fine-grained polygon around detected text. For more information, see Geometry in
    the Amazon Rekognition Developer Guide.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "x",
                "X",
                TypeInfo(float),
            ),
            (
                "y",
                "Y",
                TypeInfo(float),
            ),
        ]

    # The value of the X coordinate for a point on a `Polygon`.
    x: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of the Y coordinate for a point on a `Polygon`.
    y: float = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Pose(ShapeBase):
    """
    Indicates the pose of the face as determined by its pitch, roll, and yaw.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "roll",
                "Roll",
                TypeInfo(float),
            ),
            (
                "yaw",
                "Yaw",
                TypeInfo(float),
            ),
            (
                "pitch",
                "Pitch",
                TypeInfo(float),
            ),
        ]

    # Value representing the face rotation on the roll axis.
    roll: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Value representing the face rotation on the yaw axis.
    yaw: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Value representing the face rotation on the pitch axis.
    pitch: float = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ProvisionedThroughputExceededException(ShapeBase):
    """
    The number of requests exceeded your throughput limit. If you want to increase
    this limit, contact Amazon Rekognition.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class RecognizeCelebritiesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "image",
                "Image",
                TypeInfo(Image),
            ),
        ]

    # The input image as base64-encoded bytes or an S3 object. If you use the AWS
    # CLI to call Amazon Rekognition operations, passing base64-encoded image
    # bytes is not supported.
    image: "Image" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RecognizeCelebritiesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "celebrity_faces",
                "CelebrityFaces",
                TypeInfo(typing.List[Celebrity]),
            ),
            (
                "unrecognized_faces",
                "UnrecognizedFaces",
                TypeInfo(typing.List[ComparedFace]),
            ),
            (
                "orientation_correction",
                "OrientationCorrection",
                TypeInfo(typing.Union[str, OrientationCorrection]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Details about each celebrity found in the image. Amazon Rekognition can
    # detect a maximum of 15 celebrities in an image.
    celebrity_faces: typing.List["Celebrity"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Details about each unrecognized face in the image.
    unrecognized_faces: typing.List["ComparedFace"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The orientation of the input image (counterclockwise direction). If your
    # application displays the image, you can use this value to correct the
    # orientation. The bounding box coordinates returned in `CelebrityFaces` and
    # `UnrecognizedFaces` represent face locations before the image orientation
    # is corrected.

    # If the input image is in .jpeg format, it might contain exchangeable image
    # (Exif) metadata that includes the image's orientation. If so, and the Exif
    # metadata for the input image populates the orientation field, the value of
    # `OrientationCorrection` is null and the `CelebrityFaces` and
    # `UnrecognizedFaces` bounding box coordinates represent face locations after
    # Exif metadata is used to correct the image orientation. Images in .png
    # format don't contain Exif metadata.
    orientation_correction: typing.Union[str, "OrientationCorrection"
                                        ] = dataclasses.field(
                                            default=ShapeBase.NOT_SET,
                                        )


@dataclasses.dataclass
class ResourceAlreadyExistsException(ShapeBase):
    """
    A collection with the specified ID already exists.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ResourceInUseException(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ResourceNotFoundException(ShapeBase):
    """
    The collection specified in the request cannot be found.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class S3Object(ShapeBase):
    """
    Provides the S3 bucket name and object name.

    The region for the S3 bucket containing the S3 object must match the region you
    use for Amazon Rekognition operations.

    For Amazon Rekognition to process an S3 object, the user must have permission to
    access the S3 object. For more information, see Resource Based Policies in the
    Amazon Rekognition Developer Guide.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "version",
                "Version",
                TypeInfo(str),
            ),
        ]

    # Name of the S3 bucket.
    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # S3 object key name.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If the bucket is versioning enabled, you can specify the object version.
    version: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SearchFacesByImageRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "collection_id",
                "CollectionId",
                TypeInfo(str),
            ),
            (
                "image",
                "Image",
                TypeInfo(Image),
            ),
            (
                "max_faces",
                "MaxFaces",
                TypeInfo(int),
            ),
            (
                "face_match_threshold",
                "FaceMatchThreshold",
                TypeInfo(float),
            ),
        ]

    # ID of the collection to search.
    collection_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The input image as base64-encoded bytes or an S3 object. If you use the AWS
    # CLI to call Amazon Rekognition operations, passing base64-encoded image
    # bytes is not supported.
    image: "Image" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Maximum number of faces to return. The operation returns the maximum number
    # of faces with the highest confidence in the match.
    max_faces: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Specifies the minimum confidence in the face match to return.
    # For example, don't return any matches where confidence in matches is less
    # than 70%.
    face_match_threshold: float = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SearchFacesByImageResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "searched_face_bounding_box",
                "SearchedFaceBoundingBox",
                TypeInfo(BoundingBox),
            ),
            (
                "searched_face_confidence",
                "SearchedFaceConfidence",
                TypeInfo(float),
            ),
            (
                "face_matches",
                "FaceMatches",
                TypeInfo(typing.List[FaceMatch]),
            ),
            (
                "face_model_version",
                "FaceModelVersion",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The bounding box around the face in the input image that Amazon Rekognition
    # used for the search.
    searched_face_bounding_box: "BoundingBox" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The level of confidence that the `searchedFaceBoundingBox`, contains a
    # face.
    searched_face_confidence: float = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of faces that match the input face, along with the confidence in
    # the match.
    face_matches: typing.List["FaceMatch"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Version number of the face detection model associated with the input
    # collection (`CollectionId`).
    face_model_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SearchFacesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "collection_id",
                "CollectionId",
                TypeInfo(str),
            ),
            (
                "face_id",
                "FaceId",
                TypeInfo(str),
            ),
            (
                "max_faces",
                "MaxFaces",
                TypeInfo(int),
            ),
            (
                "face_match_threshold",
                "FaceMatchThreshold",
                TypeInfo(float),
            ),
        ]

    # ID of the collection the face belongs to.
    collection_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # ID of a face to find matches for in the collection.
    face_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Maximum number of faces to return. The operation returns the maximum number
    # of faces with the highest confidence in the match.
    max_faces: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Optional value specifying the minimum confidence in the face match to
    # return. For example, don't return any matches where confidence in matches
    # is less than 70%.
    face_match_threshold: float = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SearchFacesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "searched_face_id",
                "SearchedFaceId",
                TypeInfo(str),
            ),
            (
                "face_matches",
                "FaceMatches",
                TypeInfo(typing.List[FaceMatch]),
            ),
            (
                "face_model_version",
                "FaceModelVersion",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # ID of the face that was searched for matches in a collection.
    searched_face_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of faces that matched the input face, along with the confidence in
    # the match.
    face_matches: typing.List["FaceMatch"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Version number of the face detection model associated with the input
    # collection (`CollectionId`).
    face_model_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Smile(ShapeBase):
    """
    Indicates whether or not the face is smiling, and the confidence level in the
    determination.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "value",
                "Value",
                TypeInfo(bool),
            ),
            (
                "confidence",
                "Confidence",
                TypeInfo(float),
            ),
        ]

    # Boolean value that indicates whether the face is smiling or not.
    value: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Level of confidence in the determination.
    confidence: float = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartCelebrityRecognitionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "video",
                "Video",
                TypeInfo(Video),
            ),
            (
                "client_request_token",
                "ClientRequestToken",
                TypeInfo(str),
            ),
            (
                "notification_channel",
                "NotificationChannel",
                TypeInfo(NotificationChannel),
            ),
            (
                "job_tag",
                "JobTag",
                TypeInfo(str),
            ),
        ]

    # The video in which you want to recognize celebrities. The video must be
    # stored in an Amazon S3 bucket.
    video: "Video" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Idempotent token used to identify the start request. If you use the same
    # token with multiple `StartCelebrityRecognition` requests, the same `JobId`
    # is returned. Use `ClientRequestToken` to prevent the same job from being
    # accidently started more than once.
    client_request_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon SNS topic ARN that you want Amazon Rekognition Video to publish
    # the completion status of the celebrity recognition analysis to.
    notification_channel: "NotificationChannel" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Unique identifier you specify to identify the job in the completion status
    # published to the Amazon Simple Notification Service topic.
    job_tag: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartCelebrityRecognitionResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "job_id",
                "JobId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier for the celebrity recognition analysis job. Use `JobId` to
    # identify the job in a subsequent call to `GetCelebrityRecognition`.
    job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartContentModerationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "video",
                "Video",
                TypeInfo(Video),
            ),
            (
                "min_confidence",
                "MinConfidence",
                TypeInfo(float),
            ),
            (
                "client_request_token",
                "ClientRequestToken",
                TypeInfo(str),
            ),
            (
                "notification_channel",
                "NotificationChannel",
                TypeInfo(NotificationChannel),
            ),
            (
                "job_tag",
                "JobTag",
                TypeInfo(str),
            ),
        ]

    # The video in which you want to moderate content. The video must be stored
    # in an Amazon S3 bucket.
    video: "Video" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the minimum confidence that Amazon Rekognition must have in order
    # to return a moderated content label. Confidence represents how certain
    # Amazon Rekognition is that the moderated content is correctly identified. 0
    # is the lowest confidence. 100 is the highest confidence. Amazon Rekognition
    # doesn't return any moderated content labels with a confidence level lower
    # than this specified value.
    min_confidence: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Idempotent token used to identify the start request. If you use the same
    # token with multiple `StartContentModeration` requests, the same `JobId` is
    # returned. Use `ClientRequestToken` to prevent the same job from being
    # accidently started more than once.
    client_request_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon SNS topic ARN that you want Amazon Rekognition Video to publish
    # the completion status of the content moderation analysis to.
    notification_channel: "NotificationChannel" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Unique identifier you specify to identify the job in the completion status
    # published to the Amazon Simple Notification Service topic.
    job_tag: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartContentModerationResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "job_id",
                "JobId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier for the content moderation analysis job. Use `JobId` to
    # identify the job in a subsequent call to `GetContentModeration`.
    job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartFaceDetectionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "video",
                "Video",
                TypeInfo(Video),
            ),
            (
                "client_request_token",
                "ClientRequestToken",
                TypeInfo(str),
            ),
            (
                "notification_channel",
                "NotificationChannel",
                TypeInfo(NotificationChannel),
            ),
            (
                "face_attributes",
                "FaceAttributes",
                TypeInfo(typing.Union[str, FaceAttributes]),
            ),
            (
                "job_tag",
                "JobTag",
                TypeInfo(str),
            ),
        ]

    # The video in which you want to detect faces. The video must be stored in an
    # Amazon S3 bucket.
    video: "Video" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Idempotent token used to identify the start request. If you use the same
    # token with multiple `StartFaceDetection` requests, the same `JobId` is
    # returned. Use `ClientRequestToken` to prevent the same job from being
    # accidently started more than once.
    client_request_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the Amazon SNS topic to which you want Amazon Rekognition Video
    # to publish the completion status of the face detection operation.
    notification_channel: "NotificationChannel" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The face attributes you want returned.

    # `DEFAULT` \- The following subset of facial attributes are returned:
    # BoundingBox, Confidence, Pose, Quality and Landmarks.

    # `ALL` \- All facial attributes are returned.
    face_attributes: typing.Union[str, "FaceAttributes"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Unique identifier you specify to identify the job in the completion status
    # published to the Amazon Simple Notification Service topic.
    job_tag: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartFaceDetectionResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "job_id",
                "JobId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier for the face detection job. Use `JobId` to identify the job
    # in a subsequent call to `GetFaceDetection`.
    job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartFaceSearchRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "video",
                "Video",
                TypeInfo(Video),
            ),
            (
                "collection_id",
                "CollectionId",
                TypeInfo(str),
            ),
            (
                "client_request_token",
                "ClientRequestToken",
                TypeInfo(str),
            ),
            (
                "face_match_threshold",
                "FaceMatchThreshold",
                TypeInfo(float),
            ),
            (
                "notification_channel",
                "NotificationChannel",
                TypeInfo(NotificationChannel),
            ),
            (
                "job_tag",
                "JobTag",
                TypeInfo(str),
            ),
        ]

    # The video you want to search. The video must be stored in an Amazon S3
    # bucket.
    video: "Video" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # ID of the collection that contains the faces you want to search for.
    collection_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Idempotent token used to identify the start request. If you use the same
    # token with multiple `StartFaceSearch` requests, the same `JobId` is
    # returned. Use `ClientRequestToken` to prevent the same job from being
    # accidently started more than once.
    client_request_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The minimum confidence in the person match to return. For example, don't
    # return any matches where confidence in matches is less than 70%.
    face_match_threshold: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the Amazon SNS topic to which you want Amazon Rekognition Video
    # to publish the completion status of the search.
    notification_channel: "NotificationChannel" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Unique identifier you specify to identify the job in the completion status
    # published to the Amazon Simple Notification Service topic.
    job_tag: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartFaceSearchResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "job_id",
                "JobId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier for the search job. Use `JobId` to identify the job in a
    # subsequent call to `GetFaceSearch`.
    job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartLabelDetectionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "video",
                "Video",
                TypeInfo(Video),
            ),
            (
                "client_request_token",
                "ClientRequestToken",
                TypeInfo(str),
            ),
            (
                "min_confidence",
                "MinConfidence",
                TypeInfo(float),
            ),
            (
                "notification_channel",
                "NotificationChannel",
                TypeInfo(NotificationChannel),
            ),
            (
                "job_tag",
                "JobTag",
                TypeInfo(str),
            ),
        ]

    # The video in which you want to detect labels. The video must be stored in
    # an Amazon S3 bucket.
    video: "Video" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Idempotent token used to identify the start request. If you use the same
    # token with multiple `StartLabelDetection` requests, the same `JobId` is
    # returned. Use `ClientRequestToken` to prevent the same job from being
    # accidently started more than once.
    client_request_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the minimum confidence that Amazon Rekognition Video must have in
    # order to return a detected label. Confidence represents how certain Amazon
    # Rekognition is that a label is correctly identified.0 is the lowest
    # confidence. 100 is the highest confidence. Amazon Rekognition Video doesn't
    # return any labels with a confidence level lower than this specified value.

    # If you don't specify `MinConfidence`, the operation returns labels with
    # confidence values greater than or equal to 50 percent.
    min_confidence: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon SNS topic ARN you want Amazon Rekognition Video to publish the
    # completion status of the label detection operation to.
    notification_channel: "NotificationChannel" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Unique identifier you specify to identify the job in the completion status
    # published to the Amazon Simple Notification Service topic.
    job_tag: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartLabelDetectionResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "job_id",
                "JobId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier for the label detection job. Use `JobId` to identify the job
    # in a subsequent call to `GetLabelDetection`.
    job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartPersonTrackingRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "video",
                "Video",
                TypeInfo(Video),
            ),
            (
                "client_request_token",
                "ClientRequestToken",
                TypeInfo(str),
            ),
            (
                "notification_channel",
                "NotificationChannel",
                TypeInfo(NotificationChannel),
            ),
            (
                "job_tag",
                "JobTag",
                TypeInfo(str),
            ),
        ]

    # The video in which you want to detect people. The video must be stored in
    # an Amazon S3 bucket.
    video: "Video" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Idempotent token used to identify the start request. If you use the same
    # token with multiple `StartPersonTracking` requests, the same `JobId` is
    # returned. Use `ClientRequestToken` to prevent the same job from being
    # accidently started more than once.
    client_request_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon SNS topic ARN you want Amazon Rekognition Video to publish the
    # completion status of the people detection operation to.
    notification_channel: "NotificationChannel" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Unique identifier you specify to identify the job in the completion status
    # published to the Amazon Simple Notification Service topic.
    job_tag: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartPersonTrackingResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "job_id",
                "JobId",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier for the person detection job. Use `JobId` to identify the
    # job in a subsequent call to `GetPersonTracking`.
    job_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartStreamProcessorRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The name of the stream processor to start processing.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartStreamProcessorResponse(OutputShapeBase):
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
class StopStreamProcessorRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The name of a stream processor created by .
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StopStreamProcessorResponse(OutputShapeBase):
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
class StreamProcessor(ShapeBase):
    """
    An object that recognizes faces in a streaming video. An Amazon Rekognition
    stream processor is created by a call to . The request parameters for
    `CreateStreamProcessor` describe the Kinesis video stream source for the
    streaming video, face recognition parameters, and where to stream the analysis
    resullts.
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
                "status",
                "Status",
                TypeInfo(typing.Union[str, StreamProcessorStatus]),
            ),
        ]

    # Name of the Amazon Rekognition stream processor.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Current status of the Amazon Rekognition stream processor.
    status: typing.Union[str, "StreamProcessorStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StreamProcessorInput(ShapeBase):
    """
    Information about the source streaming video.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "kinesis_video_stream",
                "KinesisVideoStream",
                TypeInfo(KinesisVideoStream),
            ),
        ]

    # The Kinesis video stream input stream for the source streaming video.
    kinesis_video_stream: "KinesisVideoStream" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StreamProcessorOutput(ShapeBase):
    """
    Information about the Amazon Kinesis Data Streams stream to which a Amazon
    Rekognition Video stream processor streams the results of a video analysis. For
    more information, see CreateStreamProcessor in the Amazon Rekognition Developer
    Guide.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "kinesis_data_stream",
                "KinesisDataStream",
                TypeInfo(KinesisDataStream),
            ),
        ]

    # The Amazon Kinesis Data Streams stream to which the Amazon Rekognition
    # stream processor streams the analysis results.
    kinesis_data_stream: "KinesisDataStream" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StreamProcessorSettings(ShapeBase):
    """
    Input parameters used to recognize faces in a streaming video analyzed by a
    Amazon Rekognition stream processor.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "face_search",
                "FaceSearch",
                TypeInfo(FaceSearchSettings),
            ),
        ]

    # Face search settings to use on a streaming video.
    face_search: "FaceSearchSettings" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class StreamProcessorStatus(str):
    STOPPED = "STOPPED"
    STARTING = "STARTING"
    RUNNING = "RUNNING"
    FAILED = "FAILED"
    STOPPING = "STOPPING"


@dataclasses.dataclass
class Sunglasses(ShapeBase):
    """
    Indicates whether or not the face is wearing sunglasses, and the confidence
    level in the determination.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "value",
                "Value",
                TypeInfo(bool),
            ),
            (
                "confidence",
                "Confidence",
                TypeInfo(float),
            ),
        ]

    # Boolean value that indicates whether the face is wearing sunglasses or not.
    value: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Level of confidence in the determination.
    confidence: float = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TextDetection(ShapeBase):
    """
    Information about a word or line of text detected by .

    The `DetectedText` field contains the text that Amazon Rekognition detected in
    the image.

    Every word and line has an identifier (`Id`). Each word belongs to a line and
    has a parent identifier (`ParentId`) that identifies the line of text in which
    the word appears. The word `Id` is also an index for the word within a line of
    words.

    For more information, see Detecting Text in the Amazon Rekognition Developer
    Guide.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detected_text",
                "DetectedText",
                TypeInfo(str),
            ),
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, TextTypes]),
            ),
            (
                "id",
                "Id",
                TypeInfo(int),
            ),
            (
                "parent_id",
                "ParentId",
                TypeInfo(int),
            ),
            (
                "confidence",
                "Confidence",
                TypeInfo(float),
            ),
            (
                "geometry",
                "Geometry",
                TypeInfo(Geometry),
            ),
        ]

    # The word or line of text recognized by Amazon Rekognition.
    detected_text: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of text that was detected.
    type: typing.Union[str, "TextTypes"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier for the detected text. The identifier is only unique for a
    # single call to `DetectText`.
    id: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Parent identifier for the detected text identified by the value of
    # `ID`. If the type of detected text is `LINE`, the value of `ParentId` is
    # `Null`.
    parent_id: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The confidence that Amazon Rekognition has in the accuracy of the detected
    # text and the accuracy of the geometry points around the detected text.
    confidence: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The location of the detected text on the image. Includes an axis aligned
    # coarse bounding box surrounding the text and a finer grain polygon for more
    # accurate spatial information.
    geometry: "Geometry" = dataclasses.field(default=ShapeBase.NOT_SET, )


class TextTypes(str):
    LINE = "LINE"
    WORD = "WORD"


@dataclasses.dataclass
class ThrottlingException(ShapeBase):
    """
    Amazon Rekognition is temporarily unable to process the request. Try your call
    again.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class Video(ShapeBase):
    """
    Video file stored in an Amazon S3 bucket. Amazon Rekognition video start
    operations such as use `Video` to specify a video for analysis. The supported
    file formats are .mp4, .mov and .avi.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "s3_object",
                "S3Object",
                TypeInfo(S3Object),
            ),
        ]

    # The Amazon S3 bucket name and file name for the video.
    s3_object: "S3Object" = dataclasses.field(default=ShapeBase.NOT_SET, )


class VideoJobStatus(str):
    IN_PROGRESS = "IN_PROGRESS"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"


@dataclasses.dataclass
class VideoMetadata(ShapeBase):
    """
    Information about a video that Amazon Rekognition analyzed. `Videometadata` is
    returned in every page of paginated responses from a Amazon Rekognition video
    operation.
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
                "duration_millis",
                "DurationMillis",
                TypeInfo(int),
            ),
            (
                "format",
                "Format",
                TypeInfo(str),
            ),
            (
                "frame_rate",
                "FrameRate",
                TypeInfo(float),
            ),
            (
                "frame_height",
                "FrameHeight",
                TypeInfo(int),
            ),
            (
                "frame_width",
                "FrameWidth",
                TypeInfo(int),
            ),
        ]

    # Type of compression used in the analyzed video.
    codec: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Length of the video in milliseconds.
    duration_millis: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Format of the analyzed video. Possible values are MP4, MOV and AVI.
    format: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Number of frames per second in the video.
    frame_rate: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Vertical pixel dimension of the video.
    frame_height: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Horizontal pixel dimension of the video.
    frame_width: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class VideoTooLargeException(ShapeBase):
    """
    The file size or duration of the supplied media is too large. The maximum file
    size is 8GB. The maximum duration is 2 hours.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []
