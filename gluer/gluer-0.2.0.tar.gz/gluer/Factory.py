import inspect

from typing import Callable, get_type_hints, Type, Any

from .exceptions import Unannotated



class Factory:
    """Wrapper for a factory function/class constructor"""

    def __init__(self, init: Callable):
        self.single_instance = False
        self.instance = None
        self.parameters = dict()
        self.type = None

        self.init = init

        self.analyze(init)


    def analyze(self, init: Callable):
        if inspect.isclass(init):
            self.analyze_type(init)
        else:
            self.analyze_factory(init)


    def analyze_type(self, type_: Type):
        self.type = type_
        self.init = type_

        self.analyze_parameters(type_.__init__)


    def analyze_factory(self, factory: Callable):
        self.init = factory

        annotations = get_type_hints(factory)
        if "return" not in annotations:
            raise Unannotated(f"Factory {factory} has an unannotated return type")
        self.type = annotations["return"]

        self.analyze_parameters(factory)


    def analyze_parameters(self, factory: Callable):
        parameters = inspect.signature(factory).parameters
        annotations = get_type_hints(factory)

        for name, parameter in parameters.items():
            if name == "self":
                continue
            if parameter.kind in [parameter.VAR_POSITIONAL, parameter.VAR_KEYWORD]: #*args and **kwargs
                continue
            if parameter.default is not inspect._empty:
                continue
            if name not in annotations:
                raise Unannotated(f"Factory {factory} has an unannotated, not default parameter: {name}")

            self.parameters[name] = annotations[name]


    def __call__(self, container: Callable[[Type], Any]):
        if self.instance is not None:
            return self.instance

        parameters = self.resolve_parameters(container)
        instance = self.init(**parameters)

        if self.single_instance:
            self.instance = instance

        return instance


    def resolve_parameters(self, resolver: Callable[[Type], Any]):
        resolved = dict()
        for name, cls in self.parameters.items():
            resolved[name] = resolver(cls)
        return resolved

