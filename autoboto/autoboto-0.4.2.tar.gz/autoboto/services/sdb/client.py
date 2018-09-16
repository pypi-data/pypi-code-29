import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("sdb", *args, **kwargs)

    def batch_delete_attributes(
        self,
        _request: shapes.BatchDeleteAttributesRequest = None,
        *,
        domain_name: str,
        items: typing.List[shapes.DeletableItem],
    ) -> None:
        """
        Performs multiple DeleteAttributes operations in a single call, which reduces
        round trips and latencies. This enables Amazon SimpleDB to optimize requests,
        which generally yields better throughput.

        The following limitations are enforced for this operation:

          * 1 MB request size
          * 25 item limit per BatchDeleteAttributes operation
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            if items is not ShapeBase.NOT_SET:
                _params['items'] = items
            _request = shapes.BatchDeleteAttributesRequest(**_params)
        response = self._boto_client.batch_delete_attributes(
            **_request.to_boto()
        )

    def batch_put_attributes(
        self,
        _request: shapes.BatchPutAttributesRequest = None,
        *,
        domain_name: str,
        items: typing.List[shapes.ReplaceableItem],
    ) -> None:
        """
        The `BatchPutAttributes` operation creates or replaces attributes within one or
        more items. By using this operation, the client can perform multiple
        PutAttribute operation with a single call. This helps yield savings in round
        trips and latencies, enabling Amazon SimpleDB to optimize requests and generally
        produce better throughput.

        The client may specify the item name with the `Item.X.ItemName` parameter. The
        client may specify new attributes using a combination of the
        `Item.X.Attribute.Y.Name` and `Item.X.Attribute.Y.Value` parameters. The client
        may specify the first attribute for the first item using the parameters
        `Item.0.Attribute.0.Name` and `Item.0.Attribute.0.Value`, and for the second
        attribute for the first item by the parameters `Item.0.Attribute.1.Name` and
        `Item.0.Attribute.1.Value`, and so on.

        Attributes are uniquely identified within an item by their name/value
        combination. For example, a single item can have the attributes `{ "first_name",
        "first_value" }` and `{ "first_name", "second_value" }`. However, it cannot have
        two attribute instances where both the `Item.X.Attribute.Y.Name` and
        `Item.X.Attribute.Y.Value` are the same.

        Optionally, the requester can supply the `Replace` parameter for each individual
        value. Setting this value to `true` will cause the new attribute values to
        replace the existing attribute values. For example, if an item `I` has the
        attributes `{ 'a', '1' }, { 'b', '2'}` and `{ 'b', '3' }` and the requester does
        a BatchPutAttributes of `{'I', 'b', '4' }` with the Replace parameter set to
        true, the final attributes of the item will be `{ 'a', '1' }` and `{ 'b', '4'
        }`, replacing the previous values of the 'b' attribute with the new value.

        This operation is vulnerable to exceeding the maximum URL size when making a
        REST request using the HTTP GET method. This operation does not support
        conditions using `Expected.X.Name`, `Expected.X.Value`, or `Expected.X.Exists`.

        You can execute multiple `BatchPutAttributes` operations and other operations in
        parallel. However, large numbers of concurrent `BatchPutAttributes` calls can
        result in Service Unavailable (503) responses.

        The following limitations are enforced for this operation:

          * 256 attribute name-value pairs per item
          * 1 MB request size
          * 1 billion attributes per domain
          * 10 GB of total user data storage per domain
          * 25 item limit per `BatchPutAttributes` operation
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            if items is not ShapeBase.NOT_SET:
                _params['items'] = items
            _request = shapes.BatchPutAttributesRequest(**_params)
        response = self._boto_client.batch_put_attributes(**_request.to_boto())

    def create_domain(
        self,
        _request: shapes.CreateDomainRequest = None,
        *,
        domain_name: str,
    ) -> None:
        """
        The `CreateDomain` operation creates a new domain. The domain name should be
        unique among the domains associated with the Access Key ID provided in the
        request. The `CreateDomain` operation may take 10 or more seconds to complete.

        The client can create up to 100 domains per account.

        If the client requires additional domains, go to [
        http://aws.amazon.com/contact-us/simpledb-limit-
        request/](http://aws.amazon.com/contact-us/simpledb-limit-request/).
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            _request = shapes.CreateDomainRequest(**_params)
        response = self._boto_client.create_domain(**_request.to_boto())

    def delete_attributes(
        self,
        _request: shapes.DeleteAttributesRequest = None,
        *,
        domain_name: str,
        item_name: str,
        attributes: typing.List[shapes.Attribute] = ShapeBase.NOT_SET,
        expected: shapes.UpdateCondition = ShapeBase.NOT_SET,
    ) -> None:
        """
        Deletes one or more attributes associated with an item. If all attributes of the
        item are deleted, the item is deleted.

        `DeleteAttributes` is an idempotent operation; running it multiple times on the
        same item or attribute does not result in an error response.

        Because Amazon SimpleDB makes multiple copies of item data and uses an eventual
        consistency update model, performing a GetAttributes or Select operation (read)
        immediately after a `DeleteAttributes` or PutAttributes operation (write) might
        not return updated item data.
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            if item_name is not ShapeBase.NOT_SET:
                _params['item_name'] = item_name
            if attributes is not ShapeBase.NOT_SET:
                _params['attributes'] = attributes
            if expected is not ShapeBase.NOT_SET:
                _params['expected'] = expected
            _request = shapes.DeleteAttributesRequest(**_params)
        response = self._boto_client.delete_attributes(**_request.to_boto())

    def delete_domain(
        self,
        _request: shapes.DeleteDomainRequest = None,
        *,
        domain_name: str,
    ) -> None:
        """
        The `DeleteDomain` operation deletes a domain. Any items (and their attributes)
        in the domain are deleted as well. The `DeleteDomain` operation might take 10 or
        more seconds to complete.
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            _request = shapes.DeleteDomainRequest(**_params)
        response = self._boto_client.delete_domain(**_request.to_boto())

    def domain_metadata(
        self,
        _request: shapes.DomainMetadataRequest = None,
        *,
        domain_name: str,
    ) -> shapes.DomainMetadataResult:
        """
        Returns information about the domain, including when the domain was created, the
        number of items and attributes in the domain, and the size of the attribute
        names and values.
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            _request = shapes.DomainMetadataRequest(**_params)
        response = self._boto_client.domain_metadata(**_request.to_boto())

        return shapes.DomainMetadataResult.from_boto(response)

    def get_attributes(
        self,
        _request: shapes.GetAttributesRequest = None,
        *,
        domain_name: str,
        item_name: str,
        attribute_names: typing.List[str] = ShapeBase.NOT_SET,
        consistent_read: bool = ShapeBase.NOT_SET,
    ) -> shapes.GetAttributesResult:
        """
        Returns all of the attributes associated with the specified item. Optionally,
        the attributes returned can be limited to one or more attributes by specifying
        an attribute name parameter.

        If the item does not exist on the replica that was accessed for this operation,
        an empty set is returned. The system does not return an error as it cannot
        guarantee the item does not exist on other replicas.
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            if item_name is not ShapeBase.NOT_SET:
                _params['item_name'] = item_name
            if attribute_names is not ShapeBase.NOT_SET:
                _params['attribute_names'] = attribute_names
            if consistent_read is not ShapeBase.NOT_SET:
                _params['consistent_read'] = consistent_read
            _request = shapes.GetAttributesRequest(**_params)
        response = self._boto_client.get_attributes(**_request.to_boto())

        return shapes.GetAttributesResult.from_boto(response)

    def list_domains(
        self,
        _request: shapes.ListDomainsRequest = None,
        *,
        max_number_of_domains: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListDomainsResult:
        """
        The `ListDomains` operation lists all domains associated with the Access Key ID.
        It returns domain names up to the limit set by MaxNumberOfDomains. A NextToken
        is returned if there are more than `MaxNumberOfDomains` domains. Calling
        `ListDomains` successive times with the `NextToken` provided by the operation
        returns up to `MaxNumberOfDomains` more domain names with each successive
        operation call.
        """
        if _request is None:
            _params = {}
            if max_number_of_domains is not ShapeBase.NOT_SET:
                _params['max_number_of_domains'] = max_number_of_domains
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListDomainsRequest(**_params)
        paginator = self.get_paginator("list_domains").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListDomainsResult.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListDomainsResult.from_boto(response)

    def put_attributes(
        self,
        _request: shapes.PutAttributesRequest = None,
        *,
        domain_name: str,
        item_name: str,
        attributes: typing.List[shapes.ReplaceableAttribute],
        expected: shapes.UpdateCondition = ShapeBase.NOT_SET,
    ) -> None:
        """
        The PutAttributes operation creates or replaces attributes in an item. The
        client may specify new attributes using a combination of the `Attribute.X.Name`
        and `Attribute.X.Value` parameters. The client specifies the first attribute by
        the parameters `Attribute.0.Name` and `Attribute.0.Value`, the second attribute
        by the parameters `Attribute.1.Name` and `Attribute.1.Value`, and so on.

        Attributes are uniquely identified in an item by their name/value combination.
        For example, a single item can have the attributes `{ "first_name",
        "first_value" }` and `{ "first_name", second_value" }`. However, it cannot have
        two attribute instances where both the `Attribute.X.Name` and
        `Attribute.X.Value` are the same.

        Optionally, the requestor can supply the `Replace` parameter for each individual
        attribute. Setting this value to `true` causes the new attribute value to
        replace the existing attribute value(s). For example, if an item has the
        attributes `{ 'a', '1' }`, `{ 'b', '2'}` and `{ 'b', '3' }` and the requestor
        calls `PutAttributes` using the attributes `{ 'b', '4' }` with the `Replace`
        parameter set to true, the final attributes of the item are changed to `{ 'a',
        '1' }` and `{ 'b', '4' }`, which replaces the previous values of the 'b'
        attribute with the new value.

        You cannot specify an empty string as an attribute name.

        Because Amazon SimpleDB makes multiple copies of client data and uses an
        eventual consistency update model, an immediate GetAttributes or Select
        operation (read) immediately after a PutAttributes or DeleteAttributes operation
        (write) might not return the updated data.

        The following limitations are enforced for this operation:

          * 256 total attribute name-value pairs per item
          * One billion attributes per domain
          * 10 GB of total user data storage per domain
        """
        if _request is None:
            _params = {}
            if domain_name is not ShapeBase.NOT_SET:
                _params['domain_name'] = domain_name
            if item_name is not ShapeBase.NOT_SET:
                _params['item_name'] = item_name
            if attributes is not ShapeBase.NOT_SET:
                _params['attributes'] = attributes
            if expected is not ShapeBase.NOT_SET:
                _params['expected'] = expected
            _request = shapes.PutAttributesRequest(**_params)
        response = self._boto_client.put_attributes(**_request.to_boto())

    def select(
        self,
        _request: shapes.SelectRequest = None,
        *,
        select_expression: str,
        next_token: str = ShapeBase.NOT_SET,
        consistent_read: bool = ShapeBase.NOT_SET,
    ) -> shapes.SelectResult:
        """
        The `Select` operation returns a set of attributes for `ItemNames` that match
        the select expression. `Select` is similar to the standard SQL SELECT statement.

        The total size of the response cannot exceed 1 MB in total size. Amazon SimpleDB
        automatically adjusts the number of items returned per page to enforce this
        limit. For example, if the client asks to retrieve 2500 items, but each
        individual item is 10 kB in size, the system returns 100 items and an
        appropriate `NextToken` so the client can access the next page of results.

        For information on how to construct select expressions, see Using Select to
        Create Amazon SimpleDB Queries in the Developer Guide.
        """
        if _request is None:
            _params = {}
            if select_expression is not ShapeBase.NOT_SET:
                _params['select_expression'] = select_expression
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if consistent_read is not ShapeBase.NOT_SET:
                _params['consistent_read'] = consistent_read
            _request = shapes.SelectRequest(**_params)
        paginator = self.get_paginator("select").paginate(**_request.to_boto())
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.SelectResult.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.SelectResult.from_boto(response)
