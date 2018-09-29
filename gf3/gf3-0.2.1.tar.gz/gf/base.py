# -*- coding: utf-8 -*-
"""Generic functions and multi methods.

This module was snarfed from:
<http://svn.python.org/view/*checkout*/sandbox/trunk/overload/overloading.py?content-type=text%2Fplain&rev=43727>

The original doc string follows:

Dynamically overloaded functions.

This is an implementation of (dynamically, or run-time) overloaded
functions; also known as generic functions or multi-methods.

The dispatch algorithm uses the types of all argument for dispatch,
similar to (compile-time) overloaded functions or methods in C++ and
Java.

Most of the complexity in the algorithm comes from the need to support
subclasses in call signatures.  For example, if an function is
registered for a signature (T1, T2), then a call with a signature (S1,
S2) is acceptable, assuming that S1 is a subclass of T1, S2 a subclass
of T2, and there are no other more specific matches (see below).

If there are multiple matches and one of those doesn't *dominate* all
others, the match is deemed ambiguous and an exception is raised.  A
subtlety here: if, after removing the dominated matches, there are
still multiple matches left, but they all map to the same function,
then the match is not deemed ambiguous and that function is used.
Read the method find_func() below for details.

Python 2.5 is required due to the use of predicates any() and all().
"""


import sys
from types import FunctionType, BuiltinFunctionType
from inspect import signature as get_signature, getfullargspec, Parameter
from enum import Enum
from warnings import warn


class Dispatch(Enum):

    ON_OBJECT = 0
    ON_CLASS = 1
    ON_OBJECT_AND_CLASS_HIERARCHY = 2


