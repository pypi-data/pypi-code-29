import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import botocore.response
import dataclasses


@dataclasses.dataclass
class AccessDeniedException(ShapeBase):
    """
    Access denied. Check your permissions.
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
class AddFacetToObjectRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_arn",
                "DirectoryArn",
                TypeInfo(str),
            ),
            (
                "schema_facet",
                "SchemaFacet",
                TypeInfo(SchemaFacet),
            ),
            (
                "object_reference",
                "ObjectReference",
                TypeInfo(ObjectReference),
            ),
            (
                "object_attribute_list",
                "ObjectAttributeList",
                TypeInfo(typing.List[AttributeKeyAndValue]),
            ),
        ]

    # The Amazon Resource Name (ARN) that is associated with the Directory where
    # the object resides. For more information, see arns.
    directory_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Identifiers for the facet that you are adding to the object. See
    # SchemaFacet for details.
    schema_facet: "SchemaFacet" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A reference to the object you are adding the specified facet to.
    object_reference: "ObjectReference" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Attributes on the facet that you are adding to the object.
    object_attribute_list: typing.List["AttributeKeyAndValue"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )


@dataclasses.dataclass
class AddFacetToObjectResponse(OutputShapeBase):
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
class ApplySchemaRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "published_schema_arn",
                "PublishedSchemaArn",
                TypeInfo(str),
            ),
            (
                "directory_arn",
                "DirectoryArn",
                TypeInfo(str),
            ),
        ]

    # Published schema Amazon Resource Name (ARN) that needs to be copied. For
    # more information, see arns.
    published_schema_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) that is associated with the Directory into
    # which the schema is copied. For more information, see arns.
    directory_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ApplySchemaResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "applied_schema_arn",
                "AppliedSchemaArn",
                TypeInfo(str),
            ),
            (
                "directory_arn",
                "DirectoryArn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The applied schema ARN that is associated with the copied schema in the
    # Directory. You can use this ARN to describe the schema information applied
    # on this directory. For more information, see arns.
    applied_schema_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN that is associated with the Directory. For more information, see
    # arns.
    directory_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AttachObjectRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_arn",
                "DirectoryArn",
                TypeInfo(str),
            ),
            (
                "parent_reference",
                "ParentReference",
                TypeInfo(ObjectReference),
            ),
            (
                "child_reference",
                "ChildReference",
                TypeInfo(ObjectReference),
            ),
            (
                "link_name",
                "LinkName",
                TypeInfo(str),
            ),
        ]

    # Amazon Resource Name (ARN) that is associated with the Directory where both
    # objects reside. For more information, see arns.
    directory_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The parent object reference.
    parent_reference: "ObjectReference" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The child object reference to be attached to the object.
    child_reference: "ObjectReference" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The link name with which the child object is attached to the parent.
    link_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AttachObjectResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "attached_object_identifier",
                "AttachedObjectIdentifier",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The attached `ObjectIdentifier`, which is the child `ObjectIdentifier`.
    attached_object_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AttachPolicyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_arn",
                "DirectoryArn",
                TypeInfo(str),
            ),
            (
                "policy_reference",
                "PolicyReference",
                TypeInfo(ObjectReference),
            ),
            (
                "object_reference",
                "ObjectReference",
                TypeInfo(ObjectReference),
            ),
        ]

    # The Amazon Resource Name (ARN) that is associated with the Directory where
    # both objects reside. For more information, see arns.
    directory_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The reference that is associated with the policy object.
    policy_reference: "ObjectReference" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The reference that identifies the object to which the policy will be
    # attached.
    object_reference: "ObjectReference" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AttachPolicyResponse(OutputShapeBase):
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
class AttachToIndexRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_arn",
                "DirectoryArn",
                TypeInfo(str),
            ),
            (
                "index_reference",
                "IndexReference",
                TypeInfo(ObjectReference),
            ),
            (
                "target_reference",
                "TargetReference",
                TypeInfo(ObjectReference),
            ),
        ]

    # The Amazon Resource Name (ARN) of the directory where the object and index
    # exist.
    directory_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A reference to the index that you are attaching the object to.
    index_reference: "ObjectReference" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A reference to the object that you are attaching to the index.
    target_reference: "ObjectReference" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AttachToIndexResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "attached_object_identifier",
                "AttachedObjectIdentifier",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The `ObjectIdentifier` of the object that was attached to the index.
    attached_object_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AttachTypedLinkRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_arn",
                "DirectoryArn",
                TypeInfo(str),
            ),
            (
                "source_object_reference",
                "SourceObjectReference",
                TypeInfo(ObjectReference),
            ),
            (
                "target_object_reference",
                "TargetObjectReference",
                TypeInfo(ObjectReference),
            ),
            (
                "typed_link_facet",
                "TypedLinkFacet",
                TypeInfo(TypedLinkSchemaAndFacetName),
            ),
            (
                "attributes",
                "Attributes",
                TypeInfo(typing.List[AttributeNameAndValue]),
            ),
        ]

    # The Amazon Resource Name (ARN) of the directory where you want to attach
    # the typed link.
    directory_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Identifies the source object that the typed link will attach to.
    source_object_reference: "ObjectReference" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Identifies the target object that the typed link will attach to.
    target_object_reference: "ObjectReference" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Identifies the typed link facet that is associated with the typed link.
    typed_link_facet: "TypedLinkSchemaAndFacetName" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A set of attributes that are associated with the typed link.
    attributes: typing.List["AttributeNameAndValue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AttachTypedLinkResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "typed_link_specifier",
                "TypedLinkSpecifier",
                TypeInfo(TypedLinkSpecifier),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Returns a typed link specifier as output.
    typed_link_specifier: "TypedLinkSpecifier" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AttributeKey(ShapeBase):
    """
    A unique identifier for an attribute.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "schema_arn",
                "SchemaArn",
                TypeInfo(str),
            ),
            (
                "facet_name",
                "FacetName",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the schema that contains the facet and
    # attribute.
    schema_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the facet that the attribute exists within.
    facet_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the attribute.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AttributeKeyAndValue(ShapeBase):
    """
    The combination of an attribute key and an attribute value.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "Key",
                TypeInfo(AttributeKey),
            ),
            (
                "value",
                "Value",
                TypeInfo(TypedAttributeValue),
            ),
        ]

    # The key of the attribute.
    key: "AttributeKey" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of the attribute.
    value: "TypedAttributeValue" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AttributeNameAndValue(ShapeBase):
    """
    Identifies the attribute name and value for a typed link.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attribute_name",
                "AttributeName",
                TypeInfo(str),
            ),
            (
                "value",
                "Value",
                TypeInfo(TypedAttributeValue),
            ),
        ]

    # The attribute name of the typed link.
    attribute_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value for the typed link.
    value: "TypedAttributeValue" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchAddFacetToObject(ShapeBase):
    """
    Represents the output of a batch add facet to object operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "schema_facet",
                "SchemaFacet",
                TypeInfo(SchemaFacet),
            ),
            (
                "object_attribute_list",
                "ObjectAttributeList",
                TypeInfo(typing.List[AttributeKeyAndValue]),
            ),
            (
                "object_reference",
                "ObjectReference",
                TypeInfo(ObjectReference),
            ),
        ]

    # Represents the facet being added to the object.
    schema_facet: "SchemaFacet" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The attributes to set on the object.
    object_attribute_list: typing.List["AttributeKeyAndValue"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    # A reference to the object being mutated.
    object_reference: "ObjectReference" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchAddFacetToObjectResponse(ShapeBase):
    """
    The result of a batch add facet to object operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class BatchAttachObject(ShapeBase):
    """
    Represents the output of an AttachObject operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "parent_reference",
                "ParentReference",
                TypeInfo(ObjectReference),
            ),
            (
                "child_reference",
                "ChildReference",
                TypeInfo(ObjectReference),
            ),
            (
                "link_name",
                "LinkName",
                TypeInfo(str),
            ),
        ]

    # The parent object reference.
    parent_reference: "ObjectReference" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The child object reference that is to be attached to the object.
    child_reference: "ObjectReference" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the link.
    link_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BatchAttachObjectResponse(ShapeBase):
    """
    Represents the output batch AttachObject response operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attached_object_identifier",
                "attachedObjectIdentifier",
                TypeInfo(str),
            ),
        ]

    # The `ObjectIdentifier` of the object that has been attached.
    attached_object_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchAttachPolicy(ShapeBase):
    """
    Attaches a policy object to a regular object inside a BatchRead operation. For
    more information, see AttachPolicy and BatchReadRequest$Operations.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_reference",
                "PolicyReference",
                TypeInfo(ObjectReference),
            ),
            (
                "object_reference",
                "ObjectReference",
                TypeInfo(ObjectReference),
            ),
        ]

    # The reference that is associated with the policy object.
    policy_reference: "ObjectReference" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The reference that identifies the object to which the policy will be
    # attached.
    object_reference: "ObjectReference" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchAttachPolicyResponse(ShapeBase):
    """
    Represents the output of an AttachPolicy response operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class BatchAttachToIndex(ShapeBase):
    """
    Attaches the specified object to the specified index inside a BatchRead
    operation. For more information, see AttachToIndex and
    BatchReadRequest$Operations.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "index_reference",
                "IndexReference",
                TypeInfo(ObjectReference),
            ),
            (
                "target_reference",
                "TargetReference",
                TypeInfo(ObjectReference),
            ),
        ]

    # A reference to the index that you are attaching the object to.
    index_reference: "ObjectReference" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A reference to the object that you are attaching to the index.
    target_reference: "ObjectReference" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchAttachToIndexResponse(ShapeBase):
    """
    Represents the output of a AttachToIndex response operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attached_object_identifier",
                "AttachedObjectIdentifier",
                TypeInfo(str),
            ),
        ]

    # The `ObjectIdentifier` of the object that was attached to the index.
    attached_object_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchAttachTypedLink(ShapeBase):
    """
    Attaches a typed link to a specified source and target object inside a BatchRead
    operation. For more information, see AttachTypedLink and
    BatchReadRequest$Operations.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "source_object_reference",
                "SourceObjectReference",
                TypeInfo(ObjectReference),
            ),
            (
                "target_object_reference",
                "TargetObjectReference",
                TypeInfo(ObjectReference),
            ),
            (
                "typed_link_facet",
                "TypedLinkFacet",
                TypeInfo(TypedLinkSchemaAndFacetName),
            ),
            (
                "attributes",
                "Attributes",
                TypeInfo(typing.List[AttributeNameAndValue]),
            ),
        ]

    # Identifies the source object that the typed link will attach to.
    source_object_reference: "ObjectReference" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Identifies the target object that the typed link will attach to.
    target_object_reference: "ObjectReference" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Identifies the typed link facet that is associated with the typed link.
    typed_link_facet: "TypedLinkSchemaAndFacetName" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A set of attributes that are associated with the typed link.
    attributes: typing.List["AttributeNameAndValue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchAttachTypedLinkResponse(ShapeBase):
    """
    Represents the output of a AttachTypedLink response operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "typed_link_specifier",
                "TypedLinkSpecifier",
                TypeInfo(TypedLinkSpecifier),
            ),
        ]

    # Returns a typed link specifier as output.
    typed_link_specifier: "TypedLinkSpecifier" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchCreateIndex(ShapeBase):
    """
    Creates an index object inside of a BatchRead operation. For more information,
    see CreateIndex and BatchReadRequest$Operations.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ordered_indexed_attribute_list",
                "OrderedIndexedAttributeList",
                TypeInfo(typing.List[AttributeKey]),
            ),
            (
                "is_unique",
                "IsUnique",
                TypeInfo(bool),
            ),
            (
                "parent_reference",
                "ParentReference",
                TypeInfo(ObjectReference),
            ),
            (
                "link_name",
                "LinkName",
                TypeInfo(str),
            ),
            (
                "batch_reference_name",
                "BatchReferenceName",
                TypeInfo(str),
            ),
        ]

    # Specifies the attributes that should be indexed on. Currently only a single
    # attribute is supported.
    ordered_indexed_attribute_list: typing.List["AttributeKey"
                                               ] = dataclasses.field(
                                                   default=ShapeBase.NOT_SET,
                                               )

    # Indicates whether the attribute that is being indexed has unique values or
    # not.
    is_unique: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A reference to the parent object that contains the index object.
    parent_reference: "ObjectReference" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the link between the parent object and the index object.
    link_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The batch reference name. See
    # [Batches](http://docs.aws.amazon.com/directoryservice/latest/admin-
    # guide/cd_advanced.html#batches) for more information.
    batch_reference_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BatchCreateIndexResponse(ShapeBase):
    """
    Represents the output of a CreateIndex response operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "object_identifier",
                "ObjectIdentifier",
                TypeInfo(str),
            ),
        ]

    # The `ObjectIdentifier` of the index created by this operation.
    object_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BatchCreateObject(ShapeBase):
    """
    Represents the output of a CreateObject operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "schema_facet",
                "SchemaFacet",
                TypeInfo(typing.List[SchemaFacet]),
            ),
            (
                "object_attribute_list",
                "ObjectAttributeList",
                TypeInfo(typing.List[AttributeKeyAndValue]),
            ),
            (
                "parent_reference",
                "ParentReference",
                TypeInfo(ObjectReference),
            ),
            (
                "link_name",
                "LinkName",
                TypeInfo(str),
            ),
            (
                "batch_reference_name",
                "BatchReferenceName",
                TypeInfo(str),
            ),
        ]

    # A list of `FacetArns` that will be associated with the object. For more
    # information, see arns.
    schema_facet: typing.List["SchemaFacet"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An attribute map, which contains an attribute ARN as the key and attribute
    # value as the map value.
    object_attribute_list: typing.List["AttributeKeyAndValue"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    # If specified, the parent reference to which this object will be attached.
    parent_reference: "ObjectReference" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the link.
    link_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The batch reference name. See
    # [Batches](http://docs.aws.amazon.com/directoryservice/latest/admin-
    # guide/cd_advanced.html#batches) for more information.
    batch_reference_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BatchCreateObjectResponse(ShapeBase):
    """
    Represents the output of a CreateObject response operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "object_identifier",
                "ObjectIdentifier",
                TypeInfo(str),
            ),
        ]

    # The ID that is associated with the object.
    object_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BatchDeleteObject(ShapeBase):
    """
    Represents the output of a DeleteObject operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "object_reference",
                "ObjectReference",
                TypeInfo(ObjectReference),
            ),
        ]

    # The reference that identifies the object.
    object_reference: "ObjectReference" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchDeleteObjectResponse(ShapeBase):
    """
    Represents the output of a DeleteObject response operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class BatchDetachFromIndex(ShapeBase):
    """
    Detaches the specified object from the specified index inside a BatchRead
    operation. For more information, see DetachFromIndex and
    BatchReadRequest$Operations.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "index_reference",
                "IndexReference",
                TypeInfo(ObjectReference),
            ),
            (
                "target_reference",
                "TargetReference",
                TypeInfo(ObjectReference),
            ),
        ]

    # A reference to the index object.
    index_reference: "ObjectReference" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A reference to the object being detached from the index.
    target_reference: "ObjectReference" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchDetachFromIndexResponse(ShapeBase):
    """
    Represents the output of a DetachFromIndex response operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detached_object_identifier",
                "DetachedObjectIdentifier",
                TypeInfo(str),
            ),
        ]

    # The `ObjectIdentifier` of the object that was detached from the index.
    detached_object_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchDetachObject(ShapeBase):
    """
    Represents the output of a DetachObject operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "parent_reference",
                "ParentReference",
                TypeInfo(ObjectReference),
            ),
            (
                "link_name",
                "LinkName",
                TypeInfo(str),
            ),
            (
                "batch_reference_name",
                "BatchReferenceName",
                TypeInfo(str),
            ),
        ]

    # Parent reference from which the object with the specified link name is
    # detached.
    parent_reference: "ObjectReference" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the link.
    link_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The batch reference name. See
    # [Batches](http://docs.aws.amazon.com/directoryservice/latest/admin-
    # guide/cd_advanced.html#batches) for more information.
    batch_reference_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BatchDetachObjectResponse(ShapeBase):
    """
    Represents the output of a DetachObject response operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "detached_object_identifier",
                "detachedObjectIdentifier",
                TypeInfo(str),
            ),
        ]

    # The `ObjectIdentifier` of the detached object.
    detached_object_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchDetachPolicy(ShapeBase):
    """
    Detaches the specified policy from the specified directory inside a BatchWrite
    operation. For more information, see DetachPolicy and
    BatchWriteRequest$Operations.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_reference",
                "PolicyReference",
                TypeInfo(ObjectReference),
            ),
            (
                "object_reference",
                "ObjectReference",
                TypeInfo(ObjectReference),
            ),
        ]

    # Reference that identifies the policy object.
    policy_reference: "ObjectReference" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Reference that identifies the object whose policy object will be detached.
    object_reference: "ObjectReference" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchDetachPolicyResponse(ShapeBase):
    """
    Represents the output of a DetachPolicy response operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class BatchDetachTypedLink(ShapeBase):
    """
    Detaches a typed link from a specified source and target object inside a
    BatchRead operation. For more information, see DetachTypedLink and
    BatchReadRequest$Operations.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "typed_link_specifier",
                "TypedLinkSpecifier",
                TypeInfo(TypedLinkSpecifier),
            ),
        ]

    # Used to accept a typed link specifier as input.
    typed_link_specifier: "TypedLinkSpecifier" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchDetachTypedLinkResponse(ShapeBase):
    """
    Represents the output of a DetachTypedLink response operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class BatchGetLinkAttributes(ShapeBase):
    """
    Retrieves attributes that are associated with a typed link inside a BatchRead
    operation. For more information, see GetLinkAttributes and
    BatchReadRequest$Operations.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "typed_link_specifier",
                "TypedLinkSpecifier",
                TypeInfo(TypedLinkSpecifier),
            ),
            (
                "attribute_names",
                "AttributeNames",
                TypeInfo(typing.List[str]),
            ),
        ]

    # Allows a typed link specifier to be accepted as input.
    typed_link_specifier: "TypedLinkSpecifier" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of attribute names whose values will be retrieved.
    attribute_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchGetLinkAttributesResponse(ShapeBase):
    """
    Represents the output of a GetLinkAttributes response operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attributes",
                "Attributes",
                TypeInfo(typing.List[AttributeKeyAndValue]),
            ),
        ]

    # The attributes that are associated with the typed link.
    attributes: typing.List["AttributeKeyAndValue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchGetObjectAttributes(ShapeBase):
    """
    Retrieves attributes within a facet that are associated with an object inside an
    BatchRead operation. For more information, see GetObjectAttributes and
    BatchReadRequest$Operations.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "object_reference",
                "ObjectReference",
                TypeInfo(ObjectReference),
            ),
            (
                "schema_facet",
                "SchemaFacet",
                TypeInfo(SchemaFacet),
            ),
            (
                "attribute_names",
                "AttributeNames",
                TypeInfo(typing.List[str]),
            ),
        ]

    # Reference that identifies the object whose attributes will be retrieved.
    object_reference: "ObjectReference" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Identifier for the facet whose attributes will be retrieved. See
    # SchemaFacet for details.
    schema_facet: "SchemaFacet" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # List of attribute names whose values will be retrieved.
    attribute_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchGetObjectAttributesResponse(ShapeBase):
    """
    Represents the output of a GetObjectAttributes response operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attributes",
                "Attributes",
                TypeInfo(typing.List[AttributeKeyAndValue]),
            ),
        ]

    # The attribute values that are associated with an object.
    attributes: typing.List["AttributeKeyAndValue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchGetObjectInformation(ShapeBase):
    """
    Retrieves metadata about an object inside a BatchRead operation. For more
    information, see GetObjectInformation and BatchReadRequest$Operations.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "object_reference",
                "ObjectReference",
                TypeInfo(ObjectReference),
            ),
        ]

    # A reference to the object.
    object_reference: "ObjectReference" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchGetObjectInformationResponse(ShapeBase):
    """
    Represents the output of a GetObjectInformation response operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "schema_facets",
                "SchemaFacets",
                TypeInfo(typing.List[SchemaFacet]),
            ),
            (
                "object_identifier",
                "ObjectIdentifier",
                TypeInfo(str),
            ),
        ]

    # The facets attached to the specified object.
    schema_facets: typing.List["SchemaFacet"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The `ObjectIdentifier` of the specified object.
    object_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BatchListAttachedIndices(ShapeBase):
    """
    Lists indices attached to an object inside a BatchRead operation. For more
    information, see ListAttachedIndices and BatchReadRequest$Operations.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "target_reference",
                "TargetReference",
                TypeInfo(ObjectReference),
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

    # A reference to the object that has indices attached.
    target_reference: "ObjectReference" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pagination token.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to retrieve.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BatchListAttachedIndicesResponse(ShapeBase):
    """
    Represents the output of a ListAttachedIndices response operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "index_attachments",
                "IndexAttachments",
                TypeInfo(typing.List[IndexAttachment]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The indices attached to the specified object.
    index_attachments: typing.List["IndexAttachment"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pagination token.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BatchListIncomingTypedLinks(ShapeBase):
    """
    Returns a paginated list of all the incoming TypedLinkSpecifier information for
    an object inside a BatchRead operation. For more information, see
    ListIncomingTypedLinks and BatchReadRequest$Operations.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "object_reference",
                "ObjectReference",
                TypeInfo(ObjectReference),
            ),
            (
                "filter_attribute_ranges",
                "FilterAttributeRanges",
                TypeInfo(typing.List[TypedLinkAttributeRange]),
            ),
            (
                "filter_typed_link",
                "FilterTypedLink",
                TypeInfo(TypedLinkSchemaAndFacetName),
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

    # The reference that identifies the object whose attributes will be listed.
    object_reference: "ObjectReference" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Provides range filters for multiple attributes. When providing ranges to
    # typed link selection, any inexact ranges must be specified at the end. Any
    # attributes that do not have a range specified are presumed to match the
    # entire range.
    filter_attribute_ranges: typing.List["TypedLinkAttributeRange"
                                        ] = dataclasses.field(
                                            default=ShapeBase.NOT_SET,
                                        )

    # Filters are interpreted in the order of the attributes on the typed link
    # facet, not the order in which they are supplied to any API calls.
    filter_typed_link: "TypedLinkSchemaAndFacetName" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pagination token.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to retrieve.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BatchListIncomingTypedLinksResponse(ShapeBase):
    """
    Represents the output of a ListIncomingTypedLinks response operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "link_specifiers",
                "LinkSpecifiers",
                TypeInfo(typing.List[TypedLinkSpecifier]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # Returns one or more typed link specifiers as output.
    link_specifiers: typing.List["TypedLinkSpecifier"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pagination token.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BatchListIndex(ShapeBase):
    """
    Lists objects attached to the specified index inside a BatchRead operation. For
    more information, see ListIndex and BatchReadRequest$Operations.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "index_reference",
                "IndexReference",
                TypeInfo(ObjectReference),
            ),
            (
                "ranges_on_indexed_values",
                "RangesOnIndexedValues",
                TypeInfo(typing.List[ObjectAttributeRange]),
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

    # The reference to the index to list.
    index_reference: "ObjectReference" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the ranges of indexed values that you want to query.
    ranges_on_indexed_values: typing.List["ObjectAttributeRange"
                                         ] = dataclasses.field(
                                             default=ShapeBase.NOT_SET,
                                         )

    # The maximum number of results to retrieve.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The pagination token.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BatchListIndexResponse(ShapeBase):
    """
    Represents the output of a ListIndex response operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "index_attachments",
                "IndexAttachments",
                TypeInfo(typing.List[IndexAttachment]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The objects and indexed values attached to the index.
    index_attachments: typing.List["IndexAttachment"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pagination token.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BatchListObjectAttributes(ShapeBase):
    """
    Represents the output of a ListObjectAttributes operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "object_reference",
                "ObjectReference",
                TypeInfo(ObjectReference),
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
            (
                "facet_filter",
                "FacetFilter",
                TypeInfo(SchemaFacet),
            ),
        ]

    # Reference of the object whose attributes need to be listed.
    object_reference: "ObjectReference" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pagination token.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of items to be retrieved in a single call. This is an
    # approximate number.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Used to filter the list of object attributes that are associated with a
    # certain facet.
    facet_filter: "SchemaFacet" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BatchListObjectAttributesResponse(ShapeBase):
    """
    Represents the output of a ListObjectAttributes response operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attributes",
                "Attributes",
                TypeInfo(typing.List[AttributeKeyAndValue]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The attributes map that is associated with the object. `AttributeArn` is
    # the key; attribute value is the value.
    attributes: typing.List["AttributeKeyAndValue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pagination token.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BatchListObjectChildren(ShapeBase):
    """
    Represents the output of a ListObjectChildren operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "object_reference",
                "ObjectReference",
                TypeInfo(ObjectReference),
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

    # Reference of the object for which child objects are being listed.
    object_reference: "ObjectReference" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pagination token.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Maximum number of items to be retrieved in a single call. This is an
    # approximate number.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BatchListObjectChildrenResponse(ShapeBase):
    """
    Represents the output of a ListObjectChildren response operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "children",
                "Children",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The children structure, which is a map with the key as the `LinkName` and
    # `ObjectIdentifier` as the value.
    children: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pagination token.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BatchListObjectParentPaths(ShapeBase):
    """
    Retrieves all available parent paths for any object type such as node, leaf
    node, policy node, and index node objects inside a BatchRead operation. For more
    information, see ListObjectParentPaths and BatchReadRequest$Operations.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "object_reference",
                "ObjectReference",
                TypeInfo(ObjectReference),
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

    # The reference that identifies the object whose attributes will be listed.
    object_reference: "ObjectReference" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pagination token.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to retrieve.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BatchListObjectParentPathsResponse(ShapeBase):
    """
    Represents the output of a ListObjectParentPaths response operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "path_to_object_identifiers_list",
                "PathToObjectIdentifiersList",
                TypeInfo(typing.List[PathToObjectIdentifiers]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # Returns the path to the `ObjectIdentifiers` that are associated with the
    # directory.
    path_to_object_identifiers_list: typing.List["PathToObjectIdentifiers"
                                                ] = dataclasses.field(
                                                    default=ShapeBase.NOT_SET,
                                                )

    # The pagination token.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BatchListObjectPolicies(ShapeBase):
    """
    Returns policies attached to an object in pagination fashion inside a BatchRead
    operation. For more information, see ListObjectPolicies and
    BatchReadRequest$Operations.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "object_reference",
                "ObjectReference",
                TypeInfo(ObjectReference),
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

    # The reference that identifies the object whose attributes will be listed.
    object_reference: "ObjectReference" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pagination token.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to retrieve.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BatchListObjectPoliciesResponse(ShapeBase):
    """
    Represents the output of a ListObjectPolicies response operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attached_policy_ids",
                "AttachedPolicyIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # A list of policy `ObjectIdentifiers`, that are attached to the object.
    attached_policy_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pagination token.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BatchListOutgoingTypedLinks(ShapeBase):
    """
    Returns a paginated list of all the outgoing TypedLinkSpecifier information for
    an object inside a BatchRead operation. For more information, see
    ListOutgoingTypedLinks and BatchReadRequest$Operations.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "object_reference",
                "ObjectReference",
                TypeInfo(ObjectReference),
            ),
            (
                "filter_attribute_ranges",
                "FilterAttributeRanges",
                TypeInfo(typing.List[TypedLinkAttributeRange]),
            ),
            (
                "filter_typed_link",
                "FilterTypedLink",
                TypeInfo(TypedLinkSchemaAndFacetName),
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

    # The reference that identifies the object whose attributes will be listed.
    object_reference: "ObjectReference" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Provides range filters for multiple attributes. When providing ranges to
    # typed link selection, any inexact ranges must be specified at the end. Any
    # attributes that do not have a range specified are presumed to match the
    # entire range.
    filter_attribute_ranges: typing.List["TypedLinkAttributeRange"
                                        ] = dataclasses.field(
                                            default=ShapeBase.NOT_SET,
                                        )

    # Filters are interpreted in the order of the attributes defined on the typed
    # link facet, not the order they are supplied to any API calls.
    filter_typed_link: "TypedLinkSchemaAndFacetName" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pagination token.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to retrieve.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BatchListOutgoingTypedLinksResponse(ShapeBase):
    """
    Represents the output of a ListOutgoingTypedLinks response operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "typed_link_specifiers",
                "TypedLinkSpecifiers",
                TypeInfo(typing.List[TypedLinkSpecifier]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # Returns a typed link specifier as output.
    typed_link_specifiers: typing.List["TypedLinkSpecifier"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    # The pagination token.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BatchListPolicyAttachments(ShapeBase):
    """
    Returns all of the `ObjectIdentifiers` to which a given policy is attached
    inside a BatchRead operation. For more information, see ListPolicyAttachments
    and BatchReadRequest$Operations.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_reference",
                "PolicyReference",
                TypeInfo(ObjectReference),
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

    # The reference that identifies the policy object.
    policy_reference: "ObjectReference" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pagination token.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to retrieve.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BatchListPolicyAttachmentsResponse(ShapeBase):
    """
    Represents the output of a ListPolicyAttachments response operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "object_identifiers",
                "ObjectIdentifiers",
                TypeInfo(typing.List[str]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # A list of `ObjectIdentifiers` to which the policy is attached.
    object_identifiers: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pagination token.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BatchLookupPolicy(ShapeBase):
    """
    Lists all policies from the root of the Directory to the object specified inside
    a BatchRead operation. For more information, see LookupPolicy and
    BatchReadRequest$Operations.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "object_reference",
                "ObjectReference",
                TypeInfo(ObjectReference),
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

    # Reference that identifies the object whose policies will be looked up.
    object_reference: "ObjectReference" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pagination token.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to retrieve.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BatchLookupPolicyResponse(ShapeBase):
    """
    Represents the output of a LookupPolicy response operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_to_path_list",
                "PolicyToPathList",
                TypeInfo(typing.List[PolicyToPath]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # Provides list of path to policies. Policies contain `PolicyId`,
    # `ObjectIdentifier`, and `PolicyType`. For more information, see
    # [Policies](http://docs.aws.amazon.com/directoryservice/latest/admin-
    # guide/cd_key_concepts.html#policies).
    policy_to_path_list: typing.List["PolicyToPath"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pagination token.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BatchReadException(ShapeBase):
    """
    The batch read exception structure, which contains the exception type and
    message.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, BatchReadExceptionType]),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    # A type of exception, such as `InvalidArnException`.
    type: typing.Union[str, "BatchReadExceptionType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An exception message that is associated with the failure.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class BatchReadExceptionType(str):
    ValidationException = "ValidationException"
    InvalidArnException = "InvalidArnException"
    ResourceNotFoundException = "ResourceNotFoundException"
    InvalidNextTokenException = "InvalidNextTokenException"
    AccessDeniedException = "AccessDeniedException"
    NotNodeException = "NotNodeException"
    FacetValidationException = "FacetValidationException"
    CannotListParentOfRootException = "CannotListParentOfRootException"
    NotIndexException = "NotIndexException"
    NotPolicyException = "NotPolicyException"
    DirectoryNotEnabledException = "DirectoryNotEnabledException"
    LimitExceededException = "LimitExceededException"
    InternalServiceException = "InternalServiceException"


@dataclasses.dataclass
class BatchReadOperation(ShapeBase):
    """
    Represents the output of a `BatchRead` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "list_object_attributes",
                "ListObjectAttributes",
                TypeInfo(BatchListObjectAttributes),
            ),
            (
                "list_object_children",
                "ListObjectChildren",
                TypeInfo(BatchListObjectChildren),
            ),
            (
                "list_attached_indices",
                "ListAttachedIndices",
                TypeInfo(BatchListAttachedIndices),
            ),
            (
                "list_object_parent_paths",
                "ListObjectParentPaths",
                TypeInfo(BatchListObjectParentPaths),
            ),
            (
                "get_object_information",
                "GetObjectInformation",
                TypeInfo(BatchGetObjectInformation),
            ),
            (
                "get_object_attributes",
                "GetObjectAttributes",
                TypeInfo(BatchGetObjectAttributes),
            ),
            (
                "list_object_policies",
                "ListObjectPolicies",
                TypeInfo(BatchListObjectPolicies),
            ),
            (
                "list_policy_attachments",
                "ListPolicyAttachments",
                TypeInfo(BatchListPolicyAttachments),
            ),
            (
                "lookup_policy",
                "LookupPolicy",
                TypeInfo(BatchLookupPolicy),
            ),
            (
                "list_index",
                "ListIndex",
                TypeInfo(BatchListIndex),
            ),
            (
                "list_outgoing_typed_links",
                "ListOutgoingTypedLinks",
                TypeInfo(BatchListOutgoingTypedLinks),
            ),
            (
                "list_incoming_typed_links",
                "ListIncomingTypedLinks",
                TypeInfo(BatchListIncomingTypedLinks),
            ),
            (
                "get_link_attributes",
                "GetLinkAttributes",
                TypeInfo(BatchGetLinkAttributes),
            ),
        ]

    # Lists all attributes that are associated with an object.
    list_object_attributes: "BatchListObjectAttributes" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Returns a paginated list of child objects that are associated with a given
    # object.
    list_object_children: "BatchListObjectChildren" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Lists indices attached to an object.
    list_attached_indices: "BatchListAttachedIndices" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Retrieves all available parent paths for any object type such as node, leaf
    # node, policy node, and index node objects. For more information about
    # objects, see [Directory
    # Structure](http://docs.aws.amazon.com/directoryservice/latest/admin-
    # guide/cd_key_concepts.html#dirstructure).
    list_object_parent_paths: "BatchListObjectParentPaths" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Retrieves metadata about an object.
    get_object_information: "BatchGetObjectInformation" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Retrieves attributes within a facet that are associated with an object.
    get_object_attributes: "BatchGetObjectAttributes" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Returns policies attached to an object in pagination fashion.
    list_object_policies: "BatchListObjectPolicies" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Returns all of the `ObjectIdentifiers` to which a given policy is attached.
    list_policy_attachments: "BatchListPolicyAttachments" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Lists all policies from the root of the Directory to the object specified.
    # If there are no policies present, an empty list is returned. If policies
    # are present, and if some objects don't have the policies attached, it
    # returns the `ObjectIdentifier` for such objects. If policies are present,
    # it returns `ObjectIdentifier`, `policyId`, and `policyType`. Paths that
    # don't lead to the root from the target object are ignored. For more
    # information, see
    # [Policies](http://docs.aws.amazon.com/directoryservice/latest/admin-
    # guide/cd_key_concepts.html#policies).
    lookup_policy: "BatchLookupPolicy" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Lists objects attached to the specified index.
    list_index: "BatchListIndex" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Returns a paginated list of all the outgoing TypedLinkSpecifier information
    # for an object. It also supports filtering by typed link facet and identity
    # attributes. For more information, see [Typed
    # link](http://docs.aws.amazon.com/directoryservice/latest/admin-
    # guide/objectsandlinks.html#typedlink).
    list_outgoing_typed_links: "BatchListOutgoingTypedLinks" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Returns a paginated list of all the incoming TypedLinkSpecifier information
    # for an object. It also supports filtering by typed link facet and identity
    # attributes. For more information, see [Typed
    # link](http://docs.aws.amazon.com/directoryservice/latest/admin-
    # guide/objectsandlinks.html#typedlink).
    list_incoming_typed_links: "BatchListIncomingTypedLinks" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Retrieves attributes that are associated with a typed link.
    get_link_attributes: "BatchGetLinkAttributes" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchReadOperationResponse(ShapeBase):
    """
    Represents the output of a `BatchRead` response operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "successful_response",
                "SuccessfulResponse",
                TypeInfo(BatchReadSuccessfulResponse),
            ),
            (
                "exception_response",
                "ExceptionResponse",
                TypeInfo(BatchReadException),
            ),
        ]

    # Identifies which operation in a batch has succeeded.
    successful_response: "BatchReadSuccessfulResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Identifies which operation in a batch has failed.
    exception_response: "BatchReadException" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchReadRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_arn",
                "DirectoryArn",
                TypeInfo(str),
            ),
            (
                "operations",
                "Operations",
                TypeInfo(typing.List[BatchReadOperation]),
            ),
            (
                "consistency_level",
                "ConsistencyLevel",
                TypeInfo(typing.Union[str, ConsistencyLevel]),
            ),
        ]

    # The Amazon Resource Name (ARN) that is associated with the Directory. For
    # more information, see arns.
    directory_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of operations that are part of the batch.
    operations: typing.List["BatchReadOperation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Represents the manner and timing in which the successful write or update of
    # an object is reflected in a subsequent read operation of that same object.
    consistency_level: typing.Union[str, "ConsistencyLevel"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )


@dataclasses.dataclass
class BatchReadResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "responses",
                "Responses",
                TypeInfo(typing.List[BatchReadOperationResponse]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of all the responses for each batch read.
    responses: typing.List["BatchReadOperationResponse"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchReadSuccessfulResponse(ShapeBase):
    """
    Represents the output of a `BatchRead` success response operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "list_object_attributes",
                "ListObjectAttributes",
                TypeInfo(BatchListObjectAttributesResponse),
            ),
            (
                "list_object_children",
                "ListObjectChildren",
                TypeInfo(BatchListObjectChildrenResponse),
            ),
            (
                "get_object_information",
                "GetObjectInformation",
                TypeInfo(BatchGetObjectInformationResponse),
            ),
            (
                "get_object_attributes",
                "GetObjectAttributes",
                TypeInfo(BatchGetObjectAttributesResponse),
            ),
            (
                "list_attached_indices",
                "ListAttachedIndices",
                TypeInfo(BatchListAttachedIndicesResponse),
            ),
            (
                "list_object_parent_paths",
                "ListObjectParentPaths",
                TypeInfo(BatchListObjectParentPathsResponse),
            ),
            (
                "list_object_policies",
                "ListObjectPolicies",
                TypeInfo(BatchListObjectPoliciesResponse),
            ),
            (
                "list_policy_attachments",
                "ListPolicyAttachments",
                TypeInfo(BatchListPolicyAttachmentsResponse),
            ),
            (
                "lookup_policy",
                "LookupPolicy",
                TypeInfo(BatchLookupPolicyResponse),
            ),
            (
                "list_index",
                "ListIndex",
                TypeInfo(BatchListIndexResponse),
            ),
            (
                "list_outgoing_typed_links",
                "ListOutgoingTypedLinks",
                TypeInfo(BatchListOutgoingTypedLinksResponse),
            ),
            (
                "list_incoming_typed_links",
                "ListIncomingTypedLinks",
                TypeInfo(BatchListIncomingTypedLinksResponse),
            ),
            (
                "get_link_attributes",
                "GetLinkAttributes",
                TypeInfo(BatchGetLinkAttributesResponse),
            ),
        ]

    # Lists all attributes that are associated with an object.
    list_object_attributes: "BatchListObjectAttributesResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Returns a paginated list of child objects that are associated with a given
    # object.
    list_object_children: "BatchListObjectChildrenResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Retrieves metadata about an object.
    get_object_information: "BatchGetObjectInformationResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Retrieves attributes within a facet that are associated with an object.
    get_object_attributes: "BatchGetObjectAttributesResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Lists indices attached to an object.
    list_attached_indices: "BatchListAttachedIndicesResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Retrieves all available parent paths for any object type such as node, leaf
    # node, policy node, and index node objects. For more information about
    # objects, see [Directory
    # Structure](http://docs.aws.amazon.com/directoryservice/latest/admin-
    # guide/cd_key_concepts.html#dirstructure).
    list_object_parent_paths: "BatchListObjectParentPathsResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Returns policies attached to an object in pagination fashion.
    list_object_policies: "BatchListObjectPoliciesResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Returns all of the `ObjectIdentifiers` to which a given policy is attached.
    list_policy_attachments: "BatchListPolicyAttachmentsResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Lists all policies from the root of the Directory to the object specified.
    # If there are no policies present, an empty list is returned. If policies
    # are present, and if some objects don't have the policies attached, it
    # returns the `ObjectIdentifier` for such objects. If policies are present,
    # it returns `ObjectIdentifier`, `policyId`, and `policyType`. Paths that
    # don't lead to the root from the target object are ignored. For more
    # information, see
    # [Policies](http://docs.aws.amazon.com/directoryservice/latest/admin-
    # guide/cd_key_concepts.html#policies).
    lookup_policy: "BatchLookupPolicyResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Lists objects attached to the specified index.
    list_index: "BatchListIndexResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Returns a paginated list of all the outgoing TypedLinkSpecifier information
    # for an object. It also supports filtering by typed link facet and identity
    # attributes. For more information, see [Typed
    # link](http://docs.aws.amazon.com/directoryservice/latest/admin-
    # guide/objectsandlinks.html#typedlink).
    list_outgoing_typed_links: "BatchListOutgoingTypedLinksResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Returns a paginated list of all the incoming TypedLinkSpecifier information
    # for an object. It also supports filtering by typed link facet and identity
    # attributes. For more information, see [Typed
    # link](http://docs.aws.amazon.com/directoryservice/latest/admin-
    # guide/objectsandlinks.html#typedlink).
    list_incoming_typed_links: "BatchListIncomingTypedLinksResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of attributes to retrieve from the typed link.
    get_link_attributes: "BatchGetLinkAttributesResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchRemoveFacetFromObject(ShapeBase):
    """
    A batch operation to remove a facet from an object.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "schema_facet",
                "SchemaFacet",
                TypeInfo(SchemaFacet),
            ),
            (
                "object_reference",
                "ObjectReference",
                TypeInfo(ObjectReference),
            ),
        ]

    # The facet to remove from the object.
    schema_facet: "SchemaFacet" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A reference to the object whose facet will be removed.
    object_reference: "ObjectReference" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchRemoveFacetFromObjectResponse(ShapeBase):
    """
    An empty result that represents success.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class BatchUpdateLinkAttributes(ShapeBase):
    """
    Updates a given typed link’s attributes inside a BatchRead operation. Attributes
    to be updated must not contribute to the typed link’s identity, as defined by
    its `IdentityAttributeOrder`. For more information, see UpdateLinkAttributes and
    BatchReadRequest$Operations.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "typed_link_specifier",
                "TypedLinkSpecifier",
                TypeInfo(TypedLinkSpecifier),
            ),
            (
                "attribute_updates",
                "AttributeUpdates",
                TypeInfo(typing.List[LinkAttributeUpdate]),
            ),
        ]

    # Allows a typed link specifier to be accepted as input.
    typed_link_specifier: "TypedLinkSpecifier" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The attributes update structure.
    attribute_updates: typing.List["LinkAttributeUpdate"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchUpdateLinkAttributesResponse(ShapeBase):
    """
    Represents the output of a UpdateLinkAttributes response operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class BatchUpdateObjectAttributes(ShapeBase):
    """
    Represents the output of a `BatchUpdate` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "object_reference",
                "ObjectReference",
                TypeInfo(ObjectReference),
            ),
            (
                "attribute_updates",
                "AttributeUpdates",
                TypeInfo(typing.List[ObjectAttributeUpdate]),
            ),
        ]

    # Reference that identifies the object.
    object_reference: "ObjectReference" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Attributes update structure.
    attribute_updates: typing.List["ObjectAttributeUpdate"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchUpdateObjectAttributesResponse(ShapeBase):
    """
    Represents the output of a `BatchUpdate` response operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "object_identifier",
                "ObjectIdentifier",
                TypeInfo(str),
            ),
        ]

    # ID that is associated with the object.
    object_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BatchWriteException(ShapeBase):
    """
    A `BatchWrite` exception has occurred.
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
                "type",
                "Type",
                TypeInfo(typing.Union[str, BatchWriteExceptionType]),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    index: int = dataclasses.field(default=ShapeBase.NOT_SET, )
    type: typing.Union[str, "BatchWriteExceptionType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class BatchWriteExceptionType(str):
    InternalServiceException = "InternalServiceException"
    ValidationException = "ValidationException"
    InvalidArnException = "InvalidArnException"
    LinkNameAlreadyInUseException = "LinkNameAlreadyInUseException"
    StillContainsLinksException = "StillContainsLinksException"
    FacetValidationException = "FacetValidationException"
    ObjectNotDetachedException = "ObjectNotDetachedException"
    ResourceNotFoundException = "ResourceNotFoundException"
    AccessDeniedException = "AccessDeniedException"
    InvalidAttachmentException = "InvalidAttachmentException"
    NotIndexException = "NotIndexException"
    NotNodeException = "NotNodeException"
    IndexedAttributeMissingException = "IndexedAttributeMissingException"
    ObjectAlreadyDetachedException = "ObjectAlreadyDetachedException"
    NotPolicyException = "NotPolicyException"
    DirectoryNotEnabledException = "DirectoryNotEnabledException"
    LimitExceededException = "LimitExceededException"
    UnsupportedIndexTypeException = "UnsupportedIndexTypeException"


@dataclasses.dataclass
class BatchWriteOperation(ShapeBase):
    """
    Represents the output of a `BatchWrite` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "create_object",
                "CreateObject",
                TypeInfo(BatchCreateObject),
            ),
            (
                "attach_object",
                "AttachObject",
                TypeInfo(BatchAttachObject),
            ),
            (
                "detach_object",
                "DetachObject",
                TypeInfo(BatchDetachObject),
            ),
            (
                "update_object_attributes",
                "UpdateObjectAttributes",
                TypeInfo(BatchUpdateObjectAttributes),
            ),
            (
                "delete_object",
                "DeleteObject",
                TypeInfo(BatchDeleteObject),
            ),
            (
                "add_facet_to_object",
                "AddFacetToObject",
                TypeInfo(BatchAddFacetToObject),
            ),
            (
                "remove_facet_from_object",
                "RemoveFacetFromObject",
                TypeInfo(BatchRemoveFacetFromObject),
            ),
            (
                "attach_policy",
                "AttachPolicy",
                TypeInfo(BatchAttachPolicy),
            ),
            (
                "detach_policy",
                "DetachPolicy",
                TypeInfo(BatchDetachPolicy),
            ),
            (
                "create_index",
                "CreateIndex",
                TypeInfo(BatchCreateIndex),
            ),
            (
                "attach_to_index",
                "AttachToIndex",
                TypeInfo(BatchAttachToIndex),
            ),
            (
                "detach_from_index",
                "DetachFromIndex",
                TypeInfo(BatchDetachFromIndex),
            ),
            (
                "attach_typed_link",
                "AttachTypedLink",
                TypeInfo(BatchAttachTypedLink),
            ),
            (
                "detach_typed_link",
                "DetachTypedLink",
                TypeInfo(BatchDetachTypedLink),
            ),
            (
                "update_link_attributes",
                "UpdateLinkAttributes",
                TypeInfo(BatchUpdateLinkAttributes),
            ),
        ]

    # Creates an object.
    create_object: "BatchCreateObject" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Attaches an object to a Directory.
    attach_object: "BatchAttachObject" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Detaches an object from a Directory.
    detach_object: "BatchDetachObject" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Updates a given object's attributes.
    update_object_attributes: "BatchUpdateObjectAttributes" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Deletes an object in a Directory.
    delete_object: "BatchDeleteObject" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A batch operation that adds a facet to an object.
    add_facet_to_object: "BatchAddFacetToObject" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A batch operation that removes a facet from an object.
    remove_facet_from_object: "BatchRemoveFacetFromObject" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Attaches a policy object to a regular object. An object can have a limited
    # number of attached policies.
    attach_policy: "BatchAttachPolicy" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Detaches a policy from a Directory.
    detach_policy: "BatchDetachPolicy" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Creates an index object. See
    # [Indexing](http://docs.aws.amazon.com/directoryservice/latest/admin-
    # guide/cd_indexing.html) for more information.
    create_index: "BatchCreateIndex" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Attaches the specified object to the specified index.
    attach_to_index: "BatchAttachToIndex" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Detaches the specified object from the specified index.
    detach_from_index: "BatchDetachFromIndex" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Attaches a typed link to a specified source and target object. For more
    # information, see [Typed
    # link](http://docs.aws.amazon.com/directoryservice/latest/admin-
    # guide/objectsandlinks.html#typedlink).
    attach_typed_link: "BatchAttachTypedLink" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Detaches a typed link from a specified source and target object. For more
    # information, see [Typed
    # link](http://docs.aws.amazon.com/directoryservice/latest/admin-
    # guide/objectsandlinks.html#typedlink).
    detach_typed_link: "BatchDetachTypedLink" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Updates a given object's attributes.
    update_link_attributes: "BatchUpdateLinkAttributes" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchWriteOperationResponse(ShapeBase):
    """
    Represents the output of a `BatchWrite` response operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "create_object",
                "CreateObject",
                TypeInfo(BatchCreateObjectResponse),
            ),
            (
                "attach_object",
                "AttachObject",
                TypeInfo(BatchAttachObjectResponse),
            ),
            (
                "detach_object",
                "DetachObject",
                TypeInfo(BatchDetachObjectResponse),
            ),
            (
                "update_object_attributes",
                "UpdateObjectAttributes",
                TypeInfo(BatchUpdateObjectAttributesResponse),
            ),
            (
                "delete_object",
                "DeleteObject",
                TypeInfo(BatchDeleteObjectResponse),
            ),
            (
                "add_facet_to_object",
                "AddFacetToObject",
                TypeInfo(BatchAddFacetToObjectResponse),
            ),
            (
                "remove_facet_from_object",
                "RemoveFacetFromObject",
                TypeInfo(BatchRemoveFacetFromObjectResponse),
            ),
            (
                "attach_policy",
                "AttachPolicy",
                TypeInfo(BatchAttachPolicyResponse),
            ),
            (
                "detach_policy",
                "DetachPolicy",
                TypeInfo(BatchDetachPolicyResponse),
            ),
            (
                "create_index",
                "CreateIndex",
                TypeInfo(BatchCreateIndexResponse),
            ),
            (
                "attach_to_index",
                "AttachToIndex",
                TypeInfo(BatchAttachToIndexResponse),
            ),
            (
                "detach_from_index",
                "DetachFromIndex",
                TypeInfo(BatchDetachFromIndexResponse),
            ),
            (
                "attach_typed_link",
                "AttachTypedLink",
                TypeInfo(BatchAttachTypedLinkResponse),
            ),
            (
                "detach_typed_link",
                "DetachTypedLink",
                TypeInfo(BatchDetachTypedLinkResponse),
            ),
            (
                "update_link_attributes",
                "UpdateLinkAttributes",
                TypeInfo(BatchUpdateLinkAttributesResponse),
            ),
        ]

    # Creates an object in a Directory.
    create_object: "BatchCreateObjectResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Attaches an object to a Directory.
    attach_object: "BatchAttachObjectResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Detaches an object from a Directory.
    detach_object: "BatchDetachObjectResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Updates a given object’s attributes.
    update_object_attributes: "BatchUpdateObjectAttributesResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Deletes an object in a Directory.
    delete_object: "BatchDeleteObjectResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The result of an add facet to object batch operation.
    add_facet_to_object: "BatchAddFacetToObjectResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The result of a batch remove facet from object operation.
    remove_facet_from_object: "BatchRemoveFacetFromObjectResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Attaches a policy object to a regular object. An object can have a limited
    # number of attached policies.
    attach_policy: "BatchAttachPolicyResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Detaches a policy from a Directory.
    detach_policy: "BatchDetachPolicyResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Creates an index object. See
    # [Indexing](http://docs.aws.amazon.com/directoryservice/latest/admin-
    # guide/cd_indexing.html) for more information.
    create_index: "BatchCreateIndexResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Attaches the specified object to the specified index.
    attach_to_index: "BatchAttachToIndexResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Detaches the specified object from the specified index.
    detach_from_index: "BatchDetachFromIndexResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Attaches a typed link to a specified source and target object. For more
    # information, see [Typed
    # link](http://docs.aws.amazon.com/directoryservice/latest/admin-
    # guide/objectsandlinks.html#typedlink).
    attach_typed_link: "BatchAttachTypedLinkResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Detaches a typed link from a specified source and target object. For more
    # information, see [Typed
    # link](http://docs.aws.amazon.com/directoryservice/latest/admin-
    # guide/objectsandlinks.html#typedlink).
    detach_typed_link: "BatchDetachTypedLinkResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Represents the output of a `BatchWrite` response operation.
    update_link_attributes: "BatchUpdateLinkAttributesResponse" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchWriteRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_arn",
                "DirectoryArn",
                TypeInfo(str),
            ),
            (
                "operations",
                "Operations",
                TypeInfo(typing.List[BatchWriteOperation]),
            ),
        ]

    # The Amazon Resource Name (ARN) that is associated with the Directory. For
    # more information, see arns.
    directory_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of operations that are part of the batch.
    operations: typing.List["BatchWriteOperation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchWriteResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "responses",
                "Responses",
                TypeInfo(typing.List[BatchWriteOperationResponse]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of all the responses for each batch write.
    responses: typing.List["BatchWriteOperationResponse"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class BinaryAttributeValue(botocore.response.StreamingBody):
    pass


@dataclasses.dataclass
class CannotListParentOfRootException(ShapeBase):
    """
    Cannot list the parents of a Directory root.
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


class ConsistencyLevel(str):
    SERIALIZABLE = "SERIALIZABLE"
    EVENTUAL = "EVENTUAL"


@dataclasses.dataclass
class CreateDirectoryRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "schema_arn",
                "SchemaArn",
                TypeInfo(str),
            ),
        ]

    # The name of the Directory. Should be unique per account, per region.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the published schema that will be copied
    # into the data Directory. For more information, see arns.
    schema_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateDirectoryResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "directory_arn",
                "DirectoryArn",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "object_identifier",
                "ObjectIdentifier",
                TypeInfo(str),
            ),
            (
                "applied_schema_arn",
                "AppliedSchemaArn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN that is associated with the Directory. For more information, see
    # arns.
    directory_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the Directory.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The root object node of the created directory.
    object_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the published schema in the Directory. Once a published schema
    # is copied into the directory, it has its own ARN, which is referred to
    # applied schema ARN. For more information, see arns.
    applied_schema_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateFacetRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "schema_arn",
                "SchemaArn",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "attributes",
                "Attributes",
                TypeInfo(typing.List[FacetAttribute]),
            ),
            (
                "object_type",
                "ObjectType",
                TypeInfo(typing.Union[str, ObjectType]),
            ),
            (
                "facet_style",
                "FacetStyle",
                TypeInfo(typing.Union[str, FacetStyle]),
            ),
        ]

    # The schema ARN in which the new Facet will be created. For more
    # information, see arns.
    schema_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the Facet, which is unique for a given schema.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The attributes that are associated with the Facet.
    attributes: typing.List["FacetAttribute"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies whether a given object created from this facet is of type node,
    # leaf node, policy or index.

    #   * Node: Can have multiple children but one parent.

    #   * Leaf node: Cannot have children but can have multiple parents.

    #   * Policy: Allows you to store a policy document and policy type. For more information, see [Policies](http://docs.aws.amazon.com/directoryservice/latest/admin-guide/cd_key_concepts.html#policies).

    #   * Index: Can be created with the Index API.
    object_type: typing.Union[str, "ObjectType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # There are two different styles that you can define on any given facet,
    # `Static` and `Dynamic`. For static facets, all attributes must be defined
    # in the schema. For dynamic facets, attributes can be defined during data
    # plane operations.
    facet_style: typing.Union[str, "FacetStyle"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateFacetResponse(OutputShapeBase):
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
class CreateIndexRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_arn",
                "DirectoryArn",
                TypeInfo(str),
            ),
            (
                "ordered_indexed_attribute_list",
                "OrderedIndexedAttributeList",
                TypeInfo(typing.List[AttributeKey]),
            ),
            (
                "is_unique",
                "IsUnique",
                TypeInfo(bool),
            ),
            (
                "parent_reference",
                "ParentReference",
                TypeInfo(ObjectReference),
            ),
            (
                "link_name",
                "LinkName",
                TypeInfo(str),
            ),
        ]

    # The ARN of the directory where the index should be created.
    directory_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the attributes that should be indexed on. Currently only a single
    # attribute is supported.
    ordered_indexed_attribute_list: typing.List["AttributeKey"
                                               ] = dataclasses.field(
                                                   default=ShapeBase.NOT_SET,
                                               )

    # Indicates whether the attribute that is being indexed has unique values or
    # not.
    is_unique: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A reference to the parent object that contains the index object.
    parent_reference: "ObjectReference" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the link between the parent object and the index object.
    link_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateIndexResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "object_identifier",
                "ObjectIdentifier",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The `ObjectIdentifier` of the index created by this operation.
    object_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateObjectRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_arn",
                "DirectoryArn",
                TypeInfo(str),
            ),
            (
                "schema_facets",
                "SchemaFacets",
                TypeInfo(typing.List[SchemaFacet]),
            ),
            (
                "object_attribute_list",
                "ObjectAttributeList",
                TypeInfo(typing.List[AttributeKeyAndValue]),
            ),
            (
                "parent_reference",
                "ParentReference",
                TypeInfo(ObjectReference),
            ),
            (
                "link_name",
                "LinkName",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) that is associated with the Directory in
    # which the object will be created. For more information, see arns.
    directory_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of schema facets to be associated with the object. Do not provide
    # minor version components. See SchemaFacet for details.
    schema_facets: typing.List["SchemaFacet"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The attribute map whose attribute ARN contains the key and attribute value
    # as the map value.
    object_attribute_list: typing.List["AttributeKeyAndValue"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    # If specified, the parent reference to which this object will be attached.
    parent_reference: "ObjectReference" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of link that is used to attach this object to a parent.
    link_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateObjectResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "object_identifier",
                "ObjectIdentifier",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identifier that is associated with the object.
    object_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateSchemaRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The name that is associated with the schema. This is unique to each account
    # and in each region.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateSchemaResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "schema_arn",
                "SchemaArn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) that is associated with the schema. For more
    # information, see arns.
    schema_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateTypedLinkFacetRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "schema_arn",
                "SchemaArn",
                TypeInfo(str),
            ),
            (
                "facet",
                "Facet",
                TypeInfo(TypedLinkFacet),
            ),
        ]

    # The Amazon Resource Name (ARN) that is associated with the schema. For more
    # information, see arns.
    schema_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Facet structure that is associated with the typed link facet.
    facet: "TypedLinkFacet" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateTypedLinkFacetResponse(OutputShapeBase):
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
class DeleteDirectoryRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_arn",
                "DirectoryArn",
                TypeInfo(str),
            ),
        ]

    # The ARN of the directory to delete.
    directory_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteDirectoryResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "directory_arn",
                "DirectoryArn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the deleted directory.
    directory_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteFacetRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "schema_arn",
                "SchemaArn",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) that is associated with the Facet. For more
    # information, see arns.
    schema_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the facet to delete.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteFacetResponse(OutputShapeBase):
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
class DeleteObjectRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_arn",
                "DirectoryArn",
                TypeInfo(str),
            ),
            (
                "object_reference",
                "ObjectReference",
                TypeInfo(ObjectReference),
            ),
        ]

    # The Amazon Resource Name (ARN) that is associated with the Directory where
    # the object resides. For more information, see arns.
    directory_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A reference that identifies the object.
    object_reference: "ObjectReference" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


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
class DeleteSchemaRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "schema_arn",
                "SchemaArn",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the development schema. For more
    # information, see arns.
    schema_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteSchemaResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "schema_arn",
                "SchemaArn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The input ARN that is returned as part of the response. For more
    # information, see arns.
    schema_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteTypedLinkFacetRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "schema_arn",
                "SchemaArn",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) that is associated with the schema. For more
    # information, see arns.
    schema_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique name of the typed link facet.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteTypedLinkFacetResponse(OutputShapeBase):
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
class DetachFromIndexRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_arn",
                "DirectoryArn",
                TypeInfo(str),
            ),
            (
                "index_reference",
                "IndexReference",
                TypeInfo(ObjectReference),
            ),
            (
                "target_reference",
                "TargetReference",
                TypeInfo(ObjectReference),
            ),
        ]

    # The Amazon Resource Name (ARN) of the directory the index and object exist
    # in.
    directory_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A reference to the index object.
    index_reference: "ObjectReference" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A reference to the object being detached from the index.
    target_reference: "ObjectReference" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DetachFromIndexResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "detached_object_identifier",
                "DetachedObjectIdentifier",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The `ObjectIdentifier` of the object that was detached from the index.
    detached_object_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DetachObjectRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_arn",
                "DirectoryArn",
                TypeInfo(str),
            ),
            (
                "parent_reference",
                "ParentReference",
                TypeInfo(ObjectReference),
            ),
            (
                "link_name",
                "LinkName",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) that is associated with the Directory where
    # objects reside. For more information, see arns.
    directory_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The parent reference from which the object with the specified link name is
    # detached.
    parent_reference: "ObjectReference" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The link name associated with the object that needs to be detached.
    link_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DetachObjectResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "detached_object_identifier",
                "DetachedObjectIdentifier",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The `ObjectIdentifier` that was detached from the object.
    detached_object_identifier: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DetachPolicyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_arn",
                "DirectoryArn",
                TypeInfo(str),
            ),
            (
                "policy_reference",
                "PolicyReference",
                TypeInfo(ObjectReference),
            ),
            (
                "object_reference",
                "ObjectReference",
                TypeInfo(ObjectReference),
            ),
        ]

    # The Amazon Resource Name (ARN) that is associated with the Directory where
    # both objects reside. For more information, see arns.
    directory_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Reference that identifies the policy object.
    policy_reference: "ObjectReference" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Reference that identifies the object whose policy object will be detached.
    object_reference: "ObjectReference" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DetachPolicyResponse(OutputShapeBase):
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
class DetachTypedLinkRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_arn",
                "DirectoryArn",
                TypeInfo(str),
            ),
            (
                "typed_link_specifier",
                "TypedLinkSpecifier",
                TypeInfo(TypedLinkSpecifier),
            ),
        ]

    # The Amazon Resource Name (ARN) of the directory where you want to detach
    # the typed link.
    directory_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Used to accept a typed link specifier as input.
    typed_link_specifier: "TypedLinkSpecifier" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Directory(ShapeBase):
    """
    Directory structure that includes the directory name and directory ARN.
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
                "directory_arn",
                "DirectoryArn",
                TypeInfo(str),
            ),
            (
                "state",
                "State",
                TypeInfo(typing.Union[str, DirectoryState]),
            ),
            (
                "creation_date_time",
                "CreationDateTime",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The name of the directory.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) that is associated with the directory. For
    # more information, see arns.
    directory_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The state of the directory. Can be either `Enabled`, `Disabled`, or
    # `Deleted`.
    state: typing.Union[str, "DirectoryState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time when the directory was created.
    creation_date_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DirectoryAlreadyExistsException(ShapeBase):
    """
    Indicates that a Directory could not be created due to a naming conflict. Choose
    a different name and try again.
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
class DirectoryDeletedException(ShapeBase):
    """
    A directory that has been deleted and to which access has been attempted. Note:
    The requested resource will eventually cease to exist.
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
class DirectoryNotDisabledException(ShapeBase):
    """
    An operation can only operate on a disabled directory.
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
class DirectoryNotEnabledException(ShapeBase):
    """
    Operations are only permitted on enabled directories.
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


class DirectoryState(str):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"
    DELETED = "DELETED"


@dataclasses.dataclass
class DisableDirectoryRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_arn",
                "DirectoryArn",
                TypeInfo(str),
            ),
        ]

    # The ARN of the directory to disable.
    directory_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DisableDirectoryResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "directory_arn",
                "DirectoryArn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the directory that has been disabled.
    directory_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EnableDirectoryRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_arn",
                "DirectoryArn",
                TypeInfo(str),
            ),
        ]

    # The ARN of the directory to enable.
    directory_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EnableDirectoryResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "directory_arn",
                "DirectoryArn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the enabled directory.
    directory_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Facet(ShapeBase):
    """
    A structure that contains `Name`, `ARN`, `Attributes`, ` Rules`, and
    `ObjectTypes`. See
    [Facets](http://docs.aws.amazon.com/directoryservice/latest/admin-
    guide/whatarefacets.html) for more information.
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
                "object_type",
                "ObjectType",
                TypeInfo(typing.Union[str, ObjectType]),
            ),
            (
                "facet_style",
                "FacetStyle",
                TypeInfo(typing.Union[str, FacetStyle]),
            ),
        ]

    # The name of the Facet.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The object type that is associated with the facet. See
    # CreateFacetRequest$ObjectType for more details.
    object_type: typing.Union[str, "ObjectType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # There are two different styles that you can define on any given facet,
    # `Static` and `Dynamic`. For static facets, all attributes must be defined
    # in the schema. For dynamic facets, attributes can be defined during data
    # plane operations.
    facet_style: typing.Union[str, "FacetStyle"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class FacetAlreadyExistsException(ShapeBase):
    """
    A facet with the same name already exists.
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
class FacetAttribute(ShapeBase):
    """
    An attribute that is associated with the Facet.
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
                "attribute_definition",
                "AttributeDefinition",
                TypeInfo(FacetAttributeDefinition),
            ),
            (
                "attribute_reference",
                "AttributeReference",
                TypeInfo(FacetAttributeReference),
            ),
            (
                "required_behavior",
                "RequiredBehavior",
                TypeInfo(typing.Union[str, RequiredAttributeBehavior]),
            ),
        ]

    # The name of the facet attribute.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A facet attribute consists of either a definition or a reference. This
    # structure contains the attribute definition. See [Attribute
    # References](http://docs.aws.amazon.com/directoryservice/latest/admin-
    # guide/cd_advanced.html#attributereferences) for more information.
    attribute_definition: "FacetAttributeDefinition" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An attribute reference that is associated with the attribute. See
    # [Attribute
    # References](http://docs.aws.amazon.com/directoryservice/latest/admin-
    # guide/cd_advanced.html#attributereferences) for more information.
    attribute_reference: "FacetAttributeReference" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The required behavior of the `FacetAttribute`.
    required_behavior: typing.Union[str, "RequiredAttributeBehavior"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )


