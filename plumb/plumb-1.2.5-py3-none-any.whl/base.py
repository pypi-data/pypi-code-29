from abc import ABC, abstractmethod


class BaseSource(ABC):
    @abstractmethod
    def get(self, timeout=None):
        raise NotImplementedError()

    @abstractmethod
    def close(self):
        raise NotImplementedError()


class BaseSink(ABC):
    @abstractmethod
    def put(self, message):
        raise NotImplementedError()

    @abstractmethod
    def close(self):
        raise NotImplementedError()