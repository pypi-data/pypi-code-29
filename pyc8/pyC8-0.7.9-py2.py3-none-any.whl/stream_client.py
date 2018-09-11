from __future__ import absolute_import, unicode_literals

__all__ = ['StreamClient']

import pulsar


class StreamClient():
    """Stream Client.

    :param connection: HTTP connection.
    :type connection: c8.connection.Connection
    :param executor: API executor.
    :type executor: c8.executor.Executor
    """

    def __init__(self, authentication=None,
                 operation_timeout_seconds=30,
                 io_threads=1,
                 message_listener_threads=1,
                 concurrent_lookup_requests=50000,
                 log_conf_file_path=None,
                 use_tls=False,
                 tls_trust_certs_file_path=None,
                 tls_allow_insecure_connection=False):
        """
         Create a new Strean client instance.
         **Args**
         * `service_url`: The Streams service url eg: pulsar://my-broker.com:6650/
         **Options**
         * `authentication`:
           Set the authentication provider to be used with the broker.
         * `operation_timeout_seconds`:
           Set timeout on client operations (subscribe, create producer, close,
           unsubscribe).
         * `io_threads`:
           Set the number of IO threads to be used by the Pulsar client.
         * `message_listener_threads`:
           Set the number of threads to be used by the Pulsar client when
           delivering messages through message listener. The default is 1 thread
           per Pulsar client. If using more than 1 thread, messages for distinct
           `message_listener`s will be delivered in different threads, however a
           single `MessageListener` will always be assigned to the same thread.
         * `concurrent_lookup_requests`:
           Number of concurrent lookup-requests allowed on each broker connection
           to prevent overload on the broker.
         * `log_conf_file_path`:
           Initialize log4cxx from a configuration file.
         * `use_tls`:
           Configure whether to use TLS encryption on the connection. This setting
           is deprecated. TLS will be automatically enabled if the `serviceUrl` is
           set to `pulsar+ssl://` or `https://`
         * `tls_trust_certs_file_path`:
           Set the path to the trusted TLS certificate file.
         * `tls_allow_insecure_connection`:
           Configure whether the Pulsar client accepts untrusted TLS certificates
           from the broker.
         """

        self._server_url = 'pulsar://localhost:6650'
        self._client = pulsar.Client(self._server_url, authentication,
                                     operation_timeout_seconds, io_threads,
                                     message_listener_threads, concurrent_lookup_requests,
                                     log_conf_file_path, use_tls, tls_trust_certs_file_path,
                                     tls_trust_certs_file_path)

    def close(self):
        """
            Close the client and all the associated producers and consumers
        """
        self._client.close()

    def create_producer(self, topic, producer_name=None,
                        initial_sequence_id=None, send_timeout_millis=30000,
                        compression_type=pulsar.CompressionType.NONE,
                        max_pending_messages=1000,
                        block_if_queue_full=False, batching_enabled=False,
                        batching_max_messages=1000, batching_max_allowed_size_in_bytes=131072,
                        batching_max_publish_delay_ms=10,
                        message_routing_mode=pulsar.PartitionsRoutingMode.RoundRobinDistribution):
        """
           Create a new producer on a given topic.
           **Args**
           * `topic`:
             The topic name
           **Options**
           * `producer_name`:
              Specify a name for the producer. If not assigned,
              the system will generate a globally unique name which can be accessed
              with `Producer.producer_name()`. When specifying a name, it is app to
              the user to ensure that, for a given topic, the producer name is unique
              across all Pulsar's clusters.
           * `initial_sequence_id`:
              Set the baseline for the sequence ids for messages
              published by the producer. First message will be using
              `(initialSequenceId + 1)`` as its sequence id and subsequent messages will
              be assigned incremental sequence ids, if not otherwise specified.
           * `send_timeout_seconds`:
             If a message is not acknowledged by the server before the
             `send_timeout` expires, an error will be reported.
           * `compression_type`:
             Set the compression type for the producer. By default, message
             payloads are not compressed. Supported compression types are
             `CompressionType.LZ4` and `CompressionType.ZLib`.
           * `max_pending_messages`:
             Set the max size of the queue holding the messages pending to receive
             an acknowledgment from the broker.
           * `block_if_queue_full`: Set whether `send_async` operations should
             block when the outgoing message queue is full.
           * `message_routing_mode`:
             Set the message routing mode for the partitioned producer. Default is `PartitionsRoutingMode.RoundRobinDistribution`,
             other option is `PartitionsRoutingMode.UseSinglePartition`
       """

        return self._client.create_producer(topic, producer_name,
                                            initial_sequence_id, send_timeout_millis,
                                            compression_type.CompressionType.NONE,
                                            max_pending_messages,
                                            block_if_queue_full, batching_enabled,
                                            batching_max_messages, batching_max_allowed_size_in_bytes,
                                            batching_max_publish_delay_ms,
                                            message_routing_mode)

    def create_reader(self, topic, start_message_id,
                      reader_listener=None,
                      receiver_queue_size=1000,
                      reader_name=None,
                      subscription_role_prefix=None
                      ):
        """
        Create a reader on a particular topic
        **Args**
        * `topic`: The name of the topic.
        * `start_message_id`: The initial reader positioning is done by specifying a message id.
           The options are:
            * `MessageId.earliest`: Start reading from the earliest message available in the topic
            * `MessageId.latest`: Start reading from the end topic, only getting messages published
               after the reader was created
            * `MessageId`: When passing a particular message id, the reader will position itself on
               that specific position. The first message to be read will be the message next to the
               specified messageId. Message id can be serialized into a string and deserialized
               back into a `MessageId` object:
                   # Serialize to string
                   s = msg.message_id().serialize()
                   # Deserialize from string
                   msg_id = MessageId.deserialize(s)
        **Options**
        * `reader_listener`:
          Sets a message listener for the reader. When the listener is set,
          the application will receive messages through it. Calls to
          `reader.read_next()` will not be allowed. The listener function needs
          to accept (reader, message), for example:
                def my_listener(reader, message):
                    # process message
                    pass
        * `receiver_queue_size`:
          Sets the size of the reader receive queue. The reader receive
          queue controls how many messages can be accumulated by the reader
          before the application calls `read_next()`. Using a higher value could
          potentially increase the reader throughput at the expense of higher
          memory utilization.
        * `reader_name`:
          Sets the reader name.
        * `subscription_role_prefix`:
          Sets the subscription role prefix.
        """

        return self._client.create_reader(topic, start_message_id,
                                          reader_listener, receiver_queue_size,
                                          reader_name, subscription_role_prefix)

    def subscribe(self, topic, subscription_name,
                  consumer_type=pulsar.ConsumerType.Exclusive,
                  message_listener=None,
                  receiver_queue_size=1000,
                  consumer_name=None,
                  unacked_messages_timeout_ms=None,
                  broker_consumer_stats_cache_time_ms=30000,
                  is_read_compacted=False
                  ):
        """
        Subscribe to the given topic and subscription combination.
        **Args**
        * `topic`: The name of the topic.
        * `subscription`: The name of the subscription.
        **Options**
        * `consumer_type`:
          Select the subscription type to be used when subscribing to the topic.
        * `message_listener`:
          Sets a message listener for the consumer. When the listener is set,
          the application will receive messages through it. Calls to
          `consumer.receive()` will not be allowed. The listener function needs
          to accept (consumer, message), for example:
                #!python
                def my_listener(consumer, message):
                    # process message
                    consumer.acknowledge(message)
        * `receiver_queue_size`:
          Sets the size of the consumer receive queue. The consumer receive
          queue controls how many messages can be accumulated by the consumer
          before the application calls `receive()`. Using a higher value could
          potentially increase the consumer throughput at the expense of higher
          memory utilization. Setting the consumer queue size to zero decreases
          the throughput of the consumer by disabling pre-fetching of messages.
          This approach improves the message distribution on shared subscription
          by pushing messages only to those consumers that are ready to process
          them. Neither receive with timeout nor partitioned topics can be used
          if the consumer queue size is zero. The `receive()` function call
          should not be interrupted when the consumer queue size is zero. The
          default value is 1000 messages and should work well for most use
          cases.
        * `consumer_name`:
          Sets the consumer name.
        * `unacked_messages_timeout_ms`:
          Sets the timeout in milliseconds for unacknowledged messages. The
          timeout needs to be greater than 10 seconds. An exception is thrown if
          the given value is less than 10 seconds. If a successful
          acknowledgement is not sent within the timeout, all the unacknowledged
          messages are redelivered.
        * `broker_consumer_stats_cache_time_ms`:
          Sets the time duration for which the broker-side consumer stats will
          be cached in the client.
        """

        return self._client.subscribe(topic, subscription_name, consumer_type,
                                      message_listener, receiver_queue_size, consumer_name,
                                      unacked_messages_timeout_ms, broker_consumer_stats_cache_time_ms,
                                      is_read_compacted)
