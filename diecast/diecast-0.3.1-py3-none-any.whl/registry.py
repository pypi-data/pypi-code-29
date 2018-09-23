# -*- coding: utf-8 -*-

from typing import (
    Callable,
    Dict,
    Optional,
    Type,
)

from diecast.component import Component
from diecast.inject import _call_with_bound_params, _do_inject
from diecast.types import ComponentState


class ComponentRegistry(object):

    def __init__(self):

        self._components: Dict[Type[Component], ComponentState] = {}

    def __getitem__(self, cls: Type[Component]) -> Component:
        ''' Returns a component instance or creates a new component
            instance.
        '''

        component = self.get(cls)
        instance = component.get('instance')
        if not instance:
            return self._init_component(component.get('init'))
        else:
            return instance

    def __contains__(self, cls: Type[Component]) -> bool:
        ''' Returns whether or not this registry contains
            component `cls`.
        '''

        return cls in self._components

    def _init_component(self, init: Callable[..., Component]) -> Component:

        if not init:
            return None

        sig_params = _do_inject(self, init)
        return _call_with_bound_params(init, sig_params)

    def get(self, cls: Type[Component]) -> ComponentState:
        ''' Returns ComponentState for a Component.
        '''

        return self._components.get(cls)

    def add(self,
            cls: Type[Component],
            init: Optional[Callable[..., Component]]=None,
            persist: bool=True):
        ''' Add a component to this component registry.

            `cls` is the class that will be registered in the registry.

            `init` is the Callable that will provide an instance of `cls` for injection.
                Before `init` is called, dependency injection is performed on the function.

            `persist` specifies that the created instance should be stored in the registry.
        '''

        if not init:
            init = cls.init

        instance = None

        if persist:
            # This should perform DI on the `init` callable to
            # instantiate the Component
            instance = self._init_component(init)

        self._components.update({
            cls: ComponentState({
                'init': init,
                'persist': persist,
                'instance': instance,
            }),
        })


__components: ComponentRegistry = ComponentRegistry()


def get_registry() -> ComponentRegistry:
    ''' Returns the default global registry.
    '''

    global __components
    return __components


def register_component(cls: Type[Component],
                       init: Optional[Callable[..., Component]]=None,
                       persist: bool=True,
                       registry: ComponentRegistry=None):
    ''' Register a component with the dependency injection system.

        `cls` is the class that will be registered in the registry.

        `init` is the Callable that will provide an instance of `cls` for injection.
            Before `init` is called, dependency injection is performed on the function.

        `persist` specifies that the created instance should be stored in the registry.

        `registry` is the `ComponentRegistry` instance that the component will be registered with.
            If `None`, will use the default global registry.
    '''

    if registry is None:
        global __components
        registry = __components

    assert cls not in registry

    return registry.add(
        cls=cls,
        init=init,
        persist=persist,
    )
