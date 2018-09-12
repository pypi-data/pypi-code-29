# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class Application(pulumi.CustomResource):
    """
    Provides an Elastic Beanstalk Application Resource. Elastic Beanstalk allows
    you to deploy and manage applications in the AWS cloud without worrying about
    the infrastructure that runs those applications.
    
    This resource creates an application that has one configuration template named
    `default`, and no application versions
    """
    def __init__(__self__, __name__, __opts__=None, appversion_lifecycle=None, description=None, name=None):
        """Create a Application resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if appversion_lifecycle and not isinstance(appversion_lifecycle, dict):
            raise TypeError('Expected property appversion_lifecycle to be a dict')
        __self__.appversion_lifecycle = appversion_lifecycle
        __props__['appversionLifecycle'] = appversion_lifecycle

        if description and not isinstance(description, basestring):
            raise TypeError('Expected property description to be a basestring')
        __self__.description = description
        """
        Short description of the application
        """
        __props__['description'] = description

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        The name of the application, must be unique within your account
        """
        __props__['name'] = name

        super(Application, __self__).__init__(
            'aws:elasticbeanstalk/application:Application',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'appversionLifecycle' in outs:
            self.appversion_lifecycle = outs['appversionLifecycle']
        if 'description' in outs:
            self.description = outs['description']
        if 'name' in outs:
            self.name = outs['name']
