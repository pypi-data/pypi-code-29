import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import botocore.response
import dataclasses


@dataclasses.dataclass
class AddPermissionRequest(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "queue_url",
                "QueueUrl",
                TypeInfo(str),
            ),
            (
                "label",
                "Label",
                TypeInfo(str),
            ),
            (
                "aws_account_ids",
                "AWSAccountIds",
                TypeInfo(typing.List[str]),
            ),
            (
                "actions",
                "Actions",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The URL of the Amazon SQS queue to which permissions are added.

    # Queue URLs are case-sensitive.
    queue_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The unique identification of the permission you're setting (for example,
    # `AliceSendMessage`). Maximum 80 characters. Allowed characters include
    # alphanumeric characters, hyphens (`-`), and underscores (`_`).
    label: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS account number of the
    # [principal](http://docs.aws.amazon.com/general/latest/gr/glos-chap.html#P)
    # who is given permission. The principal must have an AWS account, but does
    # not need to be signed up for Amazon SQS. For information about locating the
    # AWS account identification, see [Your AWS
    # Identifiers](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/AWSCredentials.html)
    # in the _Amazon Simple Queue Service Developer Guide_.
    aws_account_ids: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The action the client wants to allow for the specified principal. The
    # following values are valid:

    #   * `*`

    #   * `ChangeMessageVisibility`

    #   * `DeleteMessage`

    #   * `GetQueueAttributes`

    #   * `GetQueueUrl`

    #   * `ReceiveMessage`

    #   * `SendMessage`

    # For more information about these actions, see [Understanding
    # Permissions](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/acp-
    # overview.html#PermissionTypes) in the _Amazon Simple Queue Service
    # Developer Guide_.

    # Specifying `SendMessage`, `DeleteMessage`, or `ChangeMessageVisibility` for
    # `ActionName.n` also grants permissions for the corresponding batch versions
    # of those actions: `SendMessageBatch`, `DeleteMessageBatch`, and
    # `ChangeMessageVisibilityBatch`.
    actions: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BatchEntryIdsNotDistinct(ShapeBase):
    """
    Two or more batch entries in the request have the same `Id`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class BatchRequestTooLong(ShapeBase):
    """
    The length of all the messages put together is more than the limit.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class BatchResultErrorEntry(ShapeBase):
    """
    This is used in the responses of batch API to give a detailed description of the
    result of an action on each entry in the request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "sender_fault",
                "SenderFault",
                TypeInfo(bool),
            ),
            (
                "code",
                "Code",
                TypeInfo(str),
            ),
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    # The `Id` of an entry in a batch request.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies whether the error happened due to the sender's fault.
    sender_fault: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An error code representing why the action failed on this entry.
    code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A message explaining why the action failed on this entry.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class Binary(botocore.response.StreamingBody):
    pass


@dataclasses.dataclass
class ChangeMessageVisibilityBatchRequest(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "queue_url",
                "QueueUrl",
                TypeInfo(str),
            ),
            (
                "entries",
                "Entries",
                TypeInfo(typing.List[ChangeMessageVisibilityBatchRequestEntry]),
            ),
        ]

    # The URL of the Amazon SQS queue whose messages' visibility is changed.

    # Queue URLs are case-sensitive.
    queue_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of receipt handles of the messages for which the visibility timeout
    # must be changed.
    entries: typing.List["ChangeMessageVisibilityBatchRequestEntry"
                        ] = dataclasses.field(
                            default=ShapeBase.NOT_SET,
                        )


@dataclasses.dataclass
class ChangeMessageVisibilityBatchRequestEntry(ShapeBase):
    """
    Encloses a receipt handle and an entry id for each message in `
    ChangeMessageVisibilityBatch.`

    All of the following list parameters must be prefixed with
    `ChangeMessageVisibilityBatchRequestEntry.n`, where `n` is an integer value
    starting with `1`. For example, a parameter list for this action might look like
    this:

    `&amp;ChangeMessageVisibilityBatchRequestEntry.1.Id=change_visibility_msg_2`

    `&amp;ChangeMessageVisibilityBatchRequestEntry.1.ReceiptHandle=<replaceable>Your_Receipt_Handle</replaceable>`

    `&amp;ChangeMessageVisibilityBatchRequestEntry.1.VisibilityTimeout=45`
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "receipt_handle",
                "ReceiptHandle",
                TypeInfo(str),
            ),
            (
                "visibility_timeout",
                "VisibilityTimeout",
                TypeInfo(int),
            ),
        ]

    # An identifier for this particular receipt handle used to communicate the
    # result.

    # The `Id`s of a batch request need to be unique within a request
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A receipt handle.
    receipt_handle: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new value (in seconds) for the message's visibility timeout.
    visibility_timeout: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ChangeMessageVisibilityBatchResult(OutputShapeBase):
    """
    For each message in the batch, the response contains a `
    ChangeMessageVisibilityBatchResultEntry ` tag if the message succeeds or a `
    BatchResultErrorEntry ` tag if the message fails.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "successful",
                "Successful",
                TypeInfo(typing.List[ChangeMessageVisibilityBatchResultEntry]),
            ),
            (
                "failed",
                "Failed",
                TypeInfo(typing.List[BatchResultErrorEntry]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of ` ChangeMessageVisibilityBatchResultEntry ` items.
    successful: typing.List["ChangeMessageVisibilityBatchResultEntry"
                           ] = dataclasses.field(
                               default=ShapeBase.NOT_SET,
                           )

    # A list of ` BatchResultErrorEntry ` items.
    failed: typing.List["BatchResultErrorEntry"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ChangeMessageVisibilityBatchResultEntry(ShapeBase):
    """
    Encloses the `Id` of an entry in ` ChangeMessageVisibilityBatch.`
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
        ]

    # Represents a message whose visibility timeout has been changed
    # successfully.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ChangeMessageVisibilityRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "queue_url",
                "QueueUrl",
                TypeInfo(str),
            ),
            (
                "receipt_handle",
                "ReceiptHandle",
                TypeInfo(str),
            ),
            (
                "visibility_timeout",
                "VisibilityTimeout",
                TypeInfo(int),
            ),
        ]

    # The URL of the Amazon SQS queue whose message's visibility is changed.

    # Queue URLs are case-sensitive.
    queue_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The receipt handle associated with the message whose visibility timeout is
    # changed. This parameter is returned by the ` ReceiveMessage ` action.
    receipt_handle: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The new value for the message's visibility timeout (in seconds). Values
    # values: `0` to `43200`. Maximum: 12 hours.
    visibility_timeout: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateQueueRequest(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "queue_name",
                "QueueName",
                TypeInfo(str),
            ),
            (
                "attributes",
                "Attributes",
                TypeInfo(
                    typing.Dict[typing.Union[str, QueueAttributeName], str]
                ),
            ),
        ]

    # The name of the new queue. The following limits apply to this name:

    #   * A queue name can have up to 80 characters.

    #   * Valid values: alphanumeric characters, hyphens (`-`), and underscores (`_`).

    #   * A FIFO queue name must end with the `.fifo` suffix.

    # Queue names are case-sensitive.
    queue_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A map of attributes with their corresponding values.

    # The following lists the names, descriptions, and values of the special
    # request parameters that the `CreateQueue` action uses:

    #   * `DelaySeconds` \- The length of time, in seconds, for which the delivery of all messages in the queue is delayed. Valid values: An integer from 0 to 900 seconds (15 minutes). The default is 0 (zero).

    #   * `MaximumMessageSize` \- The limit of how many bytes a message can contain before Amazon SQS rejects it. Valid values: An integer from 1,024 bytes (1 KiB) to 262,144 bytes (256 KiB). The default is 262,144 (256 KiB).

    #   * `MessageRetentionPeriod` \- The length of time, in seconds, for which Amazon SQS retains a message. Valid values: An integer from 60 seconds (1 minute) to 1,209,600 seconds (14 days). The default is 345,600 (4 days).

    #   * `Policy` \- The queue's policy. A valid AWS policy. For more information about policy structure, see [Overview of AWS IAM Policies](http://docs.aws.amazon.com/IAM/latest/UserGuide/PoliciesOverview.html) in the _Amazon IAM User Guide_.

    #   * `ReceiveMessageWaitTimeSeconds` \- The length of time, in seconds, for which a ` ReceiveMessage ` action waits for a message to arrive. Valid values: An integer from 0 to 20 (seconds). The default is 0 (zero).

    #   * `RedrivePolicy` \- The string that includes the parameters for the dead-letter queue functionality of the source queue. For more information about the redrive policy and dead-letter queues, see [Using Amazon SQS Dead-Letter Queues](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html) in the _Amazon Simple Queue Service Developer Guide_.

    #     * `deadLetterTargetArn` \- The Amazon Resource Name (ARN) of the dead-letter queue to which Amazon SQS moves messages after the value of `maxReceiveCount` is exceeded.

    #     * `maxReceiveCount` \- The number of times a message is delivered to the source queue before being moved to the dead-letter queue.

    # The dead-letter queue of a FIFO queue must also be a FIFO queue. Similarly,
    # the dead-letter queue of a standard queue must also be a standard queue.

    #   * `VisibilityTimeout` \- The visibility timeout for the queue. Valid values: An integer from 0 to 43,200 (12 hours). The default is 30. For more information about the visibility timeout, see [Visibility Timeout](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html) in the _Amazon Simple Queue Service Developer Guide_.

    # The following attributes apply only to [server-side-
    # encryption](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-
    # server-side-encryption.html):

    #   * `KmsMasterKeyId` \- The ID of an AWS-managed customer master key (CMK) for Amazon SQS or a custom CMK. For more information, see [Key Terms](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-server-side-encryption.html#sqs-sse-key-terms). While the alias of the AWS-managed CMK for Amazon SQS is always `alias/aws/sqs`, the alias of a custom CMK can, for example, be `alias/ _MyAlias_ `. For more examples, see [KeyId](http://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html#API_DescribeKey_RequestParameters) in the _AWS Key Management Service API Reference_.

    #   * `KmsDataKeyReusePeriodSeconds` \- The length of time, in seconds, for which Amazon SQS can reuse a [data key](http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#data-keys) to encrypt or decrypt messages before calling AWS KMS again. An integer representing seconds, between 60 seconds (1 minute) and 86,400 seconds (24 hours). The default is 300 (5 minutes). A shorter time period provides better security but results in more calls to KMS which might incur charges after Free Tier. For more information, see [How Does the Data Key Reuse Period Work?](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-server-side-encryption.html#sqs-how-does-the-data-key-reuse-period-work).

    # The following attributes apply only to [FIFO (first-in-first-out)
    # queues](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-
    # queues.html):

    #   * `FifoQueue` \- Designates a queue as FIFO. Valid values: `true`, `false`. You can provide this attribute only during queue creation. You can't change it for an existing queue. When you set this attribute, you must also provide the `MessageGroupId` for your messages explicitly.

    # For more information, see [FIFO Queue
    # Logic](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-
    # queues.html#FIFO-queues-understanding-logic) in the _Amazon Simple Queue
    # Service Developer Guide_.

    #   * `ContentBasedDeduplication` \- Enables content-based deduplication. Valid values: `true`, `false`. For more information, see [Exactly-Once Processing](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html#FIFO-queues-exactly-once-processing) in the _Amazon Simple Queue Service Developer Guide_.

    #     * Every message must have a unique `MessageDeduplicationId`,

    #       * You may provide a `MessageDeduplicationId` explicitly.

    #       * If you aren't able to provide a `MessageDeduplicationId` and you enable `ContentBasedDeduplication` for your queue, Amazon SQS uses a SHA-256 hash to generate the `MessageDeduplicationId` using the body of the message (but not the attributes of the message).

    #       * If you don't provide a `MessageDeduplicationId` and the queue doesn't have `ContentBasedDeduplication` set, the action fails with an error.

    #       * If the queue has `ContentBasedDeduplication` set, your `MessageDeduplicationId` overrides the generated one.

    #     * When `ContentBasedDeduplication` is in effect, messages with identical content sent within the deduplication interval are treated as duplicates and only one copy of the message is delivered.

    #     * If you send one message with `ContentBasedDeduplication` enabled and then another message with a `MessageDeduplicationId` that is the same as the one generated for the first `MessageDeduplicationId`, the two messages are treated as duplicates and only one copy of the message is delivered.

    # Any other valid special request parameters (such as the following) are
    # ignored:

    #   * `ApproximateNumberOfMessages`

    #   * `ApproximateNumberOfMessagesDelayed`

    #   * `ApproximateNumberOfMessagesNotVisible`

    #   * `CreatedTimestamp`

    #   * `LastModifiedTimestamp`

    #   * `QueueArn`
    attributes: typing.Dict[typing.Union[str, "QueueAttributeName"], str
                           ] = dataclasses.field(
                               default=ShapeBase.NOT_SET,
                           )


