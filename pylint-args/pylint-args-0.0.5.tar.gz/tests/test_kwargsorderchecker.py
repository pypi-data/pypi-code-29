import astroid

import pylint.testutils

import pylint_args


class TestDefinitionKwargsOrderChecker(pylint.testutils.CheckerTestCase):
    CHECKER_CLASS = pylint_args.DefinitionKwargsOrderChecker

    def test_empty(self):
        func_node, call_node = astroid.extract_node(
            '''
            def foo(): pass  #@
            foo()  #@
            '''
        )
        with self.assertNoMessages():
            self.checker.visit_functiondef(func_node)
            self.checker.visit_call(call_node)

    def test_kwargs_only_empty(self):
        func_node, call_node = astroid.extract_node(
            '''
            def foo(**kwargs): pass  #@
            foo()  #@
            '''
        )
        with self.assertNoMessages():
            self.checker.visit_functiondef(func_node)
            self.checker.visit_call(call_node)

    def test_kwargs_only_ok(self):
        func_node, call_node = astroid.extract_node(
            '''
            def foo(**kwargs): pass  #@
            foo(a=1, c=4, b=3)  #@
            '''
        )
        with self.assertNoMessages():
            self.checker.visit_functiondef(func_node)
            self.checker.visit_call(call_node)

    def test_args_only_empty(self):
        func_node, call_node = astroid.extract_node(
            '''
            def foo(*args): pass  #@
            foo()  #@
            '''
        )
        with self.assertNoMessages():
            self.checker.visit_functiondef(func_node)
            self.checker.visit_call(call_node)

    def test_args_only_ok(self):
        func_node, call_node = astroid.extract_node(
            '''
            def foo(*args): pass  #@
            foo(1, 3)  #@
            '''
        )
        with self.assertNoMessages():
            self.checker.visit_functiondef(func_node)
            self.checker.visit_call(call_node)

    def test_args_kwargs_empty(self):
        func_node, call_node = astroid.extract_node(
            '''
            def foo(**kwargs): pass  #@
            foo()  #@
            '''
        )
        with self.assertNoMessages():
            self.checker.visit_functiondef(func_node)
            self.checker.visit_call(call_node)

    def test_args_kwargs_ok(self):
        func_node, call_node = astroid.extract_node(
            '''
            def foo(*args, **kwargs): pass  #@
            foo(1, c=4, b=3)  #@
            '''
        )
        with self.assertNoMessages():
            self.checker.visit_functiondef(func_node)
            self.checker.visit_call(call_node)

    def test_default_kwargs_ok(self):
        func_node, call_node = astroid.extract_node(
            '''
            def foo(one=1, two=2, three=3): pass  #@
            foo(one=0, two=1, three=2)  #@
            '''
        )
        with self.assertNoMessages():
            self.checker.visit_functiondef(func_node)
            self.checker.visit_call(call_node)

    def test_default_kwargs_wrong_order(self):
        func_node, call_node = astroid.extract_node(
            '''
            def foo(one=1, two=2, three=3): pass  #@
            foo(three=0, two=1, one=2)  #@
            '''
        )
        message = pylint.testutils.Message(
            msg_id='wrong-kwargs-order',
            node=call_node,
        )
        with self.assertAddsMessages(message):
            self.checker.visit_functiondef(func_node)
            self.checker.visit_call(call_node)

    def test_full_wrong_order(self):
        func_node, call_node = astroid.extract_node(
            '''
            def foo(a, b=1, *args, z, x=2, y, **kwargs): pass  #@
            foo(a=1, x=4, y=3, z=9, yy=33)  #@
            '''
        )
        message = pylint.testutils.Message(
            msg_id='wrong-kwargs-order',
            node=call_node,
        )
        with self.assertAddsMessages(message):
            self.checker.visit_functiondef(func_node)
            self.checker.visit_call(call_node)

    def test_full_ok(self):
        func_node, call_node = astroid.extract_node(
            '''
            def foo(a, b=1, *args, z, x=2, y, **kwargs): pass  #@
            foo(a=1, z=4, y=3, yy=33)  #@
            '''
        )
        with self.assertNoMessages():
            self.checker.visit_functiondef(func_node)
            self.checker.visit_call(call_node)


class TestAlphabeticalKwargsOrderChecker(pylint.testutils.CheckerTestCase):
    CHECKER_CLASS = pylint_args.AlphabeticalKwargsOrderChecker

    def test_empty_kwargs(self):
        call_node = astroid.extract_node('foo()')
        with self.assertNoMessages():
            self.checker.visit_call(call_node)

    def test_kwargs_only(self):
        call_node = astroid.extract_node('foo(**kwargs)')
        with self.assertNoMessages():
            self.checker.visit_call(call_node)

    def test_args_only(self):
        call_node = astroid.extract_node('foo(*args)')
        with self.assertNoMessages():
            self.checker.visit_call(call_node)

    def test_kwargs_ok(self):
        call_node = astroid.extract_node('foo(a=1, b=2)')
        with self.assertNoMessages():
            self.checker.visit_call(call_node)

    def test_kwargs_wrong_order(self):
        call_node = astroid.extract_node('foo(b=1, a=2)')
        message = pylint.testutils.Message(
            msg_id='wrong-alphabetical-kwargs-order',
            node=call_node,
        )
        with self.assertAddsMessages(message):
            self.checker.visit_call(call_node)

    def test_args_kwargs_ok(self):
        call_node = astroid.extract_node('foo(1, 2, *c, a=1, b=2, **kwargs, e=lol)')
        with self.assertNoMessages():
            self.checker.visit_call(call_node)

    def test_args_wrong_order(self):
        call_node = astroid.extract_node('foo(1, 2, *c, c=1, d=2, **kwargs, a=lol)')
        message = pylint.testutils.Message(
            msg_id='wrong-alphabetical-kwargs-order',
            node=call_node,
        )
        with self.assertAddsMessages(message):
            self.checker.visit_call(call_node)