@dataclasses.dataclass
class FacetAttributeDefinition(ShapeBase):
    """
    A facet attribute definition. See [Attribute
    References](http://docs.aws.amazon.com/directoryservice/latest/admin-
    guide/cd_advanced.html#attributereferences) for more information.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, FacetAttributeType]),
            ),
            (
                "default_value",
                "DefaultValue",
                TypeInfo(TypedAttributeValue),
            ),
            (
                "is_immutable",
                "IsImmutable",
                TypeInfo(bool),
            ),
            (
                "rules",
                "Rules",
                TypeInfo(typing.Dict[str, Rule]),
            ),
        ]

    # The type of the attribute.
    type: typing.Union[str, "FacetAttributeType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The default value of the attribute (if configured).
    default_value: "TypedAttributeValue" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Whether the attribute is mutable or not.
    is_immutable: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Validation rules attached to the attribute definition.
    rules: typing.Dict[str, "Rule"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class FacetAttributeReference(ShapeBase):
    """
    The facet attribute reference that specifies the attribute definition that
    contains the attribute facet name and attribute name.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "target_facet_name",
                "TargetFacetName",
                TypeInfo(str),
            ),
            (
                "target_attribute_name",
                "TargetAttributeName",
                TypeInfo(str),
            ),
        ]

    # The target facet name that is associated with the facet reference. See
    # [Attribute
    # References](http://docs.aws.amazon.com/directoryservice/latest/admin-
    # guide/cd_advanced.html#attributereferences) for more information.
    target_facet_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The target attribute name that is associated with the facet reference. See
    # [Attribute
    # References](http://docs.aws.amazon.com/directoryservice/latest/admin-
    # guide/cd_advanced.html#attributereferences) for more information.
    target_attribute_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class FacetAttributeType(str):
    STRING = "STRING"
    BINARY = "BINARY"
    BOOLEAN = "BOOLEAN"
    NUMBER = "NUMBER"
    DATETIME = "DATETIME"
    VARIANT = "VARIANT"


