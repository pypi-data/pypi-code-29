from abc import ABCMeta, abstractmethod
from functools import partial

from voluptuous import Schema as VolSchema

Schema = partial(VolSchema, required=True)


class SDKObject(metaclass=ABCMeta):
    pass


class Receivable(SDKObject, metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def get_receiving_schema():
        raise NotImplemented

    @classmethod
    def from_json(cls, obj):
        """
        :param obj: a json dictionary
        :return: the object parsed from the json dictionary
        """
        return cls(**obj)

    @classmethod
    def validate_dict(cls, dictionary):
        return cls.get_receiving_schema()(dictionary)


class Sendable(SDKObject, metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def get_sending_schema():
        raise NotImplemented

    def to_json(self):
        """
        :return: a json representation of the object
        """
        return self.__dict__

    def validate_obj(self):
        return self.__class__.get_sending_schema()(self.__dict__)
