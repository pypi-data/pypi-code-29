import operator, builtins
from types import FunctionType, BuiltinFunctionType
from io import StringIO

from .base import generic, method, variadic_method


def _get_operations():
    """Enumerate all operations to implemented as methods/generics."""
    answer = []
    for name, value in operator.__dict__.items():
        if name.startswith("__") and name.endswith("__") and isinstance(
                value, (FunctionType, BuiltinFunctionType)):
            answer.append((name, value))
    answer.append(("__iter__", iter))
    answer.append(("__divmod__", divmod))
    answer.sort(key=lambda element: element[0])
    return answer

operations = {}
__all__ = [
    "__spy__", "__out__", "__init__", "__call__", "__del__",
    "__float__", "__int__",
    "AbstractObject", "Object", "FinalizingMixin",
    "Writer", "IndentingWriter",
    "spy", "as_string", "as_indented_string", "get_text",
    "push", "pop", "indent", "dedent",
    "CSep", "csep",
    ]

_reverse_operation_names = (
            "add", "sub", "mul",
            "truediv", "floordiv", "mod", "divmod",
            "pow",
            "lshift", "rshift",
            "and", "xor", "or" )

# TODO: Check these sets for completeness
_operations_returning_not_implemented = set((
    "__eq__", "__ne__",
    "__add__",
    "__sub__",
    "__mul__",
    "__matmul__",
    "__truediv__",
    "__floordiv__",
    "__mod__",
    "__divmod__",
    "__pow__",
    "__lshift__",
    "__rshift__",
    "__and__",
    "__xor__",
    "__or_",
    ))

_operations_returning_not_implemented |= set((
    "__i" + name[2:] for name in _operations_returning_not_implemented))

_operations_raising_type_error = set((
    "__lt__", "__le__", "__gt__", "__ge__")) 


def gni2(generic, name):
    """Generate a method returning `NotImplemented`."""
    raise NotImplementedError("TODO")

def gte2(generic, name, operator_symbol=None):
    """Generate a method raising a `TypeError`."""
    if operator_symbol is None:
        operator_symbol = name
    raise NotImplementedError("TODO")


# A specification for default implementations of some operations
default_implementations = dict(
    __eq__= gni2,
    __ne__= gni2,
    
    __lt__= (gte2, "<"),
    __le__= (gte2, "<="),

)


def _install_operations():
    """Install all the operations as generics in this module."""
    for name, value in _get_operations():
        doc = value.__doc__
        doc += "\n\n"
        doc += ("Called by the :meth:`AbstractObject.%s` special method." %
                name)
        basic_name = name[2:-2]
        if basic_name in _reverse_operation_names:
            doc += "\n"
            doc += "Also called by :meth:`AbstractObject.__r%s__` "\
                   "with arguments reversed." % basic_name
        operations[name] = globals()[name] = generic(name, doc)
        if 1:
            if name in _operations_returning_not_implemented:

                def operation(o0: object, o1: object):
                    """Defaults to not comparable."""
                    return NotImplemented

                operation.__name__ = name
                operations[name].method()(operation)
            elif name in _operations_raising_type_error:
                message = ("%r not supported between instance of %%r and %%r"
                % name)

                def operation(o0: object, o1: object):
                    """Defaults to not comparable."""
                    raise TypeError(message %
                        (type(o0).__name__, type(o1).__name__))

                operation.__name__ = name
                operations[name].method()(operation)

        __all__.append(name)

_install_operations()


__init__ = generic("__init__",
""":func:`__init__` initializes instantiates instances of :class:`AbstractObject` and it's subclasses.

It has a multi method for :class:`Object`. This multi-method does not accept any
additional parameters and has no effect.
There is no method for :class:`AbstractObject`, therefore
this class can not be instantiated.""")


__call__ = generic("__call__",
""":func:`__call__` is called when instances of :class:`AbstractObject` are called.""")

__del__ = generic("__del__",
""":func:`__del__` is called when instances of :class:`FinalizingMixin` are about to be destroyed.""")


class AbstractObject(object):
    """An abstract (mixin) class that maps all the python magic functions to generics."""

    def __init__(self, *arguments):
        "Call the :func:`__init__` generic function."""
        __init__(self, *arguments)

    def __call__(self, *arguments):
        "Call the :func:`__call__` generic function."""
        return __call__(self, *arguments)

    def __str__(self):
        "Answer the objects print-string by calling :func:`as_string`."""
        return as_string(self)

    def __repr__(self):
        "Answer the objects debug-string by calling :func:`spy`."""
        return spy(self)

    def __float__(self):
        """Convert the object to a `float` by calling the :func:`__float__` generic."""
        return __float__(self)

    def __int__(self):
        """Convert the object to an `int` by calling the :func:`__int__` generic."""
        return __int__(self)


