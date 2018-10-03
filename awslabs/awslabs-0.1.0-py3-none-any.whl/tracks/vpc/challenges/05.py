from awslabs.challenge import Challenge
import boto3
import yaml
import os
import click
from cfn_tools.yaml_loader import CfnYamlLoader, ODict

class MyChallenge(Challenge):

    title = "Export"
    description = (
        "Export some variables in your CloudFormation Stack."
        "\n"
        "Tasks:"
        "\n"
        " - Export: VPCID\n"
        " - Export: PublicSubnetIDs\n"
        " - Export: PrivateSubnetIDs\n"
        " - Update the current awslabs-vpc stack\n"
        "\n"
        "Tips & Links:\n"
        "\n"
        "\n"
    )

    def start(self):
        self.instructions()

    def validate(self):
        self.fail("Fail")

        
