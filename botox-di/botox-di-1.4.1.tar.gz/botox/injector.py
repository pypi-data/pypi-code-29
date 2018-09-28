from abc import ABCMeta
from types import LambdaType, FunctionType, MethodType
from typing import TypeVar, Type, List, Any, Callable, Dict, Optional

__all__ = [
    'Injector',
    'DependencyInjectionError',
    'PreparationError',
    'DeliveryError'
]

T = TypeVar('T')

Token = Type[T]


class DependencyInjectionError(Exception):
    pass


class PreparationError(DependencyInjectionError):
    pass


class DeliveryError(DependencyInjectionError):
    pass


class Injection(metaclass=ABCMeta):

    @property
    def ingredients(self) -> List[Token]:
        """
        A list of `DependencyToken`s which need to be resolved by the `Injector` before deliver.
        """
        raise NotImplementedError()

    def deliver(self, dependencies: List) -> Any:
        raise NotImplementedError()


class ValueInjection(Injection):
    """
    Configures the `Injector` to return a value for a dependency token.
    """

    def __init__(self, value: Any):
        self._value = value

    @property
    def ingredients(self) -> List[Token]:
        return []

    def deliver(self, dependencies: List) -> Any:
        return self._value


class ClassInjection(Injection):
    """
    Configures the `Injector` to return an instance of `useClass` for a dependency token.
    """

    def __init__(self, _class: Type):
        self._class = _class

    @property
    def ingredients(self) -> List[Token]:
        init_function = self._class.__init__
        if init_function is object.__init__:
            return []
        else:
            references = init_function.__annotations__.items()
            tokens = [token for name, token in references if name != 'return']
            return tokens

    def deliver(self, dependencies: List) -> Any:
        return self._class(*dependencies)


class LambdaInjection(Injection):
    """
    Configures the `Injector` to return a dependency by invoking lambda.
    """

    def __init__(self, _lambda: LambdaType):
        self._lambda = _lambda

    @property
    def ingredients(self) -> List[Token]:
        return []

    def deliver(self, dependencies: List) -> Any:
        return self._lambda()


class FunctionInjection(Injection):
    """
    Configures the `Injector` to return a dependency by invoking function or bound method.
    """

    def __init__(self, function: Callable):
        self._function = function

    @property
    def ingredients(self) -> List[Token]:
        references = self._function.__annotations__.items()
        tokens = [token for name, token in references if name != 'return']
        return tokens

    def deliver(self, dependencies: List) -> Any:
        return self._function(*dependencies)


class Injector:

    def __init__(self):
        self._injections: Dict[Token, Injection] = {}

    def prepare(self, token: Token, value: Any = None) -> None:
        if isinstance(value, type):
            injection = ClassInjection(value)

        elif isinstance(value, FunctionType) and '<lambda>' in value.__name__:
            if value.__code__.co_argcount:
                raise PreparationError(
                    f'Unable to prepare token={token} injection, '
                    f'lambda has arguments'
                )
            injection = LambdaInjection(value)

        elif isinstance(value, MethodType):
            injection = FunctionInjection(value)

        elif isinstance(value, FunctionType):
            if value.__code__.co_argcount and not len(value.__annotations__):
                raise PreparationError(
                    f'Unable to prepare token={token} injection, '
                    f'function {value} has arguments but no annotations'
                )
            injection = FunctionInjection(value)

        elif value is None:
            injection = ClassInjection(token)

        else:
            injection = ValueInjection(value)

        self.prepare_injection(token, injection)

    def prepare_injection(self, token: Token, injection: Injection) -> None:
        if not isinstance(injection, Injection):
            raise PreparationError(
                f'Unable to prepare token={token} injection, '
                f'argument must be instance of Injection class'
            )
        self._injections[token] = injection

    def deliver(self, token: Token, strict=True) -> Optional[T]:
        """
        :param token: Dependency class used as token.
        :param strict: Strict mode eliminates dependency configuration silent errors by changing them to exceptions.
        :return: An instance of dependency based on the specified 'token'.
        """
        injection = self._injections.get(token, None)
        if injection is None:
            if strict:
                raise DeliveryError(
                    f'Dependency injection token={token} not configured,'
                    f'try Injector.prepare before deliver'
                )
            return None

        dependencies = [self.deliver(token, strict) for token in injection.ingredients]
        return injection.deliver(dependencies)

    def create(self) -> 'Injector':
        """
        Creates a new Injector which contains all prepared injections.
        Can be used to organize dependency scopes.
        """
        injector = Injector()
        injector._injections = self._injections.copy()
        return injector
