# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class DocumentationVersion(pulumi.CustomResource):
    """
    Provides a resource to manage an API Gateway Documentation Version.
    """
    def __init__(__self__, __name__, __opts__=None, description=None, rest_api_id=None, version=None):
        """Create a DocumentationVersion resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if description and not isinstance(description, basestring):
            raise TypeError('Expected property description to be a basestring')
        __self__.description = description
        """
        The description of the API documentation version.
        """
        __props__['description'] = description

        if not rest_api_id:
            raise TypeError('Missing required property rest_api_id')
        elif not isinstance(rest_api_id, basestring):
            raise TypeError('Expected property rest_api_id to be a basestring')
        __self__.rest_api_id = rest_api_id
        """
        The ID of the associated Rest API
        """
        __props__['restApiId'] = rest_api_id

        if not version:
            raise TypeError('Missing required property version')
        elif not isinstance(version, basestring):
            raise TypeError('Expected property version to be a basestring')
        __self__.version = version
        """
        The version identifier of the API documentation snapshot.
        """
        __props__['version'] = version

        super(DocumentationVersion, __self__).__init__(
            'aws:apigateway/documentationVersion:DocumentationVersion',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'description' in outs:
            self.description = outs['description']
        if 'restApiId' in outs:
            self.rest_api_id = outs['restApiId']
        if 'version' in outs:
            self.version = outs['version']
