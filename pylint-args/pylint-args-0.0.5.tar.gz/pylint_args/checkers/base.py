from pylint.checkers import BaseChecker
from pylint.interfaces import IAstroidChecker


class ArgsCheckerBase(BaseChecker):
    """
    Base class of keyword arguments checkers.
    """
    __implements__ = IAstroidChecker

    msg = None
    priority = -1

    @staticmethod
    def _get_kwargs_names(call_node):
        # Names of keyword arguments without `**kwargs`
        return [kw.arg for kw in call_node.keywords if kw.arg]

    def __init__(self, linter):
        if self.__class__.msg:
            msg = self.__class__.msg
            self.__class__.msgs = {msg['ID']: (msg['TITLE'], msg['KEY'], msg['DESCRIPTION'])}
        super(ArgsCheckerBase, self).__init__(linter)
