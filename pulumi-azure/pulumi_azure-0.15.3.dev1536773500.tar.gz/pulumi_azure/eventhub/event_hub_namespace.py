# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class EventHubNamespace(pulumi.CustomResource):
    """
    Create an EventHub Namespace.
    """
    def __init__(__self__, __name__, __opts__=None, auto_inflate_enabled=None, capacity=None, location=None, maximum_throughput_units=None, name=None, resource_group_name=None, sku=None, tags=None):
        """Create a EventHubNamespace resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if auto_inflate_enabled and not isinstance(auto_inflate_enabled, bool):
            raise TypeError('Expected property auto_inflate_enabled to be a bool')
        __self__.auto_inflate_enabled = auto_inflate_enabled
        """
        Is Auto Inflate enabled for the EventHub Namespace?
        """
        __props__['autoInflateEnabled'] = auto_inflate_enabled

        if capacity and not isinstance(capacity, int):
            raise TypeError('Expected property capacity to be a int')
        __self__.capacity = capacity
        """
        Specifies the Capacity / Throughput Units for a `Standard` SKU namespace. Valid values range from 1 - 20.
        """
        __props__['capacity'] = capacity

        if not location:
            raise TypeError('Missing required property location')
        elif not isinstance(location, basestring):
            raise TypeError('Expected property location to be a basestring')
        __self__.location = location
        """
        Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        """
        __props__['location'] = location

        if maximum_throughput_units and not isinstance(maximum_throughput_units, int):
            raise TypeError('Expected property maximum_throughput_units to be a int')
        __self__.maximum_throughput_units = maximum_throughput_units
        """
        Specifies the maximum number of throughput units when Auto Inflate is Enabled. Valid values range from 1 - 20.
        """
        __props__['maximumThroughputUnits'] = maximum_throughput_units

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        Specifies the name of the EventHub Namespace resource. Changing this forces a new resource to be created.
        """
        __props__['name'] = name

        if not resource_group_name:
            raise TypeError('Missing required property resource_group_name')
        elif not isinstance(resource_group_name, basestring):
            raise TypeError('Expected property resource_group_name to be a basestring')
        __self__.resource_group_name = resource_group_name
        """
        The name of the resource group in which to create the namespace. Changing this forces a new resource to be created.
        """
        __props__['resourceGroupName'] = resource_group_name

        if not sku:
            raise TypeError('Missing required property sku')
        elif not isinstance(sku, basestring):
            raise TypeError('Expected property sku to be a basestring')
        __self__.sku = sku
        """
        Defines which tier to use. Valid options are `Basic` and `Standard`.
        """
        __props__['sku'] = sku

        if tags and not isinstance(tags, dict):
            raise TypeError('Expected property tags to be a dict')
        __self__.tags = tags
        """
        A mapping of tags to assign to the resource.
        """
        __props__['tags'] = tags

        __self__.default_primary_connection_string = pulumi.runtime.UNKNOWN
        """
        The primary connection string for the authorization
        rule `RootManageSharedAccessKey`.
        """
        __self__.default_primary_key = pulumi.runtime.UNKNOWN
        """
        The primary access key for the authorization rule `RootManageSharedAccessKey`.
        """
        __self__.default_secondary_connection_string = pulumi.runtime.UNKNOWN
        """
        The secondary connection string for the
        authorization rule `RootManageSharedAccessKey`.
        """
        __self__.default_secondary_key = pulumi.runtime.UNKNOWN
        """
        The secondary access key for the authorization rule `RootManageSharedAccessKey`.
        """

        super(EventHubNamespace, __self__).__init__(
            'azure:eventhub/eventHubNamespace:EventHubNamespace',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'autoInflateEnabled' in outs:
            self.auto_inflate_enabled = outs['autoInflateEnabled']
        if 'capacity' in outs:
            self.capacity = outs['capacity']
        if 'defaultPrimaryConnectionString' in outs:
            self.default_primary_connection_string = outs['defaultPrimaryConnectionString']
        if 'defaultPrimaryKey' in outs:
            self.default_primary_key = outs['defaultPrimaryKey']
        if 'defaultSecondaryConnectionString' in outs:
            self.default_secondary_connection_string = outs['defaultSecondaryConnectionString']
        if 'defaultSecondaryKey' in outs:
            self.default_secondary_key = outs['defaultSecondaryKey']
        if 'location' in outs:
            self.location = outs['location']
        if 'maximumThroughputUnits' in outs:
            self.maximum_throughput_units = outs['maximumThroughputUnits']
        if 'name' in outs:
            self.name = outs['name']
        if 'resourceGroupName' in outs:
            self.resource_group_name = outs['resourceGroupName']
        if 'sku' in outs:
            self.sku = outs['sku']
        if 'tags' in outs:
            self.tags = outs['tags']
