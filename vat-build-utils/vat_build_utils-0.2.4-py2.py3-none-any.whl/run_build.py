from __future__ import print_function

import argparse
import json
import logging
import os
import sys

from vat_utils.config import create_config_client_v2

from build_utils.build_context import BuildContext
from build_utils.rules import execute_child_rules

def execute_rule(build_context_config, rule_path):
    build_context = BuildContext(build_context_config)

    # Create a synthetic root build rule
    root_build_rule = execute_child_rules.ExecuteChildRules(build_context, '.')
    return root_build_rule.run(child_rule_paths=[rule_path])

def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('build_config_source')
    parser.add_argument('build_rule_path')
    args = parser.parse_args(argv[1:])

    build_config_client = create_config_client_v2(args.build_config_source)
    build_config = build_config_client.get_root_json_value()

    build_output = execute_rule(build_config, args.build_rule_path)

    print(build_output)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main(sys.argv)
