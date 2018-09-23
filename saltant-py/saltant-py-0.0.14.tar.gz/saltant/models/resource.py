"""Contains base classes for models and related classes."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from saltant.exceptions import BadHttpRequestError
from saltant.constants import (
    HTTP_200_OK,
)

class Model(object):
    """Base class for representing a model."""
    def __str__(self):
        """String representation of model."""
        raise NotImplementedError


class ModelManager(object):
    """Base class for a model manager.

    Attributes:
        _client (:py:class:`saltant.client.Client`): An authenticated
            saltant client.
        list_url (str): The URL to list models.
        detail_url (str): The URL format to get specific models.
        model (:py:class:`saltant.models.resource.Model`): The model
            being used.
    """
    list_url = "NotImplemented"
    detail_url = "NotImplemented"
    model = Model

    def __init__(self, _client):
        """Save the client so we can make API calls in the manager.

        Args:
            _client (:py:class:`saltant.client.Client`): An
                authenticated saltant client.
        """
        self._client = _client

    def list(self, filters=None):
        """List model instances.

        Currently this gets *everything* and iterates through all
        possible pages in the API. This may be unsuitable for production
        environments with huge databases, so finer grained page support
        should likely be added at some point.

        Args:
            filters (dict, optional): API query filters to apply to the
                request. For example,

                {'name__startswith': 'azure',
                 'user__in': [1, 2, 3, 4],}

        Returns:
            list: A list of :class:`Model` instances matching the query
                parameters
        """
        # Add in the page and page_size parameters to the filter, such
        # that our request gets *all* objects in the list. However,
        # don't do this if the user has explicitly included these
        # parameters in the filter.
        if not filters:
            filters = {}

        if 'page' not in filters:
            filters['page'] = 1

        if 'page_size' not in filters:
            # The below "magic number" is 2^63 - 1, which is the largest
            # number you can hold in a 64 bit integer. The main point
            # here is that we want to get everything in one page (unless
            # otherwise specified, of course).
            filters['page_size'] = 9223372036854775807

        # Form the request URL - first add in the query filters
        query_filter_sub_url = ''

        for idx, filter_param in enumerate(filters):
            # Prepend '?' or '&'
            if idx == 0:
                query_filter_sub_url += '?'
            else:
                query_filter_sub_url += '&'

            # Add in the query filter
            query_filter_sub_url += '{param}={val}'.format(
                param=filter_param,
                val=filters[filter_param],
            )

        # Stitch together all sub-urls
        request_url = (
            self._client.base_api_url
            + self.list_url
            + query_filter_sub_url)

        # Make the request
        response = self._client.session.get(request_url)

        # Validate that the request was successful
        self.validate_request_success(
            response_text=response.text,
            request_url=request_url,
            status_code=response.status_code,
            expected_status_code=HTTP_200_OK,)

        # Return a list of model instances
        return self.response_data_to_model_instances_list(response.json())

    def get(self, id):
        """Get the model instance with a given id.

        Args:
            id (str): The primary identifier (e.g., pk or UUID) for the
                task instance to get.

        Returns:
            :class:`Model`: A model instance representing the resource
                requested.
        """
        # Get the object
        request_url = (
            self._client.base_api_url
            + self.detail_url.format(id=id))

        response = self._client.session.get(request_url)

        # Validate that the request was successful
        self.validate_request_success(
            response_text=response.text,
            request_url=request_url,
            status_code=response.status_code,
            expected_status_code=HTTP_200_OK,)

        # Return a model instance
        return self.response_data_to_model_instance(response.json())

    def create(self):
        """Create an instance of a model."""
        raise NotImplementedError

    @classmethod
    def response_data_to_model_instance(cls, response_data):
        """Convert get response data to a model.

        Args:
            response_data (dict): The data from the request's response.

        Returns:
            :obj:`saltant.models.resource.Model`:
                A model instance representing the resource from the
                response data.
        """
        # Instantiate a model
        return cls.model(**response_data)

    @classmethod
    def response_data_to_model_instances_list(cls, response_data):
        """Convert list response data to a list of models.

        Args:
            response_data (dict): The data from the request's response.

        Returns:
            list: A list of :class:`Model` instances.
        """
        return [cls.response_data_to_model_instance(subdata)
                for subdata in response_data['results']]

    @staticmethod
    def validate_request_success(
            response_text,
            request_url,
            status_code,
            expected_status_code,):
        """Validates that a request was successful.

        Args:
            response_text (str): The response body of the request.
            request_url (str): The URL the request was made at.
            status_code (int): The status code of the response.
            expected_status_code (int): The expected status code of the
                response.

        Raises:
            :py:class:`saltant.exceptions.BadHttpRequestError`: The HTTP
                request failed.
        """
        try:
            assert status_code == expected_status_code
        except AssertionError:
            msg = ("Request to {url} failed with status {status_code}:\n"
                   "The reponse from the request was as follows:\n\n"
                   "{content}").format(
                       url=request_url,
                       status_code=status_code,
                       content=response_text,)
            raise BadHttpRequestError(msg)
