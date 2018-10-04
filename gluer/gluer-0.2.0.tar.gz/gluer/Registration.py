import inspect

from typing import Mapping, Type, Sequence, Callable

from .Factory import Factory

class Registration:
    """Represents a registration of an object factory and allows for its customization"""

    def __init__(self, factory: Factory):
        self.factory = factory
        self.services = list()

        self.As(factory.type)


    def As(self, *services: Type) -> 'Registration':
        """Declares this registration as providing specified services"""

        self.services.extend(services)

        return self

    def as_parents(self):
        """If registation is of a class (not just factory funcion) treat all base classes as services"""

        cls = self.factory.type
        parents = inspect.getmro(cls)
        parents = [p for p in parents if p is not object and p is not cls]
        for parent in parents:
            self.As(parent)


    def single_instance(self) -> 'Registration':
        """Given registration will be treated as a singleton"""

        self.factory.single_instance = True
        return self

