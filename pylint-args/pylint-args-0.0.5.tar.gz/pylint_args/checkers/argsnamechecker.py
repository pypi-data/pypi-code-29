from pylint_args.checkers.base import ArgsCheckerBase
from pylint_args.messages import MSG_3 as MSG


class ArgsNameChecker(ArgsCheckerBase):
    """
    Checks name of `*args` variable.
    """
    name = 'args-name'
    msg = MSG

    def visit_functiondef(self, node):
        if node.args.vararg and node.args.vararg != 'args':
            self.add_message(MSG['KEY'], node=node)
