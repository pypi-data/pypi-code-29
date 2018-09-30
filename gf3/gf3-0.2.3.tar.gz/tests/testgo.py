"""Tests for the generic object (`go`) module."""

import sys, os
sys.path.insert(0,
        os.path.abspath(
            os.path.normpath(
                os.path.join(
                    os.path.basename(sys.argv[0]), os.pardir))))
del os, sys

from unittest import TestCase as BaseTestCase
from gf import (Object, FinalizingMixin, Writer,
        generic, method, variadic_method, 
        Dispatch, isgeneric, merge,
        __init__, __call__, __del__,
        __spy__, __add__, __out__, as_string, spy,
        __eq__, __ne__,
        )



class TestCase(BaseTestCase):
    """The base class of all the tests."""

    def setUp(self):
        """Set up the test class."""

        class TC(Object):
            """A simple test class."""

        @method()
        def __init__(test_object: TC):
            test_object.a0 = "v0"
            test_object.a1 = "v1"
        
        self.TC = TC


class InitTestCase(TestCase):
    """Test the initialisation."""

    def test_init(self):
        """Test the initialisation of our test class."""
        to = self.TC()
        self.assertEqual(to.a0, "v0")
        self.assertEqual(to.a1, "v1")
        self.assertTrue(".TC object at" in str(to))


class OutputTestCase(TestCase):
    """Test the output and string conversion functions."""

    def setUp(self):
        """Setup additional output methods."""
        super().setUp()
        TC = self.TC

        @method()
        def __out__(test_object: TC, write: Writer):
            write("TC(%s, %s)", test_object.a0, test_object.a1)

        @method()
        def __spy__(self: TC, write: Writer):
            __spy__.super(Object, Writer)(self, write)
            write("(")
            __spy__(self.a0, write)
            write(", ")
            __spy__(self.a1, write)
            write(")")

    def test_string_conversion(self):
        """Test the string conversion functions."""
        to = self.TC()
        object_as_string = str(to)
        self.assertEqual(object_as_string, "TC(v0, v1)")
        self.assertEqual(object_as_string, as_string(to))
        debug_string = repr(to)
        self.assertTrue(".TC object at" in debug_string)
        self.assertTrue(debug_string.endswith(">('v0', 'v1')"))
        self.assertEqual(debug_string, spy(to))


class OperatorTestCase(TestCase):
    """Test a bit of the operators."""

    def setUp(self):
        """Setup additional output methods."""
        super().setUp()
        TC = self.TC

        @method()
        def __add__(self: TC, an_integer: int):
            return self.a0 * self.a1 + an_integer

        @method()
        def __call__(self: TC, an_integer: int):
            return "%r %r %d" % (self.a0, self.a1, an_integer)

    def test_add(self):
        """Test the newly defined addition method.""" 
        to = self.TC()
        to.a0 = 2
        to.a1 = 3
        self.assertEqual(to + 3, 9)
        self.assertRaises(TypeError, lambda: 3 + to) 

    def test_greater(self):
        """Test the unimplemented greater operator.

        According to the documentation this should
        raise a `TypeError`."""
        TC = self.TC
        to0 = TC()
        to1 = TC()
        self.assertRaises(TypeError, lambda: to0 > to1)

    def test_call(self):
        """Test calling the instance."""
        to = self.TC()
        self.assertEqual("'v0' 'v1' 11", to(11))


class FinalizingTestCase(TestCase):
    """Test the finalizing functionality."""

    def setUp(self):
        """Set up an additional subclass."""
        super().setUp()
        self.fo = None

        class FC(FinalizingMixin, self.TC):
            """A test class with a `__del__` generic implementation."""
        
        @method()
        def __del__(an_fo: FC):
            self.fo = an_fo

        self.FC = FC

    def test_finalisation(self):
        """Test an object's finalisation."""
        self.assertTrue(self.fo is None)
        fo = self.FC()
        self.assertTrue(self.fo is None)
        del fo
        self.assertFalse(self.fo is None)


