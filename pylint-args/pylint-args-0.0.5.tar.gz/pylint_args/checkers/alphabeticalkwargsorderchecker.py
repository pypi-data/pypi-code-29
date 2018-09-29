from pylint_args.checkers.base import ArgsCheckerBase
from pylint_args.messages import MSG_0 as MSG


class AlphabeticalKwargsOrderChecker(ArgsCheckerBase):
    """
    Checks if keyword arguments passed into function call in alphabetical order.
    """

    name = 'kwargs-order'
    msg = MSG

    def visit_call(self, node):
        # Function calls without arguments or with only position arguments
        if not node.keywords:
            return

        kwargs = self._get_kwargs_names(node)
        if sorted(kwargs) != kwargs:
            self.add_message(MSG['KEY'], node=node)
