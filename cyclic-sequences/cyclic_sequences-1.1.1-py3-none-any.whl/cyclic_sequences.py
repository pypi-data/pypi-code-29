#!/usr/bin/env python3
# -*- coding: utf8 -*-

"""Sequence type objects with cyclic indexing.

The cyclic indexation works as for usual sequences, with the possible use 
of negative indexes. But it makes a jump-back to the beginning (or the end for 
negative indexes) if the index is higher than the length of the sequence::
    
      ┌───────────────────────────┐
      │                           ▼
    ┏━│━┳━━━┳━━━┳━╍┅   ┅╍━┳━━━━━┳━━━┳━━━┓
    ┃ ● ┃ 0 ┃ 1 ┃   ⋅⋅⋅   ┃ N-1 ┃ N ┃ ● ┃
    ┗━━━┻━━━┻━━━┻━╍┅   ┅╍━┻━━━━━┻━━━┻━│━┛
          ▲                           │
          └───────────────────────────┘

 Iterating over a cyclic sequence is bounded (no infinite loop).


.. note:: This module is based on a Chris Lawlor forum publication.


Content
=======

:CyclicTuple:
    Class object.
    An immutable cyclic sequence based on built-in class *tuple*.

:CyclicList:
    Class object.
    A mutable cyclic sequence based on built-in class *list*.

:CyclicStr:
    Class object.
    An immutable cyclic sequence based on built-in class *str*.


Examples
========

The following examples are using ``CyclicList`` for demonstration. 
``CyclicTuple`` and ``CyclicStr`` get similar behaviours.

- Construction from any iterable::

    >>> foo = CyclicList(['a', 'b', 'c', 'd', 'e'])
    >>> foo
    CyclicList(['a', 'b', 'c', 'd', 'e'])

- Gets its specific string representation with chevrons figuring cycling::

    >>> print(foo)
    <['a', 'b', 'c', 'd', 'e']>

.. note:: This not true for ``CyclicStr``.

- Accessing works like a regular list::

    >>> foo[1]
    'b'
    >>> foo[-4]
    'b'

- Except indexes higher than length wraps around::

    >>> foo[6]
    'b'
    >>> foo[11]
    'b'
    >>> foo[-9]
    'b'

- Slices work and return list objects::

    >>> foo[1:4]
    ['b', 'c', 'd']
    >>> foo[3:0:-1]
    ['d', 'c', 'b']

- Slices work also out of range with cyclic output::

    >>> len(foo)
    5
    >>> foo[3:7]
    ['d', 'e', 'a', 'b']
    >>> foo[8:12]
    ['d', 'e', 'a', 'b']
    >>> foo[3:12]
    ['d', 'e', 'a', 'b', 'c', 'd', 'e', 'a', 'b']
    >>> foo[-2:2]
    ['d', 'e', 'a', 'b']
    >>> foo[-7:-3]
    ['d', 'e', 'a', 'b']
    >>> foo[-7:2]
    ['d', 'e', 'a', 'b', 'c', 'd', 'e', 'a', 'b']

- Slices with non unitary steps work also::

    >>> foo[:7:2]
    ['a', 'c', 'e', 'b']
    >>> foo[:7:3]
    ['a', 'd', 'b']
    >>> foo[:7:5]
    ['a', 'a']

- As well for reversed steps::

    >>> foo[1:-3:-1]
    ['b', 'a', 'e', 'd']
    >>> foo[-4:-8:-1]
    ['b', 'a', 'e', 'd']
    >>> foo[-4:-9:-2]
    ['b', 'e', 'c']
    >>> foo[-4:-9:-3]
    ['b', 'd']
    >>> foo[-5:-11:-5]
    ['a', 'a']

- Incoherent slices return empty list::

    >>> foo[11:5]
    []

.. note:: Indexing an empty CyclicList returns an IndexError.

.. note:: Indexing on a unique element returns always this element.


First element can be played with using specific methods:

- **with_first**: return a new CyclicList with given element at first
  position::

    >>> foo.with_first('c')
    CyclicList(['c', 'd', 'e', 'a', 'b'])

- **turned**: return a new CyclicList with all elements indexes changed
  of given step (default is 1 unit onward)::

    >>> foo.turned()
    CyclicList(['b', 'c', 'd', 'e', 'a'])
    >>> foo.turned(-3)
    CyclicList(['c', 'd', 'e', 'a', 'b'])
    >>> foo.turned(10)
    CyclicList(['a', 'b', 'c', 'd', 'e'])

- **set_first**: put given element at first position::

    >>> foo.set_first('c')
    >>> foo
    CyclicList(['c', 'd', 'e', 'a', 'b'])

- **turn**: change all elements index of given step
  (default is 1 unit onward)::

    >>> foo.turn()
    >>> foo
    CyclicList(['d', 'e', 'a', 'b', 'c'])
    >>> foo.turn(-3)
    >>> foo
    CyclicList(['a', 'b', 'c', 'd', 'e'])
    >>> foo.turn(11)
    >>> foo
    CyclicList(['b', 'c', 'd', 'e', 'a'])

.. note:: ``set_first`` and ``turn`` methods are only available for ``CyclicList``, 
          since other cyclic classes are immutables.
    
    
"""

import itertools


