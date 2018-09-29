from pylint_args.checkers.base import ArgsCheckerBase
from pylint_args.messages import MSG_2 as MSG


class KwargsNameChecker(ArgsCheckerBase):
    """
    Checks name of `**kwargs` variable.
    """
    name = 'kwargs-name'
    msg = MSG

    def visit_functiondef(self, node):
        if node.args.kwarg and node.args.kwarg != 'kwargs':
            self.add_message(MSG['KEY'], node=node)