@dataclasses.dataclass
class FacetAttributeUpdate(ShapeBase):
    """
    A structure that contains information used to update an attribute.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attribute",
                "Attribute",
                TypeInfo(FacetAttribute),
            ),
            (
                "action",
                "Action",
                TypeInfo(typing.Union[str, UpdateActionType]),
            ),
        ]

    # The attribute to update.
    attribute: "FacetAttribute" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The action to perform when updating the attribute.
    action: typing.Union[str, "UpdateActionType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class FacetInUseException(ShapeBase):
    """
    Occurs when deleting a facet that contains an attribute that is a target to an
    attribute reference in a different facet.
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
class FacetNotFoundException(ShapeBase):
    """
    The specified Facet could not be found.
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


class FacetStyle(str):
    STATIC = "STATIC"
    DYNAMIC = "DYNAMIC"


@dataclasses.dataclass
class FacetValidationException(ShapeBase):
    """
    The Facet that you provided was not well formed or could not be validated with
    the schema.
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
class GetAppliedSchemaVersionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "schema_arn",
                "SchemaArn",
                TypeInfo(str),
            ),
        ]

    # The ARN of the applied schema.
    schema_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetAppliedSchemaVersionResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "applied_schema_arn",
                "AppliedSchemaArn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Current applied schema ARN, including the minor version in use if one was
    # provided.
    applied_schema_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDirectoryRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_arn",
                "DirectoryArn",
                TypeInfo(str),
            ),
        ]

    # The ARN of the directory.
    directory_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDirectoryResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "directory",
                "Directory",
                TypeInfo(Directory),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Metadata about the directory.
    directory: "Directory" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetFacetRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "schema_arn",
                "SchemaArn",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) that is associated with the Facet. For more
    # information, see arns.
    schema_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the facet to retrieve.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetFacetResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "facet",
                "Facet",
                TypeInfo(Facet),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Facet structure that is associated with the facet.
    facet: "Facet" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetLinkAttributesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_arn",
                "DirectoryArn",
                TypeInfo(str),
            ),
            (
                "typed_link_specifier",
                "TypedLinkSpecifier",
                TypeInfo(TypedLinkSpecifier),
            ),
            (
                "attribute_names",
                "AttributeNames",
                TypeInfo(typing.List[str]),
            ),
            (
                "consistency_level",
                "ConsistencyLevel",
                TypeInfo(typing.Union[str, ConsistencyLevel]),
            ),
        ]

    # The Amazon Resource Name (ARN) that is associated with the Directory where
    # the typed link resides. For more information, see arns or [Typed
    # link](http://docs.aws.amazon.com/directoryservice/latest/admin-
    # guide/objectsandlinks.html#typedlink).
    directory_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Allows a typed link specifier to be accepted as input.
    typed_link_specifier: "TypedLinkSpecifier" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of attribute names whose values will be retrieved.
    attribute_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The consistency level at which to retrieve the attributes on a typed link.
    consistency_level: typing.Union[str, "ConsistencyLevel"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )


