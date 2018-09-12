# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class Subscription(pulumi.CustomResource):
    """
    Create a ServiceBus Subscription.
    """
    def __init__(__self__, __name__, __opts__=None, auto_delete_on_idle=None, dead_lettering_on_filter_evaluation_exceptions=None, dead_lettering_on_message_expiration=None, default_message_ttl=None, enable_batched_operations=None, forward_to=None, location=None, lock_duration=None, max_delivery_count=None, name=None, namespace_name=None, requires_session=None, resource_group_name=None, topic_name=None):
        """Create a Subscription resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if auto_delete_on_idle and not isinstance(auto_delete_on_idle, basestring):
            raise TypeError('Expected property auto_delete_on_idle to be a basestring')
        __self__.auto_delete_on_idle = auto_delete_on_idle
        """
        The idle interval after which the
        Subscription is automatically deleted, minimum of 5 minutes. Provided in the
        TimeSpan format.
        """
        __props__['autoDeleteOnIdle'] = auto_delete_on_idle

        if dead_lettering_on_filter_evaluation_exceptions and not isinstance(dead_lettering_on_filter_evaluation_exceptions, bool):
            raise TypeError('Expected property dead_lettering_on_filter_evaluation_exceptions to be a bool')
        __self__.dead_lettering_on_filter_evaluation_exceptions = dead_lettering_on_filter_evaluation_exceptions
        __props__['deadLetteringOnFilterEvaluationExceptions'] = dead_lettering_on_filter_evaluation_exceptions

        if dead_lettering_on_message_expiration and not isinstance(dead_lettering_on_message_expiration, bool):
            raise TypeError('Expected property dead_lettering_on_message_expiration to be a bool')
        __self__.dead_lettering_on_message_expiration = dead_lettering_on_message_expiration
        """
        Boolean flag which controls
        whether the Subscription has dead letter support when a message expires. Defaults
        to false.
        """
        __props__['deadLetteringOnMessageExpiration'] = dead_lettering_on_message_expiration

        if default_message_ttl and not isinstance(default_message_ttl, basestring):
            raise TypeError('Expected property default_message_ttl to be a basestring')
        __self__.default_message_ttl = default_message_ttl
        """
        The TTL of messages sent to this Subscription
        if no TTL value is set on the message itself. Provided in the TimeSpan
        format.
        """
        __props__['defaultMessageTtl'] = default_message_ttl

        if enable_batched_operations and not isinstance(enable_batched_operations, bool):
            raise TypeError('Expected property enable_batched_operations to be a bool')
        __self__.enable_batched_operations = enable_batched_operations
        """
        Boolean flag which controls whether the
        Subscription supports batched operations. Defaults to false.
        """
        __props__['enableBatchedOperations'] = enable_batched_operations

        if forward_to and not isinstance(forward_to, basestring):
            raise TypeError('Expected property forward_to to be a basestring')
        __self__.forward_to = forward_to
        """
        The name of a Queue or Topic to automatically forward 
        messages to.
        """
        __props__['forwardTo'] = forward_to

        if location and not isinstance(location, basestring):
            raise TypeError('Expected property location to be a basestring')
        __self__.location = location
        """
        Specifies the supported Azure location where the resource exists.
        Changing this forces a new resource to be created.
        """
        __props__['location'] = location

        if lock_duration and not isinstance(lock_duration, basestring):
            raise TypeError('Expected property lock_duration to be a basestring')
        __self__.lock_duration = lock_duration
        """
        The lock duration for the subscription, maximum
        supported value is 5 minutes. Defaults to 1 minute.
        """
        __props__['lockDuration'] = lock_duration

        if not max_delivery_count:
            raise TypeError('Missing required property max_delivery_count')
        elif not isinstance(max_delivery_count, int):
            raise TypeError('Expected property max_delivery_count to be a int')
        __self__.max_delivery_count = max_delivery_count
        """
        The maximum number of deliveries.
        """
        __props__['maxDeliveryCount'] = max_delivery_count

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        Specifies the name of the ServiceBus Subscription resource.
        Changing this forces a new resource to be created.
        """
        __props__['name'] = name

        if not namespace_name:
            raise TypeError('Missing required property namespace_name')
        elif not isinstance(namespace_name, basestring):
            raise TypeError('Expected property namespace_name to be a basestring')
        __self__.namespace_name = namespace_name
        """
        The name of the ServiceBus Namespace to create
        this Subscription in. Changing this forces a new resource to be created.
        """
        __props__['namespaceName'] = namespace_name

        if requires_session and not isinstance(requires_session, bool):
            raise TypeError('Expected property requires_session to be a bool')
        __self__.requires_session = requires_session
        """
        Boolean flag which controls whether this Subscription
        supports the concept of a session. Defaults to false. Changing this forces a
        new resource to be created.
        """
        __props__['requiresSession'] = requires_session

        if not resource_group_name:
            raise TypeError('Missing required property resource_group_name')
        elif not isinstance(resource_group_name, basestring):
            raise TypeError('Expected property resource_group_name to be a basestring')
        __self__.resource_group_name = resource_group_name
        """
        The name of the resource group in which to
        create the namespace. Changing this forces a new resource to be created.
        """
        __props__['resourceGroupName'] = resource_group_name

        if not topic_name:
            raise TypeError('Missing required property topic_name')
        elif not isinstance(topic_name, basestring):
            raise TypeError('Expected property topic_name to be a basestring')
        __self__.topic_name = topic_name
        """
        The name of the ServiceBus Topic to create
        this Subscription in. Changing this forces a new resource to be created.
        """
        __props__['topicName'] = topic_name

        super(Subscription, __self__).__init__(
            'azure:eventhub/subscription:Subscription',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'autoDeleteOnIdle' in outs:
            self.auto_delete_on_idle = outs['autoDeleteOnIdle']
        if 'deadLetteringOnFilterEvaluationExceptions' in outs:
            self.dead_lettering_on_filter_evaluation_exceptions = outs['deadLetteringOnFilterEvaluationExceptions']
        if 'deadLetteringOnMessageExpiration' in outs:
            self.dead_lettering_on_message_expiration = outs['deadLetteringOnMessageExpiration']
        if 'defaultMessageTtl' in outs:
            self.default_message_ttl = outs['defaultMessageTtl']
        if 'enableBatchedOperations' in outs:
            self.enable_batched_operations = outs['enableBatchedOperations']
        if 'forwardTo' in outs:
            self.forward_to = outs['forwardTo']
        if 'location' in outs:
            self.location = outs['location']
        if 'lockDuration' in outs:
            self.lock_duration = outs['lockDuration']
        if 'maxDeliveryCount' in outs:
            self.max_delivery_count = outs['maxDeliveryCount']
        if 'name' in outs:
            self.name = outs['name']
        if 'namespaceName' in outs:
            self.namespace_name = outs['namespaceName']
        if 'requiresSession' in outs:
            self.requires_session = outs['requiresSession']
        if 'resourceGroupName' in outs:
            self.resource_group_name = outs['resourceGroupName']
        if 'topicName' in outs:
            self.topic_name = outs['topicName']
