"""Порт contextlib из python 3.7 и сахар."""

from typing import cast, Any, Type, TypeVar, Iterable, Mapping, Callable
import asyncio
import sys
import warnings

try:
    from contextlib import (  # type: ignore
        AbstractAsyncContextManager as _stdlib_AbstractAsyncContextManager,
        asynccontextmanager as _stdlib_asynccontextmanager,
        AsyncExitStack
    )
except ImportError:
    from .async_contextlib import (
        AbstractAsyncContextManager as _stdlib_AbstractAsyncContextManager,
        asynccontextmanager as _stdlib_asynccontextmanager,
        AsyncExitStack
    )


__all__ = ['AbstractAsyncContextManager', 'asynccontextmanager', 'AsyncExitStack']
"""Публичное АПИ `async_contextlib`."""


_AsyncContextManager = TypeVar('_AsyncContextManager', bound=_stdlib_AbstractAsyncContextManager)
"""Переменная типа ограниченная контекст менеджерами."""


class ShieldContextManagerCleanupFail(UserWarning):
    """Предупреждение о том, что невозможно завершить уборку: __aexit__ не будет выполнен."""


class ShieldContextManager(_stdlib_AbstractAsyncContextManager):
    """Класс, который оборачивает родительские `__aenter__` и `__aexit__` в `asyncio.shield`.

    Текущее поведение для `__aenter__`:
        * родительский `__aenter__` запускается в отдельном таске `task`
        * ожиданием `task` оборачивая его в `asyncio.shield`
          * `CancelledError` не должны протекать внутрь
            родительского `__aenter__` при отмене нашего `__aenter__`
        * если наш `__aenter__` отменен, то запускаем процедуру уборки за
          контекст менеджером (в отдельном таске обернутым в `asyncio.shield`):
          * дожидаемся завершения `task` родительского `__aenter__`:
            * если во время ожидания произошла отмента, то выбрасываем предупреждение
              `ShieldContextManagerCleanupFail`: невозможно завершить уборку за
               контекст менеджером
            * иначе запускаем `__aexit__`

    Текущее поведение для `__aexit__`:
        * ожидаем родительский `__aenter__` оборачивая его в `asyncio.shield`
    """

    async def __cleanup(
        self,
        task: asyncio.Task,
        aexit_args: Iterable[Any] = tuple(),
        aexit_kwargs: Mapping[str, Any] = dict()
    ) -> None:
        """Уборка за контекст менеджером.

        Алгоритм:
            * дожидаемся завершения `task` родительского `__aenter__`:
                * если во время ожидания произошла отмента, то выбрасываем предупреждение
                  `ShieldContextManagerCleanupFail`: невозможно завершить уборку за
                  контекст менеджером
                * иначе запускаем `__aexit__`

        :param task: таск в котором выполняется родительский `__aenter__`
        :param aexit_args: аргументы, будут переданны в `__aexit__`
        :param aexit_kwargs: кваргументы, будут переданны в `__aexit__`
        """
        try:
            # оборачиваем в `asyncio.shield` чтобы не отменить родительский `__aenter__` если отменят нас
            await asyncio.shield(task)
        except asyncio.CancelledError:  # нас отменили или `task` отменен
            warnings.warn(
                'Невозможно дождаться завершения  __aenter__ '
                '(вероятно он был отменен или уборка была отменена). ' +
                ' __aexit__ не будет вызван.',
                category=ShieldContextManagerCleanupFail
            )
            raise
        else:
            await self.__aexit__(*aexit_args, **aexit_kwargs)

    async def __aenter__(self) -> Any:
        """Вход в контекст менеджер.

        Алгоритм:
            * родительский `__aenter__` запускается в отдельном таске `task`
            * ожиданием `task` оборачивая его в `asyncio.shield`
              * `CancelledError` не должны протекать внутрь
                родительского `__aenter__` при отмене нашего `__aenter__`
            * если наш `__aenter__` отменен, то запускаем процедуру уборки за
              контекст менеджером (в отдельном таске обернутым в `asyncio.shield`)

        :return: результат родительского `__aenter__`
        """
        # создаем отдельный таск чтобы иметь возможность передать его в процедуру уборки
        task: asyncio.Task = asyncio.get_event_loop().create_task(
            super().__aenter__()
        )
        try:
            # оборачиваем в `asyncio.shield` чтобы не отменить родительский `__aenter__` если отменят нас
            return await asyncio.shield(task)
        except asyncio.CancelledError:
            await self.__cleanup(task, aexit_args=sys.exc_info())
            raise

    async def __aexit__(self, *args: Any, **kwargs: Any) -> Any:
        """Выход из контекст менеджера.

        Ожидаем родительский `__aenter__` оборачивая его в `asyncio.shield`.

        :param args: аргументы, будут переданны в родительский `__aexit__`
        :param kwargs: кваргументы, будут переданны в родительский `__aexit__`
        :return: результат родительского `__aexit__`
        """
        return await asyncio.shield(
            super().__aexit__(*args, **kwargs)
        )


class AbstractAsyncContextManager(_stdlib_AbstractAsyncContextManager):
    """Абстрактный класс контекст менеджеров.

    При наследовании от этого класса результирующий класс во время
    создания инстанса вместо инстанса дочернего класса возвращает
    инстанс нового класса в который подмешан `ShieldContextManager`
    через множественное наследование.
    """

    def __new__(
        cls: Type[_AsyncContextManager],
        *args: Any,
        **kwargs: Any
    ) -> _AsyncContextManager:
        """Получить инстанс дочернего класса с подмешанным ShieldContextManager.

        :param args: аргументы, игнорируются
        :param kwargs: кваргументы, игнорируются
        """
        return cast(
            _AsyncContextManager,
            super().__new__(
                type(
                    cls.__name__,
                    (ShieldContextManager, cls),
                    dict(
                        __doc__=cls.__doc__
                    )
                )
            )
        )


def asynccontextmanager(function: Callable) -> Type[AbstractAsyncContextManager]:
    """Превращаем итератор в контекст менеджер.

    Полученный контекст менеджер будет унаследован от `AbstractAsyncContextManager`.

    :param function: функция, которая возвращает итератор
    :return: контекст менеджер
    """
    class AsyncContextManager(AbstractAsyncContextManager):
        """Класс оборачивающий контекст менеджер созданный `async_contextlib`."""

        def __init__(self, *args: Any, **kwargs: Any) -> None:
            """Инициализация.

            Создаем инстанс контекст менеджера из функции `function`
            (полученной замыканием) возвращающей итератор.

            :param args: аргументы, передаются в `function`
            :param kwargs: кваргументы, передаются в `function`
            """
            super().__init__()
            self.__stdlib_asynccontextmanager = _stdlib_asynccontextmanager(function)(*args, **kwargs)

        async def __aenter__(self) -> Any:
            """Вход в контекст менеджер.

            Дожидается входа в обернутый.
            """
            return await self.__stdlib_asynccontextmanager.__aenter__()

        async def __aexit__(self, *args: Any, **kwargs: Any) -> Any:
            """Выход из контекст менеджера.

            :param args: аргументы, будут переданны в `__aexit__` обернутого контекст менеджера
            :param kwargs: кваргументы, будут переданны в `__aexit__` обернутого контекст менеджера
            :return: результат `__aexit__` обернутого контекст менеджера
            """
            return await self.__stdlib_asynccontextmanager.__aexit__(*args, **kwargs)

    return type(
        function.__name__,
        (AsyncContextManager, ),
        dict(
            __doc__=function.__doc__
        )
    )
