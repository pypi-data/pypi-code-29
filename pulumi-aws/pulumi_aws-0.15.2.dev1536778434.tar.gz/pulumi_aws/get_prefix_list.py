# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from . import utilities

class GetPrefixListResult(object):
    """
    A collection of values returned by getPrefixList.
    """
    def __init__(__self__, cidr_blocks=None, name=None, id=None):
        if cidr_blocks and not isinstance(cidr_blocks, list):
            raise TypeError('Expected argument cidr_blocks to be a list')
        __self__.cidr_blocks = cidr_blocks
        """
        The list of CIDR blocks for the AWS service associated
        with the prefix list.
        """
        if name and not isinstance(name, basestring):
            raise TypeError('Expected argument name to be a basestring')
        __self__.name = name
        """
        The name of the selected prefix list.
        """
        if id and not isinstance(id, basestring):
            raise TypeError('Expected argument id to be a basestring')
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """

def get_prefix_list(name=None, prefix_list_id=None):
    """
    `aws_prefix_list` provides details about a specific prefix list (PL)
    in the current region.
    
    This can be used both to validate a prefix list given in a variable
    and to obtain the CIDR blocks (IP address ranges) for the associated
    AWS service. The latter may be useful e.g. for adding network ACL
    rules.
    """
    __args__ = dict()

    __args__['name'] = name
    __args__['prefixListId'] = prefix_list_id
    __ret__ = pulumi.runtime.invoke('aws:index/getPrefixList:getPrefixList', __args__)

    return GetPrefixListResult(
        cidr_blocks=__ret__.get('cidrBlocks'),
        name=__ret__.get('name'),
        id=__ret__.get('id'))
