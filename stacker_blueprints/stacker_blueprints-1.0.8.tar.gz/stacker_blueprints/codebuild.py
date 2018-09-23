from troposphere import (
    codebuild,
    iam,
)

from stacker.blueprints.base import Blueprint
from stacker.blueprints.variables.types import TroposphereType


class Project(Blueprint):
    VARIABLES = {
        "ProjectConfig": {
            "type": TroposphereType(codebuild.Project),
            "description": "The configuration for the project.",
        },
    }

    @property
    def project_config(self):
        return self.get_variables()["ProjectConfig"]

    def create_template(self):
        t = self.template

        project = t.add_resources(self.project_config)

        self.add_output("ProjectId", project.Ref())
        self.add_output("ProjectArn", project.GetAtt("Arn"))
