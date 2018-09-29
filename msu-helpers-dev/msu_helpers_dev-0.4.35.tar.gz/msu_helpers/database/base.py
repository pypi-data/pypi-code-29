#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models


class SerializableModel(models.Model):

    _serializer = None

    class Meta:
        abstract = True

    @property
    def serialized(self) -> dict:
        return self.serializer.data

    @property
    def serializer(self):
        if self._serializer is None:
            self._serializer = self._get_serializer(self)
        return self._serializer

    @classmethod
    def _get_serializer(cls, data):
        from . import serializers
        serializer_class = serializers.get(cls.__name__)
        if isinstance(data, cls):
            return serializer_class(data)
        elif isinstance(data, dict):
            return serializer_class(data=data)
        else:
            raise TypeError(f'"data" should be dict or {cls.__name__}')

    @classmethod
    def deserialize(cls, data: dict):
        # serializer = cls._get_serializer(data)
        # if serializer.is_valid():
        #     return cls(**serializer.validated_data)
        # else:
        #     raise ValueError('Invalid data')
        pk: int = data.get('id', 0)
        entry: cls = cls() if (pk <= 0 or not cls.exists(pk)) else cls.objects.get(pk=pk)
        attr_list: list = [attr for attr in dir(entry) if attr[0] != '_' and attr != 'id']

        for attr in attr_list:
            entry.__setattr__(
                attr,
                data.get(
                    attr,
                    entry.__getattribute__(attr)
                )
            )

        return entry

    @classmethod
    def exists(cls, pk: int):
        if pk is None or pk <= 0:
            raise ValueError('Invalid primary key')

        return cls.objects.filter(pk=pk).exists()