class GenericFunction(object):
    """An implementation of generic functions.
    """

    def __init__(
            self,
            default_func=None,
            name=None,
            dispatch=Dispatch.ON_OBJECT):
        self.registry = {}
        self.variadics = {}
        self.generated_variadic_signatures = {}
        self.arities = set()
        self.cache = {}
        self.name = name
        self.default_func = default_func
        self.compute_mro = (
                self.compute_mro_class_method 
            if dispatch == Dispatch.ON_OBJECT_AND_CLASS_HIERARCHY else
                self.compute_mro_type_case)
        self.dispatch = dispatch
    
    @property
    def has_default_dispatch(self):
        """Answer `true` if we use the default dispatch."""
        return self.compute_mro is self.compute_mro_type_case

    @staticmethod
    def compute_mro_type_case(some_type):
        """Compute the mro in case we dispatch only on types."""
        return some_type.__mro__
    
    @staticmethod
    def compute_mro_non_type_case(some_object):
        """Compute the mro if dispatch on objects, too."""
        return (some_object,) + type(some_object).__mro__

    @staticmethod
    def compute_mro_class_method(some_object):
        """Compute the mro if we dispatch for classes."""
        if isinstance(some_object, type):
            return some_object.__mro__
        else:
            return (some_object,) + type(some_object).__mro__

    def method(self):
        """Decorator to register a method for a specific set of types.
        """
        
        def helper(function):
            types = self._get_functions_types(function)
            self.register_func(types, function, False)
            return self.substitute
            
        return helper

    def adapt_mro_to_types(self, types):
        """If we dispatch on non types change the mro computation."""
        # Early exit, won't switch if we only dispatch on class
        if self.dispatch == Dispatch.ON_CLASS:
            if any(not isinstance(t, type) for t in types):
                raise TypeError(
                    "Can't dispatch on instances in state: %s" %
                    self.dispatch)
            return
        if self.has_default_dispatch and any(not isinstance(t, type)
                                             for t in types):
            self.compute_mro = self.compute_mro_non_type_case

    def variadic_method(self):
        """Decorator to register a method for a specific set of types.
        
        The method has a variable argument count.
        """
        
        def helper(function):
            types = self._get_functions_types(function)
            self.register_func(types, function, True)
            return self.substitute
            
        return helper

    def register_func(self, types, func, variadic):
        """Helper to register an implementation."""
        if self.name is None:
            self.name = "%s.%s" % (func.__module__, func.__name__)
            self.substitute.__name__ = func.__name__
        if self.substitute.__doc__ and func.__doc__:
            doc = "\n\n"
            if not self.registry:
                doc += "Multi methods:\n\n"
            arg_spec = getfullargspec(func)
            doc += ".. function:: %s.%s(%s)" % (
                func.__module__, func.__name__,
                ", ".join(("%s: %s" % (arg, type.__name__)
                           for arg, type in zip(arg_spec[0],
                            types))) + (", *%s" % arg_spec[1]
                                if variadic else ""))
            doc += "\n\n"
            doc += "\n".join(
                    " " * 4 + line for line in func.__doc__.split("\n"))
            if variadic:
                doc += "\n    *This is a variadic method.*"
            self.substitute.__doc__ += doc
        self.adapt_mro_to_types(types)
        self.registry[tuple(types)] = func
        if variadic:
            self.variadics[tuple(types)] = func
            self.arities = set()
            for sig in self.generated_variadic_signatures:
                del self.registry[sig]
            self.generated_variadic_signatures = {}
        self.cache = {} # Clear the cache (later we can optimize this).


    def _get_functions_types(self, function):
        """Answer the types of the functions parameters."""
        return [object if parameter.annotation == Parameter.empty 
                else parameter.annotation
                for parameter in get_signature(function).parameters.values()
                if parameter.kind == Parameter.POSITIONAL_OR_KEYWORD]
        
    def __call__(self, *args):
        """Call the overloaded function."""
        types = []
        real_arguments = []
        ta = types.append
        raa = real_arguments.append
        if self.has_default_dispatch:
            for argument in args:
                if isinstance(argument, super):
                    ta(argument.__thisclass__)
                    raa(argument.__self__)
                else:
                    ta(type(argument))
                    raa(argument)
        else:
            for argument in args:
                if isinstance(argument, super):
                    ta(argument.__thisclass__)
                    raa(argument.__self__)
                else:
                    if argument.__hash__ is gf_hash:
                        #D: print('C gf_hash in:', argument, isinstance(argument, type))
                        ta(type(argument))
                    elif type(argument).__hash__ is gf_hash:
                        #D: print('I gf_hash in:', argument, isinstance(argument, type))
                        ta(type(argument))                      
                    else:
                        ta(argument)
                    raa(argument)
        types = tuple(types)
        try:
            func = self.cache[types]
        except TypeError:  # types is not hashable, so don't cache it
            func = self.find_func(types)
        except KeyError:
            self.cache[types] = func = self.find_func(types)
        return func(*real_arguments)

    def super(self, *types):
        """Answer a specific (base) method that for the types passed."""
        return self.find_func(types)

    def _fix_variadics(self, arity):
        """Fix the registry for all the variadic functions.
        
        Don't touch the cache, we never processed functions
        with this `arity`."""
        if arity not in self.arities:
            for sig, function in self.variadics.items():
                sig_len = len(sig)
                if sig_len < arity:
                    new_sig = sig + (object,) * (arity - len(sig))
                    generated_arity = self.generated_variadic_signatures.get(
                        new_sig)
                    if ((generated_arity is None or generated_arity <= arity)
                        and new_sig not in self.registry):
                        self.registry[new_sig] = function
                        self.generated_variadic_signatures[new_sig] = arity
                        
            self.arities.add(arity)

    def find_func(self, types):
        """Find the appropriate overloaded function; don't call it."""
        # XXX: Types is a misnomer, sometimes we dispatch on objects
        try:
            func = self.registry.get(types)
        except TypeError as error:  # Switch to types if we have unhashable objects
            warn("Can't dispatch on unhashable signature: %r (details: «%s») in %r" %
                          (types, error.args[0], self.name), RuntimeWarning)
            converted_type_list = []
            for some_type in types:
                if some_type.__hash__ is None:
                    converted_type_list.append(type(some_type))
                elif some_type.__hash__ is gf_hash:
                    #D: print('Adding type with gf_hash:', some_type, self.name)
                    converted_type_list.append(type(some_type))
                else:
                    converted_type_list.append(some_type)
            types = tuple(converted_type_list)
            func = self.registry.get(types)           
        if func is not None:
            # Easy case -- direct hit in registry.
            return func
    
        self._fix_variadics(len(types))
        # I can't help myself -- this is going to be intense functional code.
        # Find all possible candidate signatures. (2018-09-29: Comment by GvR)
        mros = tuple(self.compute_mro(t) for t in types)
        n = len(mros)
        candidates = [sig for sig in self.registry
                      if len(sig) == n and
                         all(t in mro for t, mro in zip(sig, mros))]
        if not candidates:
            # No match at all -- use the default function.
            answer = self.default_func
            if answer is None:

                def answer(*arguments):
                    raise NotImplementedError( 
                            "Generic %r has no implementation for type(s): %s" % (
                                self.name,
                                ", ".join(("%s.%s" % 
                                           (o.__module__,
                                            o.__name__ )) if isinstance(o, type) else
                                          ("%s.%s(%r)" % (
                                              type(o).__module__,
                                              type(o).__name__,
                                              o))
                                for o in types)))

            return answer
        if len(candidates) == 1:
            # Unique match -- that's an easy case.
            return self.registry[candidates[0]]
    
        # More than one match -- weed out the subordinate ones.
    
        def dominates(dom, sub,
                      orders=tuple(dict((t, i) for i, t in enumerate(mro))
                                   for mro in mros)):
            # 2018-09-29: Comment by GvR
            # Predicate to decide whether dom strictly dominates sub.
            # Strict domination is defined as domination without equality.
            # The arguments dom and sub are type tuples of equal length.
            # The orders argument is a precomputed auxiliary data structure
            # giving dicts of ordering information corresponding to the
            # positions in the type tuples.
            # A type d dominates a type s iff order[d] <= order[s].
            # A type tuple (d1, d2, ...) dominates a type tuple of equal length
            # (s1, s2, ...) iff d1 dominates s1, d2 dominates s2, etc.
            if dom is sub:
                return False
            return all(order[d] <= order[s]
                       for d, s, order in zip(dom, sub, orders))
    
        # I suppose I could inline dominates() but it wouldn't get any clearer.
        candidates = [cand
                      for cand in candidates
                      if not any(dominates(dom, cand) for dom in candidates)]
        if len(candidates) == 1:
            # There's exactly one candidate left.
            return self.registry[candidates[0]]
    
        # Perhaps these multiple candidates all have the same implementation?
        funcs = set(self.registry[cand] for cand in candidates)
        if len(funcs) == 1:
            return funcs.pop()
    
        # No, the situation is irreducibly ambiguous.
        raise TypeError("ambiguous call to generic %r; types=%r; candidates=%r" %
                        (self.name, types, candidates))

    def merged(self, other, new_name=None):
        """Generate a new generic function form `self` and `other`."""
        if self.default_func != other.default_func:
            raise TypeError(
                "Both generics must have the same default function")
        if self.dispatch != other.dispatch:
            raise TypeError(
                "Both generics must have the same dispatch type")
        if new_name is None:
            if self.name is None:
                new_name = other.name
            elif other.name is None:
                new_name = self.name
            elif self.name == other.name:
                new_name = self.name
            else:
                new_name = "%s__%s" % (self.name, other.name)
        # TODO: Handle the documentation
        answer = _generic(
            self.default_func, 
            name=new_name, 
            dispatch=self.dispatch,
            implementation_constructor=self.__class__)
        new_generic = answer.implementation
        for signature, implementation in self.registry.items():
            new_generic.register_func(
                signature,
                implementation,
                signature in self.variadics)
        for signature, implementation in other.registry.items():
            new_generic.register_func(
                signature,
                implementation,
                signature in other.variadics)
        return answer
  