@dataclasses.dataclass
class GetLinkAttributesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "attributes",
                "Attributes",
                TypeInfo(typing.List[AttributeKeyAndValue]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The attributes that are associated with the typed link.
    attributes: typing.List["AttributeKeyAndValue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetObjectAttributesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_arn",
                "DirectoryArn",
                TypeInfo(str),
            ),
            (
                "object_reference",
                "ObjectReference",
                TypeInfo(ObjectReference),
            ),
            (
                "schema_facet",
                "SchemaFacet",
                TypeInfo(SchemaFacet),
            ),
            (
                "attribute_names",
                "AttributeNames",
                TypeInfo(typing.List[str]),
            ),
            (
                "consistency_level",
                "ConsistencyLevel",
                TypeInfo(typing.Union[str, ConsistencyLevel]),
            ),
        ]

    # The Amazon Resource Name (ARN) that is associated with the Directory where
    # the object resides.
    directory_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Reference that identifies the object whose attributes will be retrieved.
    object_reference: "ObjectReference" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Identifier for the facet whose attributes will be retrieved. See
    # SchemaFacet for details.
    schema_facet: "SchemaFacet" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # List of attribute names whose values will be retrieved.
    attribute_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The consistency level at which to retrieve the attributes on an object.
    consistency_level: typing.Union[str, "ConsistencyLevel"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )


