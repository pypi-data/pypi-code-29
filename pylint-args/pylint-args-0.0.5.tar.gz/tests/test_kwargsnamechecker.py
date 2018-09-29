import astroid

import pylint.testutils

import pylint_args


class TestKwargsNameChecker(pylint.testutils.CheckerTestCase):
    CHECKER_CLASS = pylint_args.KwargsNameChecker

    def test_kwargs_name_ok(self):
        call_node = astroid.extract_node('def foo(**kwargs): pass')
        with self.assertNoMessages():
            self.checker.visit_functiondef(call_node)

    def test_kwargs_wrong_name(self):
        call_node = astroid.extract_node('def foo(**other): pass')
        message = pylint.testutils.Message(
            msg_id='wrong-kwargs-name',
            node=call_node,
        )
        with self.assertAddsMessages(message):
            self.checker.visit_functiondef(call_node)
