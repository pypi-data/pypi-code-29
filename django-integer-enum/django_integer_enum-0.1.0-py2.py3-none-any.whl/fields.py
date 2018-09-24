# -*- coding: utf-8 -*-

from django.db import models
from django.core.exceptions import ValidationError

from .enums import Enum


class EnumIntegerField(models.fields.IntegerField):

    description = "An extended IntegerField that validates an Enum"

    def __init__(self, *args, **kwargs):
        self.enum_choices = kwargs.pop('enum_choices', None)
        if self.enum_choices and not isinstance(self.enum_choices(), Enum):
            raise TypeError("enum_choices instance must be of type {}.".format(Enum.__name__))
        if self.enum_choices is not None:
            kwargs['choices'] = self.enum_choices.choices()
            kwargs['db_index'] = kwargs.pop('db_index', True)
            kwargs['default'] = kwargs.pop('default', self.enum_choices.DEFAULT)
        super(EnumIntegerField, self).__init__(*args, **kwargs)

    def validate_input(self, value):
        if not self.enum_choices.is_in_values(value):
            raise ValidationError("Input for field '{}' is invalid.".format(self.attname))

    @staticmethod
    def validate_fields(meta_fields, dict_fields):
        fields = [field for field in meta_fields if isinstance(field, EnumIntegerField)]
        for field in fields:
            value = dict_fields.get(field.name)
            field.validate_input(value)