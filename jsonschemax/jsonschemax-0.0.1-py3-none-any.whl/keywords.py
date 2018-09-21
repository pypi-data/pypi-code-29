"""
This module store all keyword definitions.

All keyword functions accept three params (`value`, `instance` and `validator`) and return `True` or `False` as the return of validation.

Param `value` is the value of this keyword in schema. Param `instance` is the part of the whole instance this keyword valid. For example, a validation with a schema `{type: "int"}` and an instance `10` will call `_type(10, "int", ...)` in the process.

Param `value` is considered to be valid against JSON Schema's definition. So schema should be test by meta-schema's before calling keyword function. For example, `_min_items(-1, [], ...)` should not happened because value for keyword "minItems" should be a non-negative integer based on meta-schema (http://json-schema.org/draft-07/schema)
"""

import itertools
import re
import typing

from jsonschemax.types import (
    is_array,
    is_boolean,
    is_integer,
    is_null,
    is_number,
    is_object,
    is_string,
)
from jsonschemax.utils import type_map
from jsonschemax.validation import Validator


def only_for(*type_checkers: typing.Callable[[typing.Any], bool]):
    """
    A keyword function decorated by this decorator will be ignored if all function in
    type_checkers do not satisfy `type_checker(instance) is False`.

    Most validation assertions only constrain values within a certain primitive type.
    When the type of the instance is not of the type targeted by the keyword, the
    instance is considered to conform to the assertion.

    For example, the "maxLength" keyword will only restrict certain strings (that are
    too long) from being valid. If the instance is a number, boolean, null, array, or
    object, then it is valid against this assertion.

    https://json-schema.org/latest/json-schema-validation.html#rfc.section.3.2.1
    """

    def wrapper(keyword_func):
        def new_keyword_func(value, instance, validator: Validator) -> bool:
            for type_checker in type_checkers:
                if type_checker(instance):
                    return keyword_func(value, instance, validator)
            return True

        return new_keyword_func

    return wrapper


def _type(value, instance, validator: Validator) -> bool:
    """
    type

    https://json-schema.org/draft-06/json-schema-validation.html#rfc.section.6.25
    https://json-schema.org/draft-07/json-schema-validation.html#rfc.section.6.1.1
    """
    assert isinstance(value, (str, list))
    if isinstance(value, str):
        return type_map[value](instance)
    else:
        for subvalue in value:
            if _type(subvalue, instance, validator):
                return True
        return False


def _enum(value, instance, validator: Validator) -> bool:
    """
    enum

    https://json-schema.org/draft-06/json-schema-validation.html#rfc.section.6.23
    https://json-schema.org/draft-07/json-schema-validation.html#rfc.section.6.1.2
    """
    assert isinstance(value, list) and len(value) >= 1
    for item in value:
        if instance == item:
            return True
    return False


def _const(value, instance, validator: Validator) -> bool:
    """
    const

    https://json-schema.org/draft-06/json-schema-validation.html#rfc.section.6.24
    https://json-schema.org/draft-07/json-schema-validation.html#rfc.section.6.1.3
    """
    return instance == value


# Validation Keywords for Numeric Instances (number and integer)


@only_for(is_number)
def _multiple_of(value, instance, validator: Validator) -> bool:
    """
    multipleOf

    https://json-schema.org/draft-06/json-schema-validation.html#rfc.section.6.1
    https://json-schema.org/draft-07/json-schema-validation.html#rfc.section.6.2.1
    """
    return (instance / value).is_integer()


@only_for(is_number)
def _maximum(value, instance, validator: Validator) -> bool:
    """
    maximum

    https://json-schema.org/draft-06/json-schema-validation.html#rfc.section.6.2
    https://json-schema.org/draft-07/json-schema-validation.html#rfc.section.6.2.2
    """
    return instance <= value


@only_for(is_number)
def _exclusive_maximum(value, instance, validator: Validator) -> bool:
    """
    exclusiveMaximum

    https://json-schema.org/draft-06/json-schema-validation.html#rfc.section.6.3
    https://json-schema.org/draft-07/json-schema-validation.html#rfc.section.6.2.3
    """
    return instance < value


@only_for(is_number)
def _minimum(value, instance, validator: Validator) -> bool:
    """
    minimum

    https://json-schema.org/draft-06/json-schema-validation.html#rfc.section.6.4
    https://json-schema.org/draft-07/json-schema-validation.html#rfc.section.6.2.4
    """
    return instance >= value


