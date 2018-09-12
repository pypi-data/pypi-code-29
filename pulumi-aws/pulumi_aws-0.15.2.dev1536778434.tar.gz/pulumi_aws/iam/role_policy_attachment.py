# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class RolePolicyAttachment(pulumi.CustomResource):
    """
    Attaches a Managed IAM Policy to an IAM role
    """
    def __init__(__self__, __name__, __opts__=None, policy_arn=None, role=None):
        """Create a RolePolicyAttachment resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not policy_arn:
            raise TypeError('Missing required property policy_arn')
        elif not isinstance(policy_arn, basestring):
            raise TypeError('Expected property policy_arn to be a basestring')
        __self__.policy_arn = policy_arn
        """
        The ARN of the policy you want to apply
        """
        __props__['policyArn'] = policy_arn

        if not role:
            raise TypeError('Missing required property role')
        elif not isinstance(role, basestring):
            raise TypeError('Expected property role to be a basestring')
        __self__.role = role
        """
        The role the policy should be applied to
        """
        __props__['role'] = role

        super(RolePolicyAttachment, __self__).__init__(
            'aws:iam/rolePolicyAttachment:RolePolicyAttachment',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'policyArn' in outs:
            self.policy_arn = outs['policyArn']
        if 'role' in outs:
            self.role = outs['role']
