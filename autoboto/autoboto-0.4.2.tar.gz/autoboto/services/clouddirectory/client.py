import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("clouddirectory", *args, **kwargs)

    def add_facet_to_object(
        self,
        _request: shapes.AddFacetToObjectRequest = None,
        *,
        directory_arn: str,
        schema_facet: shapes.SchemaFacet,
        object_reference: shapes.ObjectReference,
        object_attribute_list: typing.List[shapes.AttributeKeyAndValue
                                          ] = ShapeBase.NOT_SET,
    ) -> shapes.AddFacetToObjectResponse:
        """
        Adds a new Facet to an object. An object can have more than one facet applied on
        it.
        """
        if _request is None:
            _params = {}
            if directory_arn is not ShapeBase.NOT_SET:
                _params['directory_arn'] = directory_arn
            if schema_facet is not ShapeBase.NOT_SET:
                _params['schema_facet'] = schema_facet
            if object_reference is not ShapeBase.NOT_SET:
                _params['object_reference'] = object_reference
            if object_attribute_list is not ShapeBase.NOT_SET:
                _params['object_attribute_list'] = object_attribute_list
            _request = shapes.AddFacetToObjectRequest(**_params)
        response = self._boto_client.add_facet_to_object(**_request.to_boto())

        return shapes.AddFacetToObjectResponse.from_boto(response)

    def apply_schema(
        self,
        _request: shapes.ApplySchemaRequest = None,
        *,
        published_schema_arn: str,
        directory_arn: str,
    ) -> shapes.ApplySchemaResponse:
        """
        Copies the input published schema, at the specified version, into the Directory
        with the same name and version as that of the published schema.
        """
        if _request is None:
            _params = {}
            if published_schema_arn is not ShapeBase.NOT_SET:
                _params['published_schema_arn'] = published_schema_arn
            if directory_arn is not ShapeBase.NOT_SET:
                _params['directory_arn'] = directory_arn
            _request = shapes.ApplySchemaRequest(**_params)
        response = self._boto_client.apply_schema(**_request.to_boto())

        return shapes.ApplySchemaResponse.from_boto(response)

    def attach_object(
        self,
        _request: shapes.AttachObjectRequest = None,
        *,
        directory_arn: str,
        parent_reference: shapes.ObjectReference,
        child_reference: shapes.ObjectReference,
        link_name: str,
    ) -> shapes.AttachObjectResponse:
        """
        Attaches an existing object to another object. An object can be accessed in two
        ways:

          1. Using the path

          2. Using `ObjectIdentifier`
        """
        if _request is None:
            _params = {}
            if directory_arn is not ShapeBase.NOT_SET:
                _params['directory_arn'] = directory_arn
            if parent_reference is not ShapeBase.NOT_SET:
                _params['parent_reference'] = parent_reference
            if child_reference is not ShapeBase.NOT_SET:
                _params['child_reference'] = child_reference
            if link_name is not ShapeBase.NOT_SET:
                _params['link_name'] = link_name
            _request = shapes.AttachObjectRequest(**_params)
        response = self._boto_client.attach_object(**_request.to_boto())

        return shapes.AttachObjectResponse.from_boto(response)

    def attach_policy(
        self,
        _request: shapes.AttachPolicyRequest = None,
        *,
        directory_arn: str,
        policy_reference: shapes.ObjectReference,
        object_reference: shapes.ObjectReference,
    ) -> shapes.AttachPolicyResponse:
        """
        Attaches a policy object to a regular object. An object can have a limited
        number of attached policies.
        """
        if _request is None:
            _params = {}
            if directory_arn is not ShapeBase.NOT_SET:
                _params['directory_arn'] = directory_arn
            if policy_reference is not ShapeBase.NOT_SET:
                _params['policy_reference'] = policy_reference
            if object_reference is not ShapeBase.NOT_SET:
                _params['object_reference'] = object_reference
            _request = shapes.AttachPolicyRequest(**_params)
        response = self._boto_client.attach_policy(**_request.to_boto())

        return shapes.AttachPolicyResponse.from_boto(response)

    def attach_to_index(
        self,
        _request: shapes.AttachToIndexRequest = None,
        *,
        directory_arn: str,
        index_reference: shapes.ObjectReference,
        target_reference: shapes.ObjectReference,
    ) -> shapes.AttachToIndexResponse:
        """
        Attaches the specified object to the specified index.
        """
        if _request is None:
            _params = {}
            if directory_arn is not ShapeBase.NOT_SET:
                _params['directory_arn'] = directory_arn
            if index_reference is not ShapeBase.NOT_SET:
                _params['index_reference'] = index_reference
            if target_reference is not ShapeBase.NOT_SET:
                _params['target_reference'] = target_reference
            _request = shapes.AttachToIndexRequest(**_params)
        response = self._boto_client.attach_to_index(**_request.to_boto())

        return shapes.AttachToIndexResponse.from_boto(response)

    def attach_typed_link(
        self,
        _request: shapes.AttachTypedLinkRequest = None,
        *,
        directory_arn: str,
        source_object_reference: shapes.ObjectReference,
        target_object_reference: shapes.ObjectReference,
        typed_link_facet: shapes.TypedLinkSchemaAndFacetName,
        attributes: typing.List[shapes.AttributeNameAndValue],
    ) -> shapes.AttachTypedLinkResponse:
        """
        Attaches a typed link to a specified source and target object. For more
        information, see [Typed
        link](http://docs.aws.amazon.com/directoryservice/latest/admin-
        guide/objectsandlinks.html#typedlink).
        """
        if _request is None:
            _params = {}
            if directory_arn is not ShapeBase.NOT_SET:
                _params['directory_arn'] = directory_arn
            if source_object_reference is not ShapeBase.NOT_SET:
                _params['source_object_reference'] = source_object_reference
            if target_object_reference is not ShapeBase.NOT_SET:
                _params['target_object_reference'] = target_object_reference
            if typed_link_facet is not ShapeBase.NOT_SET:
                _params['typed_link_facet'] = typed_link_facet
            if attributes is not ShapeBase.NOT_SET:
                _params['attributes'] = attributes
            _request = shapes.AttachTypedLinkRequest(**_params)
        response = self._boto_client.attach_typed_link(**_request.to_boto())

        return shapes.AttachTypedLinkResponse.from_boto(response)

    def batch_read(
        self,
        _request: shapes.BatchReadRequest = None,
        *,
        directory_arn: str,
        operations: typing.List[shapes.BatchReadOperation],
        consistency_level: typing.Union[str, shapes.
                                        ConsistencyLevel] = ShapeBase.NOT_SET,
    ) -> shapes.BatchReadResponse:
        """
        Performs all the read operations in a batch.
        """
        if _request is None:
            _params = {}
            if directory_arn is not ShapeBase.NOT_SET:
                _params['directory_arn'] = directory_arn
            if operations is not ShapeBase.NOT_SET:
                _params['operations'] = operations
            if consistency_level is not ShapeBase.NOT_SET:
                _params['consistency_level'] = consistency_level
            _request = shapes.BatchReadRequest(**_params)
        response = self._boto_client.batch_read(**_request.to_boto())

        return shapes.BatchReadResponse.from_boto(response)

    def batch_write(
        self,
        _request: shapes.BatchWriteRequest = None,
        *,
        directory_arn: str,
        operations: typing.List[shapes.BatchWriteOperation],
    ) -> shapes.BatchWriteResponse:
        """
        Performs all the write operations in a batch. Either all the operations succeed
        or none.
        """
        if _request is None:
            _params = {}
            if directory_arn is not ShapeBase.NOT_SET:
                _params['directory_arn'] = directory_arn
            if operations is not ShapeBase.NOT_SET:
                _params['operations'] = operations
            _request = shapes.BatchWriteRequest(**_params)
        response = self._boto_client.batch_write(**_request.to_boto())

        return shapes.BatchWriteResponse.from_boto(response)

    def create_directory(
        self,
        _request: shapes.CreateDirectoryRequest = None,
        *,
        name: str,
        schema_arn: str,
    ) -> shapes.CreateDirectoryResponse:
        """
        Creates a Directory by copying the published schema into the directory. A
        directory cannot be created without a schema.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if schema_arn is not ShapeBase.NOT_SET:
                _params['schema_arn'] = schema_arn
            _request = shapes.CreateDirectoryRequest(**_params)
        response = self._boto_client.create_directory(**_request.to_boto())

        return shapes.CreateDirectoryResponse.from_boto(response)

    def create_facet(
        self,
        _request: shapes.CreateFacetRequest = None,
        *,
        schema_arn: str,
        name: str,
        attributes: typing.List[shapes.FacetAttribute] = ShapeBase.NOT_SET,
        object_type: typing.Union[str, shapes.ObjectType] = ShapeBase.NOT_SET,
        facet_style: typing.Union[str, shapes.FacetStyle] = ShapeBase.NOT_SET,
    ) -> shapes.CreateFacetResponse:
        """
        Creates a new Facet in a schema. Facet creation is allowed only in development
        or applied schemas.
        """
        if _request is None:
            _params = {}
            if schema_arn is not ShapeBase.NOT_SET:
                _params['schema_arn'] = schema_arn
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if attributes is not ShapeBase.NOT_SET:
                _params['attributes'] = attributes
            if object_type is not ShapeBase.NOT_SET:
                _params['object_type'] = object_type
            if facet_style is not ShapeBase.NOT_SET:
                _params['facet_style'] = facet_style
            _request = shapes.CreateFacetRequest(**_params)
        response = self._boto_client.create_facet(**_request.to_boto())

        return shapes.CreateFacetResponse.from_boto(response)

    def create_index(
        self,
        _request: shapes.CreateIndexRequest = None,
        *,
        directory_arn: str,
        ordered_indexed_attribute_list: typing.List[shapes.AttributeKey],
        is_unique: bool,
        parent_reference: shapes.ObjectReference = ShapeBase.NOT_SET,
        link_name: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateIndexResponse:
        """
        Creates an index object. See
        [Indexing](http://docs.aws.amazon.com/directoryservice/latest/admin-
        guide/cd_indexing.html) for more information.
        """
        if _request is None:
            _params = {}
            if directory_arn is not ShapeBase.NOT_SET:
                _params['directory_arn'] = directory_arn
            if ordered_indexed_attribute_list is not ShapeBase.NOT_SET:
                _params['ordered_indexed_attribute_list'
                       ] = ordered_indexed_attribute_list
            if is_unique is not ShapeBase.NOT_SET:
                _params['is_unique'] = is_unique
            if parent_reference is not ShapeBase.NOT_SET:
                _params['parent_reference'] = parent_reference
            if link_name is not ShapeBase.NOT_SET:
                _params['link_name'] = link_name
            _request = shapes.CreateIndexRequest(**_params)
        response = self._boto_client.create_index(**_request.to_boto())

        return shapes.CreateIndexResponse.from_boto(response)

    def create_object(
        self,
        _request: shapes.CreateObjectRequest = None,
        *,
        directory_arn: str,
        schema_facets: typing.List[shapes.SchemaFacet],
        object_attribute_list: typing.List[shapes.AttributeKeyAndValue
                                          ] = ShapeBase.NOT_SET,
        parent_reference: shapes.ObjectReference = ShapeBase.NOT_SET,
        link_name: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateObjectResponse:
        """
        Creates an object in a Directory. Additionally attaches the object to a parent,
        if a parent reference and `LinkName` is specified. An object is simply a
        collection of Facet attributes. You can also use this API call to create a
        policy object, if the facet from which you create the object is a policy facet.
        """
        if _request is None:
            _params = {}
            if directory_arn is not ShapeBase.NOT_SET:
                _params['directory_arn'] = directory_arn
            if schema_facets is not ShapeBase.NOT_SET:
                _params['schema_facets'] = schema_facets
            if object_attribute_list is not ShapeBase.NOT_SET:
                _params['object_attribute_list'] = object_attribute_list
            if parent_reference is not ShapeBase.NOT_SET:
                _params['parent_reference'] = parent_reference
            if link_name is not ShapeBase.NOT_SET:
                _params['link_name'] = link_name
            _request = shapes.CreateObjectRequest(**_params)
        response = self._boto_client.create_object(**_request.to_boto())

        return shapes.CreateObjectResponse.from_boto(response)

    def create_schema(
        self,
        _request: shapes.CreateSchemaRequest = None,
        *,
        name: str,
    ) -> shapes.CreateSchemaResponse:
        """
        Creates a new schema in a development state. A schema can exist in three phases:

          * _Development:_ This is a mutable phase of the schema. All new schemas are in the development phase. Once the schema is finalized, it can be published.

          * _Published:_ Published schemas are immutable and have a version associated with them.

          * _Applied:_ Applied schemas are mutable in a way that allows you to add new schema facets. You can also add new, nonrequired attributes to existing schema facets. You can apply only published schemas to directories.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.CreateSchemaRequest(**_params)
        response = self._boto_client.create_schema(**_request.to_boto())

        return shapes.CreateSchemaResponse.from_boto(response)

    def create_typed_link_facet(
        self,
        _request: shapes.CreateTypedLinkFacetRequest = None,
        *,
        schema_arn: str,
        facet: shapes.TypedLinkFacet,
    ) -> shapes.CreateTypedLinkFacetResponse:
        """
        Creates a TypedLinkFacet. For more information, see [Typed
        link](http://docs.aws.amazon.com/directoryservice/latest/admin-
        guide/objectsandlinks.html#typedlink).
        """
        if _request is None:
            _params = {}
            if schema_arn is not ShapeBase.NOT_SET:
                _params['schema_arn'] = schema_arn
            if facet is not ShapeBase.NOT_SET:
                _params['facet'] = facet
            _request = shapes.CreateTypedLinkFacetRequest(**_params)
        response = self._boto_client.create_typed_link_facet(
            **_request.to_boto()
        )

        return shapes.CreateTypedLinkFacetResponse.from_boto(response)

    def delete_directory(
        self,
        _request: shapes.DeleteDirectoryRequest = None,
        *,
        directory_arn: str,
    ) -> shapes.DeleteDirectoryResponse:
        """
        Deletes a directory. Only disabled directories can be deleted. A deleted
        directory cannot be undone. Exercise extreme caution when deleting directories.
        """
        if _request is None:
            _params = {}
            if directory_arn is not ShapeBase.NOT_SET:
                _params['directory_arn'] = directory_arn
            _request = shapes.DeleteDirectoryRequest(**_params)
        response = self._boto_client.delete_directory(**_request.to_boto())

        return shapes.DeleteDirectoryResponse.from_boto(response)

    def delete_facet(
        self,
        _request: shapes.DeleteFacetRequest = None,
        *,
        schema_arn: str,
        name: str,
    ) -> shapes.DeleteFacetResponse:
        """
        Deletes a given Facet. All attributes and Rules that are associated with the
        facet will be deleted. Only development schema facets are allowed deletion.
        """
        if _request is None:
            _params = {}
            if schema_arn is not ShapeBase.NOT_SET:
                _params['schema_arn'] = schema_arn
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.DeleteFacetRequest(**_params)
        response = self._boto_client.delete_facet(**_request.to_boto())

        return shapes.DeleteFacetResponse.from_boto(response)

    def delete_object(
        self,
        _request: shapes.DeleteObjectRequest = None,
        *,
        directory_arn: str,
        object_reference: shapes.ObjectReference,
    ) -> shapes.DeleteObjectResponse:
        """
        Deletes an object and its associated attributes. Only objects with no children
        and no parents can be deleted.
        """
        if _request is None:
            _params = {}
            if directory_arn is not ShapeBase.NOT_SET:
                _params['directory_arn'] = directory_arn
            if object_reference is not ShapeBase.NOT_SET:
                _params['object_reference'] = object_reference
            _request = shapes.DeleteObjectRequest(**_params)
        response = self._boto_client.delete_object(**_request.to_boto())

        return shapes.DeleteObjectResponse.from_boto(response)

    def delete_schema(
        self,
        _request: shapes.DeleteSchemaRequest = None,
        *,
        schema_arn: str,
    ) -> shapes.DeleteSchemaResponse:
        """
        Deletes a given schema. Schemas in a development and published state can only be
        deleted.
        """
        if _request is None:
            _params = {}
            if schema_arn is not ShapeBase.NOT_SET:
                _params['schema_arn'] = schema_arn
            _request = shapes.DeleteSchemaRequest(**_params)
        response = self._boto_client.delete_schema(**_request.to_boto())

        return shapes.DeleteSchemaResponse.from_boto(response)

    def delete_typed_link_facet(
        self,
        _request: shapes.DeleteTypedLinkFacetRequest = None,
        *,
        schema_arn: str,
        name: str,
    ) -> shapes.DeleteTypedLinkFacetResponse:
        """
        Deletes a TypedLinkFacet. For more information, see [Typed
        link](http://docs.aws.amazon.com/directoryservice/latest/admin-
        guide/objectsandlinks.html#typedlink).
        """
        if _request is None:
            _params = {}
            if schema_arn is not ShapeBase.NOT_SET:
                _params['schema_arn'] = schema_arn
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.DeleteTypedLinkFacetRequest(**_params)
        response = self._boto_client.delete_typed_link_facet(
            **_request.to_boto()
        )

        return shapes.DeleteTypedLinkFacetResponse.from_boto(response)

    def detach_from_index(
        self,
        _request: shapes.DetachFromIndexRequest = None,
        *,
        directory_arn: str,
        index_reference: shapes.ObjectReference,
        target_reference: shapes.ObjectReference,
    ) -> shapes.DetachFromIndexResponse:
        """
        Detaches the specified object from the specified index.
        """
        if _request is None:
            _params = {}
            if directory_arn is not ShapeBase.NOT_SET:
                _params['directory_arn'] = directory_arn
            if index_reference is not ShapeBase.NOT_SET:
                _params['index_reference'] = index_reference
            if target_reference is not ShapeBase.NOT_SET:
                _params['target_reference'] = target_reference
            _request = shapes.DetachFromIndexRequest(**_params)
        response = self._boto_client.detach_from_index(**_request.to_boto())

        return shapes.DetachFromIndexResponse.from_boto(response)

    def detach_object(
        self,
        _request: shapes.DetachObjectRequest = None,
        *,
        directory_arn: str,
        parent_reference: shapes.ObjectReference,
        link_name: str,
    ) -> shapes.DetachObjectResponse:
        """
        Detaches a given object from the parent object. The object that is to be
        detached from the parent is specified by the link name.
        """
        if _request is None:
            _params = {}
            if directory_arn is not ShapeBase.NOT_SET:
                _params['directory_arn'] = directory_arn
            if parent_reference is not ShapeBase.NOT_SET:
                _params['parent_reference'] = parent_reference
            if link_name is not ShapeBase.NOT_SET:
                _params['link_name'] = link_name
            _request = shapes.DetachObjectRequest(**_params)
        response = self._boto_client.detach_object(**_request.to_boto())

        return shapes.DetachObjectResponse.from_boto(response)

    def detach_policy(
        self,
        _request: shapes.DetachPolicyRequest = None,
        *,
        directory_arn: str,
        policy_reference: shapes.ObjectReference,
        object_reference: shapes.ObjectReference,
    ) -> shapes.DetachPolicyResponse:
        """
        Detaches a policy from an object.
        """
        if _request is None:
            _params = {}
            if directory_arn is not ShapeBase.NOT_SET:
                _params['directory_arn'] = directory_arn
            if policy_reference is not ShapeBase.NOT_SET:
                _params['policy_reference'] = policy_reference
            if object_reference is not ShapeBase.NOT_SET:
                _params['object_reference'] = object_reference
            _request = shapes.DetachPolicyRequest(**_params)
        response = self._boto_client.detach_policy(**_request.to_boto())

        return shapes.DetachPolicyResponse.from_boto(response)

    def detach_typed_link(
        self,
        _request: shapes.DetachTypedLinkRequest = None,
        *,
        directory_arn: str,
        typed_link_specifier: shapes.TypedLinkSpecifier,
    ) -> None:
        """
        Detaches a typed link from a specified source and target object. For more
        information, see [Typed
        link](http://docs.aws.amazon.com/directoryservice/latest/admin-
        guide/objectsandlinks.html#typedlink).
        """
        if _request is None:
            _params = {}
            if directory_arn is not ShapeBase.NOT_SET:
                _params['directory_arn'] = directory_arn
            if typed_link_specifier is not ShapeBase.NOT_SET:
                _params['typed_link_specifier'] = typed_link_specifier
            _request = shapes.DetachTypedLinkRequest(**_params)
        response = self._boto_client.detach_typed_link(**_request.to_boto())

    def disable_directory(
        self,
        _request: shapes.DisableDirectoryRequest = None,
        *,
        directory_arn: str,
    ) -> shapes.DisableDirectoryResponse:
        """
        Disables the specified directory. Disabled directories cannot be read or written
        to. Only enabled directories can be disabled. Disabled directories may be
        reenabled.
        """
        if _request is None:
            _params = {}
            if directory_arn is not ShapeBase.NOT_SET:
                _params['directory_arn'] = directory_arn
            _request = shapes.DisableDirectoryRequest(**_params)
        response = self._boto_client.disable_directory(**_request.to_boto())

        return shapes.DisableDirectoryResponse.from_boto(response)

    def enable_directory(
        self,
        _request: shapes.EnableDirectoryRequest = None,
        *,
        directory_arn: str,
    ) -> shapes.EnableDirectoryResponse:
        """
        Enables the specified directory. Only disabled directories can be enabled. Once
        enabled, the directory can then be read and written to.
        """
        if _request is None:
            _params = {}
            if directory_arn is not ShapeBase.NOT_SET:
                _params['directory_arn'] = directory_arn
            _request = shapes.EnableDirectoryRequest(**_params)
        response = self._boto_client.enable_directory(**_request.to_boto())

        return shapes.EnableDirectoryResponse.from_boto(response)

    def get_applied_schema_version(
        self,
        _request: shapes.GetAppliedSchemaVersionRequest = None,
        *,
        schema_arn: str,
    ) -> shapes.GetAppliedSchemaVersionResponse:
        """
        Returns current applied schema version ARN, including the minor version in use.
        """
        if _request is None:
            _params = {}
            if schema_arn is not ShapeBase.NOT_SET:
                _params['schema_arn'] = schema_arn
            _request = shapes.GetAppliedSchemaVersionRequest(**_params)
        response = self._boto_client.get_applied_schema_version(
            **_request.to_boto()
        )

        return shapes.GetAppliedSchemaVersionResponse.from_boto(response)

    def get_directory(
        self,
        _request: shapes.GetDirectoryRequest = None,
        *,
        directory_arn: str,
    ) -> shapes.GetDirectoryResponse:
        """
        Retrieves metadata about a directory.
        """
        if _request is None:
            _params = {}
            if directory_arn is not ShapeBase.NOT_SET:
                _params['directory_arn'] = directory_arn
            _request = shapes.GetDirectoryRequest(**_params)
        response = self._boto_client.get_directory(**_request.to_boto())

        return shapes.GetDirectoryResponse.from_boto(response)

    def get_facet(
        self,
        _request: shapes.GetFacetRequest = None,
        *,
        schema_arn: str,
        name: str,
    ) -> shapes.GetFacetResponse:
        """
        Gets details of the Facet, such as facet name, attributes, Rules, or
        `ObjectType`. You can call this on all kinds of schema facets -- published,
        development, or applied.
        """
        if _request is None:
            _params = {}
            if schema_arn is not ShapeBase.NOT_SET:
                _params['schema_arn'] = schema_arn
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.GetFacetRequest(**_params)
        response = self._boto_client.get_facet(**_request.to_boto())

        return shapes.GetFacetResponse.from_boto(response)

    def get_link_attributes(
        self,
        _request: shapes.GetLinkAttributesRequest = None,
        *,
        directory_arn: str,
        typed_link_specifier: shapes.TypedLinkSpecifier,
        attribute_names: typing.List[str],
        consistency_level: typing.Union[str, shapes.
                                        ConsistencyLevel] = ShapeBase.NOT_SET,
    ) -> shapes.GetLinkAttributesResponse:
        """
        Retrieves attributes that are associated with a typed link.
        """
        if _request is None:
            _params = {}
            if directory_arn is not ShapeBase.NOT_SET:
                _params['directory_arn'] = directory_arn
            if typed_link_specifier is not ShapeBase.NOT_SET:
                _params['typed_link_specifier'] = typed_link_specifier
            if attribute_names is not ShapeBase.NOT_SET:
                _params['attribute_names'] = attribute_names
            if consistency_level is not ShapeBase.NOT_SET:
                _params['consistency_level'] = consistency_level
            _request = shapes.GetLinkAttributesRequest(**_params)
        response = self._boto_client.get_link_attributes(**_request.to_boto())

        return shapes.GetLinkAttributesResponse.from_boto(response)

    def get_object_attributes(
        self,
        _request: shapes.GetObjectAttributesRequest = None,
        *,
        directory_arn: str,
        object_reference: shapes.ObjectReference,
        schema_facet: shapes.SchemaFacet,
        attribute_names: typing.List[str],
        consistency_level: typing.Union[str, shapes.
                                        ConsistencyLevel] = ShapeBase.NOT_SET,
    ) -> shapes.GetObjectAttributesResponse:
        """
        Retrieves attributes within a facet that are associated with an object.
        """
        if _request is None:
            _params = {}
            if directory_arn is not ShapeBase.NOT_SET:
                _params['directory_arn'] = directory_arn
            if object_reference is not ShapeBase.NOT_SET:
                _params['object_reference'] = object_reference
            if schema_facet is not ShapeBase.NOT_SET:
                _params['schema_facet'] = schema_facet
            if attribute_names is not ShapeBase.NOT_SET:
                _params['attribute_names'] = attribute_names
            if consistency_level is not ShapeBase.NOT_SET:
                _params['consistency_level'] = consistency_level
            _request = shapes.GetObjectAttributesRequest(**_params)
        response = self._boto_client.get_object_attributes(**_request.to_boto())

        return shapes.GetObjectAttributesResponse.from_boto(response)

    def get_object_information(
        self,
        _request: shapes.GetObjectInformationRequest = None,
        *,
        directory_arn: str,
        object_reference: shapes.ObjectReference,
        consistency_level: typing.Union[str, shapes.
                                        ConsistencyLevel] = ShapeBase.NOT_SET,
    ) -> shapes.GetObjectInformationResponse:
        """
        Retrieves metadata about an object.
        """
        if _request is None:
            _params = {}
            if directory_arn is not ShapeBase.NOT_SET:
                _params['directory_arn'] = directory_arn
            if object_reference is not ShapeBase.NOT_SET:
                _params['object_reference'] = object_reference
            if consistency_level is not ShapeBase.NOT_SET:
                _params['consistency_level'] = consistency_level
            _request = shapes.GetObjectInformationRequest(**_params)
        response = self._boto_client.get_object_information(
            **_request.to_boto()
        )

        return shapes.GetObjectInformationResponse.from_boto(response)

    def get_schema_as_json(
        self,
        _request: shapes.GetSchemaAsJsonRequest = None,
        *,
        schema_arn: str,
    ) -> shapes.GetSchemaAsJsonResponse:
        """
        Retrieves a JSON representation of the schema. See [JSON Schema
        Format](http://docs.aws.amazon.com/directoryservice/latest/admin-
        guide/cd_schemas.html#jsonformat) for more information.
        """
        if _request is None:
            _params = {}
            if schema_arn is not ShapeBase.NOT_SET:
                _params['schema_arn'] = schema_arn
            _request = shapes.GetSchemaAsJsonRequest(**_params)
        response = self._boto_client.get_schema_as_json(**_request.to_boto())

        return shapes.GetSchemaAsJsonResponse.from_boto(response)

    def get_typed_link_facet_information(
        self,
        _request: shapes.GetTypedLinkFacetInformationRequest = None,
        *,
        schema_arn: str,
        name: str,
    ) -> shapes.GetTypedLinkFacetInformationResponse:
        """
        Returns the identity attribute order for a specific TypedLinkFacet. For more
        information, see [Typed
        link](http://docs.aws.amazon.com/directoryservice/latest/admin-
        guide/objectsandlinks.html#typedlink).
        """
        if _request is None:
            _params = {}
            if schema_arn is not ShapeBase.NOT_SET:
                _params['schema_arn'] = schema_arn
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.GetTypedLinkFacetInformationRequest(**_params)
        response = self._boto_client.get_typed_link_facet_information(
            **_request.to_boto()
        )

        return shapes.GetTypedLinkFacetInformationResponse.from_boto(response)

    def list_applied_schema_arns(
        self,
        _request: shapes.ListAppliedSchemaArnsRequest = None,
        *,
        directory_arn: str,
        schema_arn: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListAppliedSchemaArnsResponse:
        """
        Lists schema major versions applied to a directory. If `SchemaArn` is provided,
        lists the minor version.
        """
        if _request is None:
            _params = {}
            if directory_arn is not ShapeBase.NOT_SET:
                _params['directory_arn'] = directory_arn
            if schema_arn is not ShapeBase.NOT_SET:
                _params['schema_arn'] = schema_arn
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListAppliedSchemaArnsRequest(**_params)
        paginator = self.get_paginator("list_applied_schema_arns").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListAppliedSchemaArnsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListAppliedSchemaArnsResponse.from_boto(response)

    def list_attached_indices(
        self,
        _request: shapes.ListAttachedIndicesRequest = None,
        *,
        directory_arn: str,
        target_reference: shapes.ObjectReference,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        consistency_level: typing.Union[str, shapes.
                                        ConsistencyLevel] = ShapeBase.NOT_SET,
    ) -> shapes.ListAttachedIndicesResponse:
        """
        Lists indices attached to the specified object.
        """
        if _request is None:
            _params = {}
            if directory_arn is not ShapeBase.NOT_SET:
                _params['directory_arn'] = directory_arn
            if target_reference is not ShapeBase.NOT_SET:
                _params['target_reference'] = target_reference
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if consistency_level is not ShapeBase.NOT_SET:
                _params['consistency_level'] = consistency_level
            _request = shapes.ListAttachedIndicesRequest(**_params)
        paginator = self.get_paginator("list_attached_indices").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListAttachedIndicesResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListAttachedIndicesResponse.from_boto(response)

    def list_development_schema_arns(
        self,
        _request: shapes.ListDevelopmentSchemaArnsRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListDevelopmentSchemaArnsResponse:
        """
        Retrieves each Amazon Resource Name (ARN) of schemas in the development state.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListDevelopmentSchemaArnsRequest(**_params)
        paginator = self.get_paginator("list_development_schema_arns").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListDevelopmentSchemaArnsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListDevelopmentSchemaArnsResponse.from_boto(response)

    def list_directories(
        self,
        _request: shapes.ListDirectoriesRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        state: typing.Union[str, shapes.DirectoryState] = ShapeBase.NOT_SET,
    ) -> shapes.ListDirectoriesResponse:
        """
        Lists directories created within an account.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if state is not ShapeBase.NOT_SET:
                _params['state'] = state
            _request = shapes.ListDirectoriesRequest(**_params)
        paginator = self.get_paginator("list_directories").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListDirectoriesResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListDirectoriesResponse.from_boto(response)

    def list_facet_attributes(
        self,
        _request: shapes.ListFacetAttributesRequest = None,
        *,
        schema_arn: str,
        name: str,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListFacetAttributesResponse:
        """
        Retrieves attributes attached to the facet.
        """
        if _request is None:
            _params = {}
            if schema_arn is not ShapeBase.NOT_SET:
                _params['schema_arn'] = schema_arn
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListFacetAttributesRequest(**_params)
        paginator = self.get_paginator("list_facet_attributes").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListFacetAttributesResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListFacetAttributesResponse.from_boto(response)

    def list_facet_names(
        self,
        _request: shapes.ListFacetNamesRequest = None,
        *,
        schema_arn: str,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListFacetNamesResponse:
        """
        Retrieves the names of facets that exist in a schema.
        """
        if _request is None:
            _params = {}
            if schema_arn is not ShapeBase.NOT_SET:
                _params['schema_arn'] = schema_arn
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListFacetNamesRequest(**_params)
        paginator = self.get_paginator("list_facet_names").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListFacetNamesResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListFacetNamesResponse.from_boto(response)

    def list_incoming_typed_links(
        self,
        _request: shapes.ListIncomingTypedLinksRequest = None,
        *,
        directory_arn: str,
        object_reference: shapes.ObjectReference,
        filter_attribute_ranges: typing.List[shapes.TypedLinkAttributeRange
                                            ] = ShapeBase.NOT_SET,
        filter_typed_link: shapes.TypedLinkSchemaAndFacetName = ShapeBase.
        NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        consistency_level: typing.Union[str, shapes.
                                        ConsistencyLevel] = ShapeBase.NOT_SET,
    ) -> shapes.ListIncomingTypedLinksResponse:
        """
        Returns a paginated list of all the incoming TypedLinkSpecifier information for
        an object. It also supports filtering by typed link facet and identity
        attributes. For more information, see [Typed
        link](http://docs.aws.amazon.com/directoryservice/latest/admin-
        guide/objectsandlinks.html#typedlink).
        """
        if _request is None:
            _params = {}
            if directory_arn is not ShapeBase.NOT_SET:
                _params['directory_arn'] = directory_arn
            if object_reference is not ShapeBase.NOT_SET:
                _params['object_reference'] = object_reference
            if filter_attribute_ranges is not ShapeBase.NOT_SET:
                _params['filter_attribute_ranges'] = filter_attribute_ranges
            if filter_typed_link is not ShapeBase.NOT_SET:
                _params['filter_typed_link'] = filter_typed_link
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if consistency_level is not ShapeBase.NOT_SET:
                _params['consistency_level'] = consistency_level
            _request = shapes.ListIncomingTypedLinksRequest(**_params)
        response = self._boto_client.list_incoming_typed_links(
            **_request.to_boto()
        )

        return shapes.ListIncomingTypedLinksResponse.from_boto(response)

    def list_index(
        self,
        _request: shapes.ListIndexRequest = None,
        *,
        directory_arn: str,
        index_reference: shapes.ObjectReference,
        ranges_on_indexed_values: typing.List[shapes.ObjectAttributeRange
                                             ] = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        consistency_level: typing.Union[str, shapes.
                                        ConsistencyLevel] = ShapeBase.NOT_SET,
    ) -> shapes.ListIndexResponse:
        """
        Lists objects attached to the specified index.
        """
        if _request is None:
            _params = {}
            if directory_arn is not ShapeBase.NOT_SET:
                _params['directory_arn'] = directory_arn
            if index_reference is not ShapeBase.NOT_SET:
                _params['index_reference'] = index_reference
            if ranges_on_indexed_values is not ShapeBase.NOT_SET:
                _params['ranges_on_indexed_values'] = ranges_on_indexed_values
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if consistency_level is not ShapeBase.NOT_SET:
                _params['consistency_level'] = consistency_level
            _request = shapes.ListIndexRequest(**_params)
        paginator = self.get_paginator("list_index").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListIndexResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListIndexResponse.from_boto(response)

    def list_managed_schema_arns(
        self,
        _request: shapes.ListManagedSchemaArnsRequest = None,
        *,
        schema_arn: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListManagedSchemaArnsResponse:
        """
        Lists the major version families of each managed schema. If a major version ARN
        is provided as SchemaArn, the minor version revisions in that family are listed
        instead.
        """
        if _request is None:
            _params = {}
            if schema_arn is not ShapeBase.NOT_SET:
                _params['schema_arn'] = schema_arn
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListManagedSchemaArnsRequest(**_params)
        response = self._boto_client.list_managed_schema_arns(
            **_request.to_boto()
        )

        return shapes.ListManagedSchemaArnsResponse.from_boto(response)

    def list_object_attributes(
        self,
        _request: shapes.ListObjectAttributesRequest = None,
        *,
        directory_arn: str,
        object_reference: shapes.ObjectReference,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        consistency_level: typing.Union[str, shapes.
                                        ConsistencyLevel] = ShapeBase.NOT_SET,
        facet_filter: shapes.SchemaFacet = ShapeBase.NOT_SET,
    ) -> shapes.ListObjectAttributesResponse:
        """
        Lists all attributes that are associated with an object.
        """
        if _request is None:
            _params = {}
            if directory_arn is not ShapeBase.NOT_SET:
                _params['directory_arn'] = directory_arn
            if object_reference is not ShapeBase.NOT_SET:
                _params['object_reference'] = object_reference
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if consistency_level is not ShapeBase.NOT_SET:
                _params['consistency_level'] = consistency_level
            if facet_filter is not ShapeBase.NOT_SET:
                _params['facet_filter'] = facet_filter
            _request = shapes.ListObjectAttributesRequest(**_params)
        paginator = self.get_paginator("list_object_attributes").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListObjectAttributesResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListObjectAttributesResponse.from_boto(response)

    def list_object_children(
        self,
        _request: shapes.ListObjectChildrenRequest = None,
        *,
        directory_arn: str,
        object_reference: shapes.ObjectReference,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        consistency_level: typing.Union[str, shapes.
                                        ConsistencyLevel] = ShapeBase.NOT_SET,
    ) -> shapes.ListObjectChildrenResponse:
        """
        Returns a paginated list of child objects that are associated with a given
        object.
        """
        if _request is None:
            _params = {}
            if directory_arn is not ShapeBase.NOT_SET:
                _params['directory_arn'] = directory_arn
            if object_reference is not ShapeBase.NOT_SET:
                _params['object_reference'] = object_reference
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if consistency_level is not ShapeBase.NOT_SET:
                _params['consistency_level'] = consistency_level
            _request = shapes.ListObjectChildrenRequest(**_params)
        response = self._boto_client.list_object_children(**_request.to_boto())

        return shapes.ListObjectChildrenResponse.from_boto(response)

    def list_object_parent_paths(
        self,
        _request: shapes.ListObjectParentPathsRequest = None,
        *,
        directory_arn: str,
        object_reference: shapes.ObjectReference,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListObjectParentPathsResponse:
        """
        Retrieves all available parent paths for any object type such as node, leaf
        node, policy node, and index node objects. For more information about objects,
        see [Directory
        Structure](http://docs.aws.amazon.com/directoryservice/latest/admin-
        guide/cd_key_concepts.html#dirstructure).

        Use this API to evaluate all parents for an object. The call returns all objects
        from the root of the directory up to the requested object. The API returns the
        number of paths based on user-defined `MaxResults`, in case there are multiple
        paths to the parent. The order of the paths and nodes returned is consistent
        among multiple API calls unless the objects are deleted or moved. Paths not
        leading to the directory root are ignored from the target object.
        """
        if _request is None:
            _params = {}
            if directory_arn is not ShapeBase.NOT_SET:
                _params['directory_arn'] = directory_arn
            if object_reference is not ShapeBase.NOT_SET:
                _params['object_reference'] = object_reference
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListObjectParentPathsRequest(**_params)
        paginator = self.get_paginator("list_object_parent_paths").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListObjectParentPathsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListObjectParentPathsResponse.from_boto(response)

    def list_object_parents(
        self,
        _request: shapes.ListObjectParentsRequest = None,
        *,
        directory_arn: str,
        object_reference: shapes.ObjectReference,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        consistency_level: typing.Union[str, shapes.
                                        ConsistencyLevel] = ShapeBase.NOT_SET,
    ) -> shapes.ListObjectParentsResponse:
        """
        Lists parent objects that are associated with a given object in pagination
        fashion.
        """
        if _request is None:
            _params = {}
            if directory_arn is not ShapeBase.NOT_SET:
                _params['directory_arn'] = directory_arn
            if object_reference is not ShapeBase.NOT_SET:
                _params['object_reference'] = object_reference
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if consistency_level is not ShapeBase.NOT_SET:
                _params['consistency_level'] = consistency_level
            _request = shapes.ListObjectParentsRequest(**_params)
        response = self._boto_client.list_object_parents(**_request.to_boto())

        return shapes.ListObjectParentsResponse.from_boto(response)

    def list_object_policies(
        self,
        _request: shapes.ListObjectPoliciesRequest = None,
        *,
        directory_arn: str,
        object_reference: shapes.ObjectReference,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        consistency_level: typing.Union[str, shapes.
                                        ConsistencyLevel] = ShapeBase.NOT_SET,
    ) -> shapes.ListObjectPoliciesResponse:
        """
        Returns policies attached to an object in pagination fashion.
        """
        if _request is None:
            _params = {}
            if directory_arn is not ShapeBase.NOT_SET:
                _params['directory_arn'] = directory_arn
            if object_reference is not ShapeBase.NOT_SET:
                _params['object_reference'] = object_reference
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if consistency_level is not ShapeBase.NOT_SET:
                _params['consistency_level'] = consistency_level
            _request = shapes.ListObjectPoliciesRequest(**_params)
        paginator = self.get_paginator("list_object_policies").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListObjectPoliciesResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListObjectPoliciesResponse.from_boto(response)

    def list_outgoing_typed_links(
        self,
        _request: shapes.ListOutgoingTypedLinksRequest = None,
        *,
        directory_arn: str,
        object_reference: shapes.ObjectReference,
        filter_attribute_ranges: typing.List[shapes.TypedLinkAttributeRange
                                            ] = ShapeBase.NOT_SET,
        filter_typed_link: shapes.TypedLinkSchemaAndFacetName = ShapeBase.
        NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        consistency_level: typing.Union[str, shapes.
                                        ConsistencyLevel] = ShapeBase.NOT_SET,
    ) -> shapes.ListOutgoingTypedLinksResponse:
        """
        Returns a paginated list of all the outgoing TypedLinkSpecifier information for
        an object. It also supports filtering by typed link facet and identity
        attributes. For more information, see [Typed
        link](http://docs.aws.amazon.com/directoryservice/latest/admin-
        guide/objectsandlinks.html#typedlink).
        """
        if _request is None:
            _params = {}
            if directory_arn is not ShapeBase.NOT_SET:
                _params['directory_arn'] = directory_arn
            if object_reference is not ShapeBase.NOT_SET:
                _params['object_reference'] = object_reference
            if filter_attribute_ranges is not ShapeBase.NOT_SET:
                _params['filter_attribute_ranges'] = filter_attribute_ranges
            if filter_typed_link is not ShapeBase.NOT_SET:
                _params['filter_typed_link'] = filter_typed_link
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if consistency_level is not ShapeBase.NOT_SET:
                _params['consistency_level'] = consistency_level
            _request = shapes.ListOutgoingTypedLinksRequest(**_params)
        response = self._boto_client.list_outgoing_typed_links(
            **_request.to_boto()
        )

        return shapes.ListOutgoingTypedLinksResponse.from_boto(response)

    def list_policy_attachments(
        self,
        _request: shapes.ListPolicyAttachmentsRequest = None,
        *,
        directory_arn: str,
        policy_reference: shapes.ObjectReference,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
        consistency_level: typing.Union[str, shapes.
                                        ConsistencyLevel] = ShapeBase.NOT_SET,
    ) -> shapes.ListPolicyAttachmentsResponse:
        """
        Returns all of the `ObjectIdentifiers` to which a given policy is attached.
        """
        if _request is None:
            _params = {}
            if directory_arn is not ShapeBase.NOT_SET:
                _params['directory_arn'] = directory_arn
            if policy_reference is not ShapeBase.NOT_SET:
                _params['policy_reference'] = policy_reference
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if consistency_level is not ShapeBase.NOT_SET:
                _params['consistency_level'] = consistency_level
            _request = shapes.ListPolicyAttachmentsRequest(**_params)
        paginator = self.get_paginator("list_policy_attachments").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListPolicyAttachmentsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListPolicyAttachmentsResponse.from_boto(response)

    def list_published_schema_arns(
        self,
        _request: shapes.ListPublishedSchemaArnsRequest = None,
        *,
        schema_arn: str = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListPublishedSchemaArnsResponse:
        """
        Lists the major version families of each published schema. If a major version
        ARN is provided as `SchemaArn`, the minor version revisions in that family are
        listed instead.
        """
        if _request is None:
            _params = {}
            if schema_arn is not ShapeBase.NOT_SET:
                _params['schema_arn'] = schema_arn
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListPublishedSchemaArnsRequest(**_params)
        paginator = self.get_paginator("list_published_schema_arns").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListPublishedSchemaArnsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListPublishedSchemaArnsResponse.from_boto(response)

    def list_tags_for_resource(
        self,
        _request: shapes.ListTagsForResourceRequest = None,
        *,
        resource_arn: str,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListTagsForResourceResponse:
        """
        Returns tags for a resource. Tagging is currently supported only for directories
        with a limit of 50 tags per directory. All 50 tags are returned for a given
        directory with this API call.
        """
        if _request is None:
            _params = {}
            if resource_arn is not ShapeBase.NOT_SET:
                _params['resource_arn'] = resource_arn
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListTagsForResourceRequest(**_params)
        paginator = self.get_paginator("list_tags_for_resource").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListTagsForResourceResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListTagsForResourceResponse.from_boto(response)

    def list_typed_link_facet_attributes(
        self,
        _request: shapes.ListTypedLinkFacetAttributesRequest = None,
        *,
        schema_arn: str,
        name: str,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListTypedLinkFacetAttributesResponse:
        """
        Returns a paginated list of all attribute definitions for a particular
        TypedLinkFacet. For more information, see [Typed
        link](http://docs.aws.amazon.com/directoryservice/latest/admin-
        guide/objectsandlinks.html#typedlink).
        """
        if _request is None:
            _params = {}
            if schema_arn is not ShapeBase.NOT_SET:
                _params['schema_arn'] = schema_arn
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListTypedLinkFacetAttributesRequest(**_params)
        paginator = self.get_paginator("list_typed_link_facet_attributes"
                                      ).paginate(**_request.to_boto())
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListTypedLinkFacetAttributesResponse.from_boto(
            first_page
        )
        result._page_iterator = page_generator
        return result

        return shapes.ListTypedLinkFacetAttributesResponse.from_boto(response)

    def list_typed_link_facet_names(
        self,
        _request: shapes.ListTypedLinkFacetNamesRequest = None,
        *,
        schema_arn: str,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListTypedLinkFacetNamesResponse:
        """
        Returns a paginated list of `TypedLink` facet names for a particular schema. For
        more information, see [Typed
        link](http://docs.aws.amazon.com/directoryservice/latest/admin-
        guide/objectsandlinks.html#typedlink).
        """
        if _request is None:
            _params = {}
            if schema_arn is not ShapeBase.NOT_SET:
                _params['schema_arn'] = schema_arn
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListTypedLinkFacetNamesRequest(**_params)
        paginator = self.get_paginator("list_typed_link_facet_names").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListTypedLinkFacetNamesResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListTypedLinkFacetNamesResponse.from_boto(response)

    def lookup_policy(
        self,
        _request: shapes.LookupPolicyRequest = None,
        *,
        directory_arn: str,
        object_reference: shapes.ObjectReference,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.LookupPolicyResponse:
        """
        Lists all policies from the root of the Directory to the object specified. If
        there are no policies present, an empty list is returned. If policies are
        present, and if some objects don't have the policies attached, it returns the
        `ObjectIdentifier` for such objects. If policies are present, it returns
        `ObjectIdentifier`, `policyId`, and `policyType`. Paths that don't lead to the
        root from the target object are ignored. For more information, see
        [Policies](http://docs.aws.amazon.com/directoryservice/latest/admin-
        guide/cd_key_concepts.html#policies).
        """
        if _request is None:
            _params = {}
            if directory_arn is not ShapeBase.NOT_SET:
                _params['directory_arn'] = directory_arn
            if object_reference is not ShapeBase.NOT_SET:
                _params['object_reference'] = object_reference
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.LookupPolicyRequest(**_params)
        paginator = self.get_paginator("lookup_policy").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.LookupPolicyResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.LookupPolicyResponse.from_boto(response)

    def publish_schema(
        self,
        _request: shapes.PublishSchemaRequest = None,
        *,
        development_schema_arn: str,
        version: str,
        minor_version: str = ShapeBase.NOT_SET,
        name: str = ShapeBase.NOT_SET,
    ) -> shapes.PublishSchemaResponse:
        """
        Publishes a development schema with a major version and a recommended minor
        version.
        """
        if _request is None:
            _params = {}
            if development_schema_arn is not ShapeBase.NOT_SET:
                _params['development_schema_arn'] = development_schema_arn
            if version is not ShapeBase.NOT_SET:
                _params['version'] = version
            if minor_version is not ShapeBase.NOT_SET:
                _params['minor_version'] = minor_version
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.PublishSchemaRequest(**_params)
        response = self._boto_client.publish_schema(**_request.to_boto())

        return shapes.PublishSchemaResponse.from_boto(response)

    def put_schema_from_json(
        self,
        _request: shapes.PutSchemaFromJsonRequest = None,
        *,
        schema_arn: str,
        document: str,
    ) -> shapes.PutSchemaFromJsonResponse:
        """
        Allows a schema to be updated using JSON upload. Only available for development
        schemas. See [JSON Schema
        Format](http://docs.aws.amazon.com/directoryservice/latest/admin-
        guide/cd_schemas.html#jsonformat) for more information.
        """
        if _request is None:
            _params = {}
            if schema_arn is not ShapeBase.NOT_SET:
                _params['schema_arn'] = schema_arn
            if document is not ShapeBase.NOT_SET:
                _params['document'] = document
            _request = shapes.PutSchemaFromJsonRequest(**_params)
        response = self._boto_client.put_schema_from_json(**_request.to_boto())

        return shapes.PutSchemaFromJsonResponse.from_boto(response)

    def remove_facet_from_object(
        self,
        _request: shapes.RemoveFacetFromObjectRequest = None,
        *,
        directory_arn: str,
        schema_facet: shapes.SchemaFacet,
        object_reference: shapes.ObjectReference,
    ) -> shapes.RemoveFacetFromObjectResponse:
        """
        Removes the specified facet from the specified object.
        """
        if _request is None:
            _params = {}
            if directory_arn is not ShapeBase.NOT_SET:
                _params['directory_arn'] = directory_arn
            if schema_facet is not ShapeBase.NOT_SET:
                _params['schema_facet'] = schema_facet
            if object_reference is not ShapeBase.NOT_SET:
                _params['object_reference'] = object_reference
            _request = shapes.RemoveFacetFromObjectRequest(**_params)
        response = self._boto_client.remove_facet_from_object(
            **_request.to_boto()
        )

        return shapes.RemoveFacetFromObjectResponse.from_boto(response)

    def tag_resource(
        self,
        _request: shapes.TagResourceRequest = None,
        *,
        resource_arn: str,
        tags: typing.List[shapes.Tag],
    ) -> shapes.TagResourceResponse:
        """
        An API operation for adding tags to a resource.
        """
        if _request is None:
            _params = {}
            if resource_arn is not ShapeBase.NOT_SET:
                _params['resource_arn'] = resource_arn
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.TagResourceRequest(**_params)
        response = self._boto_client.tag_resource(**_request.to_boto())

        return shapes.TagResourceResponse.from_boto(response)

    def untag_resource(
        self,
        _request: shapes.UntagResourceRequest = None,
        *,
        resource_arn: str,
        tag_keys: typing.List[str],
    ) -> shapes.UntagResourceResponse:
        """
        An API operation for removing tags from a resource.
        """
        if _request is None:
            _params = {}
            if resource_arn is not ShapeBase.NOT_SET:
                _params['resource_arn'] = resource_arn
            if tag_keys is not ShapeBase.NOT_SET:
                _params['tag_keys'] = tag_keys
            _request = shapes.UntagResourceRequest(**_params)
        response = self._boto_client.untag_resource(**_request.to_boto())

        return shapes.UntagResourceResponse.from_boto(response)

    def update_facet(
        self,
        _request: shapes.UpdateFacetRequest = None,
        *,
        schema_arn: str,
        name: str,
        attribute_updates: typing.List[shapes.FacetAttributeUpdate
                                      ] = ShapeBase.NOT_SET,
        object_type: typing.Union[str, shapes.ObjectType] = ShapeBase.NOT_SET,
    ) -> shapes.UpdateFacetResponse:
        """
        Does the following:

          1. Adds new `Attributes`, `Rules`, or `ObjectTypes`.

          2. Updates existing `Attributes`, `Rules`, or `ObjectTypes`.

          3. Deletes existing `Attributes`, `Rules`, or `ObjectTypes`.
        """
        if _request is None:
            _params = {}
            if schema_arn is not ShapeBase.NOT_SET:
                _params['schema_arn'] = schema_arn
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if attribute_updates is not ShapeBase.NOT_SET:
                _params['attribute_updates'] = attribute_updates
            if object_type is not ShapeBase.NOT_SET:
                _params['object_type'] = object_type
            _request = shapes.UpdateFacetRequest(**_params)
        response = self._boto_client.update_facet(**_request.to_boto())

        return shapes.UpdateFacetResponse.from_boto(response)

    def update_link_attributes(
        self,
        _request: shapes.UpdateLinkAttributesRequest = None,
        *,
        directory_arn: str,
        typed_link_specifier: shapes.TypedLinkSpecifier,
        attribute_updates: typing.List[shapes.LinkAttributeUpdate],
    ) -> shapes.UpdateLinkAttributesResponse:
        """
        Updates a given typed link’s attributes. Attributes to be updated must not
        contribute to the typed link’s identity, as defined by its
        `IdentityAttributeOrder`.
        """
        if _request is None:
            _params = {}
            if directory_arn is not ShapeBase.NOT_SET:
                _params['directory_arn'] = directory_arn
            if typed_link_specifier is not ShapeBase.NOT_SET:
                _params['typed_link_specifier'] = typed_link_specifier
            if attribute_updates is not ShapeBase.NOT_SET:
                _params['attribute_updates'] = attribute_updates
            _request = shapes.UpdateLinkAttributesRequest(**_params)
        response = self._boto_client.update_link_attributes(
            **_request.to_boto()
        )

        return shapes.UpdateLinkAttributesResponse.from_boto(response)

    def update_object_attributes(
        self,
        _request: shapes.UpdateObjectAttributesRequest = None,
        *,
        directory_arn: str,
        object_reference: shapes.ObjectReference,
        attribute_updates: typing.List[shapes.ObjectAttributeUpdate],
    ) -> shapes.UpdateObjectAttributesResponse:
        """
        Updates a given object's attributes.
        """
        if _request is None:
            _params = {}
            if directory_arn is not ShapeBase.NOT_SET:
                _params['directory_arn'] = directory_arn
            if object_reference is not ShapeBase.NOT_SET:
                _params['object_reference'] = object_reference
            if attribute_updates is not ShapeBase.NOT_SET:
                _params['attribute_updates'] = attribute_updates
            _request = shapes.UpdateObjectAttributesRequest(**_params)
        response = self._boto_client.update_object_attributes(
            **_request.to_boto()
        )

        return shapes.UpdateObjectAttributesResponse.from_boto(response)

    def update_schema(
        self,
        _request: shapes.UpdateSchemaRequest = None,
        *,
        schema_arn: str,
        name: str,
    ) -> shapes.UpdateSchemaResponse:
        """
        Updates the schema name with a new name. Only development schema names can be
        updated.
        """
        if _request is None:
            _params = {}
            if schema_arn is not ShapeBase.NOT_SET:
                _params['schema_arn'] = schema_arn
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.UpdateSchemaRequest(**_params)
        response = self._boto_client.update_schema(**_request.to_boto())

        return shapes.UpdateSchemaResponse.from_boto(response)

    def update_typed_link_facet(
        self,
        _request: shapes.UpdateTypedLinkFacetRequest = None,
        *,
        schema_arn: str,
        name: str,
        attribute_updates: typing.List[shapes.TypedLinkFacetAttributeUpdate],
        identity_attribute_order: typing.List[str],
    ) -> shapes.UpdateTypedLinkFacetResponse:
        """
        Updates a TypedLinkFacet. For more information, see [Typed
        link](http://docs.aws.amazon.com/directoryservice/latest/admin-
        guide/objectsandlinks.html#typedlink).
        """
        if _request is None:
            _params = {}
            if schema_arn is not ShapeBase.NOT_SET:
                _params['schema_arn'] = schema_arn
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if attribute_updates is not ShapeBase.NOT_SET:
                _params['attribute_updates'] = attribute_updates
            if identity_attribute_order is not ShapeBase.NOT_SET:
                _params['identity_attribute_order'] = identity_attribute_order
            _request = shapes.UpdateTypedLinkFacetRequest(**_params)
        response = self._boto_client.update_typed_link_facet(
            **_request.to_boto()
        )

        return shapes.UpdateTypedLinkFacetResponse.from_boto(response)

    def upgrade_applied_schema(
        self,
        _request: shapes.UpgradeAppliedSchemaRequest = None,
        *,
        published_schema_arn: str,
        directory_arn: str,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.UpgradeAppliedSchemaResponse:
        """
        Upgrades a single directory in-place using the `PublishedSchemaArn` with schema
        updates found in `MinorVersion`. Backwards-compatible minor version upgrades are
        instantaneously available for readers on all objects in the directory. Note:
        This is a synchronous API call and upgrades only one schema on a given directory
        per call. To upgrade multiple directories from one schema, you would need to
        call this API on each directory.
        """
        if _request is None:
            _params = {}
            if published_schema_arn is not ShapeBase.NOT_SET:
                _params['published_schema_arn'] = published_schema_arn
            if directory_arn is not ShapeBase.NOT_SET:
                _params['directory_arn'] = directory_arn
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.UpgradeAppliedSchemaRequest(**_params)
        response = self._boto_client.upgrade_applied_schema(
            **_request.to_boto()
        )

        return shapes.UpgradeAppliedSchemaResponse.from_boto(response)

    def upgrade_published_schema(
        self,
        _request: shapes.UpgradePublishedSchemaRequest = None,
        *,
        development_schema_arn: str,
        published_schema_arn: str,
        minor_version: str,
        dry_run: bool = ShapeBase.NOT_SET,
    ) -> shapes.UpgradePublishedSchemaResponse:
        """
        Upgrades a published schema under a new minor version revision using the current
        contents of `DevelopmentSchemaArn`.
        """
        if _request is None:
            _params = {}
            if development_schema_arn is not ShapeBase.NOT_SET:
                _params['development_schema_arn'] = development_schema_arn
            if published_schema_arn is not ShapeBase.NOT_SET:
                _params['published_schema_arn'] = published_schema_arn
            if minor_version is not ShapeBase.NOT_SET:
                _params['minor_version'] = minor_version
            if dry_run is not ShapeBase.NOT_SET:
                _params['dry_run'] = dry_run
            _request = shapes.UpgradePublishedSchemaRequest(**_params)
        response = self._boto_client.upgrade_published_schema(
            **_request.to_boto()
        )

        return shapes.UpgradePublishedSchemaResponse.from_boto(response)