@only_for(is_number)
def _exclusive_minimum(value, instance, validator: Validator) -> bool:
    """
    exclusiveMinimum

    https://json-schema.org/draft-06/json-schema-validation.html#rfc.section.6.5
    https://json-schema.org/draft-07/json-schema-validation.html#rfc.section.6.2.5
    """
    return instance > value


# Validation Keywords for Strings


@only_for(is_string)
def _max_length(value, instance, validator: Validator) -> bool:
    """
    maxLength

    https://json-schema.org/draft-06/json-schema-validation.html#rfc.section.6.6
    https://json-schema.org/draft-07/json-schema-validation.html#rfc.section.6.3.1
    """
    return len(instance) <= value


@only_for(is_string)
def _min_length(value, instance, validator: Validator) -> bool:
    """
    minLength

    https://json-schema.org/draft-06/json-schema-validation.html#rfc.section.6.7
    https://json-schema.org/draft-07/json-schema-validation.html#rfc.section.6.3.2
    """
    return len(instance) >= value


@only_for(is_string)
def _pattern(value, instance, validator: Validator) -> bool:
    """
    pattern

    https://json-schema.org/draft-06/json-schema-validation.html#rfc.section.6.8
    https://json-schema.org/draft-07/json-schema-validation.html#rfc.section.6.3.3
    """
    match = re.match(value, instance)
    return bool(match)


# Validation Keywords for Arrays


@only_for(is_array)
def _items(value, instance, validator: Validator) -> bool:
    """
    items

    https://json-schema.org/draft-07/json-schema-validation.html#rfc.section.6.4.1
    https://json-schema.org/draft-06/json-schema-validation.html#rfc.section.6.9
    """
    if isinstance(value, list):
        for subschema, subinstance in zip(value, instance):
            if not validator.validate(subschema, subinstance, check_schema=False):
                return False
        return True
    else:
        for subinstance in instance:
            if not validator.validate(value, subinstance, check_schema=False):
                return False
        return True
    return len(instance) <= value


@only_for(is_array)
def _additional_items(value, instance, validator: Validator) -> bool:
    """
    additionalItems

    https://json-schema.org/draft-06/json-schema-validation.html#rfc.section.6.10
    https://json-schema.org/draft-07/json-schema-validation.html#rfc.section.6.4.2
    """
    return True  # TODO


@only_for(is_array)
def _max_items(value, instance, validator: Validator) -> bool:
    """
    maxItems

    https://json-schema.org/draft-06/json-schema-validation.html#rfc.section.6.11
    https://json-schema.org/draft-07/json-schema-validation.html#rfc.section.6.4.3
    """
    return len(instance) <= value


@only_for(is_array)
def _min_items(value, instance, validator: Validator) -> bool:
    """
    minItems

    https://json-schema.org/draft-06/json-schema-validation.html#rfc.section.6.12
    https://json-schema.org/draft-07/json-schema-validation.html#rfc.section.6.4.4
    """
    return len(instance) >= value


@only_for(is_array)
def _unique_items(value, instance, validator: Validator) -> bool:
    """
    uniqueItems

    https://json-schema.org/draft-06/json-schema-validation.html#rfc.section.6.13
    https://json-schema.org/draft-07/json-schema-validation.html#rfc.section.6.4.5
    """
    for a, b in itertools.combinations(instance, 2):
        if type(a) == type(b) and a == b:
            return False
    return True


@only_for(is_array)
def _contains(value, instance, validator: Validator) -> bool:
    """
    contains

    https://json-schema.org/draft-06/json-schema-validation.html#rfc.section.6.14
    https://json-schema.org/draft-07/json-schema-validation.html#rfc.section.6.4.6
    """
    for subinstance in instance:
        if validator.validate(value, subinstance, check_schema=False):
            return True
    return False


# Validation Keywords for Objects


@only_for(is_object)
def _max_properties(value, instance, validator: Validator) -> bool:
    """
    maxProperties

    https://json-schema.org/draft-06/json-schema-validation.html#rfc.section.6.15
    https://json-schema.org/draft-07/json-schema-validation.html#rfc.section.6.5.1
    """
    return len(instance.keys()) <= value


@only_for(is_object)
def _min_properties(value, instance, validator: Validator) -> bool:
    """
    minProperties

    https://json-schema.org/draft-06/json-schema-validation.html#rfc.section.6.16
    https://json-schema.org/draft-07/json-schema-validation.html#rfc.section.6.5.2
    """
    return len(instance.keys()) >= value


