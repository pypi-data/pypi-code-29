from typing import Type, List
from collections import defaultdict

from .exceptions import ServiceNotRegistered
from .Factory import Factory
from .Registration import Registration
from .typing_helpers import is_list_type, get_inner_type


class Container:
    def __init__(self, registrations: List[Registration]):
        self._services = defaultdict(list)
        self._register_self()
        self._analyze_registrations(registrations)


    def _register_self(self):
        def return_self() -> Container:
            return self

        factory = Factory(return_self)
        self._services[Container] = [factory]


    def _analyze_registrations(self, registrations: List[Registration]):
        for registration in registrations:
            for service in registration.services:
                self._services[service].append(registration.factory)



    def resolve(self, service: Type) -> object:
        """Returns demanded service with dependencies injected"""

        if is_list_type(service):
            service = get_inner_type(service)
            return self._resolve_all(service)
            
        return self._resolve_last_registered(service)


    def _resolve_all(self, service: Type) -> List[object]:
        return [constructor(self.resolve) for constructor in self._get_constructors(service)]


    def _resolve_last_registered(self, service: Type) -> object:
        constructor = self._get_constructors(service)[-1]
        return constructor(self.resolve)


    def _get_constructors(self, service: Type) -> List[Factory]:
        if service not in self._services:
            raise ServiceNotRegistered(f"service {service} has not been registered")
        return self._services[service]
