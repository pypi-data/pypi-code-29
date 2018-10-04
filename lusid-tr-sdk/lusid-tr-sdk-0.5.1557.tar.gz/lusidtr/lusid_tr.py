# coding=utf-8
# --------------------------------------------------------------------------
# # License
#
# Copyright &copy; 2018 FINBOURNE TECHNOLOGY LTD
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# --------------------------------------------------------------------------

from msrest.service_client import ServiceClient
from msrest import Configuration, Serializer, Deserializer
from .version import VERSION
from msrest.pipeline import ClientRawResponse
from msrest.exceptions import HttpOperationError
from . import models


class LusidTrConfiguration(Configuration):
    """Configuration for LusidTr
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Subscription credentials which uniquely identify
     client subscription.
    :type credentials: None
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if not base_url:
            base_url = 'http://localhost'

        super(LusidTrConfiguration, self).__init__(base_url)

        self.add_user_agent('lusidtr/{}'.format(VERSION))

        self.credentials = credentials


class LusidTr(object):
    """LusidTr

    :ivar config: Configuration for client.
    :vartype config: LusidTrConfiguration

    :param credentials: Subscription credentials which uniquely identify
     client subscription.
    :type credentials: None
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, base_url=None):

        self.config = LusidTrConfiguration(credentials, base_url)
        self._client = ServiceClient(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '0.5.1557'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)


    def get_aggregation_by_group(
            self, scope, code, request=None, sort_by=None, start=None, limit=None, custom_headers=None, raw=False, **operation_config):
        """Aggregate data in a group hierarchy.

        :param scope:
        :type scope: str
        :param code:
        :type code: str
        :param request:
        :type request: ~lusidtr.models.AggregationRequest
        :param sort_by:
        :type sort_by: list[str]
        :param start:
        :type start: int
        :param limit:
        :type limit: int
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ListAggregationResponse or ClientRawResponse if raw=true
        :rtype: ~lusidtr.models.ListAggregationResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_aggregation_by_group.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if sort_by is not None:
            query_parameters['sortBy'] = self._serialize.query("sort_by", sort_by, '[str]', div=',')
        if start is not None:
            query_parameters['start'] = self._serialize.query("start", start, 'int')
        if limit is not None:
            query_parameters['limit'] = self._serialize.query("limit", limit, 'int')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if request is not None:
            body_content = self._serialize.body(request, 'AggregationRequest')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ListAggregationResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_aggregation_by_group.metadata = {'url': '/data/lusid/aggregation/portfoliogroups/{scope}/{code}/$aggregate'}

    def get_nested_aggregation_by_group(
            self, scope, code, request=None, custom_headers=None, raw=False, **operation_config):
        """Obsolete - Aggregation request data in a group hierarchy into a data
        tree.

        :param scope:
        :type scope: str
        :param code:
        :type code: str
        :param request:
        :type request: ~lusidtr.models.AggregationRequest
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: NestedAggregationResponse or ClientRawResponse if raw=true
        :rtype: ~lusidtr.models.NestedAggregationResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_nested_aggregation_by_group.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if request is not None:
            body_content = self._serialize.body(request, 'AggregationRequest')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('NestedAggregationResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_nested_aggregation_by_group.metadata = {'url': '/data/lusid/aggregation/portfoliogroups/{scope}/{code}/$aggregatenested'}

    def get_aggregation_by_portfolio(
            self, scope, code, request=None, sort_by=None, start=None, limit=None, custom_headers=None, raw=False, **operation_config):
        """Aggregate data in a portfolio.

        :param scope:
        :type scope: str
        :param code:
        :type code: str
        :param request:
        :type request: ~lusidtr.models.AggregationRequest
        :param sort_by:
        :type sort_by: list[str]
        :param start:
        :type start: int
        :param limit:
        :type limit: int
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ListAggregationResponse or ClientRawResponse if raw=true
        :rtype: ~lusidtr.models.ListAggregationResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_aggregation_by_portfolio.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if sort_by is not None:
            query_parameters['sortBy'] = self._serialize.query("sort_by", sort_by, '[str]', div=',')
        if start is not None:
            query_parameters['start'] = self._serialize.query("start", start, 'int')
        if limit is not None:
            query_parameters['limit'] = self._serialize.query("limit", limit, 'int')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if request is not None:
            body_content = self._serialize.body(request, 'AggregationRequest')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ListAggregationResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_aggregation_by_portfolio.metadata = {'url': '/data/lusid/aggregation/portfolios/{scope}/{code}/$aggregate'}

    def get_aggregation_by_result_set(
            self, scope, results_key, request=None, sort_by=None, start=None, limit=None, custom_headers=None, raw=False, **operation_config):
        """Aggregate data from a result set.

        :param scope:
        :type scope: str
        :param results_key:
        :type results_key: str
        :param request:
        :type request: ~lusidtr.models.AggregationRequest
        :param sort_by:
        :type sort_by: list[str]
        :param start:
        :type start: int
        :param limit:
        :type limit: int
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ListAggregationResponse or ClientRawResponse if raw=true
        :rtype: ~lusidtr.models.ListAggregationResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_aggregation_by_result_set.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'resultsKey': self._serialize.url("results_key", results_key, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if sort_by is not None:
            query_parameters['sortBy'] = self._serialize.query("sort_by", sort_by, '[str]', div=',')
        if start is not None:
            query_parameters['start'] = self._serialize.query("start", start, 'int')
        if limit is not None:
            query_parameters['limit'] = self._serialize.query("limit", limit, 'int')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if request is not None:
            body_content = self._serialize.body(request, 'AggregationRequest')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ListAggregationResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_aggregation_by_result_set.metadata = {'url': '/data/lusid/aggregation/results/{scope}/{resultsKey}/$aggregate'}

    def list_analytic_stores(
            self, as_at=None, sort_by=None, start=None, limit=None, filter=None, custom_headers=None, raw=False, **operation_config):
        """List all analytic stores in client.

        :param as_at:
        :type as_at: datetime
        :param sort_by:
        :type sort_by: list[str]
        :param start:
        :type start: int
        :param limit:
        :type limit: int
        :param filter:
        :type filter: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ResourceListOfAnalyticStoreKey or ClientRawResponse if
         raw=true
        :rtype: ~lusidtr.models.ResourceListOfAnalyticStoreKey or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.list_analytic_stores.metadata['url']

        # Construct parameters
        query_parameters = {}
        if as_at is not None:
            query_parameters['asAt'] = self._serialize.query("as_at", as_at, 'iso-8601')
        if sort_by is not None:
            query_parameters['sortBy'] = self._serialize.query("sort_by", sort_by, '[str]', div=',')
        if start is not None:
            query_parameters['start'] = self._serialize.query("start", start, 'int')
        if limit is not None:
            query_parameters['limit'] = self._serialize.query("limit", limit, 'int')
        if filter is not None:
            query_parameters['filter'] = self._serialize.query("filter", filter, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ResourceListOfAnalyticStoreKey', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    list_analytic_stores.metadata = {'url': '/data/lusid/analytics'}

    def create_analytic_store(
            self, request=None, custom_headers=None, raw=False, **operation_config):
        """Create a new analytic store for the given scope for the given date.

        :param request: A valid and fully populated analytic store creation
         request
        :type request: ~lusidtr.models.CreateAnalyticStoreRequest
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: AnalyticStore or ClientRawResponse if raw=true
        :rtype: ~lusidtr.models.AnalyticStore or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.create_analytic_store.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if request is not None:
            body_content = self._serialize.body(request, 'CreateAnalyticStoreRequest')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [201]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 201:
            deserialized = self._deserialize('AnalyticStore', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    create_analytic_store.metadata = {'url': '/data/lusid/analytics'}

    def get_analytic_store(
            self, scope, year, month, day, as_at=None, custom_headers=None, raw=False, **operation_config):
        """Get an analytic store.

        :param scope: The analytics data scope
        :type scope: str
        :param year: The year component of the date for the data in the scope
        :type year: int
        :param month: The month component of the date for the data in the
         scope
        :type month: int
        :param day: The day component of the date for the data in the scope
        :type day: int
        :param as_at: AsAt date
        :type as_at: datetime
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: AnalyticStore or ClientRawResponse if raw=true
        :rtype: ~lusidtr.models.AnalyticStore or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_analytic_store.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'year': self._serialize.url("year", year, 'int'),
            'month': self._serialize.url("month", month, 'int'),
            'day': self._serialize.url("day", day, 'int')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if as_at is not None:
            query_parameters['asAt'] = self._serialize.query("as_at", as_at, 'iso-8601')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('AnalyticStore', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_analytic_store.metadata = {'url': '/data/lusid/analytics/{scope}/{year}/{month}/{day}'}

    def delete_analytic_store(
            self, scope, year, month, day, custom_headers=None, raw=False, **operation_config):
        """Create a new analytic store for the given scope for the given date.

        :param scope: The analytics data scope
        :type scope: str
        :param year: The year component of the date for the data in the scope
        :type year: int
        :param month: The month component of the date for the data in the
         scope
        :type month: int
        :param day: The day component of the date for the data in the scope
        :type day: int
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: DeletedEntityResponse or ClientRawResponse if raw=true
        :rtype: ~lusidtr.models.DeletedEntityResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.delete_analytic_store.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'year': self._serialize.url("year", year, 'int'),
            'month': self._serialize.url("month", month, 'int'),
            'day': self._serialize.url("day", day, 'int')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('DeletedEntityResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    delete_analytic_store.metadata = {'url': '/data/lusid/analytics/{scope}/{year}/{month}/{day}'}

    def insert_analytics(
            self, scope, year, month, day, data=None, custom_headers=None, raw=False, **operation_config):
        """Insert analytics into an existing analytic store for the given scope
        and date.

        :param scope: The analytics data scope
        :type scope: str
        :param year: The year component of the date for the data in the scope
        :type year: int
        :param month: The month component of the date for the data in the
         scope
        :type month: int
        :param day: The day component of the date for the data in the scope
        :type day: int
        :param data:
        :type data: list[~lusidtr.models.InstrumentAnalytic]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: AnalyticStore or ClientRawResponse if raw=true
        :rtype: ~lusidtr.models.AnalyticStore or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.insert_analytics.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'year': self._serialize.url("year", year, 'int'),
            'month': self._serialize.url("month", month, 'int'),
            'day': self._serialize.url("day", day, 'int')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if data is not None:
            body_content = self._serialize.body(data, '[InstrumentAnalytic]')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('AnalyticStore', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    insert_analytics.metadata = {'url': '/data/lusid/analytics/{scope}/{year}/{month}/{day}/prices'}

    def get_corporate_actions(
            self, scope, code, effective_at=None, as_at=None, sort_by=None, start=None, limit=None, filter=None, custom_headers=None, raw=False, **operation_config):
        """Gets a corporate action based on dates.

        :param scope: Scope
        :type scope: str
        :param code: Corporate action source id
        :type code: str
        :param effective_at: Effective Date
        :type effective_at: datetime
        :param as_at: AsAt Date filter
        :type as_at: datetime
        :param sort_by:
        :type sort_by: list[str]
        :param start:
        :type start: int
        :param limit:
        :type limit: int
        :param filter:
        :type filter: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ResourceListOfCorporateActionEvent or ClientRawResponse if
         raw=true
        :rtype: ~lusidtr.models.ResourceListOfCorporateActionEvent or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_corporate_actions.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if effective_at is not None:
            query_parameters['effectiveAt'] = self._serialize.query("effective_at", effective_at, 'iso-8601')
        if as_at is not None:
            query_parameters['asAt'] = self._serialize.query("as_at", as_at, 'iso-8601')
        if sort_by is not None:
            query_parameters['sortBy'] = self._serialize.query("sort_by", sort_by, '[str]', div=',')
        if start is not None:
            query_parameters['start'] = self._serialize.query("start", start, 'int')
        if limit is not None:
            query_parameters['limit'] = self._serialize.query("limit", limit, 'int')
        if filter is not None:
            query_parameters['filter'] = self._serialize.query("filter", filter, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ResourceListOfCorporateActionEvent', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_corporate_actions.metadata = {'url': '/data/lusid/corporateactions/{scope}/{code}'}

    def batch_upsert_corporate_actions(
            self, scope, code, actions=None, custom_headers=None, raw=False, **operation_config):
        """Attempt to create/update one or more corporate action. Failed actions
        will be identified in the body of the response.

        :param scope: The intended scope of the corporate action
        :type scope: str
        :param code: Source of the corporate action
        :type code: str
        :param actions: The corporate actions to create
        :type actions: list[~lusidtr.models.CreateCorporateAction]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: UpsertCorporateActionsResponse or ClientRawResponse if
         raw=true
        :rtype: ~lusidtr.models.UpsertCorporateActionsResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.batch_upsert_corporate_actions.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if actions is not None:
            body_content = self._serialize.body(actions, '[CreateCorporateAction]')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [201]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 201:
            deserialized = self._deserialize('UpsertCorporateActionsResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    batch_upsert_corporate_actions.metadata = {'url': '/data/lusid/corporateactions/{scope}/{code}'}

    def create_data_type(
            self, request=None, custom_headers=None, raw=False, **operation_config):
        """Create a new PropertyDataFormat. Note: Only non-default formats can be
        created.

        :param request: The definition of the new format
        :type request: ~lusidtr.models.CreateDataTypeRequest
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: DataType or ClientRawResponse if raw=true
        :rtype: ~lusidtr.models.DataType or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.create_data_type.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if request is not None:
            body_content = self._serialize.body(request, 'CreateDataTypeRequest')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [201]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 201:
            deserialized = self._deserialize('DataType', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    create_data_type.metadata = {'url': '/data/lusid/datatypes'}

    def list_data_types(
            self, scope, include_default=None, include_system=None, sort_by=None, start=None, limit=None, filter=None, custom_headers=None, raw=False, **operation_config):
        """Lists all property data formats in the specified scope.

        :param scope:
        :type scope: str
        :param include_default:
        :type include_default: bool
        :param include_system:
        :type include_system: bool
        :param sort_by:
        :type sort_by: list[str]
        :param start:
        :type start: int
        :param limit:
        :type limit: int
        :param filter:
        :type filter: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ResourceListOfDataType or ClientRawResponse if raw=true
        :rtype: ~lusidtr.models.ResourceListOfDataType or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.list_data_types.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if include_default is not None:
            query_parameters['includeDefault'] = self._serialize.query("include_default", include_default, 'bool')
        if include_system is not None:
            query_parameters['includeSystem'] = self._serialize.query("include_system", include_system, 'bool')
        if sort_by is not None:
            query_parameters['sortBy'] = self._serialize.query("sort_by", sort_by, '[str]', div=',')
        if start is not None:
            query_parameters['start'] = self._serialize.query("start", start, 'int')
        if limit is not None:
            query_parameters['limit'] = self._serialize.query("limit", limit, 'int')
        if filter is not None:
            query_parameters['filter'] = self._serialize.query("filter", filter, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ResourceListOfDataType', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    list_data_types.metadata = {'url': '/data/lusid/datatypes/{scope}'}

    def get_data_type(
            self, scope, name, custom_headers=None, raw=False, **operation_config):
        """Gets a property data format.

        :param scope:
        :type scope: str
        :param name:
        :type name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: DataType or ClientRawResponse if raw=true
        :rtype: ~lusidtr.models.DataType or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_data_type.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'name': self._serialize.url("name", name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('DataType', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_data_type.metadata = {'url': '/data/lusid/datatypes/{scope}/{name}'}

    def update_data_type(
            self, scope, name, request=None, custom_headers=None, raw=False, **operation_config):
        """Update a PropertyDataFormat. Note: Only non-default formats can be
        updated.

        :param scope: The scope of the format being updated
        :type scope: str
        :param name: The name of the format to update
        :type name: str
        :param request: The new definition of the format
        :type request: ~lusidtr.models.UpdateDataTypeRequest
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: DataType or ClientRawResponse if raw=true
        :rtype: ~lusidtr.models.DataType or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.update_data_type.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'name': self._serialize.url("name", name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if request is not None:
            body_content = self._serialize.body(request, 'UpdateDataTypeRequest')
        else:
            body_content = None

        # Construct and send request
        request = self._client.put(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('DataType', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    update_data_type.metadata = {'url': '/data/lusid/datatypes/{scope}/{name}'}

    def get_units_from_data_type(
            self, scope, name, units=None, filter=None, custom_headers=None, raw=False, **operation_config):
        """Return the definitions for the specified list of units.

        :param scope:
        :type scope: str
        :param name:
        :type name: str
        :param units:
        :type units: list[str]
        :param filter:
        :type filter: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: IUnitDefinition or ClientRawResponse if raw=true
        :rtype: ~lusidtr.models.IUnitDefinition or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_units_from_data_type.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'name': self._serialize.url("name", name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if units is not None:
            query_parameters['units'] = self._serialize.query("units", units, '[str]', div=',')
        if filter is not None:
            query_parameters['filter'] = self._serialize.query("filter", filter, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('IUnitDefinition', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_units_from_data_type.metadata = {'url': '/data/lusid/datatypes/{scope}/{name}/units'}

    def batch_add_client_instruments(
            self, definitions=None, custom_headers=None, raw=False, **operation_config):
        """Attempt to create one or more client instruments. Failed instruments
        will be identified in the body of the response.

        :param definitions:
        :type definitions: list[~lusidtr.models.CreateClientInstrumentRequest]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: TryAddClientInstruments or ClientRawResponse if raw=true
        :rtype: ~lusidtr.models.TryAddClientInstruments or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.batch_add_client_instruments.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if definitions is not None:
            body_content = self._serialize.body(definitions, '[CreateClientInstrumentRequest]')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [201]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 201:
            deserialized = self._deserialize('TryAddClientInstruments', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    batch_add_client_instruments.metadata = {'url': '/data/lusid/instruments'}

    def batch_delete_client_instruments(
            self, uids=None, custom_headers=None, raw=False, **operation_config):
        """Attempt to delete one or more client instruments. Failed instruments
        will be identified in the body of the response.

        :param uids:
        :type uids: list[str]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: DeleteClientInstrumentsResponse or ClientRawResponse if
         raw=true
        :rtype: ~lusidtr.models.DeleteClientInstrumentsResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.batch_delete_client_instruments.metadata['url']

        # Construct parameters
        query_parameters = {}
        if uids is not None:
            query_parameters['uids'] = self._serialize.query("uids", uids, '[str]', div=',')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('DeleteClientInstrumentsResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    batch_delete_client_instruments.metadata = {'url': '/data/lusid/instruments'}

    def get_instrument(
            self, uid, as_at=None, instrument_property_keys=None, custom_headers=None, raw=False, **operation_config):
        """Get an individual instrument by the unique instrument uid.  Optionally,
        decorate each instrument with specific properties.

        :param uid: The uid of the requested instrument
        :type uid: str
        :param as_at: As at date
        :type as_at: datetime
        :param instrument_property_keys: Keys of the properties to be
         retrieved
        :type instrument_property_keys: list[str]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Instrument or ClientRawResponse if raw=true
        :rtype: ~lusidtr.models.Instrument or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_instrument.metadata['url']
        path_format_arguments = {
            'uid': self._serialize.url("uid", uid, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if as_at is not None:
            query_parameters['asAt'] = self._serialize.query("as_at", as_at, 'iso-8601')
        if instrument_property_keys is not None:
            query_parameters['instrumentPropertyKeys'] = self._serialize.query("instrument_property_keys", instrument_property_keys, '[str]', div=',')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('Instrument', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_instrument.metadata = {'url': '/data/lusid/instruments/{uid}'}

    def lookup_instruments_from_codes_bulk(
            self, code_type=None, codes=None, as_at=None, instrument_property_keys=None, custom_headers=None, raw=False, **operation_config):
        """Lookup a large number of instruments by supplying a collection of
        non-Finbourne codes.  Optionally, decorate each instrument with
        specific properties.

        :param code_type: The type of identifier. Possible values include:
         'Undefined', 'ReutersAssetId', 'CINS', 'Isin', 'Sedol', 'Cusip',
         'Ticker', 'ClientInternal', 'Figi', 'CompositeFigi', 'ShareClassFigi',
         'Wertpapier'
        :type code_type: str
        :param codes: An array of codes
        :type codes: list[str]
        :param as_at: As at date
        :type as_at: datetime
        :param instrument_property_keys: Keys of the properties to be
         retrieved
        :type instrument_property_keys: list[str]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: LookupInstrumentsFromCodesResponse or ClientRawResponse if
         raw=true
        :rtype: ~lusidtr.models.LookupInstrumentsFromCodesResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.lookup_instruments_from_codes_bulk.metadata['url']

        # Construct parameters
        query_parameters = {}
        if code_type is not None:
            query_parameters['codeType'] = self._serialize.query("code_type", code_type, 'str')
        if as_at is not None:
            query_parameters['asAt'] = self._serialize.query("as_at", as_at, 'iso-8601')
        if instrument_property_keys is not None:
            query_parameters['instrumentPropertyKeys'] = self._serialize.query("instrument_property_keys", instrument_property_keys, '[str]', div=',')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if codes is not None:
            body_content = self._serialize.body(codes, '[str]')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('LookupInstrumentsFromCodesResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    lookup_instruments_from_codes_bulk.metadata = {'url': '/data/lusid/instruments/$lookup'}

    def batch_upsert_classifications(
            self, classifications=None, custom_headers=None, raw=False, **operation_config):
        """Update classification data.

        :param classifications:
        :type classifications: list[~lusidtr.models.InstrumentProperty]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: UpsertInstrumentPropertiesResponse or ClientRawResponse if
         raw=true
        :rtype: ~lusidtr.models.UpsertInstrumentPropertiesResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.batch_upsert_classifications.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if classifications is not None:
            body_content = self._serialize.body(classifications, '[InstrumentProperty]')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [201]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 201:
            deserialized = self._deserialize('UpsertInstrumentPropertiesResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    batch_upsert_classifications.metadata = {'url': '/data/lusid/instruments/$upsertproperties'}

    def get_lusid_versions(
            self, custom_headers=None, raw=False, **operation_config):
        """Returns the current major application version.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: VersionSummary or ClientRawResponse if raw=true
        :rtype: ~lusidtr.models.VersionSummary or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_lusid_versions.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('VersionSummary', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_lusid_versions.metadata = {'url': '/data/lusid/metadata/versions'}

    def get_multiple_property_definitions(
            self, keys=None, as_at=None, sort_by=None, start=None, limit=None, filter=None, custom_headers=None, raw=False, **operation_config):
        """Gets multiple property definitions.

        :param keys:
        :type keys: list[str]
        :param as_at:
        :type as_at: datetime
        :param sort_by:
        :type sort_by: list[str]
        :param start:
        :type start: int
        :param limit:
        :type limit: int
        :param filter:
        :type filter: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ResourceListOfPropertyDefinition or ClientRawResponse if
         raw=true
        :rtype: ~lusidtr.models.ResourceListOfPropertyDefinition or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_multiple_property_definitions.metadata['url']

        # Construct parameters
        query_parameters = {}
        if keys is not None:
            query_parameters['keys'] = self._serialize.query("keys", keys, '[str]', div=',')
        if as_at is not None:
            query_parameters['asAt'] = self._serialize.query("as_at", as_at, 'iso-8601')
        if sort_by is not None:
            query_parameters['sortBy'] = self._serialize.query("sort_by", sort_by, '[str]', div=',')
        if start is not None:
            query_parameters['start'] = self._serialize.query("start", start, 'int')
        if limit is not None:
            query_parameters['limit'] = self._serialize.query("limit", limit, 'int')
        if filter is not None:
            query_parameters['filter'] = self._serialize.query("filter", filter, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ResourceListOfPropertyDefinition', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_multiple_property_definitions.metadata = {'url': '/data/lusid/propertydefinitions'}

    def create_property_definition(
            self, definition=None, custom_headers=None, raw=False, **operation_config):
        """Creates a new property definition.

        :param definition:
        :type definition: ~lusidtr.models.CreatePropertyDefinitionRequest
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: PropertyDefinition or ClientRawResponse if raw=true
        :rtype: ~lusidtr.models.PropertyDefinition or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.create_property_definition.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if definition is not None:
            body_content = self._serialize.body(definition, 'CreatePropertyDefinitionRequest')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [201]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 201:
            deserialized = self._deserialize('PropertyDefinition', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    create_property_definition.metadata = {'url': '/data/lusid/propertydefinitions'}

    def get_property_definition(
            self, domain, scope, name, as_at=None, custom_headers=None, raw=False, **operation_config):
        """Gets a property definition.

        :param domain: Possible values include: 'Trade', 'Portfolio',
         'Security', 'Holding', 'ReferenceHolding', 'TxnType'
        :type domain: str
        :param scope:
        :type scope: str
        :param name:
        :type name: str
        :param as_at:
        :type as_at: datetime
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: PropertyDefinition or ClientRawResponse if raw=true
        :rtype: ~lusidtr.models.PropertyDefinition or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_property_definition.metadata['url']
        path_format_arguments = {
            'domain': self._serialize.url("domain", domain, 'str'),
            'scope': self._serialize.url("scope", scope, 'str'),
            'name': self._serialize.url("name", name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if as_at is not None:
            query_parameters['asAt'] = self._serialize.query("as_at", as_at, 'iso-8601')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('PropertyDefinition', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_property_definition.metadata = {'url': '/data/lusid/propertydefinitions/{domain}/{scope}/{name}'}

    def update_property_definition(
            self, domain, scope, name, definition=None, custom_headers=None, raw=False, **operation_config):
        """Updates the specified property definition.

        :param domain: Possible values include: 'Trade', 'Portfolio',
         'Security', 'Holding', 'ReferenceHolding', 'TxnType'
        :type domain: str
        :param scope:
        :type scope: str
        :param name:
        :type name: str
        :param definition:
        :type definition: ~lusidtr.models.UpdatePropertyDefinitionRequest
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: PropertyDefinition or ClientRawResponse if raw=true
        :rtype: ~lusidtr.models.PropertyDefinition or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.update_property_definition.metadata['url']
        path_format_arguments = {
            'domain': self._serialize.url("domain", domain, 'str'),
            'scope': self._serialize.url("scope", scope, 'str'),
            'name': self._serialize.url("name", name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if definition is not None:
            body_content = self._serialize.body(definition, 'UpdatePropertyDefinitionRequest')
        else:
            body_content = None

        # Construct and send request
        request = self._client.put(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('PropertyDefinition', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    update_property_definition.metadata = {'url': '/data/lusid/propertydefinitions/{domain}/{scope}/{name}'}

    def delete_property_definition(
            self, domain, scope, name, custom_headers=None, raw=False, **operation_config):
        """Deletes the property definition.

        :param domain: Possible values include: 'Trade', 'Portfolio',
         'Security', 'Holding', 'ReferenceHolding', 'TxnType'
        :type domain: str
        :param scope:
        :type scope: str
        :param name:
        :type name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: DeletedEntityResponse or ClientRawResponse if raw=true
        :rtype: ~lusidtr.models.DeletedEntityResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.delete_property_definition.metadata['url']
        path_format_arguments = {
            'domain': self._serialize.url("domain", domain, 'str'),
            'scope': self._serialize.url("scope", scope, 'str'),
            'name': self._serialize.url("name", name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('DeletedEntityResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    delete_property_definition.metadata = {'url': '/data/lusid/propertydefinitions/{domain}/{scope}/{name}'}

    def get_results(
            self, scope, key, date_parameter, as_at=None, sort_by=None, start=None, limit=None, custom_headers=None, raw=False, **operation_config):
        """Retrieve some previously stored results.

        :param scope: The scope of the data
        :type scope: str
        :param key: The key that identifies the data
        :type key: str
        :param date_parameter: The date for which the data was loaded
        :type date_parameter: datetime
        :param as_at:
        :type as_at: datetime
        :param sort_by:
        :type sort_by: list[str]
        :param start:
        :type start: int
        :param limit:
        :type limit: int
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Results or ClientRawResponse if raw=true
        :rtype: ~lusidtr.models.Results or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_results.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'key': self._serialize.url("key", key, 'str'),
            'date': self._serialize.url("date_parameter", date_parameter, 'iso-8601')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if as_at is not None:
            query_parameters['asAt'] = self._serialize.query("as_at", as_at, 'iso-8601')
        if sort_by is not None:
            query_parameters['sortBy'] = self._serialize.query("sort_by", sort_by, '[str]', div=',')
        if start is not None:
            query_parameters['start'] = self._serialize.query("start", start, 'int')
        if limit is not None:
            query_parameters['limit'] = self._serialize.query("limit", limit, 'int')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('Results', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_results.metadata = {'url': '/data/lusid/results/{scope}/{key}/{date}'}

    def upsert_results(
            self, scope, key, date_parameter, request=None, custom_headers=None, raw=False, **operation_config):
        """Upsert precalculated results against a specified scope/key/date
        combination.

        :param scope: The scope of the data
        :type scope: str
        :param key: The key that identifies the data
        :type key: str
        :param date_parameter: The date for which the data is relevant
        :type date_parameter: datetime
        :param request: The results to upload
        :type request: ~lusidtr.models.CreateResults
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Results or ClientRawResponse if raw=true
        :rtype: ~lusidtr.models.Results or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.upsert_results.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'key': self._serialize.url("key", key, 'str'),
            'date': self._serialize.url("date_parameter", date_parameter, 'iso-8601')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if request is not None:
            body_content = self._serialize.body(request, 'CreateResults')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('Results', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    upsert_results.metadata = {'url': '/data/lusid/results/{scope}/{key}/{date}'}

    def get_property_schema(
            self, property_keys=None, as_at=None, custom_headers=None, raw=False, **operation_config):
        """Get the schemas for the provided list of property keys.

        :param property_keys: A comma delimited list of property keys in
         string format. e.g.
         "Portfolio/default/PropertyName,Portfolio/differentScope/MyProperty"
        :type property_keys: list[str]
        :param as_at: AsAt date
        :type as_at: datetime
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: PropertySchema or ClientRawResponse if raw=true
        :rtype: ~lusidtr.models.PropertySchema or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_property_schema.metadata['url']

        # Construct parameters
        query_parameters = {}
        if property_keys is not None:
            query_parameters['propertyKeys'] = self._serialize.query("property_keys", property_keys, '[str]', div=',')
        if as_at is not None:
            query_parameters['asAt'] = self._serialize.query("as_at", as_at, 'iso-8601')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('PropertySchema', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_property_schema.metadata = {'url': '/data/lusid/schemas/properties'}

    def get_value_types(
            self, sort_by=None, start=None, limit=None, custom_headers=None, raw=False, **operation_config):
        """Gets the available value types that could be returned in a schema.

        :param sort_by:
        :type sort_by: list[str]
        :param start:
        :type start: int
        :param limit:
        :type limit: int
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ResourceListOfValueType or ClientRawResponse if raw=true
        :rtype: ~lusidtr.models.ResourceListOfValueType or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_value_types.metadata['url']

        # Construct parameters
        query_parameters = {}
        if sort_by is not None:
            query_parameters['sortBy'] = self._serialize.query("sort_by", sort_by, '[str]', div=',')
        if start is not None:
            query_parameters['start'] = self._serialize.query("start", start, 'int')
        if limit is not None:
            query_parameters['limit'] = self._serialize.query("limit", limit, 'int')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ResourceListOfValueType', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_value_types.metadata = {'url': '/data/lusid/schemas/types'}

    def list_configuration_transaction_types(
            self, custom_headers=None, raw=False, **operation_config):
        """Gets the list of persisted transaction types.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ResourceListOfTransactionMetaData or ClientRawResponse if
         raw=true
        :rtype: ~lusidtr.models.ResourceListOfTransactionMetaData or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.list_configuration_transaction_types.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ResourceListOfTransactionMetaData', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    list_configuration_transaction_types.metadata = {'url': '/data/lusid/systemconfiguration/transactiontypes'}

    def set_configuration_transaction_types(
            self, types=None, custom_headers=None, raw=False, **operation_config):
        """Uploads a list of transaction types to be used by the movements engine.

        :param types:
        :type types: list[~lusidtr.models.TransactionConfigurationDataRequest]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ResourceListOfTransactionMetaData or ClientRawResponse if
         raw=true
        :rtype: ~lusidtr.models.ResourceListOfTransactionMetaData or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.set_configuration_transaction_types.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if types is not None:
            body_content = self._serialize.body(types, '[TransactionConfigurationDataRequest]')
        else:
            body_content = None

        # Construct and send request
        request = self._client.put(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ResourceListOfTransactionMetaData', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    set_configuration_transaction_types.metadata = {'url': '/data/lusid/systemconfiguration/transactiontypes'}

    def add_configuration_transaction_type(
            self, type=None, custom_headers=None, raw=False, **operation_config):
        """Adds a new transaction type movement to the list of existing types.

        :param type:
        :type type: ~lusidtr.models.TransactionConfigurationDataRequest
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: TransactionConfigurationData or ClientRawResponse if raw=true
        :rtype: ~lusidtr.models.TransactionConfigurationData or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.add_configuration_transaction_type.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if type is not None:
            body_content = self._serialize.body(type, 'TransactionConfigurationDataRequest')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [201]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 201:
            deserialized = self._deserialize('TransactionConfigurationData', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    add_configuration_transaction_type.metadata = {'url': '/data/lusid/systemconfiguration/transactiontypes'}

    def list_portfolio_scopes(
            self, sort_by=None, start=None, limit=None, filter=None, custom_headers=None, raw=False, **operation_config):
        """List scopes that contain portfolios.

        Lists all scopes that have previously been used.

        :param sort_by: How to order the returned scopes
        :type sort_by: list[str]
        :param start: The starting index for the returned scopes
        :type start: int
        :param limit: The final index for the returned scopes
        :type limit: int
        :param filter: Filter to be applied to the list of scopes
        :type filter: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ResourceListOfScope or ClientRawResponse if raw=true
        :rtype: ~lusidtr.models.ResourceListOfScope or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.list_portfolio_scopes.metadata['url']

        # Construct parameters
        query_parameters = {}
        if sort_by is not None:
            query_parameters['sortBy'] = self._serialize.query("sort_by", sort_by, '[str]', div=',')
        if start is not None:
            query_parameters['start'] = self._serialize.query("start", start, 'int')
        if limit is not None:
            query_parameters['limit'] = self._serialize.query("limit", limit, 'int')
        if filter is not None:
            query_parameters['filter'] = self._serialize.query("filter", filter, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ResourceListOfScope', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    list_portfolio_scopes.metadata = {'url': '/data/portfolios/common'}

    def list_portfolios(
            self, scope, effective_at=None, as_at=None, sort_by=None, start=None, limit=None, filter=None, custom_headers=None, raw=False, **operation_config):
        """Get all portfolios.

        Get all portfolios in a scope.

        :param scope: The scope to get portfolios from
        :type scope: str
        :param effective_at: Effective date
        :type effective_at: datetime
        :param as_at: The asAt date to use
        :type as_at: datetime
        :param sort_by: The columns to sort the returned data by
        :type sort_by: list[str]
        :param start: How many items to skip from the returned set
        :type start: int
        :param limit: How many items to return from the set
        :type limit: int
        :param filter:
        :type filter: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ResourceListOfPortfolio or ClientRawResponse if raw=true
        :rtype: ~lusidtr.models.ResourceListOfPortfolio or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.list_portfolios.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if effective_at is not None:
            query_parameters['effectiveAt'] = self._serialize.query("effective_at", effective_at, 'iso-8601')
        if as_at is not None:
            query_parameters['asAt'] = self._serialize.query("as_at", as_at, 'iso-8601')
        if sort_by is not None:
            query_parameters['sortBy'] = self._serialize.query("sort_by", sort_by, '[str]', div=',')
        if start is not None:
            query_parameters['start'] = self._serialize.query("start", start, 'int')
        if limit is not None:
            query_parameters['limit'] = self._serialize.query("limit", limit, 'int')
        if filter is not None:
            query_parameters['filter'] = self._serialize.query("filter", filter, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ResourceListOfPortfolio', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    list_portfolios.metadata = {'url': '/data/portfolios/common/{scope}'}

    def get_portfolio(
            self, scope, code, effective_at=None, as_at=None, custom_headers=None, raw=False, **operation_config):
        """Get portfolio.

        Gets a single portfolio by code.

        :param scope: The scope of the portfolio
        :type scope: str
        :param code: Code for the portfolio
        :type code: str
        :param effective_at: Effective date
        :type effective_at: datetime
        :param as_at: The asAt date to use
        :type as_at: datetime
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Portfolio or ClientRawResponse if raw=true
        :rtype: ~lusidtr.models.Portfolio or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_portfolio.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if effective_at is not None:
            query_parameters['effectiveAt'] = self._serialize.query("effective_at", effective_at, 'iso-8601')
        if as_at is not None:
            query_parameters['asAt'] = self._serialize.query("as_at", as_at, 'iso-8601')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('Portfolio', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_portfolio.metadata = {'url': '/data/portfolios/common/{scope}/{code}'}

    def update_portfolio(
            self, scope, code, request=None, effective_at=None, custom_headers=None, raw=False, **operation_config):
        """Update portfolio.

        :param scope: The scope of the portfolio to be updated
        :type scope: str
        :param code: Code for the portfolio
        :type code: str
        :param request: The update request
        :type request: ~lusidtr.models.UpdatePortfolioRequest
        :param effective_at: The effective date for the change
        :type effective_at: datetime
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Portfolio or ClientRawResponse if raw=true
        :rtype: ~lusidtr.models.Portfolio or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.update_portfolio.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if effective_at is not None:
            query_parameters['effectiveAt'] = self._serialize.query("effective_at", effective_at, 'iso-8601')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if request is not None:
            body_content = self._serialize.body(request, 'UpdatePortfolioRequest')
        else:
            body_content = None

        # Construct and send request
        request = self._client.put(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('Portfolio', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    update_portfolio.metadata = {'url': '/data/portfolios/common/{scope}/{code}'}

    def delete_portfolio(
            self, scope, code, effective_at=None, custom_headers=None, raw=False, **operation_config):
        """Delete portfolio.

        Deletes a portfolio from the given effectiveAt.

        :param scope: The scope of the portfolio
        :type scope: str
        :param code: Code for the portfolio
        :type code: str
        :param effective_at: Effective date
        :type effective_at: datetime
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: DeletedEntityResponse or ClientRawResponse if raw=true
        :rtype: ~lusidtr.models.DeletedEntityResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.delete_portfolio.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if effective_at is not None:
            query_parameters['effectiveAt'] = self._serialize.query("effective_at", effective_at, 'iso-8601')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('DeletedEntityResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    delete_portfolio.metadata = {'url': '/data/portfolios/common/{scope}/{code}'}

    def get_portfolio_commands(
            self, scope, code, from_as_at=None, to_as_at=None, filter=None, custom_headers=None, raw=False, **operation_config):
        """Get modifications.

        Gets all commands that modified the portfolio.

        :param scope: The scope of the portfolio
        :type scope: str
        :param code: The portfolio id
        :type code: str
        :param from_as_at: Filters commands by those that were processed at or
         after this time. Null means there is no lower limit.
        :type from_as_at: datetime
        :param to_as_at: Filters commands by those that were processed at or
         before this time. Null means there is no upper limit (latest).
        :type to_as_at: datetime
        :param filter: Command filter
        :type filter: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ResourceListOfProcessedCommand or ClientRawResponse if
         raw=true
        :rtype: ~lusidtr.models.ResourceListOfProcessedCommand or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_portfolio_commands.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if from_as_at is not None:
            query_parameters['fromAsAt'] = self._serialize.query("from_as_at", from_as_at, 'iso-8601')
        if to_as_at is not None:
            query_parameters['toAsAt'] = self._serialize.query("to_as_at", to_as_at, 'iso-8601')
        if filter is not None:
            query_parameters['filter'] = self._serialize.query("filter", filter, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ResourceListOfProcessedCommand', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_portfolio_commands.metadata = {'url': '/data/portfolios/common/{scope}/{code}/commands'}

    def get_portfolio_properties(
            self, scope, code, effective_at=None, as_at=None, sort_by=None, start=None, limit=None, custom_headers=None, raw=False, **operation_config):
        """Get properties.

        Get properties attached to the portfolio.  If the asAt is not specified
        then
        the latest system time is used.

        :param scope: The scope of the portfolio
        :type scope: str
        :param code: Code for the portfolio
        :type code: str
        :param effective_at: Effective date
        :type effective_at: datetime
        :param as_at: The asAt date to use
        :type as_at: datetime
        :param sort_by: Property to sort the results by
        :type sort_by: list[str]
        :param start:
        :type start: int
        :param limit:
        :type limit: int
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: PortfolioProperties or ClientRawResponse if raw=true
        :rtype: ~lusidtr.models.PortfolioProperties or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_portfolio_properties.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if effective_at is not None:
            query_parameters['effectiveAt'] = self._serialize.query("effective_at", effective_at, 'iso-8601')
        if as_at is not None:
            query_parameters['asAt'] = self._serialize.query("as_at", as_at, 'iso-8601')
        if sort_by is not None:
            query_parameters['sortBy'] = self._serialize.query("sort_by", sort_by, '[str]', div=',')
        if start is not None:
            query_parameters['start'] = self._serialize.query("start", start, 'int')
        if limit is not None:
            query_parameters['limit'] = self._serialize.query("limit", limit, 'int')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('PortfolioProperties', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_portfolio_properties.metadata = {'url': '/data/portfolios/common/{scope}/{code}/properties'}

    def upsert_portfolio_properties(
            self, scope, code, portfolio_properties=None, effective_at=None, custom_headers=None, raw=False, **operation_config):
        """Update properties.

        Create one or more properties on a portfolio.

        :param scope: The scope of the portfolio
        :type scope: str
        :param code: Code for the portfolio
        :type code: str
        :param portfolio_properties:
        :type portfolio_properties: dict[str,
         ~lusidtr.models.CreatePropertyRequest]
        :param effective_at: The effective date for the change
        :type effective_at: datetime
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: PortfolioProperties or ClientRawResponse if raw=true
        :rtype: ~lusidtr.models.PortfolioProperties or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.upsert_portfolio_properties.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if effective_at is not None:
            query_parameters['effectiveAt'] = self._serialize.query("effective_at", effective_at, 'iso-8601')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if portfolio_properties is not None:
            body_content = self._serialize.body(portfolio_properties, '{CreatePropertyRequest}')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('PortfolioProperties', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    upsert_portfolio_properties.metadata = {'url': '/data/portfolios/common/{scope}/{code}/properties'}

    def delete_portfolio_properties(
            self, scope, code, effective_at=None, portfolio_property_keys=None, custom_headers=None, raw=False, **operation_config):
        """Delete one, many or all properties from a portfolio for a specified
        effective date.

        Specifying no properties will delete all properties.

        :param scope: The scope of the portfolio
        :type scope: str
        :param code: Code for the portfolio
        :type code: str
        :param effective_at: Effective date
        :type effective_at: datetime
        :param portfolio_property_keys: The keys of the property to be
         deleted. None specified indicates the intent to delete all properties
        :type portfolio_property_keys: list[str]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: DeletedEntityResponse or ClientRawResponse if raw=true
        :rtype: ~lusidtr.models.DeletedEntityResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.delete_portfolio_properties.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if effective_at is not None:
            query_parameters['effectiveAt'] = self._serialize.query("effective_at", effective_at, 'iso-8601')
        if portfolio_property_keys is not None:
            query_parameters['portfolioPropertyKeys'] = self._serialize.query("portfolio_property_keys", portfolio_property_keys, '[str]', div=',')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('DeletedEntityResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    delete_portfolio_properties.metadata = {'url': '/data/portfolios/common/{scope}/{code}/properties'}

    def create_derived_portfolio(
            self, scope, portfolio=None, custom_headers=None, raw=False, **operation_config):
        """Create derived portfolio.

        Creates a portfolio that derives from an existing portfolio.

        :param scope: The scope into which to create the new derived portfolio
        :type scope: str
        :param portfolio: The root object of the new derived portfolio,
         containing a populated reference portfolio id and reference scope
        :type portfolio:
         ~lusidtr.models.CreateDerivedTransactionPortfolioRequest
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Portfolio or ClientRawResponse if raw=true
        :rtype: ~lusidtr.models.Portfolio or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.create_derived_portfolio.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if portfolio is not None:
            body_content = self._serialize.body(portfolio, 'CreateDerivedTransactionPortfolioRequest')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [201]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 201:
            deserialized = self._deserialize('Portfolio', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    create_derived_portfolio.metadata = {'url': '/data/portfolios/derivedtransactionportfolios/{scope}'}

    def delete_derived_portfolio_details(
            self, scope, code, effective_at=None, custom_headers=None, raw=False, **operation_config):
        """Delete portfolio details.

        Deletes the portfolio details for the given code.

        :param scope: The scope of the portfolio
        :type scope: str
        :param code: Code for the portfolio
        :type code: str
        :param effective_at: The effective date of the change
        :type effective_at: datetime
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: DeletedEntityResponse or ClientRawResponse if raw=true
        :rtype: ~lusidtr.models.DeletedEntityResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.delete_derived_portfolio_details.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if effective_at is not None:
            query_parameters['effectiveAt'] = self._serialize.query("effective_at", effective_at, 'iso-8601')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('DeletedEntityResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    delete_derived_portfolio_details.metadata = {'url': '/data/portfolios/derivedtransactionportfolios/{scope}/{code}/details'}

    def list_portfolio_groups(
            self, scope, as_at=None, sort_by=None, start=None, limit=None, filter=None, custom_headers=None, raw=False, **operation_config):
        """List all groups in a specified scope.

        :param scope:
        :type scope: str
        :param as_at:
        :type as_at: datetime
        :param sort_by:
        :type sort_by: list[str]
        :param start:
        :type start: int
        :param limit:
        :type limit: int
        :param filter: A filter expression to apply to the result set
        :type filter: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ResourceListOfPortfolioGroup or ClientRawResponse if raw=true
        :rtype: ~lusidtr.models.ResourceListOfPortfolioGroup or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.list_portfolio_groups.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if as_at is not None:
            query_parameters['asAt'] = self._serialize.query("as_at", as_at, 'iso-8601')
        if sort_by is not None:
            query_parameters['sortBy'] = self._serialize.query("sort_by", sort_by, '[str]', div=',')
        if start is not None:
            query_parameters['start'] = self._serialize.query("start", start, 'int')
        if limit is not None:
            query_parameters['limit'] = self._serialize.query("limit", limit, 'int')
        if filter is not None:
            query_parameters['filter'] = self._serialize.query("filter", filter, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ResourceListOfPortfolioGroup', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    list_portfolio_groups.metadata = {'url': '/data/portfolios/portfoliogroups/{scope}'}

    def create_portfolio_group(
            self, scope, request=None, custom_headers=None, raw=False, **operation_config):
        """Create a new group.

        :param scope:
        :type scope: str
        :param request:
        :type request: ~lusidtr.models.CreatePortfolioGroupRequest
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: PortfolioGroup or ClientRawResponse if raw=true
        :rtype: ~lusidtr.models.PortfolioGroup or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.create_portfolio_group.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if request is not None:
            body_content = self._serialize.body(request, 'CreatePortfolioGroupRequest')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [201]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 201:
            deserialized = self._deserialize('PortfolioGroup', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    create_portfolio_group.metadata = {'url': '/data/portfolios/portfoliogroups/{scope}'}

    def get_portfolio_group(
            self, scope, code, as_at=None, custom_headers=None, raw=False, **operation_config):
        """Get an existing group.

        :param scope:
        :type scope: str
        :param code:
        :type code: str
        :param as_at:
        :type as_at: datetime
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: PortfolioGroup or ClientRawResponse if raw=true
        :rtype: ~lusidtr.models.PortfolioGroup or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_portfolio_group.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if as_at is not None:
            query_parameters['asAt'] = self._serialize.query("as_at", as_at, 'iso-8601')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('PortfolioGroup', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_portfolio_group.metadata = {'url': '/data/portfolios/portfoliogroups/{scope}/{code}'}

    def update_portfolio_group(
            self, scope, code, request=None, custom_headers=None, raw=False, **operation_config):
        """Update an existing group.

        :param scope:
        :type scope: str
        :param code:
        :type code: str
        :param request:
        :type request: ~lusidtr.models.UpdatePortfolioGroupRequest
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: PortfolioGroup or ClientRawResponse if raw=true
        :rtype: ~lusidtr.models.PortfolioGroup or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.update_portfolio_group.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if request is not None:
            body_content = self._serialize.body(request, 'UpdatePortfolioGroupRequest')
        else:
            body_content = None

        # Construct and send request
        request = self._client.put(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [201]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 201:
            deserialized = self._deserialize('PortfolioGroup', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    update_portfolio_group.metadata = {'url': '/data/portfolios/portfoliogroups/{scope}/{code}'}

    def delete_portfolio_group(
            self, scope, code, custom_headers=None, raw=False, **operation_config):
        """Delete a group.

        :param scope:
        :type scope: str
        :param code:
        :type code: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: DeletedEntityResponse or ClientRawResponse if raw=true
        :rtype: ~lusidtr.models.DeletedEntityResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.delete_portfolio_group.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('DeletedEntityResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    delete_portfolio_group.metadata = {'url': '/data/portfolios/portfoliogroups/{scope}/{code}'}

    def get_portfolio_group_commands(
            self, scope, code, from_as_at=None, to_as_at=None, sort_by=None, start=None, limit=None, filter=None, custom_headers=None, raw=False, **operation_config):
        """Gets all commands that modified the portfolio groups(s) with the
        specified id.

        :param scope: The scope of the portfolio group
        :type scope: str
        :param code: The portfolio group id
        :type code: str
        :param from_as_at: Filters commands by those that were processed at or
         after this time. Null means there is no lower limit.
        :type from_as_at: datetime
        :param to_as_at: Filters commands by those that were processed at or
         before this time. Null means there is no upper limit (latest).
        :type to_as_at: datetime
        :param sort_by:
        :type sort_by: list[str]
        :param start:
        :type start: int
        :param limit:
        :type limit: int
        :param filter: A filter expression to apply to the result set
        :type filter: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ResourceListOfProcessedCommand or ClientRawResponse if
         raw=true
        :rtype: ~lusidtr.models.ResourceListOfProcessedCommand or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_portfolio_group_commands.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if from_as_at is not None:
            query_parameters['fromAsAt'] = self._serialize.query("from_as_at", from_as_at, 'iso-8601')
        if to_as_at is not None:
            query_parameters['toAsAt'] = self._serialize.query("to_as_at", to_as_at, 'iso-8601')
        if sort_by is not None:
            query_parameters['sortBy'] = self._serialize.query("sort_by", sort_by, '[str]', div=',')
        if start is not None:
            query_parameters['start'] = self._serialize.query("start", start, 'int')
        if limit is not None:
            query_parameters['limit'] = self._serialize.query("limit", limit, 'int')
        if filter is not None:
            query_parameters['filter'] = self._serialize.query("filter", filter, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ResourceListOfProcessedCommand', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_portfolio_group_commands.metadata = {'url': '/data/portfolios/portfoliogroups/{scope}/{code}/commands'}

    def get_portfolio_group_expansion(
            self, scope, code, effective_at=None, as_at=None, property_filter=None, custom_headers=None, raw=False, **operation_config):
        """Get a full expansion of an existing group.

        :param scope:
        :type scope: str
        :param code:
        :type code: str
        :param effective_at:
        :type effective_at: datetime
        :param as_at:
        :type as_at: datetime
        :param property_filter:
        :type property_filter: list[str]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ExpandedGroup or ClientRawResponse if raw=true
        :rtype: ~lusidtr.models.ExpandedGroup or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_portfolio_group_expansion.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if effective_at is not None:
            query_parameters['effectiveAt'] = self._serialize.query("effective_at", effective_at, 'iso-8601')
        if as_at is not None:
            query_parameters['asAt'] = self._serialize.query("as_at", as_at, 'iso-8601')
        if property_filter is not None:
            query_parameters['propertyFilter'] = self._serialize.query("property_filter", property_filter, '[str]', div=',')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ExpandedGroup', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_portfolio_group_expansion.metadata = {'url': '/data/portfolios/portfoliogroups/{scope}/{code}/expansion'}

    def add_portfolio_to_group(
            self, scope, code, identifier=None, custom_headers=None, raw=False, **operation_config):
        """Add a portfolio to an existing group.

        :param scope:
        :type scope: str
        :param code:
        :type code: str
        :param identifier:
        :type identifier: ~lusidtr.models.ResourceId
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: PortfolioGroup or ClientRawResponse if raw=true
        :rtype: ~lusidtr.models.PortfolioGroup or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.add_portfolio_to_group.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if identifier is not None:
            body_content = self._serialize.body(identifier, 'ResourceId')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [201]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 201:
            deserialized = self._deserialize('PortfolioGroup', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    add_portfolio_to_group.metadata = {'url': '/data/portfolios/portfoliogroups/{scope}/{code}/portfolios'}

    def delete_portfolio_from_group(
            self, scope, code, portfolio_scope, portfolio_code, custom_headers=None, raw=False, **operation_config):
        """Remove a portfolio that is currently present within an existing group.

        :param scope:
        :type scope: str
        :param code:
        :type code: str
        :param portfolio_scope:
        :type portfolio_scope: str
        :param portfolio_code:
        :type portfolio_code: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: PortfolioGroup or ClientRawResponse if raw=true
        :rtype: ~lusidtr.models.PortfolioGroup or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.delete_portfolio_from_group.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str'),
            'portfolioScope': self._serialize.url("portfolio_scope", portfolio_scope, 'str'),
            'portfolioCode': self._serialize.url("portfolio_code", portfolio_code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('PortfolioGroup', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    delete_portfolio_from_group.metadata = {'url': '/data/portfolios/portfoliogroups/{scope}/{code}/portfolios/{portfolioScope}/{portfolioCode}'}

    def add_sub_group_to_group(
            self, scope, code, identifier=None, custom_headers=None, raw=False, **operation_config):
        """Add a sub group to an existing group.

        :param scope:
        :type scope: str
        :param code:
        :type code: str
        :param identifier:
        :type identifier: ~lusidtr.models.ResourceId
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: PortfolioGroup or ClientRawResponse if raw=true
        :rtype: ~lusidtr.models.PortfolioGroup or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.add_sub_group_to_group.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if identifier is not None:
            body_content = self._serialize.body(identifier, 'ResourceId')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [201]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 201:
            deserialized = self._deserialize('PortfolioGroup', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    add_sub_group_to_group.metadata = {'url': '/data/portfolios/portfoliogroups/{scope}/{code}/subgroups'}

    def delete_sub_group_from_group(
            self, scope, code, subgroup_scope, subgroup_code, custom_headers=None, raw=False, **operation_config):
        """Remove a subgroup that is currently present within an existing group.

        :param scope:
        :type scope: str
        :param code:
        :type code: str
        :param subgroup_scope:
        :type subgroup_scope: str
        :param subgroup_code:
        :type subgroup_code: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: PortfolioGroup or ClientRawResponse if raw=true
        :rtype: ~lusidtr.models.PortfolioGroup or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.delete_sub_group_from_group.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str'),
            'subgroupScope': self._serialize.url("subgroup_scope", subgroup_scope, 'str'),
            'subgroupCode': self._serialize.url("subgroup_code", subgroup_code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('PortfolioGroup', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    delete_sub_group_from_group.metadata = {'url': '/data/portfolios/portfoliogroups/{scope}/{code}/subgroups/{subgroupScope}/{subgroupCode}'}

    def create_reference_portfolio(
            self, scope, reference_portfolio=None, custom_headers=None, raw=False, **operation_config):
        """Create a new reference portfolio.

        :param scope: The intended scope of the portfolio
        :type scope: str
        :param reference_portfolio: The portfolio creation request object
        :type reference_portfolio:
         ~lusidtr.models.CreateReferencePortfolioRequest
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Portfolio or ClientRawResponse if raw=true
        :rtype: ~lusidtr.models.Portfolio or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.create_reference_portfolio.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if reference_portfolio is not None:
            body_content = self._serialize.body(reference_portfolio, 'CreateReferencePortfolioRequest')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [201]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 201:
            deserialized = self._deserialize('Portfolio', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    create_reference_portfolio.metadata = {'url': '/data/portfolios/referenceportfolios/{scope}'}

    def get_reference_portfolio_constituents(
            self, scope, code, effective_at, as_at=None, sort_by=None, start=None, limit=None, custom_headers=None, raw=False, **operation_config):
        """Get all the constituents in a reference portfolio.

        :param scope:
        :type scope: str
        :param code:
        :type code: str
        :param effective_at:
        :type effective_at: datetime
        :param as_at:
        :type as_at: datetime
        :param sort_by:
        :type sort_by: list[str]
        :param start:
        :type start: int
        :param limit:
        :type limit: int
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ResourceListOfReferencePortfolioConstituent or
         ClientRawResponse if raw=true
        :rtype: ~lusidtr.models.ResourceListOfReferencePortfolioConstituent or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_reference_portfolio_constituents.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str'),
            'effectiveAt': self._serialize.url("effective_at", effective_at, 'iso-8601')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if as_at is not None:
            query_parameters['asAt'] = self._serialize.query("as_at", as_at, 'iso-8601')
        if sort_by is not None:
            query_parameters['sortBy'] = self._serialize.query("sort_by", sort_by, '[str]', div=',')
        if start is not None:
            query_parameters['start'] = self._serialize.query("start", start, 'int')
        if limit is not None:
            query_parameters['limit'] = self._serialize.query("limit", limit, 'int')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ResourceListOfReferencePortfolioConstituent', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_reference_portfolio_constituents.metadata = {'url': '/data/portfolios/referenceportfolios/{scope}/{code}/{effectiveAt}/constituents'}

    def upsert_reference_portfolio_constituents(
            self, scope, code, effective_at, constituents=None, custom_headers=None, raw=False, **operation_config):
        """Add constituents to a specific reference portfolio.

        :param scope:
        :type scope: str
        :param code:
        :type code: str
        :param effective_at:
        :type effective_at: datetime
        :param constituents:
        :type constituents:
         list[~lusidtr.models.ReferencePortfolioConstituentRequest]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: UpsertReferencePortfolioConstituentsResponse or
         ClientRawResponse if raw=true
        :rtype: ~lusidtr.models.UpsertReferencePortfolioConstituentsResponse
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.upsert_reference_portfolio_constituents.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str'),
            'effectiveAt': self._serialize.url("effective_at", effective_at, 'iso-8601')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if constituents is not None:
            body_content = self._serialize.body(constituents, '[ReferencePortfolioConstituentRequest]')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('UpsertReferencePortfolioConstituentsResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    upsert_reference_portfolio_constituents.metadata = {'url': '/data/portfolios/referenceportfolios/{scope}/{code}/{effectiveAt}/constituents'}

    def create_portfolio(
            self, scope, create_request=None, custom_headers=None, raw=False, **operation_config):
        """Create portfolio.

        Creates a new portfolio.

        :param scope: The intended scope of the portfolio
        :type scope: str
        :param create_request: The portfolio creation request object
        :type create_request:
         ~lusidtr.models.CreateTransactionPortfolioRequest
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Portfolio or ClientRawResponse if raw=true
        :rtype: ~lusidtr.models.Portfolio or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.create_portfolio.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if create_request is not None:
            body_content = self._serialize.body(create_request, 'CreateTransactionPortfolioRequest')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [201]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 201:
            deserialized = self._deserialize('Portfolio', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    create_portfolio.metadata = {'url': '/data/portfolios/transactionportfolios/{scope}'}

    def get_details(
            self, scope, code, effective_at=None, as_at=None, custom_headers=None, raw=False, **operation_config):
        """Get portfolio details.

        Gets the details for a portfolio.  For a derived portfolio this can be
        the details of another reference portfolio.

        :param scope: The scope of the portfolio
        :type scope: str
        :param code: Code for the portfolio
        :type code: str
        :param effective_at: Effective date
        :type effective_at: datetime
        :param as_at: The asAt date to use
        :type as_at: datetime
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: PortfolioDetails or ClientRawResponse if raw=true
        :rtype: ~lusidtr.models.PortfolioDetails or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_details.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if effective_at is not None:
            query_parameters['effectiveAt'] = self._serialize.query("effective_at", effective_at, 'iso-8601')
        if as_at is not None:
            query_parameters['asAt'] = self._serialize.query("as_at", as_at, 'iso-8601')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('PortfolioDetails', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_details.metadata = {'url': '/data/portfolios/transactionportfolios/{scope}/{code}/details'}

    def upsert_portfolio_details(
            self, scope, code, details=None, effective_at=None, custom_headers=None, raw=False, **operation_config):
        """Add/update portfolio details.

        Update the portfolio details for the given code or add if it doesn't
        already exist. Updates with
        null values will remove any existing values.

        :param scope: The scope of the portfolio
        :type scope: str
        :param code: Code for the portfolio
        :type code: str
        :param details:
        :type details: ~lusidtr.models.CreatePortfolioDetails
        :param effective_at: The effective date of the change
        :type effective_at: datetime
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: PortfolioDetails or ClientRawResponse if raw=true
        :rtype: ~lusidtr.models.PortfolioDetails or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.upsert_portfolio_details.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if effective_at is not None:
            query_parameters['effectiveAt'] = self._serialize.query("effective_at", effective_at, 'iso-8601')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if details is not None:
            body_content = self._serialize.body(details, 'CreatePortfolioDetails')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('PortfolioDetails', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    upsert_portfolio_details.metadata = {'url': '/data/portfolios/transactionportfolios/{scope}/{code}/details'}

    def get_holdings(
            self, scope, code, effective_at=None, as_at=None, sort_by=None, start=None, limit=None, filter=None, instrument_property_keys=None, custom_headers=None, raw=False, **operation_config):
        """Get holdings.

        Get the aggregate holdings of a portfolio.  If no effectiveAt or asAt
        are supplied then values will be defaulted to the latest system time.

        :param scope: The scope of the portfolio
        :type scope: str
        :param code: Code for the portfolio
        :type code: str
        :param effective_at: Effective date
        :type effective_at: datetime
        :param as_at: As at date
        :type as_at: datetime
        :param sort_by: The columns to sort the returned data by
        :type sort_by: list[str]
        :param start: How many items to skip from the returned set
        :type start: int
        :param limit: How many items to return from the set
        :type limit: int
        :param filter: A filter on the results
        :type filter: str
        :param instrument_property_keys: Keys for the instrument properties to
         be decorated onto the holdings
        :type instrument_property_keys: list[str]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: VersionedResourceListOfHolding or ClientRawResponse if
         raw=true
        :rtype: ~lusidtr.models.VersionedResourceListOfHolding or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_holdings.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if effective_at is not None:
            query_parameters['effectiveAt'] = self._serialize.query("effective_at", effective_at, 'iso-8601')
        if as_at is not None:
            query_parameters['asAt'] = self._serialize.query("as_at", as_at, 'iso-8601')
        if sort_by is not None:
            query_parameters['sortBy'] = self._serialize.query("sort_by", sort_by, '[str]', div=',')
        if start is not None:
            query_parameters['start'] = self._serialize.query("start", start, 'int')
        if limit is not None:
            query_parameters['limit'] = self._serialize.query("limit", limit, 'int')
        if filter is not None:
            query_parameters['filter'] = self._serialize.query("filter", filter, 'str')
        if instrument_property_keys is not None:
            query_parameters['instrumentPropertyKeys'] = self._serialize.query("instrument_property_keys", instrument_property_keys, '[str]', div=',')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('VersionedResourceListOfHolding', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_holdings.metadata = {'url': '/data/portfolios/transactionportfolios/{scope}/{code}/holdings'}

    def set_holdings(
            self, scope, code, effective_at, holding_adjustments=None, custom_headers=None, raw=False, **operation_config):
        """Adjust holdings.

        Create transactions in a specific portfolio to bring it to the
        specified holdings.

        :param scope: The scope of the portfolio
        :type scope: str
        :param code: Code for the portfolio
        :type code: str
        :param effective_at: Effective date
        :type effective_at: datetime
        :param holding_adjustments:
        :type holding_adjustments: list[~lusidtr.models.AdjustHoldingRequest]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: AdjustHolding or ClientRawResponse if raw=true
        :rtype: ~lusidtr.models.AdjustHolding or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.set_holdings.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str'),
            'effectiveAt': self._serialize.url("effective_at", effective_at, 'iso-8601')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if holding_adjustments is not None:
            body_content = self._serialize.body(holding_adjustments, '[AdjustHoldingRequest]')
        else:
            body_content = None

        # Construct and send request
        request = self._client.put(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('AdjustHolding', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    set_holdings.metadata = {'url': '/data/portfolios/transactionportfolios/{scope}/{code}/holdings/{effectiveAt}'}

    def adjust_holdings(
            self, scope, code, effective_at, holding_adjustments=None, custom_headers=None, raw=False, **operation_config):
        """Adjust holdings.

        Create transactions in a specific portfolio to bring it to the
        specified holdings.

        :param scope: The scope of the portfolio
        :type scope: str
        :param code: Code for the portfolio
        :type code: str
        :param effective_at: Effective date
        :type effective_at: datetime
        :param holding_adjustments:
        :type holding_adjustments: list[~lusidtr.models.AdjustHoldingRequest]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: AdjustHolding or ClientRawResponse if raw=true
        :rtype: ~lusidtr.models.AdjustHolding or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.adjust_holdings.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str'),
            'effectiveAt': self._serialize.url("effective_at", effective_at, 'iso-8601')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if holding_adjustments is not None:
            body_content = self._serialize.body(holding_adjustments, '[AdjustHoldingRequest]')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('AdjustHolding', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    adjust_holdings.metadata = {'url': '/data/portfolios/transactionportfolios/{scope}/{code}/holdings/{effectiveAt}'}

    def cancel_adjust_holdings(
            self, scope, code, effective_at, custom_headers=None, raw=False, **operation_config):
        """Cancel adjust-holdings.

        Cancels a previous adjust holdings request.

        :param scope: The scope of the portfolio
        :type scope: str
        :param code: Code for the portfolio
        :type code: str
        :param effective_at: Effective date
        :type effective_at: datetime
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: DeletedEntityResponse or ClientRawResponse if raw=true
        :rtype: ~lusidtr.models.DeletedEntityResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.cancel_adjust_holdings.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str'),
            'effectiveAt': self._serialize.url("effective_at", effective_at, 'iso-8601')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('DeletedEntityResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    cancel_adjust_holdings.metadata = {'url': '/data/portfolios/transactionportfolios/{scope}/{code}/holdings/{effectiveAt}'}

    def list_holdings_adjustments(
            self, scope, code, from_effective_at=None, to_effective_at=None, as_at_time=None, custom_headers=None, raw=False, **operation_config):
        """Gets holdings adjustments in an interval of effective time.

        :param scope: The scope of the portfolio
        :type scope: str
        :param code: Code for the portfolio
        :type code: str
        :param from_effective_at: Events between this time (inclusive) and the
         toEffectiveAt are returned.
        :type from_effective_at: datetime
        :param to_effective_at: Events between this time (inclusive) and the
         fromEffectiveAt are returned.
        :type to_effective_at: datetime
        :param as_at_time: The as-at time for which the result is valid.
        :type as_at_time: datetime
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ResourceListOfHoldingsAdjustmentHeader or ClientRawResponse
         if raw=true
        :rtype: ~lusidtr.models.ResourceListOfHoldingsAdjustmentHeader or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.list_holdings_adjustments.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if from_effective_at is not None:
            query_parameters['fromEffectiveAt'] = self._serialize.query("from_effective_at", from_effective_at, 'iso-8601')
        if to_effective_at is not None:
            query_parameters['toEffectiveAt'] = self._serialize.query("to_effective_at", to_effective_at, 'iso-8601')
        if as_at_time is not None:
            query_parameters['asAtTime'] = self._serialize.query("as_at_time", as_at_time, 'iso-8601')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ResourceListOfHoldingsAdjustmentHeader', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    list_holdings_adjustments.metadata = {'url': '/data/portfolios/transactionportfolios/{scope}/{code}/holdingsadjustments'}

    def get_holdings_adjustment(
            self, scope, code, effective_at, as_at_time=None, custom_headers=None, raw=False, **operation_config):
        """Get a holdings adjustment for a single portfolio at a specific
        effective time.
        If no adjustment exists at this effective time, not found is returned.

        :param scope: The scope of the portfolio
        :type scope: str
        :param code: Code for the portfolio
        :type code: str
        :param effective_at: The effective time of the holdings adjustment.
        :type effective_at: datetime
        :param as_at_time: The as-at time for which the result is valid.
        :type as_at_time: datetime
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: HoldingsAdjustment or ClientRawResponse if raw=true
        :rtype: ~lusidtr.models.HoldingsAdjustment or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_holdings_adjustment.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str'),
            'effectiveAt': self._serialize.url("effective_at", effective_at, 'iso-8601')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if as_at_time is not None:
            query_parameters['asAtTime'] = self._serialize.query("as_at_time", as_at_time, 'iso-8601')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('HoldingsAdjustment', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_holdings_adjustment.metadata = {'url': '/data/portfolios/transactionportfolios/{scope}/{code}/holdingsadjustments/{effectiveAt}'}

    def get_transactions(
            self, scope, code, from_transaction_date=None, to_transaction_date=None, as_at=None, sort_by=None, start=None, limit=None, instrument_property_keys=None, filter=None, custom_headers=None, raw=False, **operation_config):
        """Get transactions.

        :param scope: The scope of the portfolio
        :type scope: str
        :param code: Code for the portfolio
        :type code: str
        :param from_transaction_date: Include transactions with a transaction
         date equal or later than this date. If not supplied, no lower filter
         is applied
        :type from_transaction_date: datetime
        :param to_transaction_date: Include transactions with a transaction
         date equal or before this date. If not supplied, no upper filter is
         applied
        :type to_transaction_date: datetime
        :param as_at:
        :type as_at: datetime
        :param sort_by: The columns to sort the returned data by
        :type sort_by: list[str]
        :param start: How many items to skip from the returned set
        :type start: int
        :param limit: How many items to return from the set
        :type limit: int
        :param instrument_property_keys: Keys for the instrument properties to
         be decorated onto the transactions
        :type instrument_property_keys: list[str]
        :param filter: Transaction filter
        :type filter: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: VersionedResourceListOfTransaction or ClientRawResponse if
         raw=true
        :rtype: ~lusidtr.models.VersionedResourceListOfTransaction or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_transactions.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if from_transaction_date is not None:
            query_parameters['fromTransactionDate'] = self._serialize.query("from_transaction_date", from_transaction_date, 'iso-8601')
        if to_transaction_date is not None:
            query_parameters['toTransactionDate'] = self._serialize.query("to_transaction_date", to_transaction_date, 'iso-8601')
        if as_at is not None:
            query_parameters['asAt'] = self._serialize.query("as_at", as_at, 'iso-8601')
        if sort_by is not None:
            query_parameters['sortBy'] = self._serialize.query("sort_by", sort_by, '[str]', div=',')
        if start is not None:
            query_parameters['start'] = self._serialize.query("start", start, 'int')
        if limit is not None:
            query_parameters['limit'] = self._serialize.query("limit", limit, 'int')
        if instrument_property_keys is not None:
            query_parameters['instrumentPropertyKeys'] = self._serialize.query("instrument_property_keys", instrument_property_keys, '[str]', div=',')
        if filter is not None:
            query_parameters['filter'] = self._serialize.query("filter", filter, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('VersionedResourceListOfTransaction', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_transactions.metadata = {'url': '/data/portfolios/transactionportfolios/{scope}/{code}/transactions'}

    def upsert_transactions(
            self, scope, code, transactions=None, custom_headers=None, raw=False, **operation_config):
        """Upsert transactions.

        :param scope: The scope of the portfolio
        :type scope: str
        :param code: Code for the portfolio
        :type code: str
        :param transactions: The transactions to be updated
        :type transactions: list[~lusidtr.models.TransactionRequest]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: UpsertPortfolioTransactionsResponse or ClientRawResponse if
         raw=true
        :rtype: ~lusidtr.models.UpsertPortfolioTransactionsResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.upsert_transactions.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if transactions is not None:
            body_content = self._serialize.body(transactions, '[TransactionRequest]')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('UpsertPortfolioTransactionsResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    upsert_transactions.metadata = {'url': '/data/portfolios/transactionportfolios/{scope}/{code}/transactions'}

    def delete_transactions(
            self, scope, code, id=None, custom_headers=None, raw=False, **operation_config):
        """Delete transactions.

        Delete one or more transactions from a portfolio.

        :param scope: The scope of the portfolio
        :type scope: str
        :param code: Code for the portfolio
        :type code: str
        :param id: Ids of transactions to delete
        :type id: list[str]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: DeletedEntityResponse or ClientRawResponse if raw=true
        :rtype: ~lusidtr.models.DeletedEntityResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.delete_transactions.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if id is not None:
            query_parameters['id'] = self._serialize.query("id", id, '[str]', div=',')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('DeletedEntityResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    delete_transactions.metadata = {'url': '/data/portfolios/transactionportfolios/{scope}/{code}/transactions'}

    def add_transaction_property(
            self, scope, code, transaction_id, transaction_properties=None, custom_headers=None, raw=False, **operation_config):
        """Add/update transaction properties.

        Add one or more properties to a specific transaction in a portfolio.

        :param scope: The scope of the portfolio
        :type scope: str
        :param code: Code for the portfolio
        :type code: str
        :param transaction_id: Id of transaction to add properties to
        :type transaction_id: str
        :param transaction_properties: Transaction properties to add
        :type transaction_properties: dict[str,
         ~lusidtr.models.CreatePerpetualPropertyRequest]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: AddTransactionPropertyResponse or ClientRawResponse if
         raw=true
        :rtype: ~lusidtr.models.AddTransactionPropertyResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.add_transaction_property.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str'),
            'transactionId': self._serialize.url("transaction_id", transaction_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if transaction_properties is not None:
            body_content = self._serialize.body(transaction_properties, '{CreatePerpetualPropertyRequest}')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [201]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 201:
            deserialized = self._deserialize('AddTransactionPropertyResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    add_transaction_property.metadata = {'url': '/data/portfolios/transactionportfolios/{scope}/{code}/transactions/{transactionId}/properties'}

    def delete_property_from_transaction(
            self, scope, code, transaction_id, transaction_property_key=None, custom_headers=None, raw=False, **operation_config):
        """Delete transaction property.

        Delete a property from a specific transaction.

        :param scope: The scope of the portfolio
        :type scope: str
        :param code: Code for the portfolio
        :type code: str
        :param transaction_id: Id of the transaction to delete the property
         from
        :type transaction_id: str
        :param transaction_property_key: The key of the property to be deleted
        :type transaction_property_key: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: DeletedEntityResponse or ClientRawResponse if raw=true
        :rtype: ~lusidtr.models.DeletedEntityResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.delete_property_from_transaction.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str'),
            'transactionId': self._serialize.url("transaction_id", transaction_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if transaction_property_key is not None:
            query_parameters['transactionPropertyKey'] = self._serialize.query("transaction_property_key", transaction_property_key, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('DeletedEntityResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    delete_property_from_transaction.metadata = {'url': '/data/portfolios/transactionportfolios/{scope}/{code}/transactions/{transactionId}/properties'}

    def build_transactions(
            self, scope, code, as_at=None, sort_by=None, start=None, limit=None, instrument_property_keys=None, filter=None, parameters=None, custom_headers=None, raw=False, **operation_config):
        """Get transactions.

        :param scope: The scope of the portfolio
        :type scope: str
        :param code: Code for the portfolio
        :type code: str
        :param as_at:
        :type as_at: datetime
        :param sort_by: The columns to sort the returned data by
        :type sort_by: list[str]
        :param start: How many items to skip from the returned set
        :type start: int
        :param limit: How many items to return from the set
        :type limit: int
        :param instrument_property_keys: Keys for the instrument properties to
         be decorated onto the trades
        :type instrument_property_keys: list[str]
        :param filter: Trade filter
        :type filter: str
        :param parameters: Core query parameters
        :type parameters: ~lusidtr.models.TransactionQueryParameters
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: VersionedResourceListOfOutputTransaction or ClientRawResponse
         if raw=true
        :rtype: ~lusidtr.models.VersionedResourceListOfOutputTransaction or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.build_transactions.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if as_at is not None:
            query_parameters['asAt'] = self._serialize.query("as_at", as_at, 'iso-8601')
        if sort_by is not None:
            query_parameters['sortBy'] = self._serialize.query("sort_by", sort_by, '[str]', div=',')
        if start is not None:
            query_parameters['start'] = self._serialize.query("start", start, 'int')
        if limit is not None:
            query_parameters['limit'] = self._serialize.query("limit", limit, 'int')
        if instrument_property_keys is not None:
            query_parameters['instrumentPropertyKeys'] = self._serialize.query("instrument_property_keys", instrument_property_keys, '[str]', div=',')
        if filter is not None:
            query_parameters['filter'] = self._serialize.query("filter", filter, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if parameters is not None:
            body_content = self._serialize.body(parameters, 'TransactionQueryParameters')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('VersionedResourceListOfOutputTransaction', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    build_transactions.metadata = {'url': '/data/portfolios/transactionportfolios/{scope}/{code}/transactions/$build'}
