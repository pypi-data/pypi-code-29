from __future__ import absolute_import, unicode_literals

__all__ = ['Stream']


from c8.api import APIWrapper
from c8.request import Request
from c8.executor import (
    DefaultExecutor
)
from c8.exceptions import (
    StreamPropertiesError,
    StreamStatisticsError,
    TopicDeleteError,
    TopicListError,
)


class Stream(APIWrapper):
    """Base class for Stream API wrappers.

    :param connection: HTTP connection.
    :type connection: c8.connection.Connection
    :param executor: API executor.
    :type executor: c8.executor.Executor
    """

    def __init__(self, connection, executor):
        super(Stream, self).__init__(connection, executor)

    def __init__(self, connection):
        super(Stream, self).__init__(
            connection=connection,
            executor=DefaultExecutor(connection)
        )

    @property
    def name(self):
        """Return stream name.

        :return: stream name.
        :rtype: str | unicode
        """
        return self.stream_name


    def get_properties(self):
        """Return policies assigned to the stream

        :return: list of policies
        :rtype: [obj]
        :raise c8.exceptions.StreamPropertiesError: If retrieval fails.
        """
        request = Request(
            method='get',
            endpoint='/c8/_tenant/<tenant-name>/_streams/<stream-name>', #sample
        )

        def response_handler(resp):
            if not resp.is_success:
                raise StreamPropertiesError(resp, request)
            return resp.body['version']

        return self._execute(request, response_handler)

    def get_replication_clusters(self):
        """Return list of regions the stream is replicated to

        :return: list of regions
        :rtype: [string]
        :raise c8.exceptions.StreamPropertiesError: If retrieval fails.
        """
        request = Request(
            method='get',
            endpoint='/c8/_tenant/<tenant-name>/_streams/<stream-name>/replication', #sample
        )

        def response_handler(resp):
            if not resp.is_success:
                raise StreamPropertiesError(resp, request)
            return resp.body['version']

        return self._execute(request, response_handler)

    def set_replication_clusters(self, dclist=[]):
        """Set replication clusters

        :param dclist: list of regions
        :type dclist: [str]

        :return: True if replication clusters were set successfully.
        :rtype: bool
        :raise c8.exceptions.StreamPropertiesError: If create fails.
        """
        request = Request(
            method='post',
            endpoint='/c8/_tenant/<tenant-name>/_streams/<stream-name>/replication',
            data=dclist
        )

        def response_handler(resp):
            if not resp.is_success:
                raise StreamPropertiesError(resp, request)
            return True

        return self._execute(request, response_handler)

    def get_statistics(self):
        """Return stream statistics.

        :return: Stream statistics.
        :rtype: dict
        :raise c8.exceptions.StreamStatisticsError: If retrieval fails.
        """
        url = '/c8/_tenant/<tenant-name>/_streams/<stream-name>/stats'

        request = Request(
            method='get',
            endpoint=url
        )

        def response_handler(resp):
            if not resp.is_success:
                raise StreamStatisticsError(resp, request)
            return resp.body

        return self._execute(request, response_handler)

    ###################
    # Topic Management
    ###################

    def topics(self):
        """Return the names of all topics for this stream .

        :return: topic names.
        :rtype: [str | unicode]
        :raise c8.exceptions.TopicListError: If retrieval fails.
        """
        url = "/c8/_tenant/<tenant-name>/_streams/<stream-name>/topics"

        request = Request(
            method='get',
            endpoint=url  # sample
        )

        def response_handler(resp):
            if not resp.is_success:
                raise TopicListError(resp, request)
            return resp.body['result']

        return self._execute(request, response_handler)

    def has_topic(self, name):
        """Check if a topic exists.

        :param name: topic name.
        :type name: str | unicode
        :return: True if topic exists, False otherwise.
        :rtype: bool
        """
        return name in self.topics()

    def delete_topic(self, name, force=False, authoritative=False):
        """Delete topic.

        :param name: topic name.
        :type name: str | unicode
        :param force: Force delete topic ignoring connected clients
        :type ignore_missing: bool
        :return: True if topic is deleted successfully.
        :rtype: bool
        :raise c8.exceptions.TopicDeleteError: If delete fails.
        """
        request = Request(
            method='delete',
            endpoint='/c8/_tenant/<tenant-name>/streams/<stream-name>', # sample
            #data=data # query params to include -- force, authoritative
        )

        def response_handler(resp):
            if resp.error_code == 404: # topic does not exist
                return False
            if resp.error_code == 412:  # topic has active producers and subscriptions
                return False
            if not resp.is_success:
                raise TopicDeleteError(resp, request)
            return resp.body['result']

        return self._execute(request, response_handler)

class StandardStream(Stream):
    """Standard stream API wrapper.

    :param connection: HTTP connection.
    :type connection: c8.connection.Connection
    """

    def __init__(self, connection):
        super(StandardStream, self).__init__(
            connection=connection,
            executor=DefaultExecutor(connection)
        )

    def __repr__(self):
        return '<StandardStream {}>'.format(self.name)
