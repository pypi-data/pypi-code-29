from abc import ABCMeta
from typing import List

from dataclasses import dataclass

from .consts import ResponseStatus
from .errors import FieldError


class SdkBase(metaclass=ABCMeta):
    methods = []

    def __init__(self, requester):
        self.requester = requester

        for method in self.methods:
            setattr(self, method.__name__, self._new_method(method))

    def _new_method(self, func):
        def fn(*args, **kwargs):
            return func(self.requester, *args, **kwargs)

        return fn


@dataclass
class SdkResp:
    status: ResponseStatus = None
    errors: List[FieldError] = None

    @property
    def success(self):
        return self.status == ResponseStatus.SUCCESS


@dataclass
class SdkPage(SdkResp):
    cursor: int = None