@only_for(is_object)
def _required(value, instance, validator: Validator) -> bool:
    """
    required

    https://json-schema.org/draft-06/json-schema-validation.html#rfc.section.6.17
    https://json-schema.org/draft-07/json-schema-validation.html#rfc.section.6.5.3
    """
    return all([key in instance for key in value])


@only_for(is_object)
def _properties(value, instance, validator: Validator) -> bool:
    """
    properties

    https://json-schema.org/draft-06/json-schema-validation.html#rfc.section.6.18
    https://json-schema.org/draft-07/json-schema-validation.html#rfc.section.6.5.4
    """
    for key, subschema in value.items():
        if key in instance:
            # `check_schema` is not need, because `subschema` is a part of `value` and
            # `value` is considered to be valid against JSON Schema's definition
            if not validator.validate(subschema, instance[key], check_schema=False):
                return False

    return True


@only_for(is_object)
def _pattern_properties(value, instance, validator: Validator) -> bool:
    """
    patternProperties

    https://json-schema.org/draft-06/json-schema-validation.html#rfc.section.6.19
    https://json-schema.org/draft-07/json-schema-validation.html#rfc.section.6.5.5
    """
    for key_pattern, subschema in value.items():
        for key in instance:
            if re.match(key_pattern, key):
                if not validator.validate(subschema, instance[key], check_schema=False):
                    return False

    return True


@only_for(is_object)
def _additional_properties(value, instance, validator: Validator) -> bool:
    """
    additionalProperties

    https://json-schema.org/draft-06/json-schema-validation.html#rfc.section.6.20
    https://json-schema.org/draft-07/json-schema-validation.html#rfc.section.6.5.6
    """
    return True  # TODO


@only_for(is_object)
def _dependencies(value, instance, validator: Validator) -> bool:
    """
    dependencies

    https://json-schema.org/draft-06/json-schema-validation.html#rfc.section.6.21
    https://json-schema.org/draft-07/json-schema-validation.html#rfc.section.6.5.7
    """
    return True  # TODO


@only_for(is_object)
def _property_names(value, instance, validator: Validator) -> bool:
    """
    propertyNames

    https://json-schema.org/draft-06/json-schema-validation.html#rfc.section.6.22
    https://json-schema.org/draft-07/json-schema-validation.html#rfc.section.6.5.8
    """
    for key in instance:
        if validator.validate(value, key, check_schema=False):
            return True
    return False


# Keywords for Applying Subschemas Conditionally


def _if(value, instance, validator: Validator) -> bool:
    """
    if

    https://json-schema.org/draft-07/json-schema-validation.html#rfc.section.6.6.1
    """
    return True  # TODO


def _then(value, instance, validator: Validator) -> bool:
    """
    then

    https://json-schema.org/draft-07/json-schema-validation.html#rfc.section.6.6.2
    """
    return True  # TODO


def _else(value, instance, validator: Validator) -> bool:
    """
    else

    https://json-schema.org/draft-07/json-schema-validation.html#rfc.section.6.6.3
    """
    return True  # TODO


# Keywords for Applying Subschemas With Boolean Logic


def _all_of(value, instance, validator: Validator) -> bool:
    """
    allOf

    https://json-schema.org/draft-06/json-schema-validation.html#rfc.section.6.26
    https://json-schema.org/draft-07/json-schema-validation.html#rfc.section.6.7.1
    """
    for subschema in value:
        if not validator.validate(subschema, instance, check_schema=False):
            return False
    return True


def _any_of(value, instance, validator: Validator) -> bool:
    """
    anyOf

    https://json-schema.org/draft-06/json-schema-validation.html#rfc.section.6.27
    https://json-schema.org/draft-07/json-schema-validation.html#rfc.section.6.7.2
    """
    for subschema in value:
        if validator.validate(subschema, instance, check_schema=False):
            return True
    return False


def _one_of(value, instance, validator: Validator) -> bool:
    """
    oneOf

    https://json-schema.org/draft-06/json-schema-validation.html#rfc.section.6.28
    https://json-schema.org/draft-07/json-schema-validation.html#rfc.section.6.7.3
    """
    return (
        len(
            [
                validator.validate(subschema, instance, check_schema=False)
                for subschema in value
            ]
        )
        == 1
    )


def _not(value, instance, validator: Validator) -> bool:
    """
    not

    https://json-schema.org/draft-06/json-schema-validation.html#rfc.section.6.29
    https://json-schema.org/draft-07/json-schema-validation.html#rfc.section.6.7.4
    """
    return not validator.validate(value, instance, check_schema=False)
