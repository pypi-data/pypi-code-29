from collections import defaultdict
from itertools import islice
from math import log
from typing import Dict, Iterator, List, Optional

__all__ = ['mersenne_primes', 'mersenne_primes_up_to', 'primes', 'primes_up_to']


def primes(n: Optional[int] = None) -> Iterator[int]:
    def infinite_primes() -> Iterator[int]:
        D: Dict[int, List[int]] = defaultdict(list)
        q = 2
        while True:
            if q not in D:
                yield q
                D[q * q] = [q]
            else:
                for p in D[q]:
                    D[p + q].append(p)
                del D[q]
            q += 1
    if n is None:
        return infinite_primes()
    return islice(infinite_primes(), n)


def primes_up_to(n: int) -> Iterator[int]:
    _primes = primes()
    p = next(_primes)
    while p <= n:
        yield p
        p = next(_primes)


def mersenne_primes(n: Optional[int] = None) -> Iterator[int]:
    def infinite_mersenne_primes() -> Iterator[int]:
        D: Dict[int, List[int]] = defaultdict(list)
        q = 2
        while True:
            if q not in D:
                if log(q + 1, 2).is_integer():
                    yield q
                D[q * q] = [q]
            else:
                for p in D[q]:
                    D[p + q].append(p)
                del D[q]
            q += 1
    if n is None:
        return infinite_mersenne_primes()
    return islice(infinite_mersenne_primes(), n)


def mersenne_primes_up_to(n: int) -> Iterator[int]:
    _primes = mersenne_primes()
    p = next(_primes)
    while p <= n:
        yield p
        p = next(_primes)