@dataclasses.dataclass
class GetObjectAttributesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "attributes",
                "Attributes",
                TypeInfo(typing.List[AttributeKeyAndValue]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The attributes that are associated with the object.
    attributes: typing.List["AttributeKeyAndValue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetObjectInformationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_arn",
                "DirectoryArn",
                TypeInfo(str),
            ),
            (
                "object_reference",
                "ObjectReference",
                TypeInfo(ObjectReference),
            ),
            (
                "consistency_level",
                "ConsistencyLevel",
                TypeInfo(typing.Union[str, ConsistencyLevel]),
            ),
        ]

    # The ARN of the directory being retrieved.
    directory_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A reference to the object.
    object_reference: "ObjectReference" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The consistency level at which to retrieve the object information.
    consistency_level: typing.Union[str, "ConsistencyLevel"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )


@dataclasses.dataclass
class GetObjectInformationResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "schema_facets",
                "SchemaFacets",
                TypeInfo(typing.List[SchemaFacet]),
            ),
            (
                "object_identifier",
                "ObjectIdentifier",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The facets attached to the specified object. Although the response does not
    # include minor version information, the most recently applied minor version
    # of each Facet is in effect. See GetAppliedSchemaVersion for details.
    schema_facets: typing.List["SchemaFacet"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The `ObjectIdentifier` of the specified object.
    object_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetSchemaAsJsonRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "schema_arn",
                "SchemaArn",
                TypeInfo(str),
            ),
        ]

    # The ARN of the schema to retrieve.
    schema_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetSchemaAsJsonResponse(OutputShapeBase):
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
                "document",
                "Document",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the retrieved schema.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The JSON representation of the schema document.
    document: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetTypedLinkFacetInformationRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "schema_arn",
                "SchemaArn",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) that is associated with the schema. For more
    # information, see arns.
    schema_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique name of the typed link facet.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetTypedLinkFacetInformationResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "identity_attribute_order",
                "IdentityAttributeOrder",
                TypeInfo(typing.List[str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The order of identity attributes for the facet, from most significant to
    # least significant. The ability to filter typed links considers the order
    # that the attributes are defined on the typed link facet. When providing
    # ranges to typed link selection, any inexact ranges must be specified at the
    # end. Any attributes that do not have a range specified are presumed to
    # match the entire range. Filters are interpreted in the order of the
    # attributes on the typed link facet, not the order in which they are
    # supplied to any API calls. For more information about identity attributes,
    # see [Typed link](http://docs.aws.amazon.com/directoryservice/latest/admin-
    # guide/objectsandlinks.html#typedlink).
    identity_attribute_order: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class IncompatibleSchemaException(ShapeBase):
    """
    Indicates a failure occurred while performing a check for backward compatibility
    between the specified schema and the schema that is currently applied to the
    directory.
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
class IndexAttachment(ShapeBase):
    """
    Represents an index and an attached object.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "indexed_attributes",
                "IndexedAttributes",
                TypeInfo(typing.List[AttributeKeyAndValue]),
            ),
            (
                "object_identifier",
                "ObjectIdentifier",
                TypeInfo(str),
            ),
        ]

    # The indexed attribute values.
    indexed_attributes: typing.List["AttributeKeyAndValue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # In response to ListIndex, the `ObjectIdentifier` of the object attached to
    # the index. In response to ListAttachedIndices, the `ObjectIdentifier` of
    # the index attached to the object. This field will always contain the
    # `ObjectIdentifier` of the object on the opposite side of the attachment
    # specified in the query.
    object_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class IndexedAttributeMissingException(ShapeBase):
    """
    An object has been attempted to be attached to an object that does not have the
    appropriate attribute value.
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
class InternalServiceException(ShapeBase):
    """
    Indicates a problem that must be resolved by Amazon Web Services. This might be
    a transient error in which case you can retry your request until it succeeds.
    Otherwise, go to the [AWS Service Health
    Dashboard](http://status.aws.amazon.com/) site to see if there are any
    operational issues with the service.
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
class InvalidArnException(ShapeBase):
    """
    Indicates that the provided ARN value is not valid.
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
class InvalidAttachmentException(ShapeBase):
    """
    Indicates that an attempt to attach an object with the same link name or to
    apply a schema with the same name has occurred. Rename the link or the schema
    and then try again.
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
class InvalidFacetUpdateException(ShapeBase):
    """
    An attempt to modify a Facet resulted in an invalid schema exception.
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
class InvalidNextTokenException(ShapeBase):
    """
    Indicates that the `NextToken` value is not valid.
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
class InvalidRuleException(ShapeBase):
    """
    Occurs when any of the rule parameter keys or values are invalid.
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
class InvalidSchemaDocException(ShapeBase):
    """
    Indicates that the provided `SchemaDoc` value is not valid.
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
class InvalidTaggingRequestException(ShapeBase):
    """
    Can occur for multiple reasons such as when you tag a resource that doesn’t
    exist or if you specify a higher number of tags for a resource than the allowed
    limit. Allowed limit is 50 tags per resource.
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
class LimitExceededException(ShapeBase):
    """
    Indicates that limits are exceeded. See
    [Limits](http://docs.aws.amazon.com/directoryservice/latest/admin-
    guide/limits.html) for more information.
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
class LinkAttributeAction(ShapeBase):
    """
    The action to take on a typed link attribute value. Updates are only supported
    for attributes which don’t contribute to link identity.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attribute_action_type",
                "AttributeActionType",
                TypeInfo(typing.Union[str, UpdateActionType]),
            ),
            (
                "attribute_update_value",
                "AttributeUpdateValue",
                TypeInfo(TypedAttributeValue),
            ),
        ]

    # A type that can be either `UPDATE_OR_CREATE` or `DELETE`.
    attribute_action_type: typing.Union[str, "UpdateActionType"
                                       ] = dataclasses.field(
                                           default=ShapeBase.NOT_SET,
                                       )

    # The value that you want to update to.
    attribute_update_value: "TypedAttributeValue" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class LinkAttributeUpdate(ShapeBase):
    """
    Structure that contains attribute update information.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attribute_key",
                "AttributeKey",
                TypeInfo(AttributeKey),
            ),
            (
                "attribute_action",
                "AttributeAction",
                TypeInfo(LinkAttributeAction),
            ),
        ]

    # The key of the attribute being updated.
    attribute_key: "AttributeKey" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The action to perform as part of the attribute update.
    attribute_action: "LinkAttributeAction" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class LinkNameAlreadyInUseException(ShapeBase):
    """
    Indicates that a link could not be created due to a naming conflict. Choose a
    different name and then try again.
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
class ListAppliedSchemaArnsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_arn",
                "DirectoryArn",
                TypeInfo(str),
            ),
            (
                "schema_arn",
                "SchemaArn",
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

    # The ARN of the directory you are listing.
    directory_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The response for `ListAppliedSchemaArns` when this parameter is used will
    # list all minor version ARNs for a major version.
    schema_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The pagination token.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to retrieve.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListAppliedSchemaArnsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "schema_arns",
                "SchemaArns",
                TypeInfo(typing.List[str]),
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

    # The ARNs of schemas that are applied to the directory.
    schema_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pagination token.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["ListAppliedSchemaArnsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListAttachedIndicesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_arn",
                "DirectoryArn",
                TypeInfo(str),
            ),
            (
                "target_reference",
                "TargetReference",
                TypeInfo(ObjectReference),
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
            (
                "consistency_level",
                "ConsistencyLevel",
                TypeInfo(typing.Union[str, ConsistencyLevel]),
            ),
        ]

    # The ARN of the directory.
    directory_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A reference to the object that has indices attached.
    target_reference: "ObjectReference" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pagination token.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to retrieve.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The consistency level to use for this operation.
    consistency_level: typing.Union[str, "ConsistencyLevel"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )


@dataclasses.dataclass
class ListAttachedIndicesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "index_attachments",
                "IndexAttachments",
                TypeInfo(typing.List[IndexAttachment]),
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

    # The indices attached to the specified object.
    index_attachments: typing.List["IndexAttachment"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pagination token.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["ListAttachedIndicesResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListDevelopmentSchemaArnsRequest(ShapeBase):
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

    # The pagination token.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to retrieve.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListDevelopmentSchemaArnsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "schema_arns",
                "SchemaArns",
                TypeInfo(typing.List[str]),
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

    # The ARNs of retrieved development schemas.
    schema_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pagination token.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["ListDevelopmentSchemaArnsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListDirectoriesRequest(ShapeBase):
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
            (
                "state",
                "state",
                TypeInfo(typing.Union[str, DirectoryState]),
            ),
        ]

    # The pagination token.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to retrieve.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The state of the directories in the list. Can be either Enabled, Disabled,
    # or Deleted.
    state: typing.Union[str, "DirectoryState"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListDirectoriesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "directories",
                "Directories",
                TypeInfo(typing.List[Directory]),
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

    # Lists all directories that are associated with your account in pagination
    # fashion.
    directories: typing.List["Directory"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pagination token.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ListDirectoriesResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListFacetAttributesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "schema_arn",
                "SchemaArn",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
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

    # The ARN of the schema where the facet resides.
    schema_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the facet whose attributes will be retrieved.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The pagination token.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to retrieve.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListFacetAttributesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "attributes",
                "Attributes",
                TypeInfo(typing.List[FacetAttribute]),
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

    # The attributes attached to the facet.
    attributes: typing.List["FacetAttribute"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pagination token.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["ListFacetAttributesResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListFacetNamesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "schema_arn",
                "SchemaArn",
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

    # The Amazon Resource Name (ARN) to retrieve facet names from.
    schema_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The pagination token.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to retrieve.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListFacetNamesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "facet_names",
                "FacetNames",
                TypeInfo(typing.List[str]),
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

    # The names of facets that exist within the schema.
    facet_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pagination token.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ListFacetNamesResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListIncomingTypedLinksRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_arn",
                "DirectoryArn",
                TypeInfo(str),
            ),
            (
                "object_reference",
                "ObjectReference",
                TypeInfo(ObjectReference),
            ),
            (
                "filter_attribute_ranges",
                "FilterAttributeRanges",
                TypeInfo(typing.List[TypedLinkAttributeRange]),
            ),
            (
                "filter_typed_link",
                "FilterTypedLink",
                TypeInfo(TypedLinkSchemaAndFacetName),
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
            (
                "consistency_level",
                "ConsistencyLevel",
                TypeInfo(typing.Union[str, ConsistencyLevel]),
            ),
        ]

    # The Amazon Resource Name (ARN) of the directory where you want to list the
    # typed links.
    directory_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Reference that identifies the object whose attributes will be listed.
    object_reference: "ObjectReference" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Provides range filters for multiple attributes. When providing ranges to
    # typed link selection, any inexact ranges must be specified at the end. Any
    # attributes that do not have a range specified are presumed to match the
    # entire range.
    filter_attribute_ranges: typing.List["TypedLinkAttributeRange"
                                        ] = dataclasses.field(
                                            default=ShapeBase.NOT_SET,
                                        )

    # Filters are interpreted in the order of the attributes on the typed link
    # facet, not the order in which they are supplied to any API calls.
    filter_typed_link: "TypedLinkSchemaAndFacetName" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pagination token.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to retrieve.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The consistency level to execute the request at.
    consistency_level: typing.Union[str, "ConsistencyLevel"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )


@dataclasses.dataclass
class ListIncomingTypedLinksResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "link_specifiers",
                "LinkSpecifiers",
                TypeInfo(typing.List[TypedLinkSpecifier]),
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

    # Returns one or more typed link specifiers as output.
    link_specifiers: typing.List["TypedLinkSpecifier"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pagination token.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListIndexRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_arn",
                "DirectoryArn",
                TypeInfo(str),
            ),
            (
                "index_reference",
                "IndexReference",
                TypeInfo(ObjectReference),
            ),
            (
                "ranges_on_indexed_values",
                "RangesOnIndexedValues",
                TypeInfo(typing.List[ObjectAttributeRange]),
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
                "consistency_level",
                "ConsistencyLevel",
                TypeInfo(typing.Union[str, ConsistencyLevel]),
            ),
        ]

    # The ARN of the directory that the index exists in.
    directory_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The reference to the index to list.
    index_reference: "ObjectReference" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Specifies the ranges of indexed values that you want to query.
    ranges_on_indexed_values: typing.List["ObjectAttributeRange"
                                         ] = dataclasses.field(
                                             default=ShapeBase.NOT_SET,
                                         )

    # The maximum number of objects in a single page to retrieve from the index
    # during a request. For more information, see [AWS Directory Service
    # Limits](http://docs.aws.amazon.com/directoryservice/latest/admin-
    # guide/limits.html#limits_cd).
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The pagination token.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The consistency level to execute the request at.
    consistency_level: typing.Union[str, "ConsistencyLevel"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )


@dataclasses.dataclass
class ListIndexResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "index_attachments",
                "IndexAttachments",
                TypeInfo(typing.List[IndexAttachment]),
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

    # The objects and indexed values attached to the index.
    index_attachments: typing.List["IndexAttachment"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pagination token.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self, ) -> typing.Generator["ListIndexResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListManagedSchemaArnsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "schema_arn",
                "SchemaArn",
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

    # The response for ListManagedSchemaArns. When this parameter is used, all
    # minor version ARNs for a major version are listed.
    schema_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The pagination token.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to retrieve.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListManagedSchemaArnsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "schema_arns",
                "SchemaArns",
                TypeInfo(typing.List[str]),
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

    # The ARNs for all AWS managed schemas.
    schema_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pagination token.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListObjectAttributesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_arn",
                "DirectoryArn",
                TypeInfo(str),
            ),
            (
                "object_reference",
                "ObjectReference",
                TypeInfo(ObjectReference),
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
            (
                "consistency_level",
                "ConsistencyLevel",
                TypeInfo(typing.Union[str, ConsistencyLevel]),
            ),
            (
                "facet_filter",
                "FacetFilter",
                TypeInfo(SchemaFacet),
            ),
        ]

    # The Amazon Resource Name (ARN) that is associated with the Directory where
    # the object resides. For more information, see arns.
    directory_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The reference that identifies the object whose attributes will be listed.
    object_reference: "ObjectReference" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pagination token.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of items to be retrieved in a single call. This is an
    # approximate number.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Represents the manner and timing in which the successful write or update of
    # an object is reflected in a subsequent read operation of that same object.
    consistency_level: typing.Union[str, "ConsistencyLevel"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # Used to filter the list of object attributes that are associated with a
    # certain facet.
    facet_filter: "SchemaFacet" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListObjectAttributesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "attributes",
                "Attributes",
                TypeInfo(typing.List[AttributeKeyAndValue]),
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

    # Attributes map that is associated with the object. `AttributeArn` is the
    # key, and attribute value is the value.
    attributes: typing.List["AttributeKeyAndValue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pagination token.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["ListObjectAttributesResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListObjectChildrenRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_arn",
                "DirectoryArn",
                TypeInfo(str),
            ),
            (
                "object_reference",
                "ObjectReference",
                TypeInfo(ObjectReference),
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
            (
                "consistency_level",
                "ConsistencyLevel",
                TypeInfo(typing.Union[str, ConsistencyLevel]),
            ),
        ]

    # The Amazon Resource Name (ARN) that is associated with the Directory where
    # the object resides. For more information, see arns.
    directory_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The reference that identifies the object for which child objects are being
    # listed.
    object_reference: "ObjectReference" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pagination token.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of items to be retrieved in a single call. This is an
    # approximate number.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Represents the manner and timing in which the successful write or update of
    # an object is reflected in a subsequent read operation of that same object.
    consistency_level: typing.Union[str, "ConsistencyLevel"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )


@dataclasses.dataclass
class ListObjectChildrenResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "children",
                "Children",
                TypeInfo(typing.Dict[str, str]),
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

    # Children structure, which is a map with key as the `LinkName` and
    # `ObjectIdentifier` as the value.
    children: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pagination token.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListObjectParentPathsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_arn",
                "DirectoryArn",
                TypeInfo(str),
            ),
            (
                "object_reference",
                "ObjectReference",
                TypeInfo(ObjectReference),
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

    # The ARN of the directory to which the parent path applies.
    directory_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The reference that identifies the object whose parent paths are listed.
    object_reference: "ObjectReference" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pagination token.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of items to be retrieved in a single call. This is an
    # approximate number.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListObjectParentPathsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "path_to_object_identifiers_list",
                "PathToObjectIdentifiersList",
                TypeInfo(typing.List[PathToObjectIdentifiers]),
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

    # Returns the path to the `ObjectIdentifiers` that are associated with the
    # directory.
    path_to_object_identifiers_list: typing.List["PathToObjectIdentifiers"
                                                ] = dataclasses.field(
                                                    default=ShapeBase.NOT_SET,
                                                )

    # The pagination token.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["ListObjectParentPathsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListObjectParentsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_arn",
                "DirectoryArn",
                TypeInfo(str),
            ),
            (
                "object_reference",
                "ObjectReference",
                TypeInfo(ObjectReference),
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
            (
                "consistency_level",
                "ConsistencyLevel",
                TypeInfo(typing.Union[str, ConsistencyLevel]),
            ),
        ]

    # The Amazon Resource Name (ARN) that is associated with the Directory where
    # the object resides. For more information, see arns.
    directory_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The reference that identifies the object for which parent objects are being
    # listed.
    object_reference: "ObjectReference" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pagination token.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of items to be retrieved in a single call. This is an
    # approximate number.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Represents the manner and timing in which the successful write or update of
    # an object is reflected in a subsequent read operation of that same object.
    consistency_level: typing.Union[str, "ConsistencyLevel"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )


@dataclasses.dataclass
class ListObjectParentsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "parents",
                "Parents",
                TypeInfo(typing.Dict[str, str]),
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

    # The parent structure, which is a map with key as the `ObjectIdentifier` and
    # LinkName as the value.
    parents: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pagination token.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListObjectPoliciesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_arn",
                "DirectoryArn",
                TypeInfo(str),
            ),
            (
                "object_reference",
                "ObjectReference",
                TypeInfo(ObjectReference),
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
            (
                "consistency_level",
                "ConsistencyLevel",
                TypeInfo(typing.Union[str, ConsistencyLevel]),
            ),
        ]

    # The Amazon Resource Name (ARN) that is associated with the Directory where
    # objects reside. For more information, see arns.
    directory_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Reference that identifies the object for which policies will be listed.
    object_reference: "ObjectReference" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pagination token.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of items to be retrieved in a single call. This is an
    # approximate number.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Represents the manner and timing in which the successful write or update of
    # an object is reflected in a subsequent read operation of that same object.
    consistency_level: typing.Union[str, "ConsistencyLevel"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )


@dataclasses.dataclass
class ListObjectPoliciesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "attached_policy_ids",
                "AttachedPolicyIds",
                TypeInfo(typing.List[str]),
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

    # A list of policy `ObjectIdentifiers`, that are attached to the object.
    attached_policy_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pagination token.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["ListObjectPoliciesResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListOutgoingTypedLinksRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_arn",
                "DirectoryArn",
                TypeInfo(str),
            ),
            (
                "object_reference",
                "ObjectReference",
                TypeInfo(ObjectReference),
            ),
            (
                "filter_attribute_ranges",
                "FilterAttributeRanges",
                TypeInfo(typing.List[TypedLinkAttributeRange]),
            ),
            (
                "filter_typed_link",
                "FilterTypedLink",
                TypeInfo(TypedLinkSchemaAndFacetName),
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
            (
                "consistency_level",
                "ConsistencyLevel",
                TypeInfo(typing.Union[str, ConsistencyLevel]),
            ),
        ]

    # The Amazon Resource Name (ARN) of the directory where you want to list the
    # typed links.
    directory_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A reference that identifies the object whose attributes will be listed.
    object_reference: "ObjectReference" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Provides range filters for multiple attributes. When providing ranges to
    # typed link selection, any inexact ranges must be specified at the end. Any
    # attributes that do not have a range specified are presumed to match the
    # entire range.
    filter_attribute_ranges: typing.List["TypedLinkAttributeRange"
                                        ] = dataclasses.field(
                                            default=ShapeBase.NOT_SET,
                                        )

    # Filters are interpreted in the order of the attributes defined on the typed
    # link facet, not the order they are supplied to any API calls.
    filter_typed_link: "TypedLinkSchemaAndFacetName" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pagination token.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to retrieve.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The consistency level to execute the request at.
    consistency_level: typing.Union[str, "ConsistencyLevel"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )


@dataclasses.dataclass
class ListOutgoingTypedLinksResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "typed_link_specifiers",
                "TypedLinkSpecifiers",
                TypeInfo(typing.List[TypedLinkSpecifier]),
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

    # Returns a typed link specifier as output.
    typed_link_specifiers: typing.List["TypedLinkSpecifier"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    # The pagination token.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListPolicyAttachmentsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_arn",
                "DirectoryArn",
                TypeInfo(str),
            ),
            (
                "policy_reference",
                "PolicyReference",
                TypeInfo(ObjectReference),
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
            (
                "consistency_level",
                "ConsistencyLevel",
                TypeInfo(typing.Union[str, ConsistencyLevel]),
            ),
        ]

    # The Amazon Resource Name (ARN) that is associated with the Directory where
    # objects reside. For more information, see arns.
    directory_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The reference that identifies the policy object.
    policy_reference: "ObjectReference" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pagination token.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of items to be retrieved in a single call. This is an
    # approximate number.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Represents the manner and timing in which the successful write or update of
    # an object is reflected in a subsequent read operation of that same object.
    consistency_level: typing.Union[str, "ConsistencyLevel"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )


@dataclasses.dataclass
class ListPolicyAttachmentsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "object_identifiers",
                "ObjectIdentifiers",
                TypeInfo(typing.List[str]),
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

    # A list of `ObjectIdentifiers` to which the policy is attached.
    object_identifiers: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pagination token.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["ListPolicyAttachmentsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListPublishedSchemaArnsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "schema_arn",
                "SchemaArn",
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

    # The response for `ListPublishedSchemaArns` when this parameter is used will
    # list all minor version ARNs for a major version.
    schema_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The pagination token.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to retrieve.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListPublishedSchemaArnsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "schema_arns",
                "SchemaArns",
                TypeInfo(typing.List[str]),
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

    # The ARNs of published schemas.
    schema_arns: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pagination token.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["ListPublishedSchemaArnsResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListTagsForResourceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arn",
                "ResourceArn",
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

    # The Amazon Resource Name (ARN) of the resource. Tagging is only supported
    # for directories.
    resource_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The pagination token. This is for future use. Currently pagination is not
    # supported for tagging.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The `MaxResults` parameter sets the maximum number of results returned in a
    # single page. This is for future use and is not supported currently.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


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
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
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

    # A list of tag key value pairs that are associated with the response.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The token to use to retrieve the next page of results. This value is null
    # when there are no more results to return.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["ListTagsForResourceResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListTypedLinkFacetAttributesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "schema_arn",
                "SchemaArn",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
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

    # The Amazon Resource Name (ARN) that is associated with the schema. For more
    # information, see arns.
    schema_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique name of the typed link facet.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The pagination token.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to retrieve.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTypedLinkFacetAttributesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "attributes",
                "Attributes",
                TypeInfo(typing.List[TypedLinkAttributeDefinition]),
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

    # An ordered set of attributes associate with the typed link.
    attributes: typing.List["TypedLinkAttributeDefinition"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pagination token.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["ListTypedLinkFacetAttributesResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListTypedLinkFacetNamesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "schema_arn",
                "SchemaArn",
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

    # The Amazon Resource Name (ARN) that is associated with the schema. For more
    # information, see arns.
    schema_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The pagination token.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of results to retrieve.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTypedLinkFacetNamesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "facet_names",
                "FacetNames",
                TypeInfo(typing.List[str]),
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

    # The names of typed link facets that exist within the schema.
    facet_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pagination token.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(
        self,
    ) -> typing.Generator["ListTypedLinkFacetNamesResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class LookupPolicyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_arn",
                "DirectoryArn",
                TypeInfo(str),
            ),
            (
                "object_reference",
                "ObjectReference",
                TypeInfo(ObjectReference),
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

    # The Amazon Resource Name (ARN) that is associated with the Directory. For
    # more information, see arns.
    directory_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Reference that identifies the object whose policies will be looked up.
    object_reference: "ObjectReference" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The token to request the next page of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of items to be retrieved in a single call. This is an
    # approximate number.
    max_results: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LookupPolicyResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "policy_to_path_list",
                "PolicyToPathList",
                TypeInfo(typing.List[PolicyToPath]),
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

    # Provides list of path to policies. Policies contain `PolicyId`,
    # `ObjectIdentifier`, and `PolicyType`. For more information, see
    # [Policies](http://docs.aws.amazon.com/directoryservice/latest/admin-
    # guide/cd_key_concepts.html#policies).
    policy_to_path_list: typing.List["PolicyToPath"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The pagination token.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    def paginate(self,
                ) -> typing.Generator["LookupPolicyResponse", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class NotIndexException(ShapeBase):
    """
    Indicates that the requested operation can only operate on index objects.
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
class NotNodeException(ShapeBase):
    """
    Occurs when any invalid operations are performed on an object that is not a
    node, such as calling `ListObjectChildren` for a leaf node object.
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
class NotPolicyException(ShapeBase):
    """
    Indicates that the requested operation can only operate on policy objects.
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
class ObjectAlreadyDetachedException(ShapeBase):
    """
    Indicates that the object is not attached to the index.
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
class ObjectAttributeAction(ShapeBase):
    """
    The action to take on the object attribute.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "object_attribute_action_type",
                "ObjectAttributeActionType",
                TypeInfo(typing.Union[str, UpdateActionType]),
            ),
            (
                "object_attribute_update_value",
                "ObjectAttributeUpdateValue",
                TypeInfo(TypedAttributeValue),
            ),
        ]

    # A type that can be either `Update` or `Delete`.
    object_attribute_action_type: typing.Union[str, "UpdateActionType"
                                              ] = dataclasses.field(
                                                  default=ShapeBase.NOT_SET,
                                              )

    # The value that you want to update to.
    object_attribute_update_value: "TypedAttributeValue" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ObjectAttributeRange(ShapeBase):
    """
    A range of attributes.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attribute_key",
                "AttributeKey",
                TypeInfo(AttributeKey),
            ),
            (
                "range",
                "Range",
                TypeInfo(TypedAttributeValueRange),
            ),
        ]

    # The key of the attribute that the attribute range covers.
    attribute_key: "AttributeKey" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The range of attribute values being selected.
    range: "TypedAttributeValueRange" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ObjectAttributeUpdate(ShapeBase):
    """
    Structure that contains attribute update information.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "object_attribute_key",
                "ObjectAttributeKey",
                TypeInfo(AttributeKey),
            ),
            (
                "object_attribute_action",
                "ObjectAttributeAction",
                TypeInfo(ObjectAttributeAction),
            ),
        ]

    # The key of the attribute being updated.
    object_attribute_key: "AttributeKey" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The action to perform as part of the attribute update.
    object_attribute_action: "ObjectAttributeAction" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ObjectNotDetachedException(ShapeBase):
    """
    Indicates that the requested operation cannot be completed because the object
    has not been detached from the tree.
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
class ObjectReference(ShapeBase):
    """
    The reference that identifies an object.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "selector",
                "Selector",
                TypeInfo(str),
            ),
        ]

    # A path selector supports easy selection of an object by the parent/child
    # links leading to it from the directory root. Use the link names from each
    # parent/child link to construct the path. Path selectors start with a slash
    # (/) and link names are separated by slashes. For more information about
    # paths, see [Accessing
    # Objects](http://docs.aws.amazon.com/directoryservice/latest/admin-
    # guide/objectsandlinks.html#accessingobjects). You can identify an object in
    # one of the following ways:

    #   * _$ObjectIdentifier_ \- An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An object’s identifier is immutable and no two objects will ever share the same object identifier

    #   * _/some/path_ \- Identifies the object based on path

    #   * _#SomeBatchReference_ \- Identifies the object in a batch call
    selector: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class ObjectType(str):
    NODE = "NODE"
    LEAF_NODE = "LEAF_NODE"
    POLICY = "POLICY"
    INDEX = "INDEX"


