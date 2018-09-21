from __future__ import annotations

import marshal
import os
import re
import shutil
from collections import Counter
from copy import deepcopy as dcopy
from functools import wraps
from random import choices
from string import ascii_letters, digits, punctuation
from time import time_ns
from types import FunctionType
from typing import Callable, Iterable, Collection, List

from ._new_ast import literal_eval as new_literal_eval
from .acnt import File, FileMeta, Combiner, Dotdict
from .path import Path

__all__ = ('DF', 'ColumnsEditor', 'Table', 'PrettyTable', 'FileColumnsEditor', 'TableFile')


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


class ColumnsEditor:
    __slots__ = '_parent'

    def __init__(self, parent: PrettyTable):
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
            assert all((type(k) is str and isinstance(v, Callable) for k, v in dct.items()))
            clmns_funcs = {**dct, **clmns_funcs}
        assert all((isinstance(v, Callable) for v in clmns_funcs.values()))
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
        return f'<{self.__class__.__name__}({repr(self._parent)})>'

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


class Table(Combiner):
    __slots__ = ('_columns', '_funcs', '_keys', 'name', '_items')

    def _prepare_funcs(self, funcs):
        """
        Возвращает обновленный список функций таблицы

        :param funcs:
        :type funcs: Iterable[str], dict, NoneType

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

    def __init__(self, columns: Iterable[str],
                 keys: Iterable[str]=None,
                 funcs: Iterable[Callable]=None,
                 name: str='no_name'):
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
            assert all((isinstance(c, Callable) for c in funcs))
        else:
            funcs = [DF.const for _ in columns]

        self._columns = columns
        self._funcs = funcs
        self._keys = keys
        self.name = name
        self._items = []

    def eq(self, other, keys=None):
        """

        :param other:
        :type other: Table

        :param keys:
        :type keys: Iterable[str]

        :return:
        :rtype: bool
        """
        keys = self._prepare_keys(self._columns if keys is None else keys)

        if set(self._columns) != set(other._columns):
            return False
        if set(self._keys) != set(other._keys):
            return False
        if len(self._items) != len(other._items):
            return False

        key_indices = self._key_indices(other._columns, keys)

        for pos in self._items:
            contains = False
            for npos in other._items:
                if self._pos_isequal(pos, npos, key_indices):
                    contains = True
                    break
            if not contains:
                return False
        return True

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

    def union_upd(self, other, keys=None, funcs=None, replace=True,
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

    def filter(self, condition):
        for pos in self._items:
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

    def contains(self, pos, columns=None, keys=None):
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
        raise ValueError(f"{npos} is not in '{self.name}'")

    def remove(self, pos, columns=None, keys=None):
        self._items.pop(self.index(pos, columns, keys))

    def insert(self, npos, columns=None, keys=None, funcs=None):
        """
        Вставляет позицию в виде списка в таблицу

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