push = generic("push", "Push the current indent on a stack of indents.")
pop = generic("pop", "Restore the current indent from a stack of indents.")


class AbstractDirective(object):
    """I am the abstract base class of all directives."""

class CSep(AbstractDirective):
    """A conditional separator"""

csep = CSep()

class IndentDirective(AbstractDirective):
    """I specify an indentation."""

indent = IndentDirective()

class DedentDirective(AbstractDirective):
    """I specify an dedentation."""

dedent = DedentDirective()


class Writer(AbstractObject):
    """A simple wrapper around a file like object.

    :class:`Writer`'s purpose is to simplify the implementation
    of the generics :func:`__out__` and :func:`__spy__`.
    
    `Writer` instances are initialised either with a file_like object
    or with no arguments. In the later case ab instance of `StringIO`
    is used.

    Output is done by simply calling the writer with at least one string object.
    The first argument acts as a %-template for formating the other arguments.

    The class is intended to be sub-classed for formatted output."""

@method()
def __init__(writer: Writer):
    """Initialize the `Write` with a `StringIO` object."""
    __init__(writer, StringIO())

@method()
def __init__(writer: Writer, file_like):
    """Initialize the `Write` with a file like object.

    :param file_like: A file-like object."""
    writer.file = file_like

@method()
def __call__(writer: Writer):
    """Write a newline on the file-like object."""
    writer.file.write("\n")

@variadic_method()
def __call__(writer: Writer, directive: AbstractDirective, *directives):
    """Only execute directives."""
    execute_and_filter_directives((directive,) + directives, writer)

@variadic_method()
def __call__(writer: Writer, text: str, *arguments):
    """Write text % arguments on the file-like object."""
    arguments = execute_and_filter_directives(arguments, writer)
    if arguments:
        writer.file.write(text % arguments)
    else:
        writer.file.write(text)

@method()
def push(writer: Writer):
    """`Push` has no effect on an ordinary `Writer` instance."""
    pass

@method()
def pop(writer: Writer):
    """`Pop` has, like `push`, no effect on an ordinary `Writer` instance."""
    pass


get_text = generic("get_text", """Get the text written so far.""") 

@method()
def get_text(writer: Writer):
    """Get the text written so far.

    :Note: This method is only supported if the file-like object
           implements :class:`StringIO`'s :meth:`getvalue` method."""
    return writer.file.getvalue()


class IndentingWriter(Writer):
    """A writer that maintains a stack of indents."""

@method()
def __init__(writer: IndentingWriter, file_like):
    __init__.super(Writer, object)(writer, file_like)
    writer.indents = []
    writer.indent = ""
    writer.indent_width = 4
    writer.indent_char = " "
    writer.only_newline = False

@method()
def __call__(writer:IndentingWriter):
    writer.only_newline = True
    __call__.super(Writer)(writer)


@variadic_method()
def __call__(writer: IndentingWriter, text: str, *arguments):
    arguments = execute_and_filter_directives(arguments, writer)
    if arguments:
        text = text % arguments
    text_list = text.split("\n")
    base_call =  __call__.super(Writer, str)
    sub_text = text_list[0]
    if writer.only_newline:
        base_call(writer, writer.indent)
    if sub_text:
        base_call(writer, sub_text)
        writer.only_newline = False
    else:
        writer.only_newline = True
    for sub_text in text_list[1:]:
        writer()
        if sub_text:
            base_call(writer, writer.indent)
            base_call(writer, sub_text)
            writer.only_newline = False

@method()
def push(writer: IndentingWriter, steps: int):
    writer.indents.append(writer.indent)
    indent = writer.indent_char * (writer.indent_width * steps)
    writer.indent += indent
    if writer.only_newline:
        writer.file.write(indent)

@method()
def push(writer: IndentingWriter):
    push(writer, 1)

@method()
def pop(writer: IndentingWriter, steps: int):
    for count in range(steps):
        writer.indent = writer.indents.pop()

@method()
def pop(writer: IndentingWriter):
    pop(writer, 1)
       

execute_directive = generic(
    "execute_directive", "Execute formatting directives")

@method()
def execute_directive(some_object: object, write: Writer):
    """Do nothing for ordinary objects.
    
    Answer `True`."""
    return True

@method()
def execute_directive(csep: CSep, write: Writer):
    """Insert a space character.

    Answer `False`."""
    write(" ")
    return False

@method()
def execute_directive(csep: CSep, write: IndentingWriter):
    write()
    return False

