import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import botocore.response
import dataclasses


@dataclasses.dataclass
class ContainerNotFoundException(ShapeBase):
    """
    The specified container was not found for the specified account.
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
class DeleteObjectRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "path",
                "Path",
                TypeInfo(str),
            ),
        ]

    # The path (including the file name) where the object is stored in the
    # container. Format: <folder name>/<folder name>/<file name>
    path: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteObjectResponse(OutputShapeBase):
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
class DescribeObjectRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "path",
                "Path",
                TypeInfo(str),
            ),
        ]

    # The path (including the file name) where the object is stored in the
    # container. Format: <folder name>/<folder name>/<file name>
    path: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeObjectResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "e_tag",
                "ETag",
                TypeInfo(str),
            ),
            (
                "content_type",
                "ContentType",
                TypeInfo(str),
            ),
            (
                "content_length",
                "ContentLength",
                TypeInfo(int),
            ),
            (
                "cache_control",
                "CacheControl",
                TypeInfo(str),
            ),
            (
                "last_modified",
                "LastModified",
                TypeInfo(datetime.datetime),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ETag that represents a unique instance of the object.
    e_tag: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The content type of the object.
    content_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The length of the object in bytes.
    content_length: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional `CacheControl` header that allows the caller to control the
    # object's cache behavior. Headers can be passed in as specified in the HTTP
    # at <https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9>.

    # Headers with a custom user-defined value are also accepted.
    cache_control: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time that the object was last modified.
    last_modified: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetObjectRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "path",
                "Path",
                TypeInfo(str),
            ),
            (
                "range",
                "Range",
                TypeInfo(str),
            ),
        ]

    # The path (including the file name) where the object is stored in the
    # container. Format: <folder name>/<folder name>/<file name>

    # For example, to upload the file `mlaw.avi` to the folder path
    # `premium\canada` in the container `movies`, enter the path
    # `premium/canada/mlaw.avi`.

    # Do not include the container name in this path.

    # If the path includes any folders that don't exist yet, the service creates
    # them. For example, suppose you have an existing `premium/usa` subfolder. If
    # you specify `premium/canada`, the service creates a `canada` subfolder in
    # the `premium` folder. You then have two subfolders, `usa` and `canada`, in
    # the `premium` folder.

    # There is no correlation between the path to the source and the path
    # (folders) in the container in AWS Elemental MediaStore.

    # For more information about folders and how they exist in a container, see
    # the [AWS Elemental MediaStore User
    # Guide](http://docs.aws.amazon.com/mediastore/latest/ug/).

    # The file name is the name that is assigned to the file that you upload. The
    # file can have the same name inside and outside of AWS Elemental MediaStore,
    # or it can have the same name. The file name can include or omit an
    # extension.
    path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The range bytes of an object to retrieve. For more information about the
    # `Range` header, go to
    # <http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35>.
    range: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetObjectResponse(OutputShapeBase):
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
                "body",
                "Body",
                TypeInfo(typing.Any),
            ),
            (
                "cache_control",
                "CacheControl",
                TypeInfo(str),
            ),
            (
                "content_range",
                "ContentRange",
                TypeInfo(str),
            ),
            (
                "content_length",
                "ContentLength",
                TypeInfo(int),
            ),
            (
                "content_type",
                "ContentType",
                TypeInfo(str),
            ),
            (
                "e_tag",
                "ETag",
                TypeInfo(str),
            ),
            (
                "last_modified",
                "LastModified",
                TypeInfo(datetime.datetime),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The HTML status code of the request. Status codes ranging from 200 to 299
    # indicate success. All other status codes indicate the type of error that
    # occurred.
    status_code: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The bytes of the object.
    body: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional `CacheControl` header that allows the caller to control the
    # object's cache behavior. Headers can be passed in as specified in the HTTP
    # spec at <https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9>.

    # Headers with a custom user-defined value are also accepted.
    cache_control: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The range of bytes to retrieve.
    content_range: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The length of the object in bytes.
    content_length: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The content type of the object.
    content_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ETag that represents a unique instance of the object.
    e_tag: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time that the object was last modified.
    last_modified: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InternalServerError(ShapeBase):
    """
    The service is temporarily unavailable.
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
class Item(ShapeBase):
    """
    A metadata entry for a folder or object.
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
                "type",
                "Type",
                TypeInfo(typing.Union[str, ItemType]),
            ),
            (
                "e_tag",
                "ETag",
                TypeInfo(str),
            ),
            (
                "last_modified",
                "LastModified",
                TypeInfo(datetime.datetime),
            ),
            (
                "content_type",
                "ContentType",
                TypeInfo(str),
            ),
            (
                "content_length",
                "ContentLength",
                TypeInfo(int),
            ),
        ]

    # The name of the item.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The item type (folder or object).
    type: typing.Union[str, "ItemType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ETag that represents a unique instance of the item.
    e_tag: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time that the item was last modified.
    last_modified: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The content type of the item.
    content_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The length of the item in bytes.
    content_length: int = dataclasses.field(default=ShapeBase.NOT_SET, )


class ItemType(str):
    OBJECT = "OBJECT"
    FOLDER = "FOLDER"


@dataclasses.dataclass
class ListItemsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "path",
                "Path",
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

    # The path in the container from which to retrieve items. Format: <folder
    # name>/<folder name>/<file name>
    path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum results to return. The service might return fewer results.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The `NextToken` received in the `ListItemsResponse` for the same container
    # and path. Tokens expire after 15 minutes.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListItemsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "items",
                "Items",
                TypeInfo(typing.List[Item]),
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

    # Metadata entries for the folders and objects at the requested path.
    items: typing.List["Item"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The `NextToken` used to request the next page of results using `ListItems`.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ObjectNotFoundException(ShapeBase):
    """
    Could not perform an operation on an object that does not exist.
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


