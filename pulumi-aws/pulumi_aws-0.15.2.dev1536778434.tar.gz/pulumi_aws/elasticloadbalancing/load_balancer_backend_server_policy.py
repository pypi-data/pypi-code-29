# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class LoadBalancerBackendServerPolicy(pulumi.CustomResource):
    """
    Attaches a load balancer policy to an ELB backend server.
    
    """
    def __init__(__self__, __name__, __opts__=None, instance_port=None, load_balancer_name=None, policy_names=None):
        """Create a LoadBalancerBackendServerPolicy resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not instance_port:
            raise TypeError('Missing required property instance_port')
        elif not isinstance(instance_port, int):
            raise TypeError('Expected property instance_port to be a int')
        __self__.instance_port = instance_port
        """
        The instance port to apply the policy to.
        """
        __props__['instancePort'] = instance_port

        if not load_balancer_name:
            raise TypeError('Missing required property load_balancer_name')
        elif not isinstance(load_balancer_name, basestring):
            raise TypeError('Expected property load_balancer_name to be a basestring')
        __self__.load_balancer_name = load_balancer_name
        """
        The load balancer to attach the policy to.
        """
        __props__['loadBalancerName'] = load_balancer_name

        if policy_names and not isinstance(policy_names, list):
            raise TypeError('Expected property policy_names to be a list')
        __self__.policy_names = policy_names
        """
        List of Policy Names to apply to the backend server.
        """
        __props__['policyNames'] = policy_names

        super(LoadBalancerBackendServerPolicy, __self__).__init__(
            'aws:elasticloadbalancing/loadBalancerBackendServerPolicy:LoadBalancerBackendServerPolicy',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'instancePort' in outs:
            self.instance_port = outs['instancePort']
        if 'loadBalancerName' in outs:
            self.load_balancer_name = outs['loadBalancerName']
        if 'policyNames' in outs:
            self.policy_names = outs['policyNames']