def _generic(
        defaultFunction=None,
        name=None,
        doc=None,
        dispatch=Dispatch.ON_OBJECT,
        implementation_constructor=GenericFunction):
    """Answer a generic function, that is a real function object.
    """
    
    genericFunction = implementation_constructor(defaultFunction, name, dispatch)
    
    def substitute(*arguments):
        return genericFunction(*arguments)
    
    substitute.method = genericFunction.method
    substitute.variadic_method = genericFunction.variadic_method
    substitute.super = genericFunction.super
    substitute.implementation = genericFunction
    if defaultFunction is not None:
        substitute.__name__ = defaultFunction.__name__
        substitute.__doc__ = defaultFunction.__doc__
        substitute.__module__ = defaultFunction.__module__
        substitute.__qualname__ = defaultFunction.__qualname__
    else:
        if name is not None:
            substitute.__name__ = substitute.__qualname__ = name
            try:
                substitute.__module__ = (
                    sys._getframe(4).f_globals['__name__'])
            except KeyError:
                # Might happen during doctests
                substitute.__module__ = '<unknown module>'
        if doc is not None:
            substitute.__doc__ = doc
    genericFunction.substitute = substitute
    return substitute

def method():
    """Automatically call the `method´ method of a generic function.

    This function is intended to be used as a decorator.
    """
    
    def helper(function):
        return find_generic(function).method()(function)
            
    return helper