class PrettyTable(Table): 
    """
    Обертка для удобной и красивой работы с Table.

    Методы:
        Сеттеры:
            columns
            funcs
            keys

        Итерация:
             __iter__
             __next__
             __reversed__
             lists
             dicts

        Работа с позициями:
            __contains__
            __index__
            __getitem__
            __delitem__
            get
            get_dict
            insert_dict
            pos_unique_str

        Работа с содержимым:
            clear
            search
            _normalise
            # where

        Текст:
            pretty_str
            pprint
            __str__
            __repr__

        Арифметические операторы:
            __add__
            __sub__
            __and__
            __iadd__
            __sub__
            __and__

        Прочее:
            __len__
            __bool__
    """
    __slots__ = ('_columns', '_funcs', '_keys', 'name', '_items')

    @property
    def columns(self):
        """
        Возвращает объект, позволяющий редактировать
        столбцы таблицы, изменяя при этом ее содержимое.

        >>> t = PrettyTable(
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

        >>> t = PrettyTable(
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
        return reversed(self._items)

    def __contains__(self, pos):
        """
        Определяет, находится ли список или словарь в таблице
        :type pos: list, dict
        """
        if isinstance(pos, dict):
            return self.contains(pos.values(), pos.keys())
        elif isinstance(pos, Iterable):
            pos = list(pos)
            return pos in self._items
        else:
            raise TypeError(f'pos must be iterable')

    def __index__(self, pos):
        """
        Определяет индекс списка или словаря в таблице.
        :type pos: list, dict
        """
        if isinstance(pos, dict):
            return self.index(pos.values(), pos.keys())
        elif isinstance(pos, Iterable):
            pos = list(pos)
            return self._items.index(pos)
        else:
            raise TypeError(f'pos must be iterable')

    def __getitem__(self, column):
        """

        :param column:
        :type column: str
        """
        index = self._columns.index(column)
        for item in self._items:
            yield item[index]

    """def __delitem__(self, ind):
        del self._items[ind]"""

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

    def __str__(self):
        """
        Возвращает красивое текстовое представление таблицы.
        :rtype: str
        """
        return self.pretty_str()

    def __repr__(self):
        return (
            f'<{self.__class__}(columns={self._columns},'
            f'keys={self._keys}, funcs={self._funcs},'
            f'__len__={len(self._items)})'
        )

    def pretty_str(self):
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

        sep_pos = '+-'
        for w in cwidths:
            sep_pos += w * '-' + '-+-'
        sep_pos = sep_pos[:-1] + '\n'

        # s = '+' + ''.join(['-' for _ in range(sum(cwidth) + len(cwidth) * 3 - 1)]) + '+\n'
        s = '| ' + self.name.center(sum(cwidths) + len(cwidths) * 3 - 3) + ' |\n' + sep_pos
        sep_value = ' | '

        str_columns = '| '
        str_funcs = '| '
        for i, (w, column, func) in enumerate(zip(cwidths, self._columns, self._funcs)):
            if column in self._keys:
                column = f'<#{column}>'
            str_columns += '{{:^{}}}'.format(w).format(column) + sep_value
            str_funcs += '{{:^{}}}'.format(w).format(func.__name__) + sep_value
        s += str_columns[:-1] + '\n' + str_funcs + '\n' + sep_pos

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
                    begin = round(pos_height / 2 - lenobj / 2 - 0.1)

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
            s += str_pos + '\n' + sep_pos
        return s

    def pprint(self):
        """
        Печатает красивое текстовое представление таблицы.
        :rtype: str
        """
        print(self.pretty_str())

    """setitem, append, del, insert"""

    def clear(self):
        """Удаляет все позиции в таблице"""
        self._items = []

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

    def insert_dict(self, dct=None, keys=None, funcs=None, **kwargs):
        dct = {**dct, **kwargs}
        return self.insert(dct.values(), dct.keys(), keys=keys, funcs=funcs)

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

    def remove_dict(self, dct, keys=None):
        self.remove(dct.values(), dct.keys(), keys=keys)

    def index_dict(self, dct, keys=None):
        return self.index(dct.values(), dct.keys(), keys=keys)

    def lists(self):
        """Итератор, возвращающий голые позиции в виде списков"""
        return iter(self._items)

    def get(self, index):
        """
        Возвращает голую позицию в виде списка по ее индексу,
        либо новую обрезанную таблицу, если передан срез.
        """
        if type(index) is int:
            return self._items[index]
        elif type(index) is slice:
            new = self.clone(copyitems=False)
            new._items = self._items[index]
            return new
        else:
            raise TypeError(f"index must be 'int' or 'slice'")

    def dicts(self):
        """Итератор, возвращающий позиции в виде словарей"""
        for item in self._items:
            yield {k: v for k, v in zip(self._columns, item)}

    def get_dict(self, index):
        assert type(index) is int
        return {k: v for k, v in zip(self._columns, self._items[index])}

    def dotdicts(self):
        for item in self._items:
            yield Dotdict({k: v for k, v in zip(self._columns, item)})

    def get_dotdict(self, index):
        assert type(index) is int
        return Dotdict({k: v for k, v in zip(self._columns, self._items[index])})

    def pop(self, index):
        self._items.pop(index)

    def __add__(self, other):
        return self.union(other)

    def __sub__(self, other):
        return self.diff(other)

    def __and__(self, other):
        return self.intersection(other)

    def __iadd__(self, other):
        self.union_upd(other)
        return self

    def __isub__(self, other):
        self.diff_upd(other)
        return self

    def __iand__(self, other):
        self.intersection_upd(other)
        return self

    def pos_unique_str(self, pos, columns=None, keys=None):
        if columns is None:
            columns = self._columns
        if keys is None:
            keys = self._keys
        return str({c: v for c, v in zip(columns, pos) if c in keys})

    def pos_unique_str_dict(self, dct: dict, keys=None):
        if keys is None:
            keys = self._keys
        return str({c: v for c, v in dct.items() if c in keys})

    def with_columns(self, *columns, clmns=None):
        if clmns is not None:
            clmns = list(clmns)
            columns = list(columns) + [c for c in clmns if c not in columns]
        indices = [self._columns.index(c) for c in columns]
        new = self.clone(copyitems=False)

        for pos in self._items:
            new._items.append([pos[i] for i in indices])
        return new

    def search(self, pat, columns=None, mode='any.in'):
        """ Search in table

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


# ---------------------------------------------------------------------------
#   File classes
# ---------------------------------------------------------------------------


