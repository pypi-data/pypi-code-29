from __future__ import annotations
import re
from collections import Counter
from copy import deepcopy as dcopy
from string import punctuation
from typing import Callable, Iterable, Collection, List

from .utils import DotDict


__all__ = 'DF', 'InnerObject', 'ColumnsEditor', 'Table', 'Table'


class DF:
    """DefaultFunctions"""
    __slots__ = ()

    # noinspection PyUnusedLocal
    @staticmethod
    def const(old, new):
        return old

    # noinspection PyUnusedLocal
    @staticmethod
    def var(old, new):
        return new

    @staticmethod
    def greater(old, new):
        try:
            return old if new > new else old
        except TypeError:
            return new

    @staticmethod
    def less(old, new):
        try:
            return old if old < new else new
        except TypeError:
            return new


class InnerObject:
    __slots__ = '_pos', '_columns'

    def __init__(self, pos, columns):
        self._pos = pos
        self._columns = columns

    def __getitem__(self, key):
        return self._pos[self._columns.index(key)]

    def __setitem__(self, key, value):
        self._pos[self._columns.index(key)] = value

    def __getattr__(self, key):
        return self[key]

    def __setattr__(self, key, value):
        if key in self.__class__.__slots__:
            super().__setattr__(key, value)
        else:
            self[key] = value

    def __str__(self):
        s = '{'
        for key, value in zip(self._columns, self._pos):
            s += f'{key}: {value}, '
        return s + '}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self._pos}, {self._columns})'

    def to_dict(self):
        return {c: v for c, v in zip(self._pos, self._columns)}

    def keys(self):
        return self._columns

    def values(self):
        return self._pos

    def items(self):
        return zip(self._columns, self._pos)


class ColumnsEditor:
    __slots__ = '_parent'

    def __init__(self, parent: Table):
        self._parent = parent

    def rename(self, dct=None, **columns):
        if dct is not None:
            columns = {**dct, **columns}
        for column in columns:
            i = self._parent._columns.index(column)
            self._parent._columns[i] = columns[column]
            if column in self._parent._keys:
                i = self._parent._keys.index(column)
                self._parent._keys[i] = columns[column]

    def set(self, *columns, lst=None):
        if lst is not None:
            lst = list(lst)
            columns = list(columns) + [c for c in lst if c not in columns]
        assert columns

        key_inds = []
        added_inds = []
        for column in columns:
            if column in self._parent._columns:
                i1 = columns.index(column)
                i2 = self._parent._columns.index(column)
                key_inds.append((i1, i2))
            else:
                added_inds.append(columns.index(column))
        deleted_inds = [self._parent._columns.index(c) for c in self._parent._columns if c not in columns]

        for pos in self._parent._items:
            old_pos = pos.copy()
            for i in reversed(deleted_inds):
                pos.pop(i)
            for i in added_inds:
                pos.insert(i, None)
            for i1, i2 in key_inds:
                pos[i1] = old_pos[i2]
        self._parent._columns = columns
        for key in self._parent._keys:
            if key not in self._parent._columns:
                self._parent._keys.remove(key)
        for i in reversed(deleted_inds):
            self._parent._funcs.pop(i)
        for i in added_inds:
            self._parent._funcs.insert(i, DF.const)

    def add(self, *columns, clmns=None, funcs=None, dct=None, **clmns_funcs):
        if clmns is not None:
            clmns = list(clmns)
            columns = list(columns) + [c for c in clmns if c not in columns]
        if funcs is not None:
            funcs = list(funcs)
            assert len(funcs) == len(columns)
        else:
            funcs = [DF.const for _ in columns]
        if dct is not None:
            assert all((type(k) is str and callable(v) for k, v in dct.items()))
            clmns_funcs = {**dct, **clmns_funcs}
        assert all((callable(v) for v in clmns_funcs.values()))
        clmns_funcs = {**dict(zip(columns, funcs)), **clmns_funcs}
        clmns_funcs = {c: f for c, f in clmns_funcs.items() if c not in self._parent._columns}

        for pos in self._parent._items:
            for _ in clmns_funcs.keys():
                pos.append(None)
        self._parent._columns += list(clmns_funcs.keys())
        self._parent._funcs += list(clmns_funcs.values())

    def append(self, column, func=DF.const, value=None, value_generator: Callable=None):
        if column not in self._parent._columns:
            self._parent._columns.append(column)
            self._parent._funcs.append(func)

            if value_generator is not None:
                for i, pos in enumerate(self._parent._items):
                    pos = {k: v for k, v in zip(self._parent._columns, pos)}
                    new_value = value_generator(pos)
                    self._parent._items[i].append(new_value)
            else:
                for pos in self._parent._items:
                    pos.append(value)

    def insert(self, ind, column, func=DF.const, default=None):
        self._parent._columns.insert(ind, column)
        self._parent._funcs.insert(ind, func)
        for pos in self._parent._items:
            pos.append(default)

    def pop(self, index):
        column_name = self._parent._columns[index]
        self._parent._columns.pop(index)
        self._parent._funcs.pop(index)
        if column_name in self._parent._keys:
            self._parent._keys.remove(column_name)
        for pos in self._parent._items:
            pos.pop(index)

    def remove(self, column):
        index = self._parent._columns.index(column)
        self._parent._columns.pop(index)
        self._parent._funcs.pop(index)
        if column in self._parent._keys:
            self._parent._keys.remove(column)
        for pos in self._parent._items:
            pos.pop(index)

    def index(self, column):
        return self._parent._columns.index(column)

    def __getitem__(self, ind):
        return self._parent._columns[ind]

    def __setitem__(self, ind, value):
        if self._parent._columns[ind] in self._parent._keys:
            self._parent._keys[self._parent._keys.index(self._parent._columns[ind])] = value
        self._parent._columns[ind] = value

    def __delitem__(self, index):
        self.pop(index)

    def __str__(self):
        return str(self._parent._columns)

    def __repr__(self):
        return f'{self.__class__.__name__}({repr(self._parent)})'

    def __len__(self):
        return len(self._parent._columns)

    def __iter__(self):
        return iter(self._parent._columns)

    def __add__(self, other):
        other = list(other)
        return (
                self._parent._columns +
                [c for c in other if c not in self._parent._columns]
        )

    def __iadd__(self, other):
        other = list(other)
        columns = (
                self._parent._columns +
                [c for c in other if c not in self._parent._columns]
        )
        self.add(clmns=columns)
        return self._parent._columns

    def __and__(self, other):
        other = list(other)
        return (c for c in other if c in self._parent._columns)

    def __iand__(self, other):
        other = list(other)
        self.set((c for c in other if c in self._parent._columns))

    def __sub__(self, other):
        other = list(other)
        return (c for c in self._parent._columns if c not in other)

    def __isub__(self, other):
        other = list(other)
        self.set((c for c in self._parent._columns if c not in other))


