from pylint_args.checkers.kwargsorderchecker import DefinitionKwargsOrderChecker
from pylint_args.checkers.alphabeticalkwargsorderchecker import AlphabeticalKwargsOrderChecker
from pylint_args.checkers.argsnamechecker import ArgsNameChecker
from pylint_args.checkers.kwargsnamechecker import KwargsNameChecker


def register(linter):
    linter.register_checker(AlphabeticalKwargsOrderChecker(linter))
    linter.register_checker(DefinitionKwargsOrderChecker(linter))
    linter.register_checker(ArgsNameChecker(linter))
    linter.register_checker(KwargsNameChecker(linter))
