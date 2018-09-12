# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class EventGridTopic(pulumi.CustomResource):
    """
    Manages an EventGrid Topic
    
    ~> **Note:** at this time EventGrid Topic's are only available in a limited number of regions.
    """
    def __init__(__self__, __name__, __opts__=None, location=None, name=None, resource_group_name=None, tags=None):
        """Create a EventGridTopic resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not location:
            raise TypeError('Missing required property location')
        elif not isinstance(location, basestring):
            raise TypeError('Expected property location to be a basestring')
        __self__.location = location
        """
        Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        """
        __props__['location'] = location

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        Specifies the name of the EventGrid Topic resource. Changing this forces a new resource to be created.
        """
        __props__['name'] = name

        if not resource_group_name:
            raise TypeError('Missing required property resource_group_name')
        elif not isinstance(resource_group_name, basestring):
            raise TypeError('Expected property resource_group_name to be a basestring')
        __self__.resource_group_name = resource_group_name
        """
        The name of the resource group in which the EventGrid Topic exists. Changing this forces a new resource to be created.
        """
        __props__['resourceGroupName'] = resource_group_name

        if tags and not isinstance(tags, dict):
            raise TypeError('Expected property tags to be a dict')
        __self__.tags = tags
        """
        A mapping of tags to assign to the resource.
        """
        __props__['tags'] = tags

        __self__.endpoint = pulumi.runtime.UNKNOWN
        """
        The Endpoint associated with the EventGrid Topic.
        """
        __self__.primary_access_key = pulumi.runtime.UNKNOWN
        """
        The Primary Shared Access Key associated with the EventGrid Topic.
        """
        __self__.secondary_access_key = pulumi.runtime.UNKNOWN
        """
        The Secondary Shared Access Key associated with the EventGrid Topic.
        """

        super(EventGridTopic, __self__).__init__(
            'azure:eventhub/eventGridTopic:EventGridTopic',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'endpoint' in outs:
            self.endpoint = outs['endpoint']
        if 'location' in outs:
            self.location = outs['location']
        if 'name' in outs:
            self.name = outs['name']
        if 'primaryAccessKey' in outs:
            self.primary_access_key = outs['primaryAccessKey']
        if 'resourceGroupName' in outs:
            self.resource_group_name = outs['resourceGroupName']
        if 'secondaryAccessKey' in outs:
            self.secondary_access_key = outs['secondaryAccessKey']
        if 'tags' in outs:
            self.tags = outs['tags']
