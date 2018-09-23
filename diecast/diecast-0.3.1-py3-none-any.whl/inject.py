# -*- coding: utf-8 -*-

import inspect
import logging
from functools import wraps
from inspect import Parameter
from typing import Any, Callable, List, Mapping, Type, get_type_hints

from diecast.types import Injector

_log = logging.getLogger(__name__)


def _not_injectable(registry: "ComponentRegistry", hint: Type) -> bool:

    return hint == Any or hint not in registry or hint is Parameter.empty


def build_arg_mapping(fn: Callable) -> Mapping[str, Any]:
    """ Builds a dictionary mapping of argument names to
        the corresponding type annotations from the function.

        Only returns a mapping of function arguments, eliding over the
        return type annotation provided by `get_type_hints`. Updates
        the type hint for arguments without type annotations to be
        `typing.Any`.
    """

    hints = get_type_hints(fn)
    if "return" in hints:
        hints.pop("return")

    arg_names = fn.__code__.co_varnames[: fn.__code__.co_argcount]
    for arg in arg_names:
        if arg not in hints:
            hints.update({arg: Any})

    return hints


def build_passthru_args(registry: "ComponentRegistry", fn: Callable) -> List[str]:
    """ Builds and returns a list of arguments (their names) that will be
        passed through when the injected function `fn` is called.
    """

    args = []

    sig = inspect.signature(fn)
    fn_params = {parm.name: parm.annotation for name, parm in sig.parameters.items()}

    for arg, hint in fn_params.items():
        if _not_injectable(registry, hint):
            # This is not an injectable argument
            args.append(arg)

    return args


def map_passthru_args(passthru_args: List[str], *args, **kw) -> Mapping[str, Any]:
    """ Builds a mapping of passthrough args to their values.
        Only maps passed through args into `**kw` that will be
        passed into the function.
    """

    arg_map = {}

    # If `*args` or `*kw` contain an ellipses, drop that entry
    args = list(filter(lambda item: item is not ..., args))
    kw = dict(filter(lambda _, val: val is not ..., kw))

    # Apply *args in order
    for name, val in zip(passthru_args, args):
        arg_map.update({name: val})

    for name, val in kw.items():
        if name in passthru_args:
            if name in arg_map:
                raise ValueError(f"Passthru arg {name} mapped through *args and **kw")

            arg_map.update({name: val})

    return arg_map


def make_injector(registry: "ComponentRegistry") -> Injector:
    """ This is just a "magical" function that returns a decorator that
        has been bound to a registry.

        `registry` is closured in to `_arg_injector`.
    """

    def _injector(fn: Callable):
        @wraps(fn)
        def _arg_injector(*args, **kw):

            sig_params = _do_inject(registry, fn, *args, **kw)
            return _call_with_bound_params(fn, sig_params)

        return _arg_injector

    return _injector


def _do_inject(
    _registry: "ComponentRegistry", _fn: Callable, *args, **kw
) -> inspect.BoundArguments:
    """ Given a `_registry`, `_fn` to inject, as well as the arguments
        to be passed to `_fn`, creates an `inspect.Signature` for the
        function. We then bind all injected and passthrough arguments to
        the `inspect.Signature` using `sig.bind_partial`.

        Funnily enough, this does not *actually* bind the function itself,
        or even execute the function.
    """

    _log.debug(f"Performing injection for {_fn} with {_registry}")

    sig = inspect.signature(_fn)

    arg_map = build_arg_mapping(_fn)
    injected_params = {}

    for arg, hint in arg_map.items():
        if _not_injectable(_registry, hint):
            continue

        dep = _registry.get(hint)

        if dep["instance"] is None:
            # Initialize dependency - should also perform DI on this!
            _log.debug(f"Initialize dependency for injection {dep}")

            injected_params.update({arg: _registry[hint]})
        else:
            injected_params.update({arg: dep.get("instance")})

    passthru_args = build_passthru_args(_registry, _fn)
    passthru_params = map_passthru_args(passthru_args, *args, **kw)

    params = dict(injected_params)
    params.update(passthru_params)

    return sig.bind_partial(**params)


def _call_with_bound_params(fn: Callable, sig_params: inspect.BoundArguments) -> Any:
    """ Uses a Signature's BoundArguments to execute the
        underlying function.
    """

    return fn(*sig_params.args, **sig_params.kwargs)