class VariadicTestCase(TestCase):
    """Test variadic methods."""
    
    def test_variadic(self):
        """Test variadic methods."""

        varfun0 = generic()
        varfun1 = generic()

        @varfun0.variadic_method()
        def varfun0(*arguments):
            return tuple(reversed(arguments))
        
        @varfun1.variadic_method()
        def varfun1(tc: self.TC, *arguments):
            return (tc,) + tuple(reversed(arguments))
        
        @method()
        def __eq__(tc0: self.TC, tc1: self.TC):  # Make `assertEqual`work!
            return tc0.a0 == tc1.a0 and tc0.a1 == tc1.a1
        
        @method()
        def __eq__(tc0: self.TC, t: tuple):  # Make `assertEqual`work!
            return False
        
        @method()
        def __ne__(tc0: self.TC, tc1: self.TC):  # Make `assertEqual`work!
            return tc0.a0 != tc1.a0 or tc0.a1 != tc1.a1

        self.assertEqual(varfun0(1, 2, 3), (3, 2, 1))
        to = self.TC()
        self.assertEqual(varfun1(to, "a", "b", "c"), (to, "c", "b", "a"))
        self.assertRaises(NotImplementedError, varfun1, "Sepp")
        self.assertEqual(varfun1(to), (to,))

        self.assertEqual(varfun0(1, 2), (2, 1))

        @varfun0.method()
        def varfun0(one: int, two: int):
            return [one, two]

        self.assertEqual(varfun0(1, 2), [1, 2])
        self.assertEqual(varfun0(1, 2, 3), (3, 2, 1))
        self.assertEqual(varfun0("1", "2"), ("2", "1"))

        varfun2 = generic()

        @varfun2.method()
        def varfun2(a: str, b: str):
            return "|".join((a, b))

        self.assertEqual(varfun2("a", "b"), "a|b")

        @varfun2.variadic_method()
        def varfun2(a_string: str, *arguments):
            return "%s: %r" % (a_string, arguments)

        self.assertEqual(varfun2("a", "b"), "a|b")
        self.assertEqual(varfun2("c") , "c: ()")
        

    def test_override(self):
        """Test variadic overrides."""
        varfun0 = generic()

        @varfun0.variadic_method()
        def varfun0(*arguments):
            return None

        self.assertEqual(varfun0("Test", "Test"), None)

        @varfun0.variadic_method()
        def varfun0(a_string: str, *arguments):
            return a_string

        self.assertEqual(varfun0("Test", "Test"), "Test")

        varfun1 = generic()

        @varfun1.variadic_method()
        def varfun1(a_string: str, *arguments):
            return a_string

        self.assertEqual(varfun1("Test", "Test"), "Test")

        @varfun1.variadic_method()
        def varfun1(*arguments):
            return None

        self.assertEqual(varfun1("Test", "Test"), "Test")
        self.assertEqual(varfun1(1, "Test"), None)
        self.assertEqual(varfun1(1), None)


# XXX: Add a ``testbase`` module?
class DispatchOnObjectTest(TestCase):
    """Test dispatching on objects."""

    def setUp(self):
        """Setup `self.tg` with `TC` and ``42``."""
        super().setUp()
        self.tg = generic("tg", "Test generic")

        @self.tg.method()
        def tg(to: self.TC, fortyTwo: 42):
            return "Gotcha"

        @self.tg.method()
        def tg(lst: list, just_an_argument):
            return "Gotta list"

    def test_forty_two(self):
        """Test our special `tg` method."""
        self.assertEqual(self.tg(self.TC(), 42), "Gotcha")

    def test_unhashable(self):
        """Test if an unhashable object raises a warning."""
        with self.assertWarns(RuntimeWarning):
            self.assertEqual(self.tg([0, 1, 2], "Sepp"), "Gotta list")


class DispatchOnObjectAndClassHierarchyTest(TestCase):
    """Test dispatching on the class mro."""

    def setUp(self):
        """Setup `self.tg` with `TC` and ``42``."""
        super().setUp()
        self.tg = generic(
            "tg",
            "Test generic",
            Dispatch.ON_OBJECT_AND_CLASS_HIERARCHY)

        @self.tg.method()
        def tg(to: self.TC, a_list: list):
            self.assertIs(a_list, list)
            return "Got a list"

        @self.tg.method()
        def tg(to: self.TC, an_int: int):
            return "Got an int: %r" % an_int

        @self.tg.method()
        def tg(to: self.TC, fortyTwo: 42):
            return "Gotcha"

    def test_forty_two(self):
        """Test our special `tg` method."""
        self.assertEqual(self.tg(self.TC(), list), "Got a list")
        self.assertEqual(self.tg(self.TC(), 4711), "Got an int: 4711")
        self.assertEqual(self.tg(self.TC(), int), "Got an int: <class 'int'>")
        self.assertEqual(self.tg(self.TC(), 42), "Gotcha")


