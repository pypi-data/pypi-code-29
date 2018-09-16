import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("sqs", *args, **kwargs)

    def add_permission(
        self,
        _request: shapes.AddPermissionRequest = None,
        *,
        queue_url: str,
        label: str,
        aws_account_ids: typing.List[str],
        actions: typing.List[str],
    ) -> None:
        """
        Adds a permission to a queue for a specific
        [principal](http://docs.aws.amazon.com/general/latest/gr/glos-chap.html#P). This
        allows sharing access to the queue.

        When you create a queue, you have full control access rights for the queue. Only
        you, the owner of the queue, can grant or deny permissions to the queue. For
        more information about these permissions, see [Shared
        Queues](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/acp-
        overview.html) in the _Amazon Simple Queue Service Developer Guide_.

        `AddPermission` writes an Amazon-SQS-generated policy. If you want to write your
        own policy, use ` SetQueueAttributes ` to upload your policy. For more
        information about writing your own policy, see [Using The Access Policy
        Language](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/AccessPolicyLanguage.html)
        in the _Amazon Simple Queue Service Developer Guide_.

        Some actions take lists of parameters. These lists are specified using the
        `param.n` notation. Values of `n` are integers starting from 1. For example, a
        parameter list with two elements looks like this:

        `&Attribute.1=this`

        `&Attribute.2=that`
        """
        if _request is None:
            _params = {}
            if queue_url is not ShapeBase.NOT_SET:
                _params['queue_url'] = queue_url
            if label is not ShapeBase.NOT_SET:
                _params['label'] = label
            if aws_account_ids is not ShapeBase.NOT_SET:
                _params['aws_account_ids'] = aws_account_ids
            if actions is not ShapeBase.NOT_SET:
                _params['actions'] = actions
            _request = shapes.AddPermissionRequest(**_params)
        response = self._boto_client.add_permission(**_request.to_boto())

    def change_message_visibility(
        self,
        _request: shapes.ChangeMessageVisibilityRequest = None,
        *,
        queue_url: str,
        receipt_handle: str,
        visibility_timeout: int,
    ) -> None:
        """
        Changes the visibility timeout of a specified message in a queue to a new value.
        The maximum allowed timeout value is 12 hours. Thus, you can't extend the
        timeout of a message in an existing queue to more than a total visibility
        timeout of 12 hours. For more information, see [Visibility
        Timeout](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-
        visibility-timeout.html) in the _Amazon Simple Queue Service Developer Guide_.

        For example, you have a message with a visibility timeout of 5 minutes. After 3
        minutes, you call `ChangeMessageVisiblity` with a timeout of 10 minutes. At that
        time, the timeout for the message is extended by 10 minutes beyond the time of
        the `ChangeMessageVisibility` action. This results in a total visibility timeout
        of 13 minutes. You can continue to call the `ChangeMessageVisibility` to extend
        the visibility timeout to a maximum of 12 hours. If you try to extend the
        visibility timeout beyond 12 hours, your request is rejected.

        A message is considered to be _in flight_ after it's received from a queue by a
        consumer, but not yet deleted from the queue.

        For standard queues, there can be a maximum of 120,000 inflight messages per
        queue. If you reach this limit, Amazon SQS returns the `OverLimit` error
        message. To avoid reaching the limit, you should delete messages from the queue
        after they're processed. You can also increase the number of queues you use to
        process your messages.

        For FIFO queues, there can be a maximum of 20,000 inflight messages per queue.
        If you reach this limit, Amazon SQS returns no error messages.

        If you attempt to set the `VisibilityTimeout` to a value greater than the
        maximum time left, Amazon SQS returns an error. Amazon SQS doesn't automatically
        recalculate and increase the timeout to the maximum remaining time.

        Unlike with a queue, when you change the visibility timeout for a specific
        message the timeout value is applied immediately but isn't saved in memory for
        that message. If you don't delete a message after it is received, the visibility
        timeout for the message reverts to the original timeout value (not to the value
        you set using the `ChangeMessageVisibility` action) the next time the message is
        received.
        """
        if _request is None:
            _params = {}
            if queue_url is not ShapeBase.NOT_SET:
                _params['queue_url'] = queue_url
            if receipt_handle is not ShapeBase.NOT_SET:
                _params['receipt_handle'] = receipt_handle
            if visibility_timeout is not ShapeBase.NOT_SET:
                _params['visibility_timeout'] = visibility_timeout
            _request = shapes.ChangeMessageVisibilityRequest(**_params)
        response = self._boto_client.change_message_visibility(
            **_request.to_boto()
        )

    def change_message_visibility_batch(
        self,
        _request: shapes.ChangeMessageVisibilityBatchRequest = None,
        *,
        queue_url: str,
        entries: typing.List[shapes.ChangeMessageVisibilityBatchRequestEntry],
    ) -> shapes.ChangeMessageVisibilityBatchResult:
        """
        Changes the visibility timeout of multiple messages. This is a batch version of
        ` ChangeMessageVisibility.` The result of the action on each message is reported
        individually in the response. You can send up to 10 ` ChangeMessageVisibility `
        requests with each `ChangeMessageVisibilityBatch` action.

        Because the batch request can result in a combination of successful and
        unsuccessful actions, you should check for batch errors even when the call
        returns an HTTP status code of `200`.

        Some actions take lists of parameters. These lists are specified using the
        `param.n` notation. Values of `n` are integers starting from 1. For example, a
        parameter list with two elements looks like this:

        `&Attribute.1=this`

        `&Attribute.2=that`
        """
        if _request is None:
            _params = {}
            if queue_url is not ShapeBase.NOT_SET:
                _params['queue_url'] = queue_url
            if entries is not ShapeBase.NOT_SET:
                _params['entries'] = entries
            _request = shapes.ChangeMessageVisibilityBatchRequest(**_params)
        response = self._boto_client.change_message_visibility_batch(
            **_request.to_boto()
        )

        return shapes.ChangeMessageVisibilityBatchResult.from_boto(response)

    def create_queue(
        self,
        _request: shapes.CreateQueueRequest = None,
        *,
        queue_name: str,
        attributes: typing.Dict[typing.Union[str, shapes.QueueAttributeName],
                                str] = ShapeBase.NOT_SET,
    ) -> shapes.CreateQueueResult:
        """
        Creates a new standard or FIFO queue. You can pass one or more attributes in the
        request. Keep the following caveats in mind:

          * If you don't specify the `FifoQueue` attribute, Amazon SQS creates a standard queue.

        You can't change the queue type after you create it and you can't convert an
        existing standard queue into a FIFO queue. You must either create a new FIFO
        queue for your application or delete your existing standard queue and recreate
        it as a FIFO queue. For more information, see [ Moving From a Standard Queue to
        a FIFO
        Queue](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-
        queues.html#FIFO-queues-moving) in the _Amazon Simple Queue Service Developer
        Guide_.

          * If you don't provide a value for an attribute, the queue is created with the default value for the attribute.

          * If you delete a queue, you must wait at least 60 seconds before creating a queue with the same name.

        To successfully create a new queue, you must provide a queue name that adheres
        to the [limits related to
        queues](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/limits-
        queues.html) and is unique within the scope of your queues.

        To get the queue URL, use the ` GetQueueUrl ` action. ` GetQueueUrl ` requires
        only the `QueueName` parameter. be aware of existing queue names:

          * If you provide the name of an existing queue along with the exact names and values of all the queue's attributes, `CreateQueue` returns the queue URL for the existing queue.

          * If the queue name, attribute names, or attribute values don't match an existing queue, `CreateQueue` returns an error.

        Some actions take lists of parameters. These lists are specified using the
        `param.n` notation. Values of `n` are integers starting from 1. For example, a
        parameter list with two elements looks like this:

        `&Attribute.1=this`

        `&Attribute.2=that`
        """
        if _request is None:
            _params = {}
            if queue_name is not ShapeBase.NOT_SET:
                _params['queue_name'] = queue_name
            if attributes is not ShapeBase.NOT_SET:
                _params['attributes'] = attributes
            _request = shapes.CreateQueueRequest(**_params)
        response = self._boto_client.create_queue(**_request.to_boto())

        return shapes.CreateQueueResult.from_boto(response)

    def delete_message(
        self,
        _request: shapes.DeleteMessageRequest = None,
        *,
        queue_url: str,
        receipt_handle: str,
    ) -> None:
        """
        Deletes the specified message from the specified queue. You specify the message
        by using the message's _receipt handle_ and not the _MessageId_ you receive when
        you send the message. Even if the message is locked by another reader due to the
        visibility timeout setting, it is still deleted from the queue. If you leave a
        message in the queue for longer than the queue's configured retention period,
        Amazon SQS automatically deletes the message.

        The receipt handle is associated with a specific instance of receiving the
        message. If you receive a message more than once, the receipt handle you get
        each time you receive the message is different. If you don't provide the most
        recently received receipt handle for the message when you use the
        `DeleteMessage` action, the request succeeds, but the message might not be
        deleted.

        For standard queues, it is possible to receive a message even after you delete
        it. This might happen on rare occasions if one of the servers storing a copy of
        the message is unavailable when you send the request to delete the message. The
        copy remains on the server and might be returned to you on a subsequent receive
        request. You should ensure that your application is idempotent, so that
        receiving a message more than once does not cause issues.
        """
        if _request is None:
            _params = {}
            if queue_url is not ShapeBase.NOT_SET:
                _params['queue_url'] = queue_url
            if receipt_handle is not ShapeBase.NOT_SET:
                _params['receipt_handle'] = receipt_handle
            _request = shapes.DeleteMessageRequest(**_params)
        response = self._boto_client.delete_message(**_request.to_boto())

    def delete_message_batch(
        self,
        _request: shapes.DeleteMessageBatchRequest = None,
        *,
        queue_url: str,
        entries: typing.List[shapes.DeleteMessageBatchRequestEntry],
    ) -> shapes.DeleteMessageBatchResult:
        """
        Deletes up to ten messages from the specified queue. This is a batch version of
        ` DeleteMessage.` The result of the action on each message is reported
        individually in the response.

        Because the batch request can result in a combination of successful and
        unsuccessful actions, you should check for batch errors even when the call
        returns an HTTP status code of `200`.

        Some actions take lists of parameters. These lists are specified using the
        `param.n` notation. Values of `n` are integers starting from 1. For example, a
        parameter list with two elements looks like this:

        `&Attribute.1=this`

        `&Attribute.2=that`
        """
        if _request is None:
            _params = {}
            if queue_url is not ShapeBase.NOT_SET:
                _params['queue_url'] = queue_url
            if entries is not ShapeBase.NOT_SET:
                _params['entries'] = entries
            _request = shapes.DeleteMessageBatchRequest(**_params)
        response = self._boto_client.delete_message_batch(**_request.to_boto())

        return shapes.DeleteMessageBatchResult.from_boto(response)

    def delete_queue(
        self,
        _request: shapes.DeleteQueueRequest = None,
        *,
        queue_url: str,
    ) -> None:
        """
        Deletes the queue specified by the `QueueUrl`, regardless of the queue's
        contents. If the specified queue doesn't exist, Amazon SQS returns a successful
        response.

        Be careful with the `DeleteQueue` action: When you delete a queue, any messages
        in the queue are no longer available.

        When you delete a queue, the deletion process takes up to 60 seconds. Requests
        you send involving that queue during the 60 seconds might succeed. For example,
        a ` SendMessage ` request might succeed, but after 60 seconds the queue and the
        message you sent no longer exist.

        When you delete a queue, you must wait at least 60 seconds before creating a
        queue with the same name.
        """
        if _request is None:
            _params = {}
            if queue_url is not ShapeBase.NOT_SET:
                _params['queue_url'] = queue_url
            _request = shapes.DeleteQueueRequest(**_params)
        response = self._boto_client.delete_queue(**_request.to_boto())

    def get_queue_attributes(
        self,
        _request: shapes.GetQueueAttributesRequest = None,
        *,
        queue_url: str,
        attribute_names: typing.List[
            typing.Union[str, shapes.QueueAttributeName]] = ShapeBase.NOT_SET,
    ) -> shapes.GetQueueAttributesResult:
        """
        Gets attributes for the specified queue.

        To determine whether a queue is
        [FIFO](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-
        queues.html), you can check whether `QueueName` ends with the `.fifo` suffix.

        Some actions take lists of parameters. These lists are specified using the
        `param.n` notation. Values of `n` are integers starting from 1. For example, a
        parameter list with two elements looks like this:

        `&Attribute.1=this`

        `&Attribute.2=that`
        """
        if _request is None:
            _params = {}
            if queue_url is not ShapeBase.NOT_SET:
                _params['queue_url'] = queue_url
            if attribute_names is not ShapeBase.NOT_SET:
                _params['attribute_names'] = attribute_names
            _request = shapes.GetQueueAttributesRequest(**_params)
        response = self._boto_client.get_queue_attributes(**_request.to_boto())

        return shapes.GetQueueAttributesResult.from_boto(response)

    def get_queue_url(
        self,
        _request: shapes.GetQueueUrlRequest = None,
        *,
        queue_name: str,
        queue_owner_aws_account_id: str = ShapeBase.NOT_SET,
    ) -> shapes.GetQueueUrlResult:
        """
        Returns the URL of an existing queue. This action provides a simple way to
        retrieve the URL of an Amazon SQS queue.

        To access a queue that belongs to another AWS account, use the
        `QueueOwnerAWSAccountId` parameter to specify the account ID of the queue's
        owner. The queue's owner must grant you permission to access the queue. For more
        information about shared queue access, see ` AddPermission ` or see [Shared
        Queues](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/acp-
        overview.html) in the _Amazon Simple Queue Service Developer Guide_.
        """
        if _request is None:
            _params = {}
            if queue_name is not ShapeBase.NOT_SET:
                _params['queue_name'] = queue_name
            if queue_owner_aws_account_id is not ShapeBase.NOT_SET:
                _params['queue_owner_aws_account_id'
                       ] = queue_owner_aws_account_id
            _request = shapes.GetQueueUrlRequest(**_params)
        response = self._boto_client.get_queue_url(**_request.to_boto())

        return shapes.GetQueueUrlResult.from_boto(response)

    def list_dead_letter_source_queues(
        self,
        _request: shapes.ListDeadLetterSourceQueuesRequest = None,
        *,
        queue_url: str,
    ) -> shapes.ListDeadLetterSourceQueuesResult:
        """
        Returns a list of your queues that have the `RedrivePolicy` queue attribute
        configured with a dead-letter queue.

        For more information about using dead-letter queues, see [Using Amazon SQS Dead-
        Letter
        Queues](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-
        dead-letter-queues.html) in the _Amazon Simple Queue Service Developer Guide_.
        """
        if _request is None:
            _params = {}
            if queue_url is not ShapeBase.NOT_SET:
                _params['queue_url'] = queue_url
            _request = shapes.ListDeadLetterSourceQueuesRequest(**_params)
        response = self._boto_client.list_dead_letter_source_queues(
            **_request.to_boto()
        )

        return shapes.ListDeadLetterSourceQueuesResult.from_boto(response)

    def list_queue_tags(
        self,
        _request: shapes.ListQueueTagsRequest = None,
        *,
        queue_url: str,
    ) -> shapes.ListQueueTagsResult:
        """
        List all cost allocation tags added to the specified Amazon SQS queue. For an
        overview, see [Tagging Amazon SQS
        Queues](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-
        tagging-queues.html) in the _Amazon Simple Queue Service Developer Guide_.

        When you use queue tags, keep the following guidelines in mind:

          * Adding more than 50 tags to a queue isn't recommended.

          * Tags don't have any semantic meaning. Amazon SQS interprets tags as character strings.

          * Tags are case-sensitive.

          * A new tag with a key identical to that of an existing tag overwrites the existing tag.

          * Tagging API actions are limited to 5 TPS per AWS account. If your application requires a higher throughput, file a [technical support request](https://console.aws.amazon.com/support/home#/case/create?issueType=technical).

        For a full list of tag restrictions, see [Limits Related to
        Queues](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/limits-
        queues.html) in the _Amazon Simple Queue Service Developer Guide_.
        """
        if _request is None:
            _params = {}
            if queue_url is not ShapeBase.NOT_SET:
                _params['queue_url'] = queue_url
            _request = shapes.ListQueueTagsRequest(**_params)
        response = self._boto_client.list_queue_tags(**_request.to_boto())

        return shapes.ListQueueTagsResult.from_boto(response)

    def list_queues(
        self,
        _request: shapes.ListQueuesRequest = None,
        *,
        queue_name_prefix: str = ShapeBase.NOT_SET,
    ) -> shapes.ListQueuesResult:
        """
        Returns a list of your queues. The maximum number of queues that can be returned
        is 1,000. If you specify a value for the optional `QueueNamePrefix` parameter,
        only queues with a name that begins with the specified value are returned.
        """
        if _request is None:
            _params = {}
            if queue_name_prefix is not ShapeBase.NOT_SET:
                _params['queue_name_prefix'] = queue_name_prefix
            _request = shapes.ListQueuesRequest(**_params)
        response = self._boto_client.list_queues(**_request.to_boto())

        return shapes.ListQueuesResult.from_boto(response)

    def purge_queue(
        self,
        _request: shapes.PurgeQueueRequest = None,
        *,
        queue_url: str,
    ) -> None:
        """
        Deletes the messages in a queue specified by the `QueueURL` parameter.

        When you use the `PurgeQueue` action, you can't retrieve a message deleted from
        a queue.

        When you purge a queue, the message deletion process takes up to 60 seconds. All
        messages sent to the queue before calling the `PurgeQueue` action are deleted.
        Messages sent to the queue while it is being purged might be deleted. While the
        queue is being purged, messages sent to the queue before `PurgeQueue` is called
        might be received, but are deleted within the next minute.
        """
        if _request is None:
            _params = {}
            if queue_url is not ShapeBase.NOT_SET:
                _params['queue_url'] = queue_url
            _request = shapes.PurgeQueueRequest(**_params)
        response = self._boto_client.purge_queue(**_request.to_boto())

    def receive_message(
        self,
        _request: shapes.ReceiveMessageRequest = None,
        *,
        queue_url: str,
        attribute_names: typing.List[
            typing.Union[str, shapes.QueueAttributeName]] = ShapeBase.NOT_SET,
        message_attribute_names: typing.List[str] = ShapeBase.NOT_SET,
        max_number_of_messages: int = ShapeBase.NOT_SET,
        visibility_timeout: int = ShapeBase.NOT_SET,
        wait_time_seconds: int = ShapeBase.NOT_SET,
        receive_request_attempt_id: str = ShapeBase.NOT_SET,
    ) -> shapes.ReceiveMessageResult:
        """
        Retrieves one or more messages (up to 10), from the specified queue. Using the
        `WaitTimeSeconds` parameter enables long-poll support. For more information, see
        [Amazon SQS Long
        Polling](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-
        long-polling.html) in the _Amazon Simple Queue Service Developer Guide_.

        Short poll is the default behavior where a weighted random set of machines is
        sampled on a `ReceiveMessage` call. Thus, only the messages on the sampled
        machines are returned. If the number of messages in the queue is small (fewer
        than 1,000), you most likely get fewer messages than you requested per
        `ReceiveMessage` call. If the number of messages in the queue is extremely
        small, you might not receive any messages in a particular `ReceiveMessage`
        response. If this happens, repeat the request.

        For each message returned, the response includes the following:

          * The message body.

          * An MD5 digest of the message body. For information about MD5, see [RFC1321](https://www.ietf.org/rfc/rfc1321.txt).

          * The `MessageId` you received when you sent the message to the queue.

          * The receipt handle.

          * The message attributes.

          * An MD5 digest of the message attributes.

        The receipt handle is the identifier you must provide when deleting the message.
        For more information, see [Queue and Message
        Identifiers](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-
        queue-message-identifiers.html) in the _Amazon Simple Queue Service Developer
        Guide_.

        You can provide the `VisibilityTimeout` parameter in your request. The parameter
        is applied to the messages that Amazon SQS returns in the response. If you don't
        include the parameter, the overall visibility timeout for the queue is used for
        the returned messages. For more information, see [Visibility
        Timeout](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-
        visibility-timeout.html) in the _Amazon Simple Queue Service Developer Guide_.

        A message that isn't deleted or a message whose visibility isn't extended before
        the visibility timeout expires counts as a failed receive. Depending on the
        configuration of the queue, the message might be sent to the dead-letter queue.

        In the future, new attributes might be added. If you write code that calls this
        action, we recommend that you structure your code so that it can handle new
        attributes gracefully.
        """
        if _request is None:
            _params = {}
            if queue_url is not ShapeBase.NOT_SET:
                _params['queue_url'] = queue_url
            if attribute_names is not ShapeBase.NOT_SET:
                _params['attribute_names'] = attribute_names
            if message_attribute_names is not ShapeBase.NOT_SET:
                _params['message_attribute_names'] = message_attribute_names
            if max_number_of_messages is not ShapeBase.NOT_SET:
                _params['max_number_of_messages'] = max_number_of_messages
            if visibility_timeout is not ShapeBase.NOT_SET:
                _params['visibility_timeout'] = visibility_timeout
            if wait_time_seconds is not ShapeBase.NOT_SET:
                _params['wait_time_seconds'] = wait_time_seconds
            if receive_request_attempt_id is not ShapeBase.NOT_SET:
                _params['receive_request_attempt_id'
                       ] = receive_request_attempt_id
            _request = shapes.ReceiveMessageRequest(**_params)
        response = self._boto_client.receive_message(**_request.to_boto())

        return shapes.ReceiveMessageResult.from_boto(response)

    def remove_permission(
        self,
        _request: shapes.RemovePermissionRequest = None,
        *,
        queue_url: str,
        label: str,
    ) -> None:
        """
        Revokes any permissions in the queue policy that matches the specified `Label`
        parameter. Only the owner of the queue can remove permissions.
        """
        if _request is None:
            _params = {}
            if queue_url is not ShapeBase.NOT_SET:
                _params['queue_url'] = queue_url
            if label is not ShapeBase.NOT_SET:
                _params['label'] = label
            _request = shapes.RemovePermissionRequest(**_params)
        response = self._boto_client.remove_permission(**_request.to_boto())

    def send_message(
        self,
        _request: shapes.SendMessageRequest = None,
        *,
        queue_url: str,
        message_body: str,
        delay_seconds: int = ShapeBase.NOT_SET,
        message_attributes: typing.
        Dict[str, shapes.MessageAttributeValue] = ShapeBase.NOT_SET,
        message_deduplication_id: str = ShapeBase.NOT_SET,
        message_group_id: str = ShapeBase.NOT_SET,
    ) -> shapes.SendMessageResult:
        """
        Delivers a message to the specified queue.

        A message can include only XML, JSON, and unformatted text. The following
        Unicode characters are allowed:

        `#x9` | `#xA` | `#xD` | `#x20` to `#xD7FF` | `#xE000` to `#xFFFD` | `#x10000` to
        `#x10FFFF`

        Any characters not included in this list will be rejected. For more information,
        see the [W3C specification for characters](http://www.w3.org/TR/REC-
        xml/#charsets).
        """
        if _request is None:
            _params = {}
            if queue_url is not ShapeBase.NOT_SET:
                _params['queue_url'] = queue_url
            if message_body is not ShapeBase.NOT_SET:
                _params['message_body'] = message_body
            if delay_seconds is not ShapeBase.NOT_SET:
                _params['delay_seconds'] = delay_seconds
            if message_attributes is not ShapeBase.NOT_SET:
                _params['message_attributes'] = message_attributes
            if message_deduplication_id is not ShapeBase.NOT_SET:
                _params['message_deduplication_id'] = message_deduplication_id
            if message_group_id is not ShapeBase.NOT_SET:
                _params['message_group_id'] = message_group_id
            _request = shapes.SendMessageRequest(**_params)
        response = self._boto_client.send_message(**_request.to_boto())

        return shapes.SendMessageResult.from_boto(response)

    def send_message_batch(
        self,
        _request: shapes.SendMessageBatchRequest = None,
        *,
        queue_url: str,
        entries: typing.List[shapes.SendMessageBatchRequestEntry],
    ) -> shapes.SendMessageBatchResult:
        """
        Delivers up to ten messages to the specified queue. This is a batch version of `
        SendMessage.` For a FIFO queue, multiple messages within a single batch are
        enqueued in the order they are sent.

        The result of sending each message is reported individually in the response.
        Because the batch request can result in a combination of successful and
        unsuccessful actions, you should check for batch errors even when the call
        returns an HTTP status code of `200`.

        The maximum allowed individual message size and the maximum total payload size
        (the sum of the individual lengths of all of the batched messages) are both 256
        KB (262,144 bytes).

        A message can include only XML, JSON, and unformatted text. The following
        Unicode characters are allowed:

        `#x9` | `#xA` | `#xD` | `#x20` to `#xD7FF` | `#xE000` to `#xFFFD` | `#x10000` to
        `#x10FFFF`

        Any characters not included in this list will be rejected. For more information,
        see the [W3C specification for characters](http://www.w3.org/TR/REC-
        xml/#charsets).

        If you don't specify the `DelaySeconds` parameter for an entry, Amazon SQS uses
        the default value for the queue.

        Some actions take lists of parameters. These lists are specified using the
        `param.n` notation. Values of `n` are integers starting from 1. For example, a
        parameter list with two elements looks like this:

        `&Attribute.1=this`

        `&Attribute.2=that`
        """
        if _request is None:
            _params = {}
            if queue_url is not ShapeBase.NOT_SET:
                _params['queue_url'] = queue_url
            if entries is not ShapeBase.NOT_SET:
                _params['entries'] = entries
            _request = shapes.SendMessageBatchRequest(**_params)
        response = self._boto_client.send_message_batch(**_request.to_boto())

        return shapes.SendMessageBatchResult.from_boto(response)

    def set_queue_attributes(
        self,
        _request: shapes.SetQueueAttributesRequest = None,
        *,
        queue_url: str,
        attributes: typing.Dict[typing.Union[str, shapes.
                                             QueueAttributeName], str],
    ) -> None:
        """
        Sets the value of one or more queue attributes. When you change a queue's
        attributes, the change can take up to 60 seconds for most of the attributes to
        propagate throughout the Amazon SQS system. Changes made to the
        `MessageRetentionPeriod` attribute can take up to 15 minutes.

        In the future, new attributes might be added. If you write code that calls this
        action, we recommend that you structure your code so that it can handle new
        attributes gracefully.
        """
        if _request is None:
            _params = {}
            if queue_url is not ShapeBase.NOT_SET:
                _params['queue_url'] = queue_url
            if attributes is not ShapeBase.NOT_SET:
                _params['attributes'] = attributes
            _request = shapes.SetQueueAttributesRequest(**_params)
        response = self._boto_client.set_queue_attributes(**_request.to_boto())

    def tag_queue(
        self,
        _request: shapes.TagQueueRequest = None,
        *,
        queue_url: str,
        tags: typing.Dict[str, str],
    ) -> None:
        """
        Add cost allocation tags to the specified Amazon SQS queue. For an overview, see
        [Tagging Amazon SQS
        Queues](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-
        tagging-queues.html) in the _Amazon Simple Queue Service Developer Guide_.

        When you use queue tags, keep the following guidelines in mind:

          * Adding more than 50 tags to a queue isn't recommended.

          * Tags don't have any semantic meaning. Amazon SQS interprets tags as character strings.

          * Tags are case-sensitive.

          * A new tag with a key identical to that of an existing tag overwrites the existing tag.

          * Tagging API actions are limited to 5 TPS per AWS account. If your application requires a higher throughput, file a [technical support request](https://console.aws.amazon.com/support/home#/case/create?issueType=technical).

        For a full list of tag restrictions, see [Limits Related to
        Queues](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/limits-
        queues.html) in the _Amazon Simple Queue Service Developer Guide_.
        """
        if _request is None:
            _params = {}
            if queue_url is not ShapeBase.NOT_SET:
                _params['queue_url'] = queue_url
            if tags is not ShapeBase.NOT_SET:
                _params['tags'] = tags
            _request = shapes.TagQueueRequest(**_params)
        response = self._boto_client.tag_queue(**_request.to_boto())

    def untag_queue(
        self,
        _request: shapes.UntagQueueRequest = None,
        *,
        queue_url: str,
        tag_keys: typing.List[str],
    ) -> None:
        """
        Remove cost allocation tags from the specified Amazon SQS queue. For an
        overview, see [Tagging Amazon SQS
        Queues](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-
        tagging-queues.html) in the _Amazon Simple Queue Service Developer Guide_.

        When you use queue tags, keep the following guidelines in mind:

          * Adding more than 50 tags to a queue isn't recommended.

          * Tags don't have any semantic meaning. Amazon SQS interprets tags as character strings.

          * Tags are case-sensitive.

          * A new tag with a key identical to that of an existing tag overwrites the existing tag.

          * Tagging API actions are limited to 5 TPS per AWS account. If your application requires a higher throughput, file a [technical support request](https://console.aws.amazon.com/support/home#/case/create?issueType=technical).

        For a full list of tag restrictions, see [Limits Related to
        Queues](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/limits-
        queues.html) in the _Amazon Simple Queue Service Developer Guide_.
        """
        if _request is None:
            _params = {}
            if queue_url is not ShapeBase.NOT_SET:
                _params['queue_url'] = queue_url
            if tag_keys is not ShapeBase.NOT_SET:
                _params['tag_keys'] = tag_keys
            _request = shapes.UntagQueueRequest(**_params)
        response = self._boto_client.untag_queue(**_request.to_boto())
