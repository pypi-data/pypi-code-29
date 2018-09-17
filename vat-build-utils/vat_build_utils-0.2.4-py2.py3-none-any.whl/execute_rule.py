from build_utils.build_context import BuildContext
from build_utils.rules.execute_child_rules import ExecuteChildRules

def execute_rule(build_context_config, rule_path):
    build_context = BuildContext(build_context_config)

    # Create a synthetic root build rule
    root_build_rule = ExecuteChildRules(build_context, '.')
    return root_build_rule.run(child_rule_paths=[rule_path])