def variadic_method():
    """Automatically call the `variadic_method´ method of a generic function.

    This function is intended to be used as a decorator.
    """
    
    def helper(function):
        return find_generic(function).variadic_method()(function)
            
    return helper


class SelfInstallingGenericFunction(GenericFunction):
    """I am a generic function that installs itself
       as special method if a new method is registered."""

    def register_func(self, types, func, variadic):
        super().register_func(types, func, variadic)
        try: 
            first_type = types[0]
        except IndexError:
            pass
        else:
            if isinstance(first_type, type):
                assert self.name is not None
                existing_special_method = getattr(first_type, self.name, False)
                if existing_special_method != self.substitute:
                    try:
                        setattr(first_type, self.name, self.substitute)
                    except TypeError:
                        pass


@_generic
def find_generic(someObject):
    """Find the generic function for some function with the same name,
    """
    raise NotImplementedError(
            "Can't find the generic function for %s" % type(someObject))


@find_generic.method()
def find_generic(function: FunctionType):
    #d#import pdb; pdb.set_trace()
    name = function.__name__
    try:
        return function.__globals__[name]
    except KeyError:
        raise TypeError(
                "Can't find a generic function for method named %s" %
                    function.__name__)
    

generic = _generic(name="generic")

@method()
def generic(default_function: FunctionType):
    return _generic(default_function)

@method()
def generic(default_function: BuiltinFunctionType):
    return _generic(default_function)

@method()
def generic(newstyle_class: type):
    return _generic(newstyle_class)

@method()
def generic(default_function: FunctionType, dispatch: Dispatch):
    return _generic(default_function, dispatch=dispatch)

@method()
def generic(default_function: BuiltinFunctionType, dispatch: Dispatch):
    return _generic(default_function, dispatch=dispatch)

@method()
def generic(newstyle_class: type, dispatch: Dispatch):
    return _generic(newstyle_class, dispatch=dispatch)

@method()
def generic():
    return _generic()

@method()
def generic(dispatch: Dispatch):
    return _generic(dispatch=dispatch)

@method()
def generic(function_name: str):
    return _generic(name=function_name)

@method()
def generic(function_name: str, dispatch: Dispatch):
    return _generic(name=function_name, dispatch=dispatch)

