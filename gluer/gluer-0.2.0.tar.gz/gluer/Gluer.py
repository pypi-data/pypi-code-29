from typing import get_type_hints, Type, Sequence, Union, Callable, Dict, List
from collections import defaultdict

from .exceptions import ServiceNotRegistered
from .Factory import Factory
from .Registration import Registration
from .typing_helpers import is_list_type, get_inner_type
from .container import Container


class Gluer:
    def __init__(self):
        self.registrations = list()


    def register(self, factory: Union[Type, Callable]) -> Registration:
        """Registers type as a set of given services"""

        factory = Factory(factory)
        registration = Registration(factory)
        self.registrations.append(registration)

        return registration


    def register_instance(self, instance: object, cls: Type = None) -> Registration:
        """Registers instance. Optionally as a given class"""
        if cls is None:
            cls = type(instance)

        def factory() -> cls:
            return instance

        self.register(factory)

    
    def build(self) -> Container:
        container = Container(self.registrations)
        return container



