# -*- coding: utf-8 -*-
from pylint.checkers import BaseChecker
from pylint.checkers.utils import check_messages
from pylint.interfaces import IAstroidChecker
from pylint.lint import PyLinter


class TopologyChecker(BaseChecker):
    __implements__ = IAstroidChecker

    name = 'topology-checker'
    msgs = {
        'W0666': (
            'Depends on a higher priority module.',
            'invalid-topological-dependencies',
            'Apps\' dependencies should match a certain topology.',
        ),
    }
    options = (
        (
            'module-topology',
            {
                'default': tuple(),
                'type': 'csv',
                'metavar': '<module names>',
                'help': 'List of module names for which are in a certain topology. Module imports '
                        'should be forwards, backwards imports are not allowed.',
            },
        ),
    )

    @check_messages('invalid-topological-dependencies')
    def visit_importfrom(self, node):
        def get_module_index(full_module_name):
            """ get module index in topology """
            for i, modules in enumerate(topology):
                for module in modules.split('='):
                    if full_module_name.startswith(module):
                        return i
            return None

        topology = self.config.module_topology
        if not topology:  # do not check if no such config
            return
        frame = node.frame()
        module_index = get_module_index(frame.name)
        if module_index is None:  # no need to check
            return
        import_index = get_module_index(node.modname)
        if import_index is None:  # no need to check either
            return
        if module_index < import_index:
            self.add_message('W0666', node=node)


def register(linter: PyLinter):
    linter.register_checker(TopologyChecker(linter))