@dataclasses.dataclass
class PathToObjectIdentifiers(ShapeBase):
    """
    Returns the path to the `ObjectIdentifiers` that is associated with the
    directory.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "path",
                "Path",
                TypeInfo(str),
            ),
            (
                "object_identifiers",
                "ObjectIdentifiers",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The path that is used to identify the object starting from directory root.
    path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Lists `ObjectIdentifiers` starting from directory root to the object in the
    # request.
    object_identifiers: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PolicyAttachment(ShapeBase):
    """
    Contains the `PolicyType`, `PolicyId`, and the `ObjectIdentifier` to which it is
    attached. For more information, see
    [Policies](http://docs.aws.amazon.com/directoryservice/latest/admin-
    guide/cd_key_concepts.html#policies).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_id",
                "PolicyId",
                TypeInfo(str),
            ),
            (
                "object_identifier",
                "ObjectIdentifier",
                TypeInfo(str),
            ),
            (
                "policy_type",
                "PolicyType",
                TypeInfo(str),
            ),
        ]

    # The ID of `PolicyAttachment`.
    policy_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The `ObjectIdentifier` that is associated with `PolicyAttachment`.
    object_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of policy that can be associated with `PolicyAttachment`.
    policy_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PolicyToPath(ShapeBase):
    """
    Used when a regular object exists in a Directory and you want to find all of the
    policies that are associated with that object and the parent to that object.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "path",
                "Path",
                TypeInfo(str),
            ),
            (
                "policies",
                "Policies",
                TypeInfo(typing.List[PolicyAttachment]),
            ),
        ]

    # The path that is referenced from the root.
    path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # List of policy objects.
    policies: typing.List["PolicyAttachment"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PublishSchemaRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "development_schema_arn",
                "DevelopmentSchemaArn",
                TypeInfo(str),
            ),
            (
                "version",
                "Version",
                TypeInfo(str),
            ),
            (
                "minor_version",
                "MinorVersion",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) that is associated with the development
    # schema. For more information, see arns.
    development_schema_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The major version under which the schema will be published. Schemas have
    # both a major and minor version associated with them.
    version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The minor version under which the schema will be published. This parameter
    # is recommended. Schemas have both a major and minor version associated with
    # them.
    minor_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new name under which the schema will be published. If this is not
    # provided, the development schema is considered.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PublishSchemaResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "published_schema_arn",
                "PublishedSchemaArn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN that is associated with the published schema. For more information,
    # see arns.
    published_schema_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutSchemaFromJsonRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "schema_arn",
                "SchemaArn",
                TypeInfo(str),
            ),
            (
                "document",
                "Document",
                TypeInfo(str),
            ),
        ]

    # The ARN of the schema to update.
    schema_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The replacement JSON schema.
    document: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutSchemaFromJsonResponse(OutputShapeBase):
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
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the schema to update.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class RangeMode(str):
    FIRST = "FIRST"
    LAST = "LAST"
    LAST_BEFORE_MISSING_VALUES = "LAST_BEFORE_MISSING_VALUES"
    INCLUSIVE = "INCLUSIVE"
    EXCLUSIVE = "EXCLUSIVE"


@dataclasses.dataclass
class RemoveFacetFromObjectRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_arn",
                "DirectoryArn",
                TypeInfo(str),
            ),
            (
                "schema_facet",
                "SchemaFacet",
                TypeInfo(SchemaFacet),
            ),
            (
                "object_reference",
                "ObjectReference",
                TypeInfo(ObjectReference),
            ),
        ]

    # The ARN of the directory in which the object resides.
    directory_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The facet to remove. See SchemaFacet for details.
    schema_facet: "SchemaFacet" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A reference to the object to remove the facet from.
    object_reference: "ObjectReference" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RemoveFacetFromObjectResponse(OutputShapeBase):
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


class RequiredAttributeBehavior(str):
    REQUIRED_ALWAYS = "REQUIRED_ALWAYS"
    NOT_REQUIRED = "NOT_REQUIRED"


@dataclasses.dataclass
class ResourceNotFoundException(ShapeBase):
    """
    The specified resource could not be found.
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
class RetryableConflictException(ShapeBase):
    """
    Occurs when a conflict with a previous successful write is detected. For
    example, if a write operation occurs on an object and then an attempt is made to
    read the object using “SERIALIZABLE” consistency, this exception may result.
    This generally occurs when the previous write did not have time to propagate to
    the host serving the current request. A retry (with appropriate backoff logic)
    is the recommended response to this exception.
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
class Rule(ShapeBase):
    """
    Contains an Amazon Resource Name (ARN) and parameters that are associated with
    the rule.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "type",
                "Type",
                TypeInfo(typing.Union[str, RuleType]),
            ),
            (
                "parameters",
                "Parameters",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The type of attribute validation rule.
    type: typing.Union[str, "RuleType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The minimum and maximum parameters that are associated with the rule.
    parameters: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class RuleType(str):
    BINARY_LENGTH = "BINARY_LENGTH"
    NUMBER_COMPARISON = "NUMBER_COMPARISON"
    STRING_FROM_SET = "STRING_FROM_SET"
    STRING_LENGTH = "STRING_LENGTH"


@dataclasses.dataclass
class SchemaAlreadyExistsException(ShapeBase):
    """
    Indicates that a schema could not be created due to a naming conflict. Please
    select a different name and then try again.
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
class SchemaAlreadyPublishedException(ShapeBase):
    """
    Indicates that a schema is already published.
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
class SchemaFacet(ShapeBase):
    """
    A facet.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "schema_arn",
                "SchemaArn",
                TypeInfo(str),
            ),
            (
                "facet_name",
                "FacetName",
                TypeInfo(str),
            ),
        ]

    # The ARN of the schema that contains the facet with no minor component. See
    # arns and [In-Place Schema
    # Upgrade](http://docs.aws.amazon.com/directoryservice/latest/admin-
    # guide/inplaceschemaupgrade.html) for a description of when to provide minor
    # versions.
    schema_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the facet.
    facet_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StillContainsLinksException(ShapeBase):
    """
    The object could not be deleted because links still exist. Remove the links and
    then try the operation again.
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
class Tag(ShapeBase):
    """
    The tag structure that contains a tag key and value.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "Key",
                TypeInfo(str),
            ),
            (
                "value",
                "Value",
                TypeInfo(str),
            ),
        ]

    # The key that is associated with the tag.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value that is associated with the tag.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TagResourceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arn",
                "ResourceArn",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # The Amazon Resource Name (ARN) of the resource. Tagging is only supported
    # for directories.
    resource_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of tag key-value pairs.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


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
class TypedAttributeValue(ShapeBase):
    """
    Represents the data for a typed attribute. You can set one, and only one, of the
    elements. Each attribute in an item is a name-value pair. Attributes have a
    single value.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "string_value",
                "StringValue",
                TypeInfo(str),
            ),
            (
                "binary_value",
                "BinaryValue",
                TypeInfo(typing.Any),
            ),
            (
                "boolean_value",
                "BooleanValue",
                TypeInfo(bool),
            ),
            (
                "number_value",
                "NumberValue",
                TypeInfo(str),
            ),
            (
                "datetime_value",
                "DatetimeValue",
                TypeInfo(datetime.datetime),
            ),
        ]

    # A string data value.
    string_value: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A binary data value.
    binary_value: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A Boolean data value.
    boolean_value: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A number data value.
    number_value: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A date and time value.
    datetime_value: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class TypedAttributeValueRange(ShapeBase):
    """
    A range of attribute values. For more information, see [Range
    Filters](http://docs.aws.amazon.com/directoryservice/latest/admin-
    guide/objectsandlinks.html#rangefilters).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "start_mode",
                "StartMode",
                TypeInfo(typing.Union[str, RangeMode]),
            ),
            (
                "end_mode",
                "EndMode",
                TypeInfo(typing.Union[str, RangeMode]),
            ),
            (
                "start_value",
                "StartValue",
                TypeInfo(TypedAttributeValue),
            ),
            (
                "end_value",
                "EndValue",
                TypeInfo(TypedAttributeValue),
            ),
        ]

    # The inclusive or exclusive range start.
    start_mode: typing.Union[str, "RangeMode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The inclusive or exclusive range end.
    end_mode: typing.Union[str, "RangeMode"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The value to start the range at.
    start_value: "TypedAttributeValue" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The attribute value to terminate the range at.
    end_value: "TypedAttributeValue" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class TypedLinkAttributeDefinition(ShapeBase):
    """
    A typed link attribute definition.
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
                TypeInfo(typing.Union[str, FacetAttributeType]),
            ),
            (
                "required_behavior",
                "RequiredBehavior",
                TypeInfo(typing.Union[str, RequiredAttributeBehavior]),
            ),
            (
                "default_value",
                "DefaultValue",
                TypeInfo(TypedAttributeValue),
            ),
            (
                "is_immutable",
                "IsImmutable",
                TypeInfo(bool),
            ),
            (
                "rules",
                "Rules",
                TypeInfo(typing.Dict[str, Rule]),
            ),
        ]

    # The unique name of the typed link attribute.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The type of the attribute.
    type: typing.Union[str, "FacetAttributeType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The required behavior of the `TypedLinkAttributeDefinition`.
    required_behavior: typing.Union[str, "RequiredAttributeBehavior"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # The default value of the attribute (if configured).
    default_value: "TypedAttributeValue" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Whether the attribute is mutable or not.
    is_immutable: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Validation rules that are attached to the attribute definition.
    rules: typing.Dict[str, "Rule"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class TypedLinkAttributeRange(ShapeBase):
    """
    Identifies the range of attributes that are used by a specified filter.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "range",
                "Range",
                TypeInfo(TypedAttributeValueRange),
            ),
            (
                "attribute_name",
                "AttributeName",
                TypeInfo(str),
            ),
        ]

    # The range of attribute values that are being selected.
    range: "TypedAttributeValueRange" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unique name of the typed link attribute.
    attribute_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TypedLinkFacet(ShapeBase):
    """
    Defines the typed links structure and its attributes. To create a typed link
    facet, use the CreateTypedLinkFacet API.
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
                "attributes",
                "Attributes",
                TypeInfo(typing.List[TypedLinkAttributeDefinition]),
            ),
            (
                "identity_attribute_order",
                "IdentityAttributeOrder",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The unique name of the typed link facet.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A set of key-value pairs associated with the typed link. Typed link
    # attributes are used when you have data values that are related to the link
    # itself, and not to one of the two objects being linked. Identity attributes
    # also serve to distinguish the link from others of the same type between the
    # same objects.
    attributes: typing.List["TypedLinkAttributeDefinition"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The set of attributes that distinguish links made from this facet from each
    # other, in the order of significance. Listing typed links can filter on the
    # values of these attributes. See ListOutgoingTypedLinks and
    # ListIncomingTypedLinks for details.
    identity_attribute_order: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class TypedLinkFacetAttributeUpdate(ShapeBase):
    """
    A typed link facet attribute update.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attribute",
                "Attribute",
                TypeInfo(TypedLinkAttributeDefinition),
            ),
            (
                "action",
                "Action",
                TypeInfo(typing.Union[str, UpdateActionType]),
            ),
        ]

    # The attribute to update.
    attribute: "TypedLinkAttributeDefinition" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The action to perform when updating the attribute.
    action: typing.Union[str, "UpdateActionType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class TypedLinkSchemaAndFacetName(ShapeBase):
    """
    Identifies the schema Amazon Resource Name (ARN) and facet name for the typed
    link.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "schema_arn",
                "SchemaArn",
                TypeInfo(str),
            ),
            (
                "typed_link_name",
                "TypedLinkName",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) that is associated with the schema. For more
    # information, see arns.
    schema_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique name of the typed link facet.
    typed_link_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TypedLinkSpecifier(ShapeBase):
    """
    Contains all the information that is used to uniquely identify a typed link. The
    parameters discussed in this topic are used to uniquely specify the typed link
    being operated on. The AttachTypedLink API returns a typed link specifier while
    the DetachTypedLink API accepts one as input. Similarly, the
    ListIncomingTypedLinks and ListOutgoingTypedLinks API operations provide typed
    link specifiers as output. You can also construct a typed link specifier from
    scratch.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "typed_link_facet",
                "TypedLinkFacet",
                TypeInfo(TypedLinkSchemaAndFacetName),
            ),
            (
                "source_object_reference",
                "SourceObjectReference",
                TypeInfo(ObjectReference),
            ),
            (
                "target_object_reference",
                "TargetObjectReference",
                TypeInfo(ObjectReference),
            ),
            (
                "identity_attribute_values",
                "IdentityAttributeValues",
                TypeInfo(typing.List[AttributeNameAndValue]),
            ),
        ]

    # Identifies the typed link facet that is associated with the typed link.
    typed_link_facet: "TypedLinkSchemaAndFacetName" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Identifies the source object that the typed link will attach to.
    source_object_reference: "ObjectReference" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Identifies the target object that the typed link will attach to.
    target_object_reference: "ObjectReference" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Identifies the attribute value to update.
    identity_attribute_values: typing.List["AttributeNameAndValue"
                                          ] = dataclasses.field(
                                              default=ShapeBase.NOT_SET,
                                          )


@dataclasses.dataclass
class UnsupportedIndexTypeException(ShapeBase):
    """
    Indicates that the requested index type is not supported.
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
class UntagResourceRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arn",
                "ResourceArn",
                TypeInfo(str),
            ),
            (
                "tag_keys",
                "TagKeys",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The Amazon Resource Name (ARN) of the resource. Tagging is only supported
    # for directories.
    resource_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Keys of the tag that need to be removed from the resource.
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


class UpdateActionType(str):
    CREATE_OR_UPDATE = "CREATE_OR_UPDATE"
    DELETE = "DELETE"


@dataclasses.dataclass
class UpdateFacetRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "schema_arn",
                "SchemaArn",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "attribute_updates",
                "AttributeUpdates",
                TypeInfo(typing.List[FacetAttributeUpdate]),
            ),
            (
                "object_type",
                "ObjectType",
                TypeInfo(typing.Union[str, ObjectType]),
            ),
        ]

    # The Amazon Resource Name (ARN) that is associated with the Facet. For more
    # information, see arns.
    schema_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the facet.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # List of attributes that need to be updated in a given schema Facet. Each
    # attribute is followed by `AttributeAction`, which specifies the type of
    # update operation to perform.
    attribute_updates: typing.List["FacetAttributeUpdate"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The object type that is associated with the facet. See
    # CreateFacetRequest$ObjectType for more details.
    object_type: typing.Union[str, "ObjectType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateFacetResponse(OutputShapeBase):
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
class UpdateLinkAttributesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_arn",
                "DirectoryArn",
                TypeInfo(str),
            ),
            (
                "typed_link_specifier",
                "TypedLinkSpecifier",
                TypeInfo(TypedLinkSpecifier),
            ),
            (
                "attribute_updates",
                "AttributeUpdates",
                TypeInfo(typing.List[LinkAttributeUpdate]),
            ),
        ]

    # The Amazon Resource Name (ARN) that is associated with the Directory where
    # the updated typed link resides. For more information, see arns or [Typed
    # link](http://docs.aws.amazon.com/directoryservice/latest/admin-
    # guide/objectsandlinks.html#typedlink).
    directory_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Allows a typed link specifier to be accepted as input.
    typed_link_specifier: "TypedLinkSpecifier" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The attributes update structure.
    attribute_updates: typing.List["LinkAttributeUpdate"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateLinkAttributesResponse(OutputShapeBase):
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
class UpdateObjectAttributesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "directory_arn",
                "DirectoryArn",
                TypeInfo(str),
            ),
            (
                "object_reference",
                "ObjectReference",
                TypeInfo(ObjectReference),
            ),
            (
                "attribute_updates",
                "AttributeUpdates",
                TypeInfo(typing.List[ObjectAttributeUpdate]),
            ),
        ]

    # The Amazon Resource Name (ARN) that is associated with the Directory where
    # the object resides. For more information, see arns.
    directory_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The reference that identifies the object.
    object_reference: "ObjectReference" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The attributes update structure.
    attribute_updates: typing.List["ObjectAttributeUpdate"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateObjectAttributesResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "object_identifier",
                "ObjectIdentifier",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The `ObjectIdentifier` of the updated object.
    object_identifier: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateSchemaRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "schema_arn",
                "SchemaArn",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
        ]

    # The Amazon Resource Name (ARN) of the development schema. For more
    # information, see arns.
    schema_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the schema.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateSchemaResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "schema_arn",
                "SchemaArn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN that is associated with the updated schema. For more information,
    # see arns.
    schema_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateTypedLinkFacetRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "schema_arn",
                "SchemaArn",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "attribute_updates",
                "AttributeUpdates",
                TypeInfo(typing.List[TypedLinkFacetAttributeUpdate]),
            ),
            (
                "identity_attribute_order",
                "IdentityAttributeOrder",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The Amazon Resource Name (ARN) that is associated with the schema. For more
    # information, see arns.
    schema_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique name of the typed link facet.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Attributes update structure.
    attribute_updates: typing.List["TypedLinkFacetAttributeUpdate"
                                  ] = dataclasses.field(
                                      default=ShapeBase.NOT_SET,
                                  )

    # The order of identity attributes for the facet, from most significant to
    # least significant. The ability to filter typed links considers the order
    # that the attributes are defined on the typed link facet. When providing
    # ranges to a typed link selection, any inexact ranges must be specified at
    # the end. Any attributes that do not have a range specified are presumed to
    # match the entire range. Filters are interpreted in the order of the
    # attributes on the typed link facet, not the order in which they are
    # supplied to any API calls. For more information about identity attributes,
    # see [Typed link](http://docs.aws.amazon.com/directoryservice/latest/admin-
    # guide/objectsandlinks.html#typedlink).
    identity_attribute_order: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateTypedLinkFacetResponse(OutputShapeBase):
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
class UpgradeAppliedSchemaRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "published_schema_arn",
                "PublishedSchemaArn",
                TypeInfo(str),
            ),
            (
                "directory_arn",
                "DirectoryArn",
                TypeInfo(str),
            ),
            (
                "dry_run",
                "DryRun",
                TypeInfo(bool),
            ),
        ]

    # The revision of the published schema to upgrade the directory to.
    published_schema_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN for the directory to which the upgraded schema will be applied.
    directory_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Used for testing whether the major version schemas are backward compatible
    # or not. If schema compatibility fails, an exception would be thrown else
    # the call would succeed but no changes will be saved. This parameter is
    # optional.
    dry_run: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpgradeAppliedSchemaResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "upgraded_schema_arn",
                "UpgradedSchemaArn",
                TypeInfo(str),
            ),
            (
                "directory_arn",
                "DirectoryArn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the upgraded schema that is returned as part of the response.
    upgraded_schema_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the directory that is returned as part of the response.
    directory_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpgradePublishedSchemaRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "development_schema_arn",
                "DevelopmentSchemaArn",
                TypeInfo(str),
            ),
            (
                "published_schema_arn",
                "PublishedSchemaArn",
                TypeInfo(str),
            ),
            (
                "minor_version",
                "MinorVersion",
                TypeInfo(str),
            ),
            (
                "dry_run",
                "DryRun",
                TypeInfo(bool),
            ),
        ]

    # The ARN of the development schema with the changes used for the upgrade.
    development_schema_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN of the published schema to be upgraded.
    published_schema_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Identifies the minor version of the published schema that will be created.
    # This parameter is NOT optional.
    minor_version: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Used for testing whether the Development schema provided is backwards
    # compatible, or not, with the publish schema provided by the user to be
    # upgraded. If schema compatibility fails, an exception would be thrown else
    # the call would succeed. This parameter is optional and defaults to false.
    dry_run: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpgradePublishedSchemaResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "upgraded_schema_arn",
                "UpgradedSchemaArn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the upgraded schema that is returned as part of the response.
    upgraded_schema_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ValidationException(ShapeBase):
    """
    Indicates that your request is malformed in some manner. See the exception
    message.
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
