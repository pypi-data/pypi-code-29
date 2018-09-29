from pylint_args.checkers.base import ArgsCheckerBase
from pylint_args.messages import MSG_1 as MSG


class DefinitionKwargsOrderChecker(ArgsCheckerBase):
    """
    Checks if keyword arguments passed into function call in same order as they defined in this function definition.

    `defs` -- dict with name -> args object pairs of defined functions.
            If defined two functions with the same names, only later defined function will save.
    """

    name = 'kwargs-order'
    msg = MSG

    def __init__(self, linter):
        super(DefinitionKwargsOrderChecker, self).__init__(linter)
        self.defs = {}

    def visit_functiondef(self, node):
        # Save this definition
        # When we visit function call with this name, we use kwargs order from last defined function with same name
        self.defs[node.name] = node.args

    def visit_call(self, node):
        # Function calls without arguments or with only position arguments
        if not node.keywords:
            return

        kwargs = self._get_kwargs_names(node)
        def_args = self.defs.get(getattr(node.func, 'attrname', None) or node.func.name)

        # We don't handle undefined functions, because pylint do it themself
        if not def_args:
            return

        # both args and kwonlyargs can be kwargs
        def_kwargs = [arg.name for arg in def_args.args] + [arg.name for arg in def_args.kwonlyargs]

        # check if def_kwargs contains kwargs in right order
        intersection = [x for x in def_kwargs if x in kwargs]
        if intersection != sorted(intersection, key=kwargs.index):
            self.add_message(MSG['KEY'], node=node)
