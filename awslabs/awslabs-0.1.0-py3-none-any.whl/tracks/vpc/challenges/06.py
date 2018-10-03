from awslabs.challenge import Challenge
import boto3
import yaml
import os
import click
from cfn_tools.yaml_loader import CfnYamlLoader, ODict

class MyChallenge(Challenge):

    title = "Test your Stack"
    description = (
        "Now our VPC is ready to deploy some workloads. Another CloudFormation "
        "template is copied to the current directory. Review this template to "
        "quickly learn how an instance and load balancer is deployed to your "
        "VPC.\n"
        "\n"
        "Tasks: \n"
        " - Deploy this Template with Stack Name: awslabs-helloworld.\n"
        " - Add the VPCID, PublicSubnetID\n"
        "\n"
    )

    def start(self):
        self.instructions()

    def validate(self):
        self.fail("Fail")

        