class AbstractCyclic(object):
    """Abstract class that implement cyclic indexing."""

    _girf = NotImplemented  # get item return function

    def __repr__(self):
        return "{}({})".format(self.__class__.__name__, super().__repr__())

    def __str__(self):
        return "<{}>".format(super().__repr__())

    def __getitem__(self, key):
        """Get-item special method with cyclic indexing.
        
        Recall that:
            x.__getitem__(i) <==> x[i]
            x.__getitem__(slice) <==> x[i:j:k]
        """
        N = self.__len__()
        if N == 0:
            raise IndexError("{} is empty".format(self.__class__.__name__))
        if isinstance(key, int):
            return super().__getitem__(key % N)
        elif isinstance(key, slice):
            start = key.start if key.start is not None else 0
            stop = key.stop if key.stop is not None else N
            step = 1 if key.step is None else key.step
            sim_start = self.index(self[start])
            if step > 0:
                direction = lambda x: x
                length = stop - start
            elif step < 0:
                direction = reversed
                length = start - stop
                step = abs(step)
                sim_start = N - sim_start - 1  # Reverse index
            else:
                raise ValueError("slice step cannot be zero")
            if length > 0:
                # Redifine start and stop with equivalent and simpler indexes.
                start = sim_start
                stop = sim_start + length
                cyclic_self = itertools.cycle(direction(self))
                iterator = ((i, next(cyclic_self)) for i in range(stop))
                return self._girf(
                    elt for i, elt in iterator if i >= start and (i - start) % step == 0
                )
            else:
                return self._girf([])
        else:
            raise TypeError(
                "{} indices must be integers or slices, "
                "not {}".format(self.__class__, type(key))
            )

    def turned(self, step=1):
        """
        foo.turned(step) -> new instance
        New instance of 'foo' with all elements shifted of given step.
        (default is 1 unit onward).
        """
        try:
            step = int(step) % self.__len__()
        except ValueError:
            raise TypeError(
                "{} method 'turned' requires an integer but received a {}".format(
                    self.__class__.__name, type(step)
                )
            )
        return self._get_first_using_index(step)

    def with_first(self, elt):
        """
        foo.with_first(elt) -> new instance
        New instance of 'foo' with first occurence of 'elt' at first position.
        Raises ValueError if 'elt' is not present.        
        """
        try:
            index = self.index(elt)
        except ValueError:
            raise ValueError("{} is not in CyclicList".format(elt))
        return self._get_first_using_index(index)

    def _get_first_using_index(self, index):
        return self.__class__(
            super().__getitem__(slice(index, None, None))
            + super().__getitem__(slice(None, index, None))
        )


class AbstractMutableCyclic(AbstractCyclic):
    """Abstract class that add methods for mutable cyclic sequence objects."""

    def turn(self, step=1):
        """
        foo.turn(step) -> None
        Change all elements indexes of given step (default is 1 unit onward)
        Equivalent to set at first position the element at index 'step'.
        """
        try:
            step = int(step) % self.__len__()
        except ValueError:
            raise TypeError(
                "{} method 'turn' requires an integer but received a {}".format(
                    self.__class__.__name, type(step)
                )
            )
        self._set_first_using_index(step)

    def set_first(self, elt):
        """
        foo.set_first(elt) -> None
        Set first occurence of 'elt' at first position.
        Raises ValueError if 'elt' is not present.
        """
        try:
            index = self.index(elt)
        except ValueError:
            raise ValueError("{} is not in CyclicList".format(elt))
        self._set_first_using_index(index)

    def _set_first_using_index(self, index):
        self.__init__(
            super().__getitem__(slice(index, None, None))
            + super().__getitem__(slice(None, index, None))
        )


class CyclicTuple(AbstractCyclic, tuple):
    """An immutable cyclic sequence based on built-in class *tuple*.

    See help of module cyclic_sequences for advanced description.
    
    Usage::
        >>> foo = CyclicList(['a', 'b', 'c', 'd', 'e'])
        >>> foo
        CyclicList(['a', 'b', 'c', 'd', 'e'])
        >>> print(foo)
        <['a', 'b', 'c', 'd', 'e']>
        >>> foo[3:7]
        ['d', 'e', 'a', 'b']
        >>> foo.set_first('d')
        >>> foo
        CyclicList(['d', 'e', 'a', 'b', 'c'])
    
    
    """

    _girf = tuple


class CyclicList(AbstractMutableCyclic, list):
    """A mutable cyclic sequence based on built-in class *list*.
    
    See help of module cyclic_sequences for advanced description.
    
    Usage::
        >>> foo = CyclicTuple(['a', 'b', 'c', 'd', 'e'])
        >>> foo
        CyclicTuple(('a', 'b', 'c', 'd', 'e'))
        >>> print(foo)
        <('a', 'b', 'c', 'd', 'e')>
        >>> foo[3:7]
        ('d', 'e', 'a', 'b')
        >>> foo.with_first('d')
        CyclicTuple(('d', 'e', 'a', 'b', 'c'))
    
    
    """

    _girf = list


class CyclicStr(AbstractCyclic, str):
    """An immutable cyclic sequence based on built-in class *str*.

    See help of module cyclic_sequences for advanced description.
    
    Usage::
        >>> foo = CyclicStr('abcde')
        >>> foo
        CyclicStr('abcde')
        >>> print(foo)
        abcde
        >>> foo[3:7]
        'deab'
        >>> foo.with_first('d')
        CyclicStr('deabc')
    
    
    """

    _girf = "".join

    def __str__(self):
        return str.__str__(self)


###############################################################################


if __name__ == "__main__":

    import doctest

    doctest_result = doctest.testmod()
    print("\ndoctest >", doctest_result, "\n")
