import json
import logging
import os

import docker
from ruamel.yaml import YAML

from build_utils import docker_utils, utils
from build_utils.rules import base_rule, build_docker_image, build_maven_artifact, \
    build_npm_package, get_passthrough_config

logger = logging.getLogger(__name__)

yaml = YAML(typ='safe')

class ExecuteChildRules(base_rule.BaseRule):
    def run(self, child_rule_paths):
        build_rule_map = self._get_build_rule_map()
        rule_output = {}
        for child_rule_path in child_rule_paths:
            full_child_rule_path = os.path.join(self.dir_path, child_rule_path)
            
            build_config = self._read_build_config(full_child_rule_path)
            for build_step_config in build_config:
                build_rule_name, build_rule_args = self._parse_build_step_config(**build_step_config)
                build_rule_class = build_rule_map[build_rule_name]

                build_rule = build_rule_class(
                    self.build_context, os.path.dirname(full_child_rule_path))
                child_rule_output = build_rule.run(**build_rule_args)

                if child_rule_output:
                    utils.recursive_merge_dicts(rule_output, child_rule_output)

        return rule_output

    @staticmethod
    def _read_build_config(config_file_path):
        _, config_ext = os.path.splitext(config_file_path)
        with open(config_file_path) as config_file:
            if config_ext == '.json':
                return json.load(config_file)
            elif config_ext in ('.yml', '.yaml'):
                return yaml.load(config_file)
            else:
                raise ValueError("Invalid build config file extension: {0}".format(config_ext))

    @staticmethod
    def _parse_build_step_config(rule, args={}):
        return rule, args

    @staticmethod
    def _get_build_rule_map():
        build_rules = [
            ExecuteChildRules,
            build_docker_image.BuildDockerImage,
            build_maven_artifact.BuildMavenArtifact,
            build_npm_package.BuildNpmPackage,
            get_passthrough_config.GetPassthroughConfig
        ]

        build_rule_map = {}
        for build_rule in build_rules:
            build_rule_map[build_rule.__name__] = build_rule

        return build_rule_map