class Table:
    __slots__ = ('_columns', '_funcs', '_keys', 'name', '_items')

    def __init__(self, columns: Iterable[str],
                 keys: Iterable[str]=None,
                 funcs: Iterable[Callable]=None,
                 name: str='no_name'):
        """
        Таблица представляет собой набор позиций(строк), каждая из которых
        содержит значения соответствующих столбцов таблицы.

        Позиции можно представить в виде словарей, где ключами являются
        имена столбцов, и каждому из них соответствует определенное значение
        позиции.

        Основное отличие этих таблиц в том, что в них можно установить
        ключевые столбцы, значения в которых определяют эквивалентность
        позиций. Это означает, что таблица не может содержать одновременно
        несколько позиций, значения всех ключевых столбцов в которых
        повторяются. Таким образом, если при добавлении в таблицу новой позиции
        в таблице присутствует позиция, эквивалентная добавляемой, то
        произойдет их слияние, а если эквивалентной позиции в таблице нет, то
        новая позиция просто будет добавлена в конец.

        :param columns: Имена столбцов таблицы
        :param keys: Имена ключевых столбцов таблицы. Значения ключевых столбцов таблицы
        :param funcs: Функции для слияния каждого из столбцов таблицы
        :param name: Имя таблицы, в основном полезно лишь для отладки
        """
        columns = list(columns)
        assert columns
        assert all((i == 1 for i in Counter(columns).values()))

        if keys is not None:
            keys = list(keys)
            assert all((c in columns for c in keys))
        else:
            keys = []
        if funcs is not None:
            funcs = list(funcs)
            assert len(funcs) == len(columns)
            assert all((callable(c) for c in funcs))
        else:
            funcs = [DF.const for _ in columns]

        self._columns = columns
        self._funcs = funcs
        self._keys = keys
        self.name = name
        self._items = []

    # ------------------------------------------------------------------------
    #   Background operations, preparers
    # ------------------------------------------------------------------------

    @staticmethod
    def _pos_adapt(pos, indices):
        """
        Адаптирует позицию таблицы other для вставки в self

        :param pos:
        :type pos:

        :param indices:
        :type indices:

        :return:
        :rtype: list
        """
        npos = [pos[i] if (type(i) is int) else i for i in indices]
        return npos

    @staticmethod
    def _pos_isequal(pos, pos2, key_indices):
        """
        Сравнивает две позиции
        :param pos:
        :param pos2:
        :param key_indices:
        :return:
        """
        for i1, i2 in key_indices:
            if pos[i1] != pos2[i2]:
                return False
        return True

    @staticmethod
    def _unpack_pos(pos):
        if isinstance(pos, dict):
            return pos.values(), pos.keys()
        elif isinstance(pos, InnerObject):
            return pos._InnerObject__pos, pos._InnerObject__columns
        else:
            raise TypeError(f'pos must be dict or InnerObject, not {type(pos)}')

    def _prepare_funcs(self, funcs):
        """
        Возвращает обновленный список функций таблицы

        :param funcs:
        :type funcs: Union[Iterable[str], dict, NoneType]

        :return: обновленный список функций таблицы
        :rtype: List[Callable]
        """
        if funcs is None:
            return dcopy(self._funcs)
        if isinstance(funcs, dict):
            new_funcs = dcopy(self._funcs)
            for column, func in funcs.items():
                if column in self._columns:
                    new_funcs[self._columns.index(column)] = func
                else:
                    raise KeyError(f'column {repr(column)} does not exists')
            return new_funcs
        elif isinstance(funcs, Collection):
            assert len(funcs) == len(self._columns)
            return funcs
        raise TypeError("parameter 'funcs' must be Collection")

    def _prepare_keys(self, keys):
        """
        Подготавливает список ключевых столбцов, используемый во внутренних функциях

        :param keys: ключевые столбцы
        :type keys: Iterable[str]

        :return: подгоиовленный список ключевых столбцов
        :rtype: List[str]
        """
        if keys is None:
            return self._keys
        return list(keys)

    def _new_columns(self, other, new):
        """

        :param other:
        :param new:
        :return:
        """
        new_columns_indices = []
        for column in other._columns:
            if column not in self._columns:
                new._columns.append(column)
                i = other._columns.index(column)
                new._funcs.append(other._funcs[i])
                new_columns_indices.append(i)
        return new_columns_indices

    def _key_indices(self, other_columns, keys):
        """
        Возвращает список из (i1, i2), где i1 - положение
        столбца в self, а i2 - положение столбца в other

        :param other_columns: столбцы второй таблицы
        :type other_columns: List[str]

        :param keys: названия столбцов, индексы которых нужно определить
        :type keys: List[str]

        :return: [(i1, i2), (i1, i2)]
        :rtype: List[Tuple[int, int]]
        """
        indices = []
        for key in keys:
            if key in self._columns and key in other_columns:
                i1 = self._columns.index(key)
                i2 = other_columns.index(key)
                indices.append((i1, i2))
        if not indices:
            raise ValueError('one of the tables haven\'t got all keys')
        return indices

    def _funcs_iter(self, other_columns, funcs):
        """

        :param other_columns:
        :param funcs:
        :return:
        """
        zip_ = []
        for column in self._columns:
            if column in other_columns:
                i1 = self._columns.index(column)
                i2 = other_columns.index(column)
                func = funcs[i1]
                zip_.append((i1, i2, func))
        return zip_

    # ------------------------------------------------------------------------
    #   Properties/setters
    # ------------------------------------------------------------------------

    @property
    def columns(self):
        """
        Возвращает объект, позволяющий редактировать
        столбцы таблицы, изменяя при этом ее содержимое.

        >>> t = Table(
        ...    ['1', '2', '3', '4'], ['1'],
        ...    [DF.const, DF.var, DF.var, DF.var]
        ...)
        >>> t.insert([1, 2, 3, 4])
        >>> t.columns.set(['3', '4', '1', 'new'])
        >>> t._items
        [[3, 4, 1, None]]
        :rtype: ColumnsEditor
        """
        return ColumnsEditor(self)

    @columns.setter
    def columns(self, value):
        """
        Устанавливает столбцы таблицы,
        изменяя при этом ее содержимое.

        >>> t = Table(
        ...    ['1', '2', '3', '4'], ['1'],
        ...    [DF.const, DF.var, DF.var, DF.var]
        ...)
        >>> t.insert([1, 2, 3, 4])
        >>> t.columns = ['3', '4', '1', 'new']
        >>> t._items
        [[3, 4, 1, None]]

        :param value: новые столбцы таблицы
        :type value: Iterable[Callable]
        """
        ColumnsEditor(self).set(lst=value)

    @property
    def funcs(self):
        """
        Возвращает список функций таблицы
        :rtype: List[Callable]
        """
        return self._funcs

    @funcs.setter
    def funcs(self, value):
        """
        Устанавливает функции для столбцов таблицы

        :type value: Iterable[Callable], dict
        """
        value = self._prepare_funcs(value)
        assert len(value) == len(self._funcs)
        self._funcs = value

    @property
    def keys(self):
        return self._keys

    # ------------------------------------------------------------------------
    #   Arithmetic operations
    # ------------------------------------------------------------------------

    def union(self, other, keys=None, funcs=None, replace=True,
              add_columns=True, add_positions=True):
        """
        Складывает две таблицы

        :param other: вторая таблица
        :type other: Table

        :param keys: ключевые столбцы, определяющие уникальность позиции
        :type keys: Iterable[str]

        :param funcs: функции столбцов, используемые при замещении
        :type funcs: Iterable[Callable], dict

        :param replace: стоит ли замещать значения позиций первой таблицы
        :type replace: bool

        :param add_columns: стоит ли добавлять в таблицу столбцы второй таблицы
        :type add_columns: bool

        :param add_positions: стоит ли добавлять новые позиции из второй таблицы
        :type add_positions: bool

        :return: новая таблица
        :rtype: Table
        """
        keys = self._prepare_keys(keys)
        funcs = self._prepare_funcs(funcs)
        new = self.clone(copyitems=True)

        key_indices = self._key_indices(other._columns, keys)
        funcs_iter = new._funcs_iter(other._columns, funcs)
        new_columns_indices = self._new_columns(other, new) if add_columns else []
        adapt_inds = [other._columns.index(column) if column in other._columns else None
                      for column in new._columns]
        len_new_columns = len(new_columns_indices)

        columns_added = False
        for npos in other._items:
            replaced = False
            for pos in new._items:
                if self._pos_isequal(pos, npos, key_indices):
                    if add_columns:
                        if columns_added:
                            pos[-len_new_columns:] = (npos[i] for i in new_columns_indices)
                        else:
                            for i in new_columns_indices:
                                pos.append(npos[i])
                    if replace:
                        for i1, i2, func in funcs_iter:
                            pos[i1] = func(pos[i1], npos[i2])
                    replaced = True
                    if columns_added:
                        break
                elif add_columns and not columns_added:
                    for _ in new_columns_indices:
                        pos.append(None)
            columns_added = True
            if add_positions and not replaced:
                new_pos = new._pos_adapt(npos, adapt_inds)
                new._items.append(new_pos)
        return new

    def update(self, other, keys=None, funcs=None, replace=True,
               add_columns=True, add_positions=True):
        """
        Складывает две таблицы, изменяя при этом self

        :param other: вторая таблица
        :type other: Table

        :param keys: ключевые столбцы, определяющие уникальность позиции
        :type keys: Iterable[str]

        :param funcs: функции столбцов, используемые при замещении
        :type funcs: Iterable[Callable], dict

        :param replace: стоит ли замещать значения позиций первой таблицы
        :type replace: bool

        :param add_columns: стоит ли добавлять в таблицу столбцы второй таблицы
        :type add_columns: bool

        :param add_positions: стоит ли добавлять новые позиции из второй таблицы
        :type add_positions: bool
        """
        keys = self._prepare_keys(keys)
        funcs = self._prepare_funcs(funcs)

        key_indices = self._key_indices(other._columns, keys)
        funcs_iter = self._funcs_iter(other._columns, funcs)
        new_columns_indices = self._new_columns(other, self) if add_columns else []
        adapt_inds = [other._columns.index(column) if column in other._columns else None
                      for column in self._columns]
        len_new_columns = len(new_columns_indices)

        columns_added = False
        for npos in other._items:
            replaced = False
            for pos in self._items:
                if self._pos_isequal(pos, npos, key_indices):
                    if add_columns:
                        if columns_added:
                            pos[-len_new_columns:] = (npos[i] for i in new_columns_indices)
                        else:
                            for i in new_columns_indices:
                                pos.append(npos[i])
                    if replace:
                        for i1, i2, func in funcs_iter:
                            pos[i1] = func(pos[i1], npos[i2])
                    replaced = True
                    if columns_added:
                        break
                elif add_columns and not columns_added:
                    for _ in new_columns_indices:
                        pos.append(None)
            columns_added = True
            if add_positions and not replaced:
                new_pos = self._pos_adapt(npos, adapt_inds)
                self._items.append(new_pos)

    def diff(self, other, keys=None):
        """
        Вычитает из одной таблицы другую

        :param other: вычитаемая таблица
        :type other: Table

        :param keys: ключевые столбцы, определяющие уникальность позиции
        :type keys: Iterable[str]

        :return: результат вычитания
        :rtype: Table
        """
        keys = self._prepare_keys(keys)
        new = self.clone(copyitems=False)
        key_indices = self._key_indices(other._columns, keys)

        for pos in self._items:
            contains = False
            for npos in other._items:
                if self._pos_isequal(pos, npos, key_indices):
                    contains = True
                    break
            if not contains:
                new._items.append(pos)
        return new

    def diff_upd(self, other, keys=None):
        """
        Вычитает other из self

        :param other: вычитаемая таблица
        :type other: Table

        :param keys: ключевые столбцы, определяющие уникальность позиции
        :type keys: Iterable[str]
        """
        keys = self._prepare_keys(keys)
        key_indices = self._key_indices(other._columns, keys)

        for pos in reversed(self._items):
            for npos in other._items:
                if self._pos_isequal(pos, npos, key_indices):
                    self._items.remove(pos)
                    break

    def intersection(self, other, keys=None, funcs=None, replace=True, add_columns=False):
        """
        Возвращает таблицу с позициями, находящимися и в одной, и в другой таблице.

        :param other: вторая таблица
        :type other: Table

        :param keys: ключевые столбцы, определяющие уникальность позиции
        :type keys: Iterable[str]

        :param funcs: функции столбцов, используемые при замещении
        :type funcs: Iterable[Callable], dict

        :param replace: стоит ли замещать значения позиций первой таблицы
        :type replace: bool

        :param add_columns: стоит ли добавлять в таблицу столбцы второй таблицы
        :type add_columns: bool

        :return: новая таблица
        :rtype: Table
        """
        keys = self._prepare_keys(keys)
        funcs = self._prepare_funcs(funcs)
        new = self.clone(copyitems=False)

        key_indices = new._key_indices(other._columns, keys)
        funcs_iter = new._funcs_iter(other._columns, funcs)
        new_columns_indices = self._new_columns(other, new) if add_columns else []

        for pos in self._items:
            for npos in other._items:
                if self._pos_isequal(pos, npos, key_indices):
                    new_pos = dcopy(pos)
                    if add_columns:
                        for i in new_columns_indices:
                            pos.append(npos[i])
                    if replace:
                        for i1, i2, func in funcs_iter:
                            new_pos[i1] = func(new_pos[i1], npos[i2])
                    new._items.append(new_pos)
                    break
        return new

    def intersection_upd(self, other, keys=None, funcs=None, replace=False, add_columns=False):
        """
        Пересечение. Оставляет только позиции, присутствующие в другой таблице.

        :param other: вторая таблица
        :type other: Table

        :param keys: ключевые столбцы, определяющие уникальность позиции
        :type keys: Iterable[str]

        :param funcs: функции столбцов, используемые при замещении
        :type funcs: Iterable[Callable], dict

        :param replace: стоит ли замещать значения позиций первой таблицы
        :type replace: bool

        :param add_columns: стоит ли добавлять в таблицу столбцы второй таблицы
        :type add_columns: bool
        """
        keys = self._prepare_keys(keys)
        funcs = self._prepare_funcs(funcs)

        key_indices = self._key_indices(other._columns, keys)
        funcs_iter = self._funcs_iter(other._columns, funcs)
        new_columns_indices = self._new_columns(other, self) if add_columns else []

        for pos in reversed(self._items):
            contains = False
            for npos in other._items:
                if self._pos_isequal(pos, npos, key_indices):
                    contains = True
                    if add_columns:
                        for i in new_columns_indices:
                            pos.append(npos[i])
                    if replace:
                        for i1, i2, func in funcs_iter:
                            pos[i1] = func(pos[i1], npos[i2])
                    break
            if not contains:
                self._items.remove(pos)

    # ------------------------------------------------------------------------
    #   Magic arithmetic operations
    # ------------------------------------------------------------------------

    def __add__(self, other):
        return self.union(other)

    def __sub__(self, other):
        return self.diff(other)

    def __and__(self, other):
        return self.intersection(other)

    def __iadd__(self, other):
        self.update(other)
        return self

    def __isub__(self, other):
        self.diff_upd(other)
        return self

    def __iand__(self, other):
        self.intersection_upd(other)
        return self

    # ------------------------------------------------------------------------
    #   Global items operations
    # ------------------------------------------------------------------------

    def _normalise(self, keys=None):
        """
        Удаляет эквивалентные позиции

        Применим, например, после принудительной смены ключей.

        :param keys: столбцы, по которым сравниваются позиции
        :type keys: Iterable[str]
        """
        keys = self._prepare_keys(keys)

        length = len(self._items)
        key_indices = self._key_indices(self._columns, keys)

        for i, pos in enumerate(self._items):
            for ni in range(length - 1, i, -1):
                npos = self._items[ni]
                if self._pos_isequal(pos, npos, key_indices):
                    del npos

    def clear(self):
        """Удаляет все позиции в таблице"""
        self._items = []

    def filter(self, condition):
        for pos in reversed(self._items):
            dct = {k: v for k, v in zip(self._columns, pos)}
            if not condition(dct):
                self._items.remove(pos)

    def filtered(self, condition):
        new = self.clone(copyitems=False)
        for pos in self._items:
            dct = {k: v for k, v in zip(self._columns, pos)}
            if condition(dct):
                new._items.append(pos)
        return new

    def sort(self, *columns, clmns=None, reverse=False):
        """
        Сортирует позиции в таблице.

        :param columns: столбцы, по которым будет производится сортировка
        :type columns: str

        :param clmns: столбцы, по которым будет производится сортировка
        :type clmns: Iterable[str]

        :param reverse: следует ли производить сортировку в обратном порядке
        :type reverse: bool

        :return: новая таблица
        :rtype: Table
        """
        columns = list(columns)
        if clmns:
            columns += list(clmns)
        assert columns

        indices = [self._columns.index(c) for c in columns]

        # noinspection PyUnusedLocal
        def joinpos(pos, k=0):
            for value in pos:
                if isinstance(value, Iterable) and type(value) is not str:
                    value = joinpos(value, k + 1)
            if k == 0:
                return ' '.join((str(pos[i]) for i in indices))
            else:
                return ' '.join((str(i) for i in pos))

        self._items.sort(key=joinpos, reverse=reverse)

    def sorted(self, *columns, clmns=None, reverse=False):
        """
        Возвращает таблицу с отсортированными позициями.

        :param columns: столбцы, по которым будет производится сортировка
        :type columns: str

        :param clmns: столбцы, по которым будет производится сортировка
        :type clmns: Iterable[str]

        :param reverse: следует ли производить сортировку в обратном порядке
        :type reverse: bool

        :return: новая таблица
        :rtype: Table
        """
        columns = list(columns)
        if clmns:
            columns += list(clmns)
        assert columns

        new = self.clone(copyitems=True)
        indices = [self._columns.index(c) for c in columns]

        # noinspection PyUnusedLocal
        def joinpos(pos, k=0):
            for value in pos:
                if isinstance(value, Iterable) and type(value) is not str:
                    value = joinpos(value, k + 1)
            if k == 0:
                return ' '.join((str(pos[i]) for i in indices))
            else:
                return ' '.join((str(i) for i in pos))

        new._items.sort(key=joinpos, reverse=reverse)
        return new

    def with_columns(self, *columns, clmns=None):
        """Возвращает таблицу со ТОЛЬКО с переданными столбцами"""
        if clmns is not None:
            clmns = list(clmns)
            columns = list(columns) + [c for c in clmns if c not in columns]
        indices = [self._columns.index(c) for c in columns]
        new = self.clone(copyitems=False)

        for pos in self._items:
            new._items.append([pos[i] for i in indices])
        return new

    def clone(self, copyitems=False):
        """
        Возвращает клон таблицы.

        :param copyitems: клонировать ли содержимое таблицы
        :type copyitems: bool

        :return: копия осходной таблицы
        :rtype: Table или дочерние классы
        """
        new = self.__class__(dcopy(self._columns),
                             keys=dcopy(self._keys),
                             funcs=dcopy(self._funcs),
                             name=dcopy(self.name))
        if copyitems:
            new._items = dcopy(self._items)
        return new

    # ------------------------------------------------------------------------
    #   Magic iterators/generators
    # ------------------------------------------------------------------------

    def __iter__(self):
        """Позволяет красиво итерировать таблицу, возвращая словари"""
        return self.dicts()

    def __next__(self):
        """Возвращает очередную позицию при итерации"""
        return next(self.__iter__())

    def __reversed__(self):
        """
        Итератор, возвращающий позиции в обратном порядке
        :rtype: reversed
        """
        return reversed(self.dicts())

    def __len__(self):
        """Возвращает количество позиций в таблице"""
        return len(self._items)

    def __bool__(self):
        """
        Булево представление таблицы.
        :return: True если таблица не пуста
        :rtype: bool
        """
        return bool(self._items)

    # ------------------------------------------------------------------------
    #   Strings
    # ------------------------------------------------------------------------

    def __repr__(self):
        return (
            f'<{self.__class__}(columns={self._columns},'
            f'keys={self._keys}, funcs={self._funcs},'
            f'__len__={len(self._items)})>'
        )

    def __str__(self):
        """
        Возвращает красивое текстовое представление таблицы.

        :rtype: str
        """
        s = ''
        for line in self._pretty_str_lines():
            s += line + '\n'
        return s

    def _pretty_str_lines(self):
        """
        Возвращает красивое текстовое представление таблицы.

        :rtype: str
        """
        def left(string: object, length: int):
            return '{{:<{}}}'.format(length).format(repr(string))

        def center(string: object, length: int):
            return '{{:^{}}}'.format(length).format(repr(string))

        cwidths = []
        hrows = []
        for column, func in zip(self._columns, self._funcs):
            lc, lf = len(column), len(func.__name__)
            if column in self._keys:
                lc += 3
            cwidths.append(lc) if lc > lf else cwidths.append(lf)

        for pos in self._items:
            hrow = 1
            for icolumn, (value, width) in enumerate(zip(pos, cwidths)):
                len_repr_column = len(repr(value))

                if isinstance(value, Collection):
                    if isinstance(value, str):
                        value = value.split('\n')
                    if len(value) > hrow:
                        hrow = len(value)
                    for row in value:
                        len_repr_row = len(repr(row))
                        if len_repr_row > width:
                            cwidths[icolumn] = len_repr_row

                elif len_repr_column > width:
                    cwidths[icolumn] = len_repr_column
            hrows.append(hrow)

        sep_line = '+-'
        for w in cwidths:
            sep_line += w*'-' + '-+-'
        sep_line = sep_line[:-1]

        # yield '+' + ''.join(['-' for _ in range(sum(cwidth) + len(cwidth) * 3 - 1)]) + '+\n'
        yield '| ' + self.name.center(sum(cwidths) + len(cwidths)*3 - 3) + ' |'
        yield sep_line

        sep_value = ' | '

        str_columns = '| '
        str_funcs = '| '
        for i, (w, column, func) in enumerate(zip(cwidths, self._columns, self._funcs)):
            if column in self._keys:
                column = f'<#{column}>'
            str_columns += '{{:^{}}}'.format(w).format(column) + sep_value
            str_funcs += '{{:^{}}}'.format(w).format(func.__name__) + sep_value

        yield str_columns[:-1]
        yield str_funcs
        yield sep_line

        last_index = len(self._columns) - 1
        for pos, pos_height in zip(self._items, hrows):
            str_pos = '| '
            for y in range(pos_height):
                for i, (column, width) in enumerate(zip(pos, cwidths)):

                    if type(column) is str:
                        lenobj = len(column.split('\n'))
                    elif isinstance(column, Collection):
                        lenobj = len(column)
                    else:
                        lenobj = 1
                    begin = round(pos_height/2 - lenobj/2 - 0.1)

                    if begin + lenobj - 1 >= y >= begin:
                        if isinstance(column, str):
                            column = column.split('\n')
                            if lenobj == 1:
                                str_pos += center(column[0], width) + sep_value
                            else:
                                str_pos += center(column[y - begin], width) + sep_value
                        elif isinstance(column, Collection):
                            column = list(column)
                            if lenobj == 1:
                                str_pos += left(column[0], width) + sep_value
                            else:
                                str_pos += left(column[y - begin], width) + sep_value
                        else:
                            str_pos += center(column, width) + sep_value
                    else:
                        str_pos += width * ' ' + sep_value

                    if i == last_index and y != pos_height - 1:
                        str_pos += '\n| '
            yield str_pos
            yield sep_line

    def pprint(self):
        """
        Печатает красивое текстовое представление таблицы.

        :rtype: str
        """
        for line in self._pretty_str_lines():
            print(line)

    # ------------------------------------------------------------------------
    #   List-items operations
    # ------------------------------------------------------------------------

    def lists(self):
        """Итератор, возвращающий голые позиции в виде списков"""
        return iter(self._items)

    def get(self, index):
        return self._items[index]

    def contains(self, pos, columns=None, keys=None):
        """Определяет, находится ли позиция в таблице."""
        pos = list(pos)
        if columns is not None:
            columns = list(columns)
        else:
            columns = self._columns
        keys = self._prepare_keys(keys)
        key_indices = self._key_indices(columns, keys)

        for npos in self._items:
            if self._pos_isequal(npos, pos, key_indices):
                return True
        return False

    def index(self, pos, columns=None, keys=None):
        """
        Определяет индекс первой встреченной эквивалентной позиции в таблице.

        :param pos: новая позиция
        :type pos: Iterable[Any]

        :param columns: столбцы позиции
        :type columns: Iterable[str]

        :param keys: ключевые столбцы, определяющие уникальность позиции
        :type keys: Iterable[str]

        :return: индекс найденной позиции
        :rtype: int
        """
        pos = list(pos)
        if columns is not None:
            columns = list(columns)
        else:
            columns = self._columns
        keys = self._prepare_keys(keys)
        key_indices = self._key_indices(columns, keys)

        for npos in self._items:
            if self._pos_isequal(npos, pos, key_indices):
                return self._items.index(npos)
        pos = {c: v for c, v in zip(columns, pos)}
        raise ValueError(f"{pos} is not in '{self.name}'")

    def insert(self, npos, columns=None, keys=None, funcs=None):
        """
        Вставляет позицию в виде списка в таблицу.

        :param npos: новая позиция
        :type npos: Iterable[Any]

        :param columns: столбцы позиции
        :type columns: Iterable[str]

        :param keys: ключевые столбцы, определяющие уникальность позиции
        :type keys: Iterable[str]

        :param funcs: функции для столбцов, используемые при замещении
        :type funcs: Iterable[Callable]
        """
        npos = list(npos)
        if columns is not None:
            columns = list(columns)
        else:
            columns = self._columns
        keys = self._prepare_keys(keys)
        funcs = self._prepare_funcs(funcs)

        key_indices = self._key_indices(columns, keys)
        funcs_iter = self._funcs_iter(columns, funcs)
        adapt_inds = [columns.index(column) if column in columns else None
                      for column in self._columns]

        for pos in self._items:
            if self._pos_isequal(pos, npos, key_indices):
                for i1, i2, func in funcs_iter:
                    pos[i1] = func(pos[i1], npos[i2])
                return pos
        new_pos = self._pos_adapt(npos, adapt_inds)
        self._items.append(new_pos)
        return new_pos

    def unique_str(self, pos, columns=None, keys=None):
        if columns is None:
            columns = self._columns
        if keys is None:
            keys = self._keys
        return str({c: v for c, v in zip(columns, pos) if c in keys})

    def remove(self, pos, columns=None, keys=None):
        self._items.pop(self.index(pos, columns, keys))

    # ------------------------------------------------------------------------
    #   Position operations
    # ------------------------------------------------------------------------

    def dicts(self):
        for item in self._items:
            yield DotDict({c: v for c, v in zip(self._columns, item)})

    def get_dict(self, index):
        return DotDict({c: v for c, v in zip(self._columns, self._items[index])})

    def positions(self):
        for item in self._items:
            yield InnerObject(item, self._columns)

    def get_pos(self, index):
        return InnerObject(self._items[index], self._columns)

    def index_pos(self, pos, keys=None):
        return self.index(pos.values(), pos.keys(), keys=keys)

    def contains_pos(self, pos, keys=None):
        return self.contains(pos.values(), pos.keys(), keys=keys)

    def insert_pos(self, pos, keys=None, funcs=None):
        self.insert(pos.values(), pos.keys(), keys=keys, funcs=funcs)

    def unique_str_pos(self, pos, keys=None):
        if keys is None:
            keys = self._keys
        return str({c: v for c, v in pos.items() if c in keys})

    def remove_pos(self, pos, keys=None):
        self.remove(pos.values(), pos.keys(), keys=keys)

    # ------------------------------------------------------------------------
    #   Magic operations with items
    # ------------------------------------------------------------------------

    def __getitem__(self, index):
        """
        Возвращает голую позицию в виде списка по ее индексу,
        либо новую обрезанную таблицу, если передан срез.
        """
        if isinstance(index, int):
            return self.get(index)
        elif isinstance(index, slice):
            new = self.clone(copyitems=False)
            new._items = self._items[index]
            return new
        else:
            raise TypeError(f"index must be int- or slice-like")

    def __contains__(self, pos):
        """
        Определяет, находится ли словарь в таблице
        :type pos: dict
        """
        return self.contains_pos(pos)

    def __delitem__(self, index):
        del self._items[index]

    def __setitem__(self, index, pos):
        self._items[index] = pos

    def pop(self, index):
        self._items.pop(index)

    # ------------------------------------------------------------------------
    #   Smart operations
    # ------------------------------------------------------------------------

    def search(self, pat, columns=None, mode='any.in'):
        """Поиск по таблице

        :param pat: search request
        :type pat: list

        :param columns: columns in which the search will be performed
        :type columns: list

        :param mode: 'any.ex', 'any.in', 'all.ex', 'all.in'
        :type mode: str

        :return: new table with results of search request
        :rtype: new.parent.__table object
        """
        def words(str_, split_=True):
            for p in punctuation:
                str_ = str_.replace(p, ' ')
            str_ = str_.lower()
            lst = str_.split()
            if not split_:
                return ' '.join(lst)
            return lst

        if columns is None:
            columns = self._columns

        new = self.clone(copyitems=False)
        new.columns += ['Key']
        new.name = f"Search: '{pat}' in '{self.name}'"

        wpat = words(pat, split_=True)
        len_ = len(wpat) + 1
        indices = [self._columns.index(c) for c in columns]

        mode1, mode2 = mode.split('.')
        if mode2 == 'full':
            re_pat = '( |^){}( |$)'
        elif mode2 == 'in':
            re_pat = '(.|^){}(.|$)'
        else:
            raise ValueError(f'mode {mode} doesn\'t exists')

        for pos in self._items:
            wpos = ' '.join([str(pos[i]) for i in indices])
            wpos = words(wpos, split_=False)
            all_cuts = []

            if mode1 == 'any':
                for n in range(len_):
                    for i in range(n):
                        cut = ' '.join(wpat[i:i + len_ - n])
                        if re.search(re_pat.format(cut), wpos):
                            all_cuts.append(len_ - n)
                            wpos = wpos.replace(cut, '')
                if all_cuts:
                    new._items.append(pos + [all_cuts])

            if mode1 == 'all':
                if all([re.search(re_pat.format(w), wpos) for w in wpat]):
                    new._items.append(pos + [wpos])

        new.sort(clmns=['Key'], reverse=True)
        new.columns.pop(-1)
        return new

    '''def where(self, dct=None, **kwargs):
        method_names = {
            '__gt__': '>',
            '__lt__': '<',
            '__ge__': '>=',
            '__le__': '<=',
            '__eq__': '==',
            '__ne__': '!='
        }
        dct = {**dct, **kwargs}
        d = []
        for key, value in dct.items():
            spl = key.split('.', 1)
            if len(spl) == 1:
                column_name = spl[0]
                func_name = '=='
            else:
                column_name = '.'.join(spl[:-1])
                func_name = spl[-1].strip()

            if func_name not in method_names.values():
                func_name = '.' + func_name
            d.append((repr(column_name), func_name, repr(value)))

        def condition(pos: dict):
            for column, func, value in d:
                if not exec(f'pos[{column}]{func}{value}'):
                    return False
            return True
        return self.clone(copyitems=True).filter(condition)'''