class DispatchOnClassOnlyTest(TestCase):

    def setUp(self):
        """Setup `self.tg` with `TC` and ``42``."""
        super().setUp()

        self.tg = generic(
            "tg",
            "Test generic",
            Dispatch.ON_CLASS)

    def test_add_dispatch_on_object(self):
        """Specifying an object to dispatch on should raise a ``TypeError``"""
        with self.assertRaises(TypeError):
        
           @self.tg.method()
           def tg(to: self.TC, fortyTwo: 42):
               return "Gotcha"


class AbstractTwoClassTest(TestCase):

    def setUp(self):
        """Setup `self.tg` with `TC` and ``42``."""
        super().setUp()
        self.tg = generic(
            "tg",
            "Test generic",
            Dispatch.ON_OBJECT)

        class SubTC(self.TC):
            """A subclass."""

        self.SubTC = SubTC
        
        @self.tg.method()
        def tg(to: self.TC):
            return "TC"

        @self.tg.method()
        def tg(to: self.SubTC):
            return tg(super(self.TC, to)) + " and SubTC"
        

class SuperCallTest(AbstractTwoClassTest):

    def test_super_calls(self):
        """Test a call using ``super``."""
        self.assertEqual(self.tg(self.TC()), "TC")
        self.assertEqual(self.tg(self.SubTC()), "TC and SubTC")


class MergeGenericsTest(AbstractTwoClassTest):
    """Test merging two generics."""

    def setUp(self):
        super().setUp()

        self.other_tg = generic("other_tg", "Test generic")
      
        @self.other_tg.method()
        def other_tg(to: self.TC):
            return "TC (other)"

        @self.other_tg.method()
        def other_tg(to: self.SubTC):
            return self.other_tg(super(self.TC, to)) + " and SubTC (other)"

        @self.other_tg.method()
        def other_tg(an_integer: int):
            return "int: [%d] (other)" % an_integer
        
        @self.tg.method()
        def other_tg(a_string: str):
            return "str: [%s]" % a_string

        @self.tg.method()
        def other_tg(a_string: str, an_integer: int):
            return self.tg(a_string) + "|" + self.other_tg(an_integer)

        @self.other_tg.method()
        def other_tg(a_string: str, an_integer: int):
            return self.other_tg(an_integer) + "|" + self.tg(a_string)

    def test_merge(self):
        """Test calling a merged generic."""
        self.assertEqual(self.other_tg(self.TC()), "TC (other)")
        self.assertEqual(self.other_tg(self.SubTC()),
                         "TC (other) and SubTC (other)")
        self.assertEqual(self.other_tg(42), "int: [42] (other)")
        self.assertEqual(self.tg("Sepp"), "str: [Sepp]")
        self.assertEqual(self.other_tg("Sepp", 12), 
                         "int: [12] (other)|str: [Sepp]")
        self.assertEqual(self.tg("Sepp", 12), 
                         "str: [Sepp]|int: [12] (other)")
        merged_tg = merge(self.tg, self.other_tg)
        self.assertEqual(merged_tg(self.TC()), "TC (other)")
        self.assertEqual(merged_tg(self.SubTC()),
                         "TC (other) and SubTC (other)")
        self.assertEqual(merged_tg(42), "int: [42] (other)")
        self.assertEqual(merged_tg("Sepp"), "str: [Sepp]")
        self.assertEqual(merged_tg("Sepp", 12), 
                         "int: [12] (other)|str: [Sepp]")
        self.assertEqual(merged_tg("Sepp", 12), 
                         "int: [12] (other)|str: [Sepp]")

    def test_merge_variadics(self):
        """Test merging variadics."""
        @self.other_tg.variadic_method()
        def other_tg(to: list, *arguments):
            return "List (other): %r" % (arguments,)
        self.assertEqual(self.other_tg([], 1, 2), "List (other): (1, 2)")
        merged_tg = merge(self.tg, self.other_tg)
        self.assertEqual(merged_tg([], 1, 2), "List (other): (1, 2)")
        self.assertEqual(merged_tg([], 1, 2, 3), 
                         "List (other): (1, 2, 3)")
    

class TestIsGeneric(BaseTestCase):
    """Test the is generic function."""

    def test_isgeneric(self):
        """Test the isgeneric function."""
        self.assertFalse(isgeneric(object))
        self.assertFalse(isgeneric(object()))
        self.assertFalse(isgeneric(1))
        self.assertFalse(isgeneric(isinstance))
        self.assertFalse(isgeneric(method))
        self.assertTrue(isgeneric(generic))
        self.assertTrue(isgeneric(isgeneric))


if __name__ == "__main__":
    from unittest import main
    main()