class FileColumnsEditor(ColumnsEditor, metaclass=FileMeta):
    change_plus_methods = ('rename',
                           'set',
                           'add',
                           'append',
                           'insert',
                           '__setitem__',
                           '__iadd__',
                           '__iand__',
                           '__isub__',)

    @staticmethod
    def _change_plus(func: Callable):
        @wraps(func)
        def wrap(self, *args, **kwargs):
            # noinspection PyCallingNonCallable
            result = func(self, *args, **kwargs)

            self._parent.changes_counter += 1
            if self._parent.save_count and self._parent.changes_counter:
                if self._parent.changes_counter % self._parent.save_count == 0:
                    self._parent.save()
            return result
        return wrap


class TableFile(PrettyTable, File):
    change_plus_methods = ('union_upd',
                           'diff_upd',
                           'intersection_upd',
                           'sort',
                           'filter',
                           'insert',
                           'clear',
                           '_normalise',)
    saving_off_methods = ('loads',)
    save_copies_methods = ('clear',)

    DATA_FILENAME = 'data'
    CACHE_PATH = 'cache'
    FILES_PATH = 'files'
    COPIES_PATH = 'copies'
    EXTENSION = 'grms'
    READABLE_ARGS = ('_columns', '_keys', '_funcs', 'name', '_paths_for_copies')
    SEPARATOR = '\n\n******\n\n'

    @staticmethod
    def _change_plus(func: Callable):
        @wraps(func)
        def wrap(self, *args, **kwargs):
            result = func(self, *args, **kwargs)

            self.changes_counter += 1
            if self.save_count and self.changes_counter:
                if self.changes_counter % self.save_count == 0:
                    self.save()
            return result
        return wrap

    @staticmethod
    def _saving_off(func: Callable):
        @wraps(func)
        def wrap(self, *args, **kwargs):
            save_count = self.save_count
            changes_counter = self.changes_counter
            self.save_count = 0

            result = func(self, *args, **kwargs)

            self.save_count = save_count
            self.changes_counter = changes_counter
            self.changes_counter += 1
            if self.save_count and self.changes_counter:
                if self.changes_counter % self.save_count == 0:
                    self.save()
            return result

        return wrap

    @staticmethod
    def _save_copies(func: Callable):
        @wraps(func)
        def wrap(self, *args, **kwargs):
            self.save_copies()
            func(self, *args, **kwargs)
        return wrap

    def _reopen(self, read=False):
        path_to_file = self._path.get_child(f'\\{TableFile.DATA_FILENAME}.{TableFile.EXTENSION}').abs_path
        try:
            self.file.close()
        except (NameError, AttributeError):
            pass
        if os.path.exists(path_to_file):
            self.file = open(path_to_file, 'r+', encoding='utf-8')
            if read:
                self.changes_counter -= 1
                self.read()
        else:
            open(path_to_file, 'w').close()
            self.file = open(path_to_file, 'r+', encoding='utf-8')
            self.saves_counter -= 1
            sync_count = self.sync_interval
            self.sync_interval = 0
            self.save()
            self.sync_interval = sync_count

    def _mkdirs(self):
        self._path_for_files = self._path.get_child(TableFile.FILES_PATH)
        self._cache_path = self._path.get_child(TableFile.CACHE_PATH)
        self._paths_for_copies = [self._path.get_child(p.path) for p in self._paths_for_copies]
        self.parent_cache = self._cache_path
        self.cache = []

        for path in [self._path, self._path_for_files] + self._paths_for_copies:
            if not os.path.exists(path.abs_path):
                os.mkdir(path.abs_path)

    @property
    def columns(self):
        return FileColumnsEditor(self)

    @columns.setter
    def columns(self, value):
        FileColumnsEditor(self).set(lst=value)

    @property
    def path(self):
        return self._path.path

    @path.setter
    def path(self, value):
        self._path = Path(value)
        self._mkdirs()
        self._reopen(read=False)
        self.save()

    @property
    def path_for_copies(self):
        return [p.path for p in self._paths_for_copies]

    @path_for_copies.setter
    def path_for_copies(self, value):
        for p in value:
            if p not in self._paths_for_copies:
                self._paths_for_copies.append(self._path.get_child(p))
        if self._path.get_child(TableFile.COPIES_PATH) not in self._paths_for_copies:
            self._paths_for_copies.append(self._path.get_child(TableFile.COPIES_PATH))

    @property
    def path_for_files(self):
        return self._path_for_files

    @property
    def cache_path(self):
        return self._cache_path

    @classmethod
    def open(cls, path):
        pass

    def __init__(self, path: str,
                 columns: Iterable[str],
                 keys: Iterable[str]=None,
                 funcs: Iterable[Callable]=None,
                 name='no_name',
                 paths_for_copies: Iterable[str]=None,
                 save_interval: int=None,
                 sync_interval: int=None,
                 read: bool=False):
        super().__init__(columns, keys, funcs, name)
        super(File).__init__()

        assert type(save_interval) is int if save_interval is not None else True
        assert type(sync_interval) is int if sync_interval is not None else True

        self._path = Path(path)
        if not paths_for_copies:
            paths_for_copies = [TableFile.COPIES_PATH]
        else:
            paths_for_copies = list(paths_for_copies)

        self._paths_for_copies = [self._path.get_child(p) for p in paths_for_copies]

        self.changes_counter = 0
        self.saves_counter = 0
        self.save_interval = save_interval
        self.sync_interval = sync_interval

        self._mkdirs()
        self._reopen(read=read)

    def __del__(self):
        def remove(parent_cache):
            # 0 - cache, 1 - parent_cache
            if isinstance(parent_cache, Path):
                shutil.rmtree(parent_cache.abs_path, ignore_errors=True)
            elif not parent_cache[0]:
                remove(parent_cache[1])

        try:
            self.file.close()
        except (NameError, AttributeError):
            pass

        if not isinstance(self.parent_cache, Path):
            self.parent_cache[0].remove(self._path.abs_path)

        if not self.cache:
            remove(self.parent_cache)

        if os.path.exists(self._path.abs_path):
            if not os.listdir(self._path.abs_path):
                shutil.rmtree(self._path.abs_path, ignore_errors=True)

    def delete_file(self):
        path = self._path.abs_path
        self.file.close()
        shutil.rmtree(path, ignore_errors=True)

    def read(self, path=None):
        if path is None:
            self.loads(self.file.read())
        else:
            with open(path, 'r', encoding='utf-8') as file:
                self.loads(file.read())

    def loads(self, data=None):
        if data:
            if bytes(data[0], encoding='utf-8') == b'\xef\xbb\xbf':
                data = data[1:]
        if data in (None, ''):
            data = self.dumps()

        settings, data = data.split(TableFile.SEPARATOR, 1)
        for line in settings.splitlines():
            arg, val = line.split('=', 1)
            arg = arg.strip()
            if arg in TableFile.READABLE_ARGS:
                val = eval(val)
                if arg == '_funcs':
                    # noinspection PyArgumentList
                    val = [FunctionType(marshal.loads(f), globals(), f'func{i}') for i, f in enumerate(val)]
                self.__setattr__(arg, val)
        self.clear()
        for pos in data.splitlines():
            pos = new_literal_eval(pos)
            if not isinstance(pos, list):
                raise ValueError(f'Incorrect position: {pos}')
            self._items.append(pos)

    def save(self, path=None):
        if path is None:
            self.file.seek(0)
            self.file.truncate()
            self.file.write(self.dumps())
            self.file.read()
        else:
            with open(path, 'w', encoding='utf-8') as file:
                file.write(self.dumps())

        self.saves_counter += 1
        if self.sync_interval and self.saves_counter % self.sync_interval == 0:
            self.save_copies()

    def dumps(self, obj=None):
        if obj is None:
            obj = self
        # noinspection PyUnresolvedReferences
        settings = [f'name = {repr(obj.name)}',
                    f'_paths_for_copies = {obj._paths_for_copies}',
                    f'_columns = {obj._columns}',
                    f'_keys = {obj._keys}',
                    f'_funcs = {[marshal.dumps(func.__code__) for func in obj._funcs]}']
        data = [str(l) for l in obj._items]
        return '\n'.join(settings) + TableFile.SEPARATOR + '\n'.join(data)

    def save_copies(self):
        filename = f'\\{self.name} - {time_ns()}.{TableFile.EXTENSION}'
        str_for_file = self.dumps()
        for path_for_copy in self._paths_for_copies:
            file = open(path_for_copy.abs_path + filename, 'w', encoding='utf-8')
            file.write(str_for_file)
            file.close()

    def clone(self, copyitems=False, copy_counters=False):
        new_par_path = self._cache_path.abs_path
        if not os.path.exists(new_par_path):
            os.mkdir(new_par_path)

        rand = ''.join(choices(ascii_letters + digits, k=4))
        new = self.__class__(
            columns=dcopy(self._columns),
            keys=dcopy(self._keys),
            funcs=dcopy(self._funcs),
            name=dcopy(self.name),
            parent_path=new_par_path,
            path=f'{self._path.path} {time_ns()}{rand}',
            paths_for_copies=[p.path for p in self._paths_for_copies],
            save_count=dcopy(self.save_interval),
            sync_count=dcopy(self.sync_interval),
            read_when_init=False,
        )
        self.cache.append(new._path.abs_path)
        new.parent_cache = (self.cache, self.parent_cache)
        if copyitems:
            new._items = dcopy(self._items)
        if copy_counters:
            new.changes_counter = self.changes_counter
            new.saves_counter = self.saves_counter
        return new
