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
            raise TypeError('"data" should be dict or StudyGroup')

    @classmethod
    def deserialize(cls, data: dict):
        serializer = cls._get_serializer(data)
        if serializer.is_valid():
            return cls(**serializer.validated_data)
        else:
            raise ValueError('Invalid data')