@dataclasses.dataclass
class CreateQueueResult(OutputShapeBase):
    """
    Returns the `QueueUrl` attribute of the created queue.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "queue_url",
                "QueueUrl",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The URL of the created Amazon SQS queue.
    queue_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteMessageBatchRequest(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "queue_url",
                "QueueUrl",
                TypeInfo(str),
            ),
            (
                "entries",
                "Entries",
                TypeInfo(typing.List[DeleteMessageBatchRequestEntry]),
            ),
        ]

    # The URL of the Amazon SQS queue from which messages are deleted.

    # Queue URLs are case-sensitive.
    queue_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of receipt handles for the messages to be deleted.
    entries: typing.List["DeleteMessageBatchRequestEntry"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteMessageBatchRequestEntry(ShapeBase):
    """
    Encloses a receipt handle and an identifier for it.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "receipt_handle",
                "ReceiptHandle",
                TypeInfo(str),
            ),
        ]

    # An identifier for this particular receipt handle. This is used to
    # communicate the result.

    # The `Id`s of a batch request need to be unique within a request
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A receipt handle.
    receipt_handle: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteMessageBatchResult(OutputShapeBase):
    """
    For each message in the batch, the response contains a `
    DeleteMessageBatchResultEntry ` tag if the message is deleted or a `
    BatchResultErrorEntry ` tag if the message can't be deleted.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "successful",
                "Successful",
                TypeInfo(typing.List[DeleteMessageBatchResultEntry]),
            ),
            (
                "failed",
                "Failed",
                TypeInfo(typing.List[BatchResultErrorEntry]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of ` DeleteMessageBatchResultEntry ` items.
    successful: typing.List["DeleteMessageBatchResultEntry"
                           ] = dataclasses.field(
                               default=ShapeBase.NOT_SET,
                           )

    # A list of ` BatchResultErrorEntry ` items.
    failed: typing.List["BatchResultErrorEntry"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteMessageBatchResultEntry(ShapeBase):
    """
    Encloses the `Id` of an entry in ` DeleteMessageBatch.`
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
        ]

    # Represents a successfully deleted message.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteMessageRequest(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "queue_url",
                "QueueUrl",
                TypeInfo(str),
            ),
            (
                "receipt_handle",
                "ReceiptHandle",
                TypeInfo(str),
            ),
        ]

    # The URL of the Amazon SQS queue from which messages are deleted.

    # Queue URLs are case-sensitive.
    queue_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The receipt handle associated with the message to delete.
    receipt_handle: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteQueueRequest(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "queue_url",
                "QueueUrl",
                TypeInfo(str),
            ),
        ]

    # The URL of the Amazon SQS queue to delete.

    # Queue URLs are case-sensitive.
    queue_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EmptyBatchRequest(ShapeBase):
    """
    The batch request doesn't contain any entries.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class GetQueueAttributesRequest(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "queue_url",
                "QueueUrl",
                TypeInfo(str),
            ),
            (
                "attribute_names",
                "AttributeNames",
                TypeInfo(typing.List[typing.Union[str, QueueAttributeName]]),
            ),
        ]

    # The URL of the Amazon SQS queue whose attribute information is retrieved.

    # Queue URLs are case-sensitive.
    queue_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of attributes for which to retrieve information.

    # In the future, new attributes might be added. If you write code that calls
    # this action, we recommend that you structure your code so that it can
    # handle new attributes gracefully.

    # The following attributes are supported:

    #   * `All` \- Returns all values.

    #   * `ApproximateNumberOfMessages` \- Returns the approximate number of visible messages in a queue. For more information, see [Resources Required to Process Messages](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-resources-required-process-messages.html) in the _Amazon Simple Queue Service Developer Guide_.

    #   * `ApproximateNumberOfMessagesDelayed` \- Returns the approximate number of messages that are waiting to be added to the queue.

    #   * `ApproximateNumberOfMessagesNotVisible` \- Returns the approximate number of messages that have not timed-out and aren't deleted. For more information, see [Resources Required to Process Messages](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-resources-required-process-messages.html) in the _Amazon Simple Queue Service Developer Guide_.

    #   * `CreatedTimestamp` \- Returns the time when the queue was created in seconds ([epoch time](http://en.wikipedia.org/wiki/Unix_time)).

    #   * `DelaySeconds` \- Returns the default delay on the queue in seconds.

    #   * `LastModifiedTimestamp` \- Returns the time when the queue was last changed in seconds ([epoch time](http://en.wikipedia.org/wiki/Unix_time)).

    #   * `MaximumMessageSize` \- Returns the limit of how many bytes a message can contain before Amazon SQS rejects it.

    #   * `MessageRetentionPeriod` \- Returns the length of time, in seconds, for which Amazon SQS retains a message.

    #   * `Policy` \- Returns the policy of the queue.

    #   * `QueueArn` \- Returns the Amazon resource name (ARN) of the queue.

    #   * `ReceiveMessageWaitTimeSeconds` \- Returns the length of time, in seconds, for which the `ReceiveMessage` action waits for a message to arrive.

    #   * `RedrivePolicy` \- Returns the string that includes the parameters for dead-letter queue functionality of the source queue. For more information about the redrive policy and dead-letter queues, see [Using Amazon SQS Dead-Letter Queues](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html) in the _Amazon Simple Queue Service Developer Guide_.

    #     * `deadLetterTargetArn` \- The Amazon Resource Name (ARN) of the dead-letter queue to which Amazon SQS moves messages after the value of `maxReceiveCount` is exceeded.

    #     * `maxReceiveCount` \- The number of times a message is delivered to the source queue before being moved to the dead-letter queue.

    #   * `VisibilityTimeout` \- Returns the visibility timeout for the queue. For more information about the visibility timeout, see [Visibility Timeout](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html) in the _Amazon Simple Queue Service Developer Guide_.

    # The following attributes apply only to [server-side-
    # encryption](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-
    # server-side-encryption.html):

    #   * `KmsMasterKeyId` \- Returns the ID of an AWS-managed customer master key (CMK) for Amazon SQS or a custom CMK. For more information, see [Key Terms](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-server-side-encryption.html#sqs-sse-key-terms).

    #   * `KmsDataKeyReusePeriodSeconds` \- Returns the length of time, in seconds, for which Amazon SQS can reuse a data key to encrypt or decrypt messages before calling AWS KMS again. For more information, see [How Does the Data Key Reuse Period Work?](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-server-side-encryption.html#sqs-how-does-the-data-key-reuse-period-work).

    # The following attributes apply only to [FIFO (first-in-first-out)
    # queues](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-
    # queues.html):

    #   * `FifoQueue` \- Returns whether the queue is FIFO. For more information, see [FIFO Queue Logic](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html#FIFO-queues-understanding-logic) in the _Amazon Simple Queue Service Developer Guide_.

    # To determine whether a queue is
    # [FIFO](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-
    # queues.html), you can check whether `QueueName` ends with the `.fifo`
    # suffix.

    #   * `ContentBasedDeduplication` \- Returns whether content-based deduplication is enabled for the queue. For more information, see [Exactly-Once Processing](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html#FIFO-queues-exactly-once-processing) in the _Amazon Simple Queue Service Developer Guide_.
    attribute_names: typing.List[typing.Union[str, "QueueAttributeName"]
                                ] = dataclasses.field(
                                    default=ShapeBase.NOT_SET,
                                )


@dataclasses.dataclass
class GetQueueAttributesResult(OutputShapeBase):
    """
    A list of returned queue attributes.
    """

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
                TypeInfo(
                    typing.Dict[typing.Union[str, QueueAttributeName], str]
                ),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A map of attributes to their respective values.
    attributes: typing.Dict[typing.Union[str, "QueueAttributeName"], str
                           ] = dataclasses.field(
                               default=ShapeBase.NOT_SET,
                           )


@dataclasses.dataclass
class GetQueueUrlRequest(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "queue_name",
                "QueueName",
                TypeInfo(str),
            ),
            (
                "queue_owner_aws_account_id",
                "QueueOwnerAWSAccountId",
                TypeInfo(str),
            ),
        ]

    # The name of the queue whose URL must be fetched. Maximum 80 characters.
    # Valid values: alphanumeric characters, hyphens (`-`), and underscores
    # (`_`).

    # Queue names are case-sensitive.
    queue_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The AWS account ID of the account that created the queue.
    queue_owner_aws_account_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetQueueUrlResult(OutputShapeBase):
    """
    For more information, see
    [Responses](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/UnderstandingResponses.html)
    in the _Amazon Simple Queue Service Developer Guide_.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "queue_url",
                "QueueUrl",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The URL of the queue.
    queue_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidAttributeName(ShapeBase):
    """
    The attribute referred to doesn't exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidBatchEntryId(ShapeBase):
    """
    The `Id` of a batch entry in a batch request doesn't abide by the specification.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidIdFormat(ShapeBase):
    """
    The receipt handle isn't valid for the current version.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class InvalidMessageContents(ShapeBase):
    """
    The message contains characters outside the allowed set.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ListDeadLetterSourceQueuesRequest(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "queue_url",
                "QueueUrl",
                TypeInfo(str),
            ),
        ]

    # The URL of a dead-letter queue.

    # Queue URLs are case-sensitive.
    queue_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListDeadLetterSourceQueuesResult(OutputShapeBase):
    """
    A list of your dead letter source queues.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "queue_urls",
                "queueUrls",
                TypeInfo(typing.List[str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of source queue URLs that have the `RedrivePolicy` queue attribute
    # configured with a dead-letter queue.
    queue_urls: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListQueueTagsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "queue_url",
                "QueueUrl",
                TypeInfo(str),
            ),
        ]

    # The URL of the queue.
    queue_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListQueueTagsResult(OutputShapeBase):
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
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The list of all tags added to the specified queue.
    tags: typing.Dict[str, str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListQueuesRequest(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "queue_name_prefix",
                "QueueNamePrefix",
                TypeInfo(str),
            ),
        ]

    # A string to use for filtering the list results. Only those queues whose
    # name begins with the specified string are returned.

    # Queue names are case-sensitive.
    queue_name_prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListQueuesResult(OutputShapeBase):
    """
    A list of your queues.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "queue_urls",
                "QueueUrls",
                TypeInfo(typing.List[str]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of queue URLs, up to 1,000 entries.
    queue_urls: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Message(ShapeBase):
    """
    An Amazon SQS message.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message_id",
                "MessageId",
                TypeInfo(str),
            ),
            (
                "receipt_handle",
                "ReceiptHandle",
                TypeInfo(str),
            ),
            (
                "md5_of_body",
                "MD5OfBody",
                TypeInfo(str),
            ),
            (
                "body",
                "Body",
                TypeInfo(str),
            ),
            (
                "attributes",
                "Attributes",
                TypeInfo(
                    typing.Dict[typing.
                                Union[str, MessageSystemAttributeName], str]
                ),
            ),
            (
                "md5_of_message_attributes",
                "MD5OfMessageAttributes",
                TypeInfo(str),
            ),
            (
                "message_attributes",
                "MessageAttributes",
                TypeInfo(typing.Dict[str, MessageAttributeValue]),
            ),
        ]

    # A unique identifier for the message. A `MessageId`is considered unique
    # across all AWS accounts for an extended period of time.
    message_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An identifier associated with the act of receiving the message. A new
    # receipt handle is returned every time you receive a message. When deleting
    # a message, you provide the last received receipt handle to delete the
    # message.
    receipt_handle: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An MD5 digest of the non-URL-encoded message body string.
    md5_of_body: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The message's contents (not URL-encoded).
    body: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # `SenderId`, `SentTimestamp`, `ApproximateReceiveCount`, and/or
    # `ApproximateFirstReceiveTimestamp`. `SentTimestamp` and
    # `ApproximateFirstReceiveTimestamp` are each returned as an integer
    # representing the [epoch time](http://en.wikipedia.org/wiki/Unix_time) in
    # milliseconds.
    attributes: typing.Dict[typing.Union[str, "MessageSystemAttributeName"], str
                           ] = dataclasses.field(
                               default=ShapeBase.NOT_SET,
                           )

    # An MD5 digest of the non-URL-encoded message attribute string. You can use
    # this attribute to verify that Amazon SQS received the message correctly.
    # Amazon SQS URL-decodes the message before creating the MD5 digest. For
    # information about MD5, see [RFC1321](https://www.ietf.org/rfc/rfc1321.txt).
    md5_of_message_attributes: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Each message attribute consists of a `Name`, `Type`, and `Value`. For more
    # information, see [Message Attribute Items and
    # Validation](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-
    # message-attributes.html#message-attributes-items-validation) in the _Amazon
    # Simple Queue Service Developer Guide_.
    message_attributes: typing.Dict[str, "MessageAttributeValue"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )


@dataclasses.dataclass
class MessageAttributeValue(ShapeBase):
    """
    The user-specified message attribute value. For string data types, the `Value`
    attribute has the same restrictions on the content as the message body. For more
    information, see ` SendMessage.`

    `Name`, `type`, `value` and the message body must not be empty or null. All
    parts of the message attribute, including `Name`, `Type`, and `Value`, are part
    of the message size restriction (256 KB or 262,144 bytes).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "data_type",
                "DataType",
                TypeInfo(str),
            ),
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
                "string_list_values",
                "StringListValues",
                TypeInfo(typing.List[str]),
            ),
            (
                "binary_list_values",
                "BinaryListValues",
                TypeInfo(typing.List[typing.Any]),
            ),
        ]

    # Amazon SQS supports the following logical data types: `String`, `Number`,
    # and `Binary`. For the `Number` data type, you must use `StringValue`.

    # You can also append custom labels. For more information, see [Message
    # Attribute Data Types and
    # Validation](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-
    # message-attributes.html#message-attributes-data-types-validation) in the
    # _Amazon Simple Queue Service Developer Guide_.
    data_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Strings are Unicode with UTF-8 binary encoding. For a list of code values,
    # see [ASCII Printable
    # Characters](http://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters).
    string_value: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Binary type attributes can store any binary data, such as compressed data,
    # encrypted data, or images.
    binary_value: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Not implemented. Reserved for future use.
    string_list_values: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Not implemented. Reserved for future use.
    binary_list_values: typing.List[typing.Any] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class MessageNotInflight(ShapeBase):
    """
    The message referred to isn't in flight.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


class MessageSystemAttributeName(str):
    SenderId = "SenderId"
    SentTimestamp = "SentTimestamp"
    ApproximateReceiveCount = "ApproximateReceiveCount"
    ApproximateFirstReceiveTimestamp = "ApproximateFirstReceiveTimestamp"
    SequenceNumber = "SequenceNumber"
    MessageDeduplicationId = "MessageDeduplicationId"
    MessageGroupId = "MessageGroupId"


@dataclasses.dataclass
class OverLimit(ShapeBase):
    """
    The action that you requested would violate a limit. For example,
    `ReceiveMessage` returns this error if the maximum number of inflight messages
    is reached. ` AddPermission ` returns this error if the maximum number of
    permissions for the queue is reached.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class PurgeQueueInProgress(ShapeBase):
    """
    Indicates that the specified queue previously received a `PurgeQueue` request
    within the last 60 seconds (the time it can take to delete the messages in the
    queue).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class PurgeQueueRequest(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "queue_url",
                "QueueUrl",
                TypeInfo(str),
            ),
        ]

    # The URL of the queue from which the `PurgeQueue` action deletes messages.

    # Queue URLs are case-sensitive.
    queue_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class QueueAttributeName(str):
    All = "All"
    Policy = "Policy"
    VisibilityTimeout = "VisibilityTimeout"
    MaximumMessageSize = "MaximumMessageSize"
    MessageRetentionPeriod = "MessageRetentionPeriod"
    ApproximateNumberOfMessages = "ApproximateNumberOfMessages"
    ApproximateNumberOfMessagesNotVisible = "ApproximateNumberOfMessagesNotVisible"
    CreatedTimestamp = "CreatedTimestamp"
    LastModifiedTimestamp = "LastModifiedTimestamp"
    QueueArn = "QueueArn"
    ApproximateNumberOfMessagesDelayed = "ApproximateNumberOfMessagesDelayed"
    DelaySeconds = "DelaySeconds"
    ReceiveMessageWaitTimeSeconds = "ReceiveMessageWaitTimeSeconds"
    RedrivePolicy = "RedrivePolicy"
    FifoQueue = "FifoQueue"
    ContentBasedDeduplication = "ContentBasedDeduplication"
    KmsMasterKeyId = "KmsMasterKeyId"
    KmsDataKeyReusePeriodSeconds = "KmsDataKeyReusePeriodSeconds"


@dataclasses.dataclass
class QueueDeletedRecently(ShapeBase):
    """
    You must wait 60 seconds after deleting a queue before you can create another
    one with the same name.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class QueueDoesNotExist(ShapeBase):
    """
    The queue referred to doesn't exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class QueueNameExists(ShapeBase):
    """
    A queue already exists with this name. Amazon SQS returns this error only if the
    request includes attributes whose values differ from those of the existing
    queue.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ReceiptHandleIsInvalid(ShapeBase):
    """
    The receipt handle provided isn't valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ReceiveMessageRequest(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "queue_url",
                "QueueUrl",
                TypeInfo(str),
            ),
            (
                "attribute_names",
                "AttributeNames",
                TypeInfo(typing.List[typing.Union[str, QueueAttributeName]]),
            ),
            (
                "message_attribute_names",
                "MessageAttributeNames",
                TypeInfo(typing.List[str]),
            ),
            (
                "max_number_of_messages",
                "MaxNumberOfMessages",
                TypeInfo(int),
            ),
            (
                "visibility_timeout",
                "VisibilityTimeout",
                TypeInfo(int),
            ),
            (
                "wait_time_seconds",
                "WaitTimeSeconds",
                TypeInfo(int),
            ),
            (
                "receive_request_attempt_id",
                "ReceiveRequestAttemptId",
                TypeInfo(str),
            ),
        ]

    # The URL of the Amazon SQS queue from which messages are received.

    # Queue URLs are case-sensitive.
    queue_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of attributes that need to be returned along with each message.
    # These attributes include:

    #   * `All` \- Returns all values.

    #   * `ApproximateFirstReceiveTimestamp` \- Returns the time the message was first received from the queue ([epoch time](http://en.wikipedia.org/wiki/Unix_time) in milliseconds).

    #   * `ApproximateReceiveCount` \- Returns the number of times a message has been received from the queue but not deleted.

    #   * `SenderId`

    #     * For an IAM user, returns the IAM user ID, for example `ABCDEFGHI1JKLMNOPQ23R`.

    #     * For an IAM role, returns the IAM role ID, for example `ABCDE1F2GH3I4JK5LMNOP:i-a123b456`.

    #   * `SentTimestamp` \- Returns the time the message was sent to the queue ([epoch time](http://en.wikipedia.org/wiki/Unix_time) in milliseconds).

    #   * `MessageDeduplicationId` \- Returns the value provided by the sender that calls the ` SendMessage ` action.

    #   * `MessageGroupId` \- Returns the value provided by the sender that calls the ` SendMessage ` action. Messages with the same `MessageGroupId` are returned in sequence.

    #   * `SequenceNumber` \- Returns the value provided by Amazon SQS.

    # Any other valid special request parameters (such as the following) are
    # ignored:

    #   * `ApproximateNumberOfMessages`

    #   * `ApproximateNumberOfMessagesDelayed`

    #   * `ApproximateNumberOfMessagesNotVisible`

    #   * `CreatedTimestamp`

    #   * `ContentBasedDeduplication`

    #   * `DelaySeconds`

    #   * `FifoQueue`

    #   * `LastModifiedTimestamp`

    #   * `MaximumMessageSize`

    #   * `MessageRetentionPeriod`

    #   * `Policy`

    #   * `QueueArn`,

    #   * `ReceiveMessageWaitTimeSeconds`

    #   * `RedrivePolicy`

    #   * `VisibilityTimeout`
    attribute_names: typing.List[typing.Union[str, "QueueAttributeName"]
                                ] = dataclasses.field(
                                    default=ShapeBase.NOT_SET,
                                )

    # The name of the message attribute, where _N_ is the index.

    #   * The name can contain alphanumeric characters and the underscore (`_`), hyphen (`-`), and period (`.`).

    #   * The name is case-sensitive and must be unique among all attribute names for the message.

    #   * The name must not start with AWS-reserved prefixes such as `AWS.` or `Amazon.` (or any casing variants).

    #   * The name must not start or end with a period (`.`), and it should not have periods in succession (`..`).

    #   * The name can be up to 256 characters long.

    # When using `ReceiveMessage`, you can send a list of attribute names to
    # receive, or you can return all of the attributes by specifying `All` or
    # `.*` in your request. You can also use all message attributes starting with
    # a prefix, for example `bar.*`.
    message_attribute_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of messages to return. Amazon SQS never returns more
    # messages than this value (however, fewer messages might be returned). Valid
    # values are 1 to 10. Default is 1.
    max_number_of_messages: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The duration (in seconds) that the received messages are hidden from
    # subsequent retrieve requests after being retrieved by a `ReceiveMessage`
    # request.
    visibility_timeout: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The duration (in seconds) for which the call waits for a message to arrive
    # in the queue before returning. If a message is available, the call returns
    # sooner than `WaitTimeSeconds`. If no messages are available and the wait
    # time expires, the call returns successfully with an empty list of messages.
    wait_time_seconds: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This parameter applies only to FIFO (first-in-first-out) queues.

    # The token used for deduplication of `ReceiveMessage` calls. If a networking
    # issue occurs after a `ReceiveMessage` action, and instead of a response you
    # receive a generic error, you can retry the same action with an identical
    # `ReceiveRequestAttemptId` to retrieve the same set of messages, even if
    # their visibility timeout has not yet expired.

    #   * You can use `ReceiveRequestAttemptId` only for 5 minutes after a `ReceiveMessage` action.

    #   * When you set `FifoQueue`, a caller of the `ReceiveMessage` action can provide a `ReceiveRequestAttemptId` explicitly.

    #   * If a caller of the `ReceiveMessage` action doesn't provide a `ReceiveRequestAttemptId`, Amazon SQS generates a `ReceiveRequestAttemptId`.

    #   * You can retry the `ReceiveMessage` action with the same `ReceiveRequestAttemptId` if none of the messages have been modified (deleted or had their visibility changes).

    #   * During a visibility timeout, subsequent calls with the same `ReceiveRequestAttemptId` return the same messages and receipt handles. If a retry occurs within the deduplication interval, it resets the visibility timeout. For more information, see [Visibility Timeout](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html) in the _Amazon Simple Queue Service Developer Guide_.

    # If a caller of the `ReceiveMessage` action is still processing messages
    # when the visibility timeout expires and messages become visible, another
    # worker reading from the same queue can receive the same messages and
    # therefore process duplicates. Also, if a reader whose message processing
    # time is longer than the visibility timeout tries to delete the processed
    # messages, the action fails with an error.

    # To mitigate this effect, ensure that your application observes a safe
    # threshold before the visibility timeout expires and extend the visibility
    # timeout as necessary.

    #   * While messages with a particular `MessageGroupId` are invisible, no more messages belonging to the same `MessageGroupId` are returned until the visibility timeout expires. You can still receive messages with another `MessageGroupId` as long as it is also visible.

    #   * If a caller of `ReceiveMessage` can't track the `ReceiveRequestAttemptId`, no retries work until the original visibility timeout expires. As a result, delays might occur but the messages in the queue remain in a strict order.

    # The length of `ReceiveRequestAttemptId` is 128 characters.
    # `ReceiveRequestAttemptId` can contain alphanumeric characters (`a-z`,
    # `A-Z`, `0-9`) and punctuation (`!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~`).

    # For best practices of using `ReceiveRequestAttemptId`, see [Using the
    # ReceiveRequestAttemptId Request
    # Parameter](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-
    # queue-recommendations.html#using-receiverequestattemptid-request-parameter)
    # in the _Amazon Simple Queue Service Developer Guide_.
    receive_request_attempt_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ReceiveMessageResult(OutputShapeBase):
    """
    A list of received messages.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "messages",
                "Messages",
                TypeInfo(typing.List[Message]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of messages.
    messages: typing.List["Message"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RemovePermissionRequest(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "queue_url",
                "QueueUrl",
                TypeInfo(str),
            ),
            (
                "label",
                "Label",
                TypeInfo(str),
            ),
        ]

    # The URL of the Amazon SQS queue from which permissions are removed.

    # Queue URLs are case-sensitive.
    queue_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identification of the permission to remove. This is the label added
    # using the ` AddPermission ` action.
    label: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SendMessageBatchRequest(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "queue_url",
                "QueueUrl",
                TypeInfo(str),
            ),
            (
                "entries",
                "Entries",
                TypeInfo(typing.List[SendMessageBatchRequestEntry]),
            ),
        ]

    # The URL of the Amazon SQS queue to which batched messages are sent.

    # Queue URLs are case-sensitive.
    queue_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of ` SendMessageBatchRequestEntry ` items.
    entries: typing.List["SendMessageBatchRequestEntry"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SendMessageBatchRequestEntry(ShapeBase):
    """
    Contains the details of a single Amazon SQS message along with an `Id`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "message_body",
                "MessageBody",
                TypeInfo(str),
            ),
            (
                "delay_seconds",
                "DelaySeconds",
                TypeInfo(int),
            ),
            (
                "message_attributes",
                "MessageAttributes",
                TypeInfo(typing.Dict[str, MessageAttributeValue]),
            ),
            (
                "message_deduplication_id",
                "MessageDeduplicationId",
                TypeInfo(str),
            ),
            (
                "message_group_id",
                "MessageGroupId",
                TypeInfo(str),
            ),
        ]

    # An identifier for a message in this batch used to communicate the result.

    # The `Id`s of a batch request need to be unique within a request
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The body of the message.
    message_body: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The length of time, in seconds, for which a specific message is delayed.
    # Valid values: 0 to 900. Maximum: 15 minutes. Messages with a positive
    # `DelaySeconds` value become available for processing after the delay period
    # is finished. If you don't specify a value, the default value for the queue
    # is applied.

    # When you set `FifoQueue`, you can't set `DelaySeconds` per message. You can
    # set this parameter only on a queue level.
    delay_seconds: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Each message attribute consists of a `Name`, `Type`, and `Value`. For more
    # information, see [Message Attribute Items and
    # Validation](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-
    # message-attributes.html#message-attributes-items-validation) in the _Amazon
    # Simple Queue Service Developer Guide_.
    message_attributes: typing.Dict[str, "MessageAttributeValue"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # This parameter applies only to FIFO (first-in-first-out) queues.

    # The token used for deduplication of messages within a 5-minute minimum
    # deduplication interval. If a message with a particular
    # `MessageDeduplicationId` is sent successfully, subsequent messages with the
    # same `MessageDeduplicationId` are accepted successfully but aren't
    # delivered. For more information, see [ Exactly-Once
    # Processing](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-
    # queues.html#FIFO-queues-exactly-once-processing) in the _Amazon Simple
    # Queue Service Developer Guide_.

    #   * Every message must have a unique `MessageDeduplicationId`,

    #     * You may provide a `MessageDeduplicationId` explicitly.

    #     * If you aren't able to provide a `MessageDeduplicationId` and you enable `ContentBasedDeduplication` for your queue, Amazon SQS uses a SHA-256 hash to generate the `MessageDeduplicationId` using the body of the message (but not the attributes of the message).

    #     * If you don't provide a `MessageDeduplicationId` and the queue doesn't have `ContentBasedDeduplication` set, the action fails with an error.

    #     * If the queue has `ContentBasedDeduplication` set, your `MessageDeduplicationId` overrides the generated one.

    #   * When `ContentBasedDeduplication` is in effect, messages with identical content sent within the deduplication interval are treated as duplicates and only one copy of the message is delivered.

    #   * If you send one message with `ContentBasedDeduplication` enabled and then another message with a `MessageDeduplicationId` that is the same as the one generated for the first `MessageDeduplicationId`, the two messages are treated as duplicates and only one copy of the message is delivered.

    # The `MessageDeduplicationId` is available to the recipient of the message
    # (this can be useful for troubleshooting delivery issues).

    # If a message is sent successfully but the acknowledgement is lost and the
    # message is resent with the same `MessageDeduplicationId` after the
    # deduplication interval, Amazon SQS can't detect duplicate messages.

    # The length of `MessageDeduplicationId` is 128 characters.
    # `MessageDeduplicationId` can contain alphanumeric characters (`a-z`, `A-Z`,
    # `0-9`) and punctuation (`!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~`).

    # For best practices of using `MessageDeduplicationId`, see [Using the
    # MessageDeduplicationId
    # Property](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-
    # queue-recommendations.html#using-messagededuplicationid-property) in the
    # _Amazon Simple Queue Service Developer Guide_.
    message_deduplication_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # This parameter applies only to FIFO (first-in-first-out) queues.

    # The tag that specifies that a message belongs to a specific message group.
    # Messages that belong to the same message group are processed in a FIFO
    # manner (however, messages in different message groups might be processed
    # out of order). To interleave multiple ordered streams within a single
    # queue, use `MessageGroupId` values (for example, session data for multiple
    # users). In this scenario, multiple readers can process the queue, but the
    # session data of each user is processed in a FIFO fashion.

    #   * You must associate a non-empty `MessageGroupId` with a message. If you don't provide a `MessageGroupId`, the action fails.

    #   * `ReceiveMessage` might return messages with multiple `MessageGroupId` values. For each `MessageGroupId`, the messages are sorted by time sent. The caller can't specify a `MessageGroupId`.

    # The length of `MessageGroupId` is 128 characters. Valid values are
    # alphanumeric characters and punctuation
    # `(!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~)`.

    # For best practices of using `MessageGroupId`, see [Using the MessageGroupId
    # Property](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-
    # queue-recommendations.html#using-messagegroupid-property) in the _Amazon
    # Simple Queue Service Developer Guide_.

    # `MessageGroupId` is required for FIFO queues. You can't use it for Standard
    # queues.
    message_group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SendMessageBatchResult(OutputShapeBase):
    """
    For each message in the batch, the response contains a `
    SendMessageBatchResultEntry ` tag if the message succeeds or a `
    BatchResultErrorEntry ` tag if the message fails.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "successful",
                "Successful",
                TypeInfo(typing.List[SendMessageBatchResultEntry]),
            ),
            (
                "failed",
                "Failed",
                TypeInfo(typing.List[BatchResultErrorEntry]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of ` SendMessageBatchResultEntry ` items.
    successful: typing.List["SendMessageBatchResultEntry"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A list of ` BatchResultErrorEntry ` items with error details about each
    # message that can't be enqueued.
    failed: typing.List["BatchResultErrorEntry"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class SendMessageBatchResultEntry(ShapeBase):
    """
    Encloses a `MessageId` for a successfully-enqueued message in a `
    SendMessageBatch.`
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "message_id",
                "MessageId",
                TypeInfo(str),
            ),
            (
                "md5_of_message_body",
                "MD5OfMessageBody",
                TypeInfo(str),
            ),
            (
                "md5_of_message_attributes",
                "MD5OfMessageAttributes",
                TypeInfo(str),
            ),
            (
                "sequence_number",
                "SequenceNumber",
                TypeInfo(str),
            ),
        ]

    # An identifier for the message in this batch.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An identifier for the message.
    message_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An MD5 digest of the non-URL-encoded message attribute string. You can use
    # this attribute to verify that Amazon SQS received the message correctly.
    # Amazon SQS URL-decodes the message before creating the MD5 digest. For
    # information about MD5, see [RFC1321](https://www.ietf.org/rfc/rfc1321.txt).
    md5_of_message_body: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An MD5 digest of the non-URL-encoded message attribute string. You can use
    # this attribute to verify that Amazon SQS received the message correctly.
    # Amazon SQS URL-decodes the message before creating the MD5 digest. For
    # information about MD5, see [RFC1321](https://www.ietf.org/rfc/rfc1321.txt).
    md5_of_message_attributes: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # This parameter applies only to FIFO (first-in-first-out) queues.

    # The large, non-consecutive number that Amazon SQS assigns to each message.

    # The length of `SequenceNumber` is 128 bits. As `SequenceNumber` continues
    # to increase for a particular `MessageGroupId`.
    sequence_number: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SendMessageRequest(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "queue_url",
                "QueueUrl",
                TypeInfo(str),
            ),
            (
                "message_body",
                "MessageBody",
                TypeInfo(str),
            ),
            (
                "delay_seconds",
                "DelaySeconds",
                TypeInfo(int),
            ),
            (
                "message_attributes",
                "MessageAttributes",
                TypeInfo(typing.Dict[str, MessageAttributeValue]),
            ),
            (
                "message_deduplication_id",
                "MessageDeduplicationId",
                TypeInfo(str),
            ),
            (
                "message_group_id",
                "MessageGroupId",
                TypeInfo(str),
            ),
        ]

    # The URL of the Amazon SQS queue to which a message is sent.

    # Queue URLs are case-sensitive.
    queue_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The message to send. The maximum string size is 256 KB.

    # A message can include only XML, JSON, and unformatted text. The following
    # Unicode characters are allowed:

    # `#x9` | `#xA` | `#xD` | `#x20` to `#xD7FF` | `#xE000` to `#xFFFD` |
    # `#x10000` to `#x10FFFF`

    # Any characters not included in this list will be rejected. For more
    # information, see the [W3C specification for
    # characters](http://www.w3.org/TR/REC-xml/#charsets).
    message_body: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The length of time, in seconds, for which to delay a specific message.
    # Valid values: 0 to 900. Maximum: 15 minutes. Messages with a positive
    # `DelaySeconds` value become available for processing after the delay period
    # is finished. If you don't specify a value, the default value for the queue
    # applies.

    # When you set `FifoQueue`, you can't set `DelaySeconds` per message. You can
    # set this parameter only on a queue level.
    delay_seconds: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Each message attribute consists of a `Name`, `Type`, and `Value`. For more
    # information, see [Message Attribute Items and
    # Validation](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-
    # message-attributes.html#message-attributes-items-validation) in the _Amazon
    # Simple Queue Service Developer Guide_.
    message_attributes: typing.Dict[str, "MessageAttributeValue"
                                   ] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # This parameter applies only to FIFO (first-in-first-out) queues.

    # The token used for deduplication of sent messages. If a message with a
    # particular `MessageDeduplicationId` is sent successfully, any messages sent
    # with the same `MessageDeduplicationId` are accepted successfully but aren't
    # delivered during the 5-minute deduplication interval. For more information,
    # see [ Exactly-Once
    # Processing](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-
    # queues.html#FIFO-queues-exactly-once-processing) in the _Amazon Simple
    # Queue Service Developer Guide_.

    #   * Every message must have a unique `MessageDeduplicationId`,

    #     * You may provide a `MessageDeduplicationId` explicitly.

    #     * If you aren't able to provide a `MessageDeduplicationId` and you enable `ContentBasedDeduplication` for your queue, Amazon SQS uses a SHA-256 hash to generate the `MessageDeduplicationId` using the body of the message (but not the attributes of the message).

    #     * If you don't provide a `MessageDeduplicationId` and the queue doesn't have `ContentBasedDeduplication` set, the action fails with an error.

    #     * If the queue has `ContentBasedDeduplication` set, your `MessageDeduplicationId` overrides the generated one.

    #   * When `ContentBasedDeduplication` is in effect, messages with identical content sent within the deduplication interval are treated as duplicates and only one copy of the message is delivered.

    #   * If you send one message with `ContentBasedDeduplication` enabled and then another message with a `MessageDeduplicationId` that is the same as the one generated for the first `MessageDeduplicationId`, the two messages are treated as duplicates and only one copy of the message is delivered.

    # The `MessageDeduplicationId` is available to the recipient of the message
    # (this can be useful for troubleshooting delivery issues).

    # If a message is sent successfully but the acknowledgement is lost and the
    # message is resent with the same `MessageDeduplicationId` after the
    # deduplication interval, Amazon SQS can't detect duplicate messages.

    # The length of `MessageDeduplicationId` is 128 characters.
    # `MessageDeduplicationId` can contain alphanumeric characters (`a-z`, `A-Z`,
    # `0-9`) and punctuation (`!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~`).

    # For best practices of using `MessageDeduplicationId`, see [Using the
    # MessageDeduplicationId
    # Property](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-
    # queue-recommendations.html#using-messagededuplicationid-property) in the
    # _Amazon Simple Queue Service Developer Guide_.
    message_deduplication_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # This parameter applies only to FIFO (first-in-first-out) queues.

    # The tag that specifies that a message belongs to a specific message group.
    # Messages that belong to the same message group are processed in a FIFO
    # manner (however, messages in different message groups might be processed
    # out of order). To interleave multiple ordered streams within a single
    # queue, use `MessageGroupId` values (for example, session data for multiple
    # users). In this scenario, multiple readers can process the queue, but the
    # session data of each user is processed in a FIFO fashion.

    #   * You must associate a non-empty `MessageGroupId` with a message. If you don't provide a `MessageGroupId`, the action fails.

    #   * `ReceiveMessage` might return messages with multiple `MessageGroupId` values. For each `MessageGroupId`, the messages are sorted by time sent. The caller can't specify a `MessageGroupId`.

    # The length of `MessageGroupId` is 128 characters. Valid values are
    # alphanumeric characters and punctuation
    # `(!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~)`.

    # For best practices of using `MessageGroupId`, see [Using the MessageGroupId
    # Property](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-
    # queue-recommendations.html#using-messagegroupid-property) in the _Amazon
    # Simple Queue Service Developer Guide_.

    # `MessageGroupId` is required for FIFO queues. You can't use it for Standard
    # queues.
    message_group_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SendMessageResult(OutputShapeBase):
    """
    The `MD5OfMessageBody` and `MessageId` elements.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "md5_of_message_body",
                "MD5OfMessageBody",
                TypeInfo(str),
            ),
            (
                "md5_of_message_attributes",
                "MD5OfMessageAttributes",
                TypeInfo(str),
            ),
            (
                "message_id",
                "MessageId",
                TypeInfo(str),
            ),
            (
                "sequence_number",
                "SequenceNumber",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An MD5 digest of the non-URL-encoded message attribute string. You can use
    # this attribute to verify that Amazon SQS received the message correctly.
    # Amazon SQS URL-decodes the message before creating the MD5 digest. For
    # information about MD5, see [RFC1321](https://www.ietf.org/rfc/rfc1321.txt).
    md5_of_message_body: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An MD5 digest of the non-URL-encoded message attribute string. You can use
    # this attribute to verify that Amazon SQS received the message correctly.
    # Amazon SQS URL-decodes the message before creating the MD5 digest. For
    # information about MD5, see [RFC1321](https://www.ietf.org/rfc/rfc1321.txt).
    md5_of_message_attributes: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An attribute containing the `MessageId` of the message sent to the queue.
    # For more information, see [Queue and Message
    # Identifiers](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-
    # queue-message-identifiers.html) in the _Amazon Simple Queue Service
    # Developer Guide_.
    message_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This parameter applies only to FIFO (first-in-first-out) queues.

    # The large, non-consecutive number that Amazon SQS assigns to each message.

    # The length of `SequenceNumber` is 128 bits. `SequenceNumber` continues to
    # increase for a particular `MessageGroupId`.
    sequence_number: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SetQueueAttributesRequest(ShapeBase):
    """

    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "queue_url",
                "QueueUrl",
                TypeInfo(str),
            ),
            (
                "attributes",
                "Attributes",
                TypeInfo(
                    typing.Dict[typing.Union[str, QueueAttributeName], str]
                ),
            ),
        ]

    # The URL of the Amazon SQS queue whose attributes are set.

    # Queue URLs are case-sensitive.
    queue_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A map of attributes to set.

    # The following lists the names, descriptions, and values of the special
    # request parameters that the `SetQueueAttributes` action uses:

    #   * `DelaySeconds` \- The length of time, in seconds, for which the delivery of all messages in the queue is delayed. Valid values: An integer from 0 to 900 (15 minutes). The default is 0 (zero).

    #   * `MaximumMessageSize` \- The limit of how many bytes a message can contain before Amazon SQS rejects it. Valid values: An integer from 1,024 bytes (1 KiB) up to 262,144 bytes (256 KiB). The default is 262,144 (256 KiB).

    #   * `MessageRetentionPeriod` \- The length of time, in seconds, for which Amazon SQS retains a message. Valid values: An integer representing seconds, from 60 (1 minute) to 1,209,600 (14 days). The default is 345,600 (4 days).

    #   * `Policy` \- The queue's policy. A valid AWS policy. For more information about policy structure, see [Overview of AWS IAM Policies](http://docs.aws.amazon.com/IAM/latest/UserGuide/PoliciesOverview.html) in the _Amazon IAM User Guide_.

    #   * `ReceiveMessageWaitTimeSeconds` \- The length of time, in seconds, for which a ` ReceiveMessage ` action waits for a message to arrive. Valid values: an integer from 0 to 20 (seconds). The default is 0.

    #   * `RedrivePolicy` \- The string that includes the parameters for the dead-letter queue functionality of the source queue. For more information about the redrive policy and dead-letter queues, see [Using Amazon SQS Dead-Letter Queues](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html) in the _Amazon Simple Queue Service Developer Guide_.

    #     * `deadLetterTargetArn` \- The Amazon Resource Name (ARN) of the dead-letter queue to which Amazon SQS moves messages after the value of `maxReceiveCount` is exceeded.

    #     * `maxReceiveCount` \- The number of times a message is delivered to the source queue before being moved to the dead-letter queue.

    # The dead-letter queue of a FIFO queue must also be a FIFO queue. Similarly,
    # the dead-letter queue of a standard queue must also be a standard queue.

    #   * `VisibilityTimeout` \- The visibility timeout for the queue. Valid values: an integer from 0 to 43,200 (12 hours). The default is 30. For more information about the visibility timeout, see [Visibility Timeout](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html) in the _Amazon Simple Queue Service Developer Guide_.

    # The following attributes apply only to [server-side-
    # encryption](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-
    # server-side-encryption.html):

    #   * `KmsMasterKeyId` \- The ID of an AWS-managed customer master key (CMK) for Amazon SQS or a custom CMK. For more information, see [Key Terms](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-server-side-encryption.html#sqs-sse-key-terms). While the alias of the AWS-managed CMK for Amazon SQS is always `alias/aws/sqs`, the alias of a custom CMK can, for example, be `alias/ _MyAlias_ `. For more examples, see [KeyId](http://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html#API_DescribeKey_RequestParameters) in the _AWS Key Management Service API Reference_.

    #   * `KmsDataKeyReusePeriodSeconds` \- The length of time, in seconds, for which Amazon SQS can reuse a [data key](http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#data-keys) to encrypt or decrypt messages before calling AWS KMS again. An integer representing seconds, between 60 seconds (1 minute) and 86,400 seconds (24 hours). The default is 300 (5 minutes). A shorter time period provides better security but results in more calls to KMS which might incur charges after Free Tier. For more information, see [How Does the Data Key Reuse Period Work?](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-server-side-encryption.html#sqs-how-does-the-data-key-reuse-period-work).

    # The following attribute applies only to [FIFO (first-in-first-out)
    # queues](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-
    # queues.html):

    #   * `ContentBasedDeduplication` \- Enables content-based deduplication. For more information, see [Exactly-Once Processing](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html#FIFO-queues-exactly-once-processing) in the _Amazon Simple Queue Service Developer Guide_.

    #     * Every message must have a unique `MessageDeduplicationId`,

    #       * You may provide a `MessageDeduplicationId` explicitly.

    #       * If you aren't able to provide a `MessageDeduplicationId` and you enable `ContentBasedDeduplication` for your queue, Amazon SQS uses a SHA-256 hash to generate the `MessageDeduplicationId` using the body of the message (but not the attributes of the message).

    #       * If you don't provide a `MessageDeduplicationId` and the queue doesn't have `ContentBasedDeduplication` set, the action fails with an error.

    #       * If the queue has `ContentBasedDeduplication` set, your `MessageDeduplicationId` overrides the generated one.

    #     * When `ContentBasedDeduplication` is in effect, messages with identical content sent within the deduplication interval are treated as duplicates and only one copy of the message is delivered.

    #     * If you send one message with `ContentBasedDeduplication` enabled and then another message with a `MessageDeduplicationId` that is the same as the one generated for the first `MessageDeduplicationId`, the two messages are treated as duplicates and only one copy of the message is delivered.

    # Any other valid special request parameters (such as the following) are
    # ignored:

    #   * `ApproximateNumberOfMessages`

    #   * `ApproximateNumberOfMessagesDelayed`

    #   * `ApproximateNumberOfMessagesNotVisible`

    #   * `CreatedTimestamp`

    #   * `LastModifiedTimestamp`

    #   * `QueueArn`
    attributes: typing.Dict[typing.Union[str, "QueueAttributeName"], str
                           ] = dataclasses.field(
                               default=ShapeBase.NOT_SET,
                           )


@dataclasses.dataclass
class TagQueueRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "queue_url",
                "QueueUrl",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The URL of the queue.
    queue_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of tags to be added to the specified queue.
    tags: typing.Dict[str, str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TooManyEntriesInBatchRequest(ShapeBase):
    """
    The batch request contains more entries than permissible.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class UnsupportedOperation(ShapeBase):
    """
    Error code 400. Unsupported operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class UntagQueueRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "queue_url",
                "QueueUrl",
                TypeInfo(str),
            ),
            (
                "tag_keys",
                "TagKeys",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The URL of the queue.
    queue_url: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The list of tags to be removed from the specified queue.
    tag_keys: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )
