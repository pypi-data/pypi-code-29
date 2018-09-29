import astroid

import pylint.testutils

import pylint_args


class TestArgsNameChecker(pylint.testutils.CheckerTestCase):
    CHECKER_CLASS = pylint_args.ArgsNameChecker

    def test_args_name_ok(self):
        call_node = astroid.extract_node('def foo(*args): pass')
        with self.assertNoMessages():
            self.checker.visit_functiondef(call_node)

    def test_args_wrong_name(self):
        call_node = astroid.extract_node('def foo(*other): pass')
        message = pylint.testutils.Message(
            msg_id='wrong-args-name',
            node=call_node,
        )
        with self.assertAddsMessages(message):
            self.checker.visit_functiondef(call_node)
