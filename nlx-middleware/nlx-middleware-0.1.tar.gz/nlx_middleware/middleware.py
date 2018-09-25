import collections
import json
from typing import List, Mapping, Union

from django.conf import settings
from django.core.cache import caches, InvalidCacheBackendError
from django.http import HttpRequest
from django.template.response import TemplateResponse

from drf_yasg import openapi
from zds_client import Client
from zds_client.schema import (
    get_request_parameters, get_request_resource, get_response_resource
)

Body = Union[List, Mapping]


class NLxInwayURLRewriteMiddleware:
    """
    Rewrite the URLs in the request and response bodies.

    The URLs of linked data properties in the request and response bodies
    are rewritten from/to NLx outway addresses. This ensures you operate
    within the NLx network, while canonical URLs (NLX agnostic) are
    communicated and stored.

    The resources exchanged across the request/response are checked with the
    OpenAPI path and schema definitions to whitelist which properties may be
    rewritten.
    """

    rewriter = None

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # middleware is NOT thread safe, so we cannot create a single instance
        # of a rewriter :(
        self.rewrite_request_nlx_urls(request)
        return self.get_response(request)

    def rewrite_request_nlx_urls(self, request) -> None:
        """
        Parse the request body and rewrite the URLs.

        NLx outway URLs are transformed into canonical URLs. Anything that is
        not application/json is left untouched.
        """
        if request.content_type != 'application/json':
            return

        body = json.loads(
            request.body,
            object_pairs_hook=collections.OrderedDict,
            encoding=request.encoding
        ) if request.body else {}

        # do the actual rewrite
        rewriter = Rewriter(request)
        rewriter.from_nlx(body)

        # request.body is a property, so hook into private API
        request._body = json.dumps(body).encode(request.encoding or 'utf-8')

    def process_template_response(self, request: HttpRequest, response: TemplateResponse) -> TemplateResponse:
        """
        Process the response data and rewrite URLs.

        Canonical URLs are transformed into NLx-based URLs. Anything that is
        not a an application/json response from DRF is left untouched.
        """
        if request.content_type != 'application/json':
            return response

        # we only rewrite json api responses
        accepted_media_type = getattr(response, 'accepted_media_type', '')
        if not accepted_media_type == 'application/json':
            return response

        rewriter = Rewriter(request)
        rewriter.to_nlx(response.data, response.status_code)

        return response


def get_url_properties(schema: dict):
    """
    Yield the names of properties that represent URLs in the schema.
    """
    # TODO: support nested schema's
    if isinstance(schema, list):
        assert len(schema) == 1, 'Unexpectedly found multiple schemas?'
        schema = schema[0]
    for prop, prop_config in schema['properties'].items():
        if prop_config['type'] != openapi.TYPE_STRING:
            continue

        if prop_config.get('format') != openapi.FORMAT_URI:
            continue

        yield prop


def get_url_parameters(parameters: list):
    """
    Yield the names of querystring parameters that represent URLs in the schema.
    """
    for param in parameters:
        if param['in'] != openapi.IN_QUERY:
            continue
        if param['schema']['type'] != openapi.TYPE_STRING:
            continue
        if param['schema'].get('format') != openapi.FORMAT_URI:
            continue

        yield param['name']


def get_client(url: str) -> Client:
    """
    Return a ZDS Client instance for the backend serving url.

    Note that this client makes an additional request to retrieve the OpenAPI
    schema. The result is cached. This is effectively hitting itself over TCP
    again.
    """
    try:
        cache = caches['nlx-middleware']
    except InvalidCacheBackendError:
        cache = caches['default']

    key = 'nlx-middleware:api-schema'
    client = Client.from_url(url, settings.BASE_DIR)

    schema = cache.get(key)
    if schema is None:
        schema = client.schema
        # timeout is optional, see
        # https://docs.djangoproject.com/en/stable/topics/cache/#basic-usage
        cache.set(key, schema)
    else:
        client._schema = schema
    return client


class Rewriter:

    def __init__(self, request: HttpRequest):
        self.request = request

        self.request_url = self.request.build_absolute_uri(self.request.path)
        self.outway_address = f'{settings.NLX_OUTWAY_ADDRESS}/{settings.NLX_ORGANIZATION}/{settings.NLX_SERVICE}'
        self.local_address = f'{self.request.scheme}://{settings.NLX_INWAY_ADDRESS}'.rstrip('/')

    def __repr__(self):
        return 'Rewriter(%r)' % self.request

    @property
    def client(self) -> Client:
        return get_client(self.request_url)

    def _rewrite_key_value(self, obj: dict, from_value: str, to_value: str, prop_iterator) -> None:
        # support collections as well
        objects = obj if isinstance(obj, list) else [obj]

        for prop in prop_iterator:
            for obj in objects:
                if prop not in obj:
                    continue

                value = obj[prop]
                scalar = not isinstance(value, (list, tuple))

                if scalar:
                    value = [value]

                rewritten_value = [
                    val.replace(from_value, to_value, 1) if val.startswith(from_value) else val
                    for val in value
                ]

                obj[prop] = rewritten_value[0] if scalar else rewritten_value

    def from_nlx(self, body: Body) -> None:
        """
        Rewrite request body & GET parameters to canonical URLs.

        Modifies the request and body in place.

        # TODO: also rewrite other-services, consult own registry
        """
        from_value, to_value = self.outway_address, self.local_address

        # These safe HTTP methods don't have a body
        if self.request.method not in ('GET', 'HEAD', 'OPTIONS', 'TRACE'):
            schema = get_request_resource(self.client.schema, self.request_url, self.request.method)
            # TODO: support arrays as well
            assert schema['type'] == 'object'
            self._rewrite_key_value(
                obj=body,
                from_value=from_value,
                to_value=to_value,
                prop_iterator=get_url_properties(schema)
            )
        else:
            # assume GET, django always provides it for us
            query_dict = self.request.GET.copy()
            parameters = get_request_parameters(self.client.schema, self.request_url, self.request.method)
            self._rewrite_key_value(
                query_dict,
                from_value=from_value,
                to_value=to_value,
                prop_iterator=get_url_parameters(parameters)
            )

            # re-assign the rewritten querydict
            self.request.GET = query_dict

    def to_nlx(self, body: Body, status_code: int) -> None:
        """
        Rewrite the response body data to NLx outway URLs.

        Modifies the body in place.

        # TODO: also rewrite other-services, consult own registry
        """
        from_value, to_value = self.local_address, self.outway_address
        schema = get_response_resource(
            self.client.schema, self.request_url,
            self.request.method, str(status_code)
        )

        self._rewrite_key_value(
            obj=body,
            from_value=from_value,
            to_value=to_value,
            prop_iterator=get_url_properties(schema)
        )