@method()
def generic(function_name: str, doc: str):
    return _generic(name=function_name, doc=doc)

@method()
def generic(function_name: str, doc: str, dispatch: Dispatch):
    return _generic(name=function_name, doc=doc, dispatch=dispatch)


self_installing_generic = _generic(name="self_installing_generic")

@method()
def self_installing_generic(default_function: FunctionType):
    answer = _generic(default_function, 
                      implementation_constructor=SelfInstallingGenericFunction)
    return answer

@method()
def self_installing_generic(default_function: BuiltinFunctionType):
    return _generic(default_function, 
                    implementation_constructor=SelfInstallingGenericFunction)
@method()
def self_installing_generic(
        default_function: BuiltinFunctionType,
        function_name: str):
    return _generic(default_function,
                    name=function_name,
                    implementation_constructor=SelfInstallingGenericFunction)
@method()
def self_installing_generic(
        default_function: FunctionType,
        function_name: str):
    return _generic(default_function,
                    name=function_name,
                    implementation_constructor=SelfInstallingGenericFunction)

@method()
def self_installing_generic(newstyle_class: type):
    return _generic(newstyle_class, 
                    implementation_constructor=SelfInstallingGenericFunction)

@method()
def self_installing_generic(default_function: FunctionType, dispatch: Dispatch):
    return _generic(default_function, dispatch=dispatch, 
                    implementation_constructor=SelfInstallingGenericFunction)

@method()
def self_installing_generic(
        default_function: BuiltinFunctionType,
        dispatch: Dispatch):
    return _generic(default_function, dispatch=dispatch, 
                    implementation_constructor=SelfInstallingGenericFunction)

@method()
def self_installing_generic(newstyle_class: type, dispatch: Dispatch):
    return _generic(newstyle_class, dispatch=dispatch, 
                    implementation_constructor=SelfInstallingGenericFunction)

@method()
def self_installing_generic(function_name: str):
    return _generic(name=function_name, 
                    implementation_constructor=SelfInstallingGenericFunction)

@method()
def self_installing_generic(function_name: str, dispatch: Dispatch):
    return _generic(name=function_name, dispatch=dispatch, 
                    implementation_constructor=SelfInstallingGenericFunction)

@method()
def self_installing_generic(function_name: str, doc: str):
    return _generic(name=function_name, doc=doc, 
                    implementation_constructor=SelfInstallingGenericFunction)

@method()
def self_installing_generic(function_name: str, doc: str, dispatch: Dispatch):
    return _generic(name=function_name, doc=doc, dispatch=dispatch, 
                    implementation_constructor=SelfInstallingGenericFunction)


isgeneric = generic(
    "isgeneric",
    """Answer ``True`` when the object is a generic function.""")

@method()
def isgeneric(some_object):
    return False

@method()
def isgeneric(implementation: GenericFunction):
    return True

@method()
def isgeneric(function: FunctionType):
    try:
        implementation = function.implementation
    except AttributeError:
        return False
    else:
        return isgeneric(implementation)


def get_implementation(a_generic):
    """Answer the implementation of a generic."""
    if isgeneric(a_generic):
        return a_generic.implementation
    else:
        raise TypeError("Need a generic")


merge = generic(
    "merge",
    """Merge two generics into a third one and answer it.""")

@method()
def merge(generic0: GenericFunction, generic1: GenericFunction):
    return generic0.merged(generic1)

@method()
def merge(generic0: FunctionType, generic1: FunctionType):
    return merge(get_implementation(generic0), get_implementation(generic1))

@method()
def merge(generic0: FunctionType, generic1: GenericFunction):
    return merge(get_implementation(generic0), generic1)

@method()
def merge(generic0: GenericFunction, generic1: FunctionType):
    return merge(generic0, get_implementation(generic1))


def basic_hash(an_object):
    return an_object.__hash__()
        

gf_hash = self_installing_generic(basic_hash, '__hash__')
