# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class ParameterGroup(pulumi.CustomResource):
    """
    Provides an ElastiCache parameter group resource.
    """
    def __init__(__self__, __name__, __opts__=None, description=None, family=None, name=None, parameters=None):
        """Create a ParameterGroup resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        description = 'Managed by Pulumi'
        if description and not isinstance(description, basestring):
            raise TypeError('Expected property description to be a basestring')
        __self__.description = description
        """
        The description of the ElastiCache parameter group. Defaults to "Managed by Terraform".
        """
        __props__['description'] = description

        if not family:
            raise TypeError('Missing required property family')
        elif not isinstance(family, basestring):
            raise TypeError('Expected property family to be a basestring')
        __self__.family = family
        """
        The family of the ElastiCache parameter group.
        """
        __props__['family'] = family

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        The name of the ElastiCache parameter.
        """
        __props__['name'] = name

        if parameters and not isinstance(parameters, list):
            raise TypeError('Expected property parameters to be a list')
        __self__.parameters = parameters
        """
        A list of ElastiCache parameters to apply.
        """
        __props__['parameters'] = parameters

        super(ParameterGroup, __self__).__init__(
            'aws:elasticache/parameterGroup:ParameterGroup',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'description' in outs:
            self.description = outs['description']
        if 'family' in outs:
            self.family = outs['family']
        if 'name' in outs:
            self.name = outs['name']
        if 'parameters' in outs:
            self.parameters = outs['parameters']
