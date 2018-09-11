from __future__ import absolute_import, unicode_literals

__all__ = ['Topic']

from c8.api import APIWrapper
from c8.request import Request
from c8.executor import (
    DefaultExecutor
)

from c8.exceptions import (
    TopicPropertiesError,
    TopicStatisticsError,
    SubscriptionDeleteError,
    SubscriptionUpdateError
)


class Topic(APIWrapper):
    """Base class for Topic API wrappers.

    :param connection: HTTP connection.
    :type connection: c8.connection.Connection
    :param executor: API executor.
    :type executor: c8.executor.Executor
    """

    def __init__(self, persistence, connection, executor):
        super(Topic, self).__init__(connection, executor)
        self._topic_persistence = persistence

    @property
    def name(self):
        """Return topic name.

        :return: topic name.
        :rtype: str | unicode
        """
        return self.topic_name

    def is_persistent(self):
        """Return true if topic is persistent topic

        :return: true if topic is persistent
        :rtype: bool
        :raise c8.exceptions.TopicPropertiesError: If retrieval fails.
        """
        return self._topic_persistence

    def get_subscriptions(self):
        """Return list of subscriptions for the topic

        :return: list of subscriptions
        :rtype: [string]
        :raise c8.exceptions.TopicPropertiesError: If retrieval fails.
        """

        url = '/c8/_tenant/<tenant-name>/_streams/<stream-name>/non-persistent/topic/<topic-name>/subscriptions'
        if self.is_persistent():
            url = '/c8/_tenant/<tenant-name>/_streams/<stream-name>/persistent/topic/<topic-name>/subscriptions'

        request = Request(
            method='get',
            endpoint=url,  # sample
        )

        def response_handler(resp):
            if not resp.is_success:
                raise TopicPropertiesError(resp, request)
            return resp.body['data']

        return self._execute(request, response_handler)

    def get_statistics(self):
        """Get statistics for the topic

        :return: topic statistics
        :rtype: dict
        :raise c8.exceptions.TopicStatisticsError: If retrieval fails.
        """

        url = '/c8/_tenant/<tenant-name>/_streams/<stream-name>/non-persistent/topic/<topic-name>/stats'
        if self.is_persistent():
            url = '/c8/_tenant/<tenant-name>/_streams/<stream-name>/persistent/topic/<topic-name>/stats'

        request = Request(
            method='get',
            endpoint=url
            # sample
        )

        def response_handler(resp):
            if not resp.is_success:
                raise TopicStatisticsError(resp, request)
            return resp.body['data']

        return self._execute(request, response_handler)

    def delete_subscription(self, name):
        """Delete subscription. There should not be any active consumers on the subscription

        :param name: subscription name.
        :type name: str | unicode
        :return: True if topic is deleted successfully.
        :rtype: bool
        :raise c8.exceptions.SubscriptionDeleteError: If delete fails.
        """

        url = '/c8/_tenant/<tenant-name>/_streams/<stream-name>/non-persistent/topic/<topic-name>/subscription/' + name
        if self.is_persistent():
            url = '/c8/_tenant/<tenant-name>/_streams/<stream-name>/persistent/topic/<topic-name>/subscription/' + name

        request = Request(
            method='delete',
            endpoint=url,  # sample
        )

        def response_handler(resp):
            if resp.error_code == 404:  # topic does not exist
                return False
            if resp.error_code == 412:  # subscription has active consumers
                return False
            if not resp.is_success:
                raise SubscriptionDeleteError(resp, request)
            return resp.body['result']

        return self._execute(request, response_handler)

    def reset_subscription(self, name):
        """Reset subscription to message position closest to given position

        :param name: subscription name.
        :type name: str | unicode
        :return: True if topic is deleted successfully.
        :rtype: bool
        :raise c8.exceptions.SubscriptionUpdateError: If delete fails.
        """

        url = '/c8/_tenant/<tenant-name>/_streams/<stream-name>/non-persistent/topic/<topic-name>/subscription/' + name
        if self.is_persistent():
            url = '/c8/_tenant/<tenant-name>/_streams/<stream-name>/persistent/topic/<topic-name>/subscription/' + name

        request = Request(
            method='put',
            endpoint=url,  # sample
        )

        def response_handler(resp):
            if resp.error_code == 404:  # topic or subscription does not exist
                return False
            if resp.error_code == 403:  # not permitted. do not have permissions
                return False
            if not resp.is_success:
                raise SubscriptionUpdateError(resp, request)
            return resp.body['result']

        return self._execute(request, response_handler)

    def reset_cursor_by_timestamp(self, name, timestamp):
        """Reset subscription to message position closest to absolute timestamp (in ms).
        It fence cursor and disconnects all active consumers before reseting cursor.

        :param name: subscription name.
        :type name: str | unicode
        :param timestamp: timestamp in milliseconds.
        :type name: int
        :return: True if subscription is reset successfully.
        :rtype: bool
        :raise c8.exceptions.SubscriptionUpdateError: If delete fails.
        """

        url = '/c8/_tenant/<tenant-name>/_streams/<stream-name>/non-persistent/topic/<topic-name>/subscription/{subName}/resetcursor/{timestamp}'
        if self.is_persistent():
            url = '/c8/_tenant/<tenant-name>/_streams/<stream-name>/persistent/topic/<topic-name>/subscription/{subName}/resetcursor/{timestamp}'

        request = Request(
            method='post',
            endpoint=url,  # sample
        )

        def response_handler(resp):
            if resp.error_code == 404:  # topic or subscription does not exist
                return False
            if resp.error_code == 403:  # not permitted. do not have permissions
                return False
            if not resp.is_success:
                raise SubscriptionUpdateError(resp, request)
            return resp.body['result']

        return self._execute(request, response_handler)

    def reset_cursor(self, name):
        """Reset subscription to message position closest to given position.
        It fence cursor and disconnects all active consumers before reseting cursor.

        :param name: subscription name.
        :type name: str | unicode
        :param timestamp: timestamp in milliseconds.
        :type name: int
        :return: True if subscription is reset successfully.
        :rtype: bool
        :raise c8.exceptions.SubscriptionUpdateError: If delete fails.
        """

        url = '/c8/_tenant/<tenant-name>/_streams/<stream-name>/non-persistent/topic/<topic-name>/subscription/{subName}/resetcursor'
        if self.is_persistent():
            url = '/c8/_tenant/<tenant-name>/_streams/<stream-name>/persistent/topic/<topic-name>/subscription/{subName}/resetcursor'

        request = Request(
            method='post',
            endpoint=url,  # sample
        )

        def response_handler(resp):
            if resp.error_code == 404:  # topic or subscription does not exist
                return False
            if resp.error_code == 405:  # Not supported for partitioned topics
                return False
            if not resp.is_success:
                raise SubscriptionUpdateError(resp, request)
            return resp.body['result']

        return self._execute(request, response_handler)

    def skip_all_messages(self, subscription):
        """ Skip all messages on a topic subscription. Completely clears the backlog on the subscription.

        :param name: subscription name.
        :type name: str | unicode
        :return: True if all messages are skipped.
        :rtype: bool
        :raise c8.exceptions.SubscriptionUpdateError: If skip fails.
        """
        url = '/c8/_tenant/<tenant-name>/_streams/<stream-name>/non-persistent/topic/<topic-name>/subscription/<subName>/skip_all'
        if self.is_persistent():
            url = '/c8/_tenant/<tenant-name>/_streams/<stream-name>/persistent/topic/<topic-name>/subscription/<subName>/skip_all'

        request = Request(
            method='post',
            endpoint=url  # sample
        )

        def response_handler(resp):
            if resp.error_code == 403:  # operation not allowed on topic
                return False
            if resp.error_code == 404:  # topic or subscription does not exist
                return False
            if not resp.is_success:
                raise SubscriptionUpdateError(resp, request)
            return resp.body['result']

        return self._execute(request, response_handler)

    def skip_messages(self, subscription, num_messages):
        """ Skip num messages on a topic subscription. Completely clears the backlog on the subscription.

        :param name: subscription name.
        :type name: str | unicode
        :param name: number of messages.
        :type name: int
        :return: True if messages are skipped successfully.
        :rtype: bool
        :raise c8.exceptions.SubscriptionUpdateError: If skip fails.
        """
        url = '/c8/_tenant/<tenant-name>/_streams/<stream-name>/non-persistent/topic/<topic-name>/subscription/<subName>/skip/<num_messages>'
        if self.is_persistent():
            url = '/c8/_tenant/<tenant-name>/_streams/<stream-name>/persistent/topic/<topic-name>/subscription/<subName>/skip/<num_messages>'

        request = Request(
            method='post',
            endpoint=url,  # sample
        )

        def response_handler(resp):
            if resp.error_code == 403:  # operation not allowed on topic
                return False
            if resp.error_code == 404:  # topic or subscription does not exist
                return False
            if not resp.is_success:
                raise SubscriptionUpdateError(resp, request)
            return resp.body['result']

        return self._execute(request, response_handler)

    def expire_messages(self, subscription, expire_time_seconds):
        """ Expire messages on a topic subscription.

        :param name: subscription name.
        :type name: str | unicode
        :param name: expire_time_seconds.
        :type name: int
        :return: True if messages are expired successfully.
        :rtype: bool
        :raise c8.exceptions.SubscriptionUpdateError: If expiry fails.
        """
        url = '/c8/_tenant/<tenant-name>/_streams/<stream-name>/non-persistent/topic/<topic-name>/subscription/{subName}/expireMessages/{expireTimeInSeconds}'
        if self.is_persistent():
            url = '/c8/_tenant/<tenant-name>/_streams/<stream-name>/persistent/topic/<topic-name>/subscription/{subName}/expireMessages/{expireTimeInSeconds}'

        request = Request(
            method='post',
            endpoint=url,  # sample
        )

        def response_handler(resp):
            if resp.error_code == 403:  # operation not allowed on topic
                return False
            if resp.error_code == 404:  # topic or subscription does not exist
                return False
            if not resp.is_success:
                raise SubscriptionUpdateError(resp, request)
            return resp.body['result']

        return self._execute(request, response_handler)


    def peek_message(self, subscription, position):
        """ Peek nth message on a topic subscription.

        :param name: subscription name.
        :type name: str | unicode
        :param name: position.
        :type name: int
        :return: message
        :rtype: object
        :raise c8.exceptions.SubscriptionUpdateError: If unable to peek nth message
        """
        url = '/c8/_tenant/<tenant-name>/_streams/<stream-name>/non-persistent/topic/<topic-name>/subscription/{subName}/position/{messagePosition}'
        if self.is_persistent():
            url = '/c8/_tenant/<tenant-name>/_streams/<stream-name>/persistent/topic/<topic-name>/subscription/{subName}/position/{messagePosition}'

        request = Request(
            method='get',
            endpoint=url,  # sample
        )

        def response_handler(resp):
            if resp.error_code == 403:  # operation not allowed on topic
                return False
            if resp.error_code == 404:  # topic or subscription does not exist
                return False
            if not resp.is_success:
                raise SubscriptionUpdateError(resp, request)
            return resp.body['result']

        return self._execute(request, response_handler)


    def terminate(self):
        """ Terminate a topic. A topic that is terminated will not accept any more
        messages to be published and will let consumer to drain existing messages in backlog

        :return: message id
        :rtype: string
        :raise c8.exceptions.TopicPropertiesError: If unable to terminate
        """
        url = '/c8/_tenant/<tenant-name>/_streams/<stream-name>/non-persistent/topic/<topic-name>'
        if self.is_persistent():
            url = '/c8/_tenant/<tenant-name>/_streams/<stream-name>/persistent/topic/<topic-name>'

        request = Request(
            method='post',
            endpoint=url,  # sample
        )

        def response_handler(resp):
            if resp.error_code == 405:  # operation not allowed on topic
                return False
            if resp.error_code == 404:  # topic does not exist
                return False
            if not resp.is_success:
                raise TopicPropertiesError(resp, request)
            return resp.body['result']

        return self._execute(request, response_handler)


    def compact(self):
        """ Trigger a compaction operation on a topic.

        :return: compaction status
        :rtype: bool
        :raise c8.exceptions.TopicPropertiesError: If unable to compact
        """
        url = '/c8/_tenant/<tenant-name>/_streams/<stream-name>/non-persistent/topic/<topic-name>/compaction'
        if self.is_persistent():
            url = '/c8/_tenant/<tenant-name>/_streams/<stream-name>/persistent/topic/<topic-name>/compaction'

        request = Request(
            method='put',
            endpoint=url,  # sample
        )

        def response_handler(resp):
            if resp.error_code == 405:  # operation not allowed on topic
                return False
            if resp.error_code == 404:  # topic does not exist
                return False
            if resp.error_code == 409:  # compaction already running
                return False
            if not resp.is_success:
                raise TopicPropertiesError(resp, request)
            return resp.body['result']

        return self._execute(request, response_handler)


    def get_compaction_status(self):
        """ Get the status of a compaction operation for a topic.

        :return: compaction status
        :rtype: bool
        :raise c8.exceptions.TopicPropertiesError: If unable to compact
        """
        url = '/c8/_tenant/<tenant-name>/_streams/<stream-name>/non-persistent/topic/<topic-name>/compaction'
        if self.is_persistent():
            url = '/c8/_tenant/<tenant-name>/_streams/<stream-name>/persistent/topic/<topic-name>/compaction'

        request = Request(
            method='get',
            endpoint=url,  # sample
        )

        def response_handler(resp):
            if resp.error_code == 405:  # operation not allowed on topic
                return False
            if resp.error_code == 404:  # topic does not exist
                return False
            if resp.error_code == 409:  # compaction already running
                return False
            if not resp.is_success:
                raise TopicPropertiesError(resp, request)
            return resp.body['result']

        return self._execute(request, response_handler)


    def get_backlog(self):
        """ Get estimated backlog for offline topic.

        :return: backlog stats
        :rtype: dict
        :raise c8.exceptions.TopicPropertiesError: If unable to compact
        """
        url = '/c8/_tenant/<tenant-name>/_streams/<stream-name>/non-persistent/topic/<topic-name>/backlog'
        if self.is_persistent():
            url = '/c8/_tenant/<tenant-name>/_streams/<stream-name>/persistent/topic/<topic-name>/backlog'

        request = Request(
            method='get',
            endpoint=url,  # sample
        )

        def response_handler(resp):
            if resp.error_code == 405:  # operation not allowed on topic
                return False
            if resp.error_code == 404:  # topic does not exist
                return False
            if not resp.is_success:
                raise TopicPropertiesError(resp, request)
            return resp.body['result']

        return self._execute(request, response_handler)


class PersistentTopic(Topic):
    """Persistent Topic API wrapper.

    :param connection: HTTP connection.
    :type connection: c8.connection.Connection
    """

    def __init__(self, connection):
        super(PersistentTopic, self).__init__(
            persistence=True,
            connection=connection,
            executor=DefaultExecutor(connection)
        )

    def __repr__(self):
        return '<PersistentTopic {}>'.format(self.name)


class NonPersistentTopic(Topic):
    """Persistent Topic API wrapper.

    :param connection: HTTP connection.
    :type connection: c8.connection.Connection
    """

    def __init__(self, connection):
        super(NonPersistentTopic, self).__init__(
            persistence=False,
            connection=connection,
            executor=DefaultExecutor(connection)
        )

    def __repr__(self):
        return '<NonPersistentTopic {}>'.format(self.name)