@method()
def execute_directive(indent: IndentDirective, write: Writer):
    return False

@method()
def execute_directive(dedent: DedentDirective, write: Writer):
    return False

@method()
def execute_directive(indent: IndentDirective, write: IndentingWriter):
    push(write)
    return False

@method()
def execute_directive(dedent: DedentDirective, write: IndentingWriter):
    pop(write)
    return False

def execute_and_filter_directives(directives, write):
    """Execute and remove all the directives from the list of directives."""
    objects = []
    for directive in directives:
        if execute_directive(directive, write):
            objects.append(directive)
    return tuple(objects)


class Object(AbstractObject):
    """Just like `AbstractObject`, but can be instantiated."""

@method()
def __init__(an_object: Object):
    """Do nothing for :class:`Object`."""
    pass


def _install_operations():
    """Install the operations in the class."""

    def get_doc(value):
        try:
            function = getattr(operator, value.__name__)
        except AttributeError:
            function = getattr(builtins, value.__name__[2:-2])
        return function.__doc__


    def generate_operation(value):

        def operation(*arguments):
            #d#print "reg:", arguments
            return value(*arguments)

        doc = get_doc(value) 
        doc += "\n\n"
        doc += ("Calls the :func:`%s`-generic with its arguments." %
                value.__name__)
        operation.__doc__ = doc
        return operation

    def generate_reverse_operation(value):

        def operation(argument0, argument1):
            #d#print "rev:", argument0, argument1
            return value(argument1, argument0)
        
        doc = get_doc(value) 
        doc += "\n\n"
        doc += ("Calls the :func:`%s`-generic with its arguments reversed." %
                value.__name__)
        operation.__doc__ = doc
        return operation

    for name, value in _get_operations():
        operation = generate_operation(operations[name])
        setattr(AbstractObject, name, operation)
    for name in _reverse_operation_names:
        operation = generate_reverse_operation(operations["__%s__" % name])
        setattr(AbstractObject, "__r%s__" % name, operation)


_install_operations()

del _install_operations
del _get_operations

__float__ = generic("__float__", "Convert an :class:`AbstractObject` to a `float`.")
__int__ = generic("__int__", "Convert an :class:`AbstractObject` to an `int`.")


class FinalizingMixin(object):
    """A mixin class with `__del__` implemented as a generic function.
    
    .. note:: This functionality was separated into mixin class,
           because Python's cycle garbage collector does not collect
           classes with a :meth:`__del__` method.
           Inherit from this class if you really 
           need :func:`__del__`.
           """

    def __del__(self):
        """Call the :func:`__del__` generic function."""
        __del__(self)


@generic
def as_string(self):
    """Answer an object's print string.

    This is done by creating a :class:`Writer` instance
    and calling the :func:`__out__` generic with the
    object and the writer. The using :meth:`Writer.get_text`
    to retrieve the text written."""
    writer = Writer()
    __out__(self, writer)
    return get_text(writer)

@generic
def as_indented_string(self):
    """Answer an object's indented string.

    This is done by creating a :class:`IndentingWriter` instance
    and calling the :func:`__out__` generic with the
    object and the writer. The using :meth:`Writer.get_text`
    to retrieve the text written."""
    writer = IndentingWriter()
    __out__(self, writer)
    return get_text(writer)

__out__ = generic("__out__",
        "Create a print string of an object using a :class:`Writer`.")

@method()
def __out__(self, write: Writer):
    """Write a just :func:`str` of self."""
    write(str(self))

@method()
def __out__(self: AbstractObject, write: Writer):
    """Write a just :func:`str` of self by directly calling :meth:`object.__str__`."""
    write(object.__str__(self))


@generic
def spy(self):
    """Answer an object's debug string.

    This is done by creating a :class:`Writer` instance
    and calling the :func:`__spy__` generic with the
    object and the writer. The using :meth:`Writer.get_text`
    to retrieve the text written.
    
    .. note:: The function's name was taken from Prolog's
           `spy` debugging aid.
           
.. _spy <http://cis.stvincent.edu/html/tutorials/prolog/spy.html> """
    writer = Writer()
    __spy__(self, writer)
    return get_text(writer)

__spy__ = generic("__spy__",
        """Create a print string of an object using a `Writer`.

.. note:: The function's name was taken from Prolog's `spy` debugging aid.""")

@method()
def __spy__(self, write: Writer):
    """Write a just :func:`repr` of self."""
    write(repr(self))

@method()
def __spy__(self: AbstractObject, write: Writer):
    """Write a just :func:`repr` of self by directly calling :meth:`object.__repr__`."""
    write(object.__repr__(self))
