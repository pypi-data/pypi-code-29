# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class RegexMatchSet(pulumi.CustomResource):
    """
    Provides a WAF Regex Match Set Resource
    """
    def __init__(__self__, __name__, __opts__=None, name=None, regex_match_tuples=None):
        """Create a RegexMatchSet resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        The name or description of the Regex Match Set.
        """
        __props__['name'] = name

        if regex_match_tuples and not isinstance(regex_match_tuples, list):
            raise TypeError('Expected property regex_match_tuples to be a list')
        __self__.regex_match_tuples = regex_match_tuples
        """
        The regular expression pattern that you want AWS WAF to search for in web requests,
        the location in requests that you want AWS WAF to search, and other settings. See below.
        """
        __props__['regexMatchTuples'] = regex_match_tuples

        super(RegexMatchSet, __self__).__init__(
            'aws:waf/regexMatchSet:RegexMatchSet',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'name' in outs:
            self.name = outs['name']
        if 'regexMatchTuples' in outs:
            self.regex_match_tuples = outs['regexMatchTuples']
