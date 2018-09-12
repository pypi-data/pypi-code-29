# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class Service(pulumi.CustomResource):
    """
    Allows you to manage an Azure Search Service
    """
    def __init__(__self__, __name__, __opts__=None, location=None, name=None, partition_count=None, replica_count=None, resource_group_name=None, sku=None, tags=None):
        """Create a Service resource with the given unique name, props, and options."""
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
        The name of the Search Service. Changing this forces a new resource to be created.
        """
        __props__['name'] = name

        if partition_count and not isinstance(partition_count, int):
            raise TypeError('Expected property partition_count to be a int')
        __self__.partition_count = partition_count
        """
        Default is 1. Valid values include 1, 2, 3, 4, 6, or 12. Valid only when `sku` is `standard`. Changing this forces a new resource to be created.
        """
        __props__['partitionCount'] = partition_count

        if replica_count and not isinstance(replica_count, int):
            raise TypeError('Expected property replica_count to be a int')
        __self__.replica_count = replica_count
        """
        Default is 1. Valid values include 1 through 12. Valid only when `sku` is `standard`. Changing this forces a new resource to be created.
        """
        __props__['replicaCount'] = replica_count

        if not resource_group_name:
            raise TypeError('Missing required property resource_group_name')
        elif not isinstance(resource_group_name, basestring):
            raise TypeError('Expected property resource_group_name to be a basestring')
        __self__.resource_group_name = resource_group_name
        """
        The name of the resource group in which to create the Search Service. Changing this forces a new resource to be created.
        """
        __props__['resourceGroupName'] = resource_group_name

        if not sku:
            raise TypeError('Missing required property sku')
        elif not isinstance(sku, basestring):
            raise TypeError('Expected property sku to be a basestring')
        __self__.sku = sku
        """
        Valid values are `free` and `standard`. `standard2` and `standard3` are also valid, but can only be used when it's enabled on the backend by Microsoft support. `free` provisions the service in shared clusters. `standard` provisions the service in dedicated clusters.  Changing this forces a new resource to be created.
        """
        __props__['sku'] = sku

        if tags and not isinstance(tags, dict):
            raise TypeError('Expected property tags to be a dict')
        __self__.tags = tags
        """
        A mapping of tags to assign to the resource. Changing this forces a new resource to be created.
        """
        __props__['tags'] = tags

        super(Service, __self__).__init__(
            'azure:search/service:Service',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'location' in outs:
            self.location = outs['location']
        if 'name' in outs:
            self.name = outs['name']
        if 'partitionCount' in outs:
            self.partition_count = outs['partitionCount']
        if 'replicaCount' in outs:
            self.replica_count = outs['replicaCount']
        if 'resourceGroupName' in outs:
            self.resource_group_name = outs['resourceGroupName']
        if 'sku' in outs:
            self.sku = outs['sku']
        if 'tags' in outs:
            self.tags = outs['tags']
