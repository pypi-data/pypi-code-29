# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class ZoneAssociation(pulumi.CustomResource):
    """
    Provides a Route53 private Hosted Zone to VPC association resource.
    """
    def __init__(__self__, __name__, __opts__=None, vpc_id=None, vpc_region=None, zone_id=None):
        """Create a ZoneAssociation resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not vpc_id:
            raise TypeError('Missing required property vpc_id')
        elif not isinstance(vpc_id, basestring):
            raise TypeError('Expected property vpc_id to be a basestring')
        __self__.vpc_id = vpc_id
        """
        The VPC to associate with the private hosted zone.
        """
        __props__['vpcId'] = vpc_id

        if vpc_region and not isinstance(vpc_region, basestring):
            raise TypeError('Expected property vpc_region to be a basestring')
        __self__.vpc_region = vpc_region
        """
        The VPC's region. Defaults to the region of the AWS provider.
        """
        __props__['vpcRegion'] = vpc_region

        if not zone_id:
            raise TypeError('Missing required property zone_id')
        elif not isinstance(zone_id, basestring):
            raise TypeError('Expected property zone_id to be a basestring')
        __self__.zone_id = zone_id
        """
        The private hosted zone to associate.
        """
        __props__['zoneId'] = zone_id

        super(ZoneAssociation, __self__).__init__(
            'aws:route53/zoneAssociation:ZoneAssociation',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'vpcId' in outs:
            self.vpc_id = outs['vpcId']
        if 'vpcRegion' in outs:
            self.vpc_region = outs['vpcRegion']
        if 'zoneId' in outs:
            self.zone_id = outs['zoneId']