class PayloadBlob(botocore.response.StreamingBody):
    pass


@dataclasses.dataclass
class PutObjectRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "body",
                "Body",
                TypeInfo(typing.Any),
            ),
            (
                "path",
                "Path",
                TypeInfo(str),
            ),
            (
                "content_type",
                "ContentType",
                TypeInfo(str),
            ),
            (
                "cache_control",
                "CacheControl",
                TypeInfo(str),
            ),
            (
                "storage_class",
                "StorageClass",
                TypeInfo(typing.Union[str, StorageClass]),
            ),
        ]

    # The bytes to be stored.
    body: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The path (including the file name) where the object is stored in the
    # container. Format: <folder name>/<folder name>/<file name>

    # For example, to upload the file `mlaw.avi` to the folder path
    # `premium\canada` in the container `movies`, enter the path
    # `premium/canada/mlaw.avi`.

    # Do not include the container name in this path.

    # If the path includes any folders that don't exist yet, the service creates
    # them. For example, suppose you have an existing `premium/usa` subfolder. If
    # you specify `premium/canada`, the service creates a `canada` subfolder in
    # the `premium` folder. You then have two subfolders, `usa` and `canada`, in
    # the `premium` folder.

    # There is no correlation between the path to the source and the path
    # (folders) in the container in AWS Elemental MediaStore.

    # For more information about folders and how they exist in a container, see
    # the [AWS Elemental MediaStore User
    # Guide](http://docs.aws.amazon.com/mediastore/latest/ug/).

    # The file name is the name that is assigned to the file that you upload. The
    # file can have the same name inside and outside of AWS Elemental MediaStore,
    # or it can have the same name. The file name can include or omit an
    # extension.
    path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The content type of the object.
    content_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional `CacheControl` header that allows the caller to control the
    # object's cache behavior. Headers can be passed in as specified in the HTTP
    # at <https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9>.

    # Headers with a custom user-defined value are also accepted.
    cache_control: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates the storage class of a `Put` request. Defaults to high-
    # performance temporal storage class, and objects are persisted into durable
    # storage shortly after being received.
    storage_class: typing.Union[str, "StorageClass"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutObjectResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "content_sha256",
                "ContentSHA256",
                TypeInfo(str),
            ),
            (
                "e_tag",
                "ETag",
                TypeInfo(str),
            ),
            (
                "storage_class",
                "StorageClass",
                TypeInfo(typing.Union[str, StorageClass]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The SHA256 digest of the object that is persisted.
    content_sha256: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique identifier of the object in the container.
    e_tag: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The storage class where the object was persisted. Should be “Temporal”.
    storage_class: typing.Union[str, "StorageClass"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RequestedRangeNotSatisfiableException(ShapeBase):
    """
    The requested content range is not valid.
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


class StorageClass(str):
    TEMPORAL = "TEMPORAL"
