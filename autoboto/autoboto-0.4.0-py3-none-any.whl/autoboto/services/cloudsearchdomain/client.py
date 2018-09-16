import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("cloudsearchdomain", *args, **kwargs)

    def search(
        self,
        _request: shapes.SearchRequest = None,
        *,
        query: str,
        cursor: str = ShapeBase.NOT_SET,
        expr: str = ShapeBase.NOT_SET,
        facet: str = ShapeBase.NOT_SET,
        filter_query: str = ShapeBase.NOT_SET,
        highlight: str = ShapeBase.NOT_SET,
        partial: bool = ShapeBase.NOT_SET,
        query_options: str = ShapeBase.NOT_SET,
        query_parser: typing.Union[str, shapes.QueryParser] = ShapeBase.NOT_SET,
        return_: str = ShapeBase.NOT_SET,
        size: int = ShapeBase.NOT_SET,
        sort: str = ShapeBase.NOT_SET,
        start: int = ShapeBase.NOT_SET,
        stats: str = ShapeBase.NOT_SET,
    ) -> shapes.SearchResponse:
        """
        Retrieves a list of documents that match the specified search criteria. How you
        specify the search criteria depends on which query parser you use. Amazon
        CloudSearch supports four query parsers:

          * `simple`: search all `text` and `text-array` fields for the specified string. Search for phrases, individual terms, and prefixes. 
          * `structured`: search specific fields, construct compound queries using Boolean operators, and use advanced features such as term boosting and proximity searching.
          * `lucene`: specify search criteria using the Apache Lucene query parser syntax.
          * `dismax`: specify search criteria using the simplified subset of the Apache Lucene query parser syntax defined by the DisMax query parser.

        For more information, see [Searching Your
        Data](http://docs.aws.amazon.com/cloudsearch/latest/developerguide/searching.html)
        in the _Amazon CloudSearch Developer Guide_.

        The endpoint for submitting `Search` requests is domain-specific. You submit
        search requests to a domain's search endpoint. To get the search endpoint for
        your domain, use the Amazon CloudSearch configuration service `DescribeDomains`
        action. A domain's endpoints are also displayed on the domain dashboard in the
        Amazon CloudSearch console.
        """
        if _request is None:
            _params = {}
            if query is not ShapeBase.NOT_SET:
                _params['query'] = query
            if cursor is not ShapeBase.NOT_SET:
                _params['cursor'] = cursor
            if expr is not ShapeBase.NOT_SET:
                _params['expr'] = expr
            if facet is not ShapeBase.NOT_SET:
                _params['facet'] = facet
            if filter_query is not ShapeBase.NOT_SET:
                _params['filter_query'] = filter_query
            if highlight is not ShapeBase.NOT_SET:
                _params['highlight'] = highlight
            if partial is not ShapeBase.NOT_SET:
                _params['partial'] = partial
            if query_options is not ShapeBase.NOT_SET:
                _params['query_options'] = query_options
            if query_parser is not ShapeBase.NOT_SET:
                _params['query_parser'] = query_parser
            if return_ is not ShapeBase.NOT_SET:
                _params['return_'] = return_
            if size is not ShapeBase.NOT_SET:
                _params['size'] = size
            if sort is not ShapeBase.NOT_SET:
                _params['sort'] = sort
            if start is not ShapeBase.NOT_SET:
                _params['start'] = start
            if stats is not ShapeBase.NOT_SET:
                _params['stats'] = stats
            _request = shapes.SearchRequest(**_params)
        response = self._boto_client.search(**_request.to_boto())

        return shapes.SearchResponse.from_boto(response)

    def suggest(
        self,
        _request: shapes.SuggestRequest = None,
        *,
        query: str,
        suggester: str,
        size: int = ShapeBase.NOT_SET,
    ) -> shapes.SuggestResponse:
        """
        Retrieves autocomplete suggestions for a partial query string. You can use
        suggestions enable you to display likely matches before users finish typing. In
        Amazon CloudSearch, suggestions are based on the contents of a particular text
        field. When you request suggestions, Amazon CloudSearch finds all of the
        documents whose values in the suggester field start with the specified query
        string. The beginning of the field must match the query string to be considered
        a match.

        For more information about configuring suggesters and retrieving suggestions,
        see [Getting
        Suggestions](http://docs.aws.amazon.com/cloudsearch/latest/developerguide/getting-
        suggestions.html) in the _Amazon CloudSearch Developer Guide_.

        The endpoint for submitting `Suggest` requests is domain-specific. You submit
        suggest requests to a domain's search endpoint. To get the search endpoint for
        your domain, use the Amazon CloudSearch configuration service `DescribeDomains`
        action. A domain's endpoints are also displayed on the domain dashboard in the
        Amazon CloudSearch console.
        """
        if _request is None:
            _params = {}
            if query is not ShapeBase.NOT_SET:
                _params['query'] = query
            if suggester is not ShapeBase.NOT_SET:
                _params['suggester'] = suggester
            if size is not ShapeBase.NOT_SET:
                _params['size'] = size
            _request = shapes.SuggestRequest(**_params)
        response = self._boto_client.suggest(**_request.to_boto())

        return shapes.SuggestResponse.from_boto(response)

    def upload_documents(
        self,
        _request: shapes.UploadDocumentsRequest = None,
        *,
        documents: typing.Any,
        content_type: typing.Union[str, shapes.ContentType],
    ) -> shapes.UploadDocumentsResponse:
        """
        Posts a batch of documents to a search domain for indexing. A document batch is
        a collection of add and delete operations that represent the documents you want
        to add, update, or delete from your domain. Batches can be described in either
        JSON or XML. Each item that you want Amazon CloudSearch to return as a search
        result (such as a product) is represented as a document. Every document has a
        unique ID and one or more fields that contain the data that you want to search
        and return in results. Individual documents cannot contain more than 1 MB of
        data. The entire batch cannot exceed 5 MB. To get the best possible upload
        performance, group add and delete operations in batches that are close the 5 MB
        limit. Submitting a large volume of single-document batches can overload a
        domain's document service.

        The endpoint for submitting `UploadDocuments` requests is domain-specific. To
        get the document endpoint for your domain, use the Amazon CloudSearch
        configuration service `DescribeDomains` action. A domain's endpoints are also
        displayed on the domain dashboard in the Amazon CloudSearch console.

        For more information about formatting your data for Amazon CloudSearch, see
        [Preparing Your
        Data](http://docs.aws.amazon.com/cloudsearch/latest/developerguide/preparing-
        data.html) in the _Amazon CloudSearch Developer Guide_. For more information
        about uploading data for indexing, see [Uploading
        Data](http://docs.aws.amazon.com/cloudsearch/latest/developerguide/uploading-
        data.html) in the _Amazon CloudSearch Developer Guide_.
        """
        if _request is None:
            _params = {}
            if documents is not ShapeBase.NOT_SET:
                _params['documents'] = documents
            if content_type is not ShapeBase.NOT_SET:
                _params['content_type'] = content_type
            _request = shapes.UploadDocumentsRequest(**_params)
        response = self._boto_client.upload_documents(**_request.to_boto())

        return shapes.UploadDocumentsResponse.from_boto(response)
