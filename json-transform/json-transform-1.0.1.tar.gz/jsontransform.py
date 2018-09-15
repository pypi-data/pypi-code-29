# -*- coding: utf-8 -*-

import collections
import datetime
import inspect
import itertools
import json
import re
import sys

from dateutil import parser
from decorator import decorator

__author__ = "Peter Morawski"
__version__ = "1.0.1"

_DATE_FORMAT_REGEX = r"^([0-9]{4}-[0-9]{1,2}-[0-9]{1,2}|[0-9]{8})$"
_DATETIME_FORMAT_REGEX = r"^([0-9]{4}-[0-9]{2}-[0-9]{2}|[0-9]{8})T([0-9]{2}(:[0-9]{2})?(:[0-9]{2})?|[0-9]{6}|[0-9]{4}" \
                         r")(\.[0-9]{3})?(Z|((\+|-)[0-9]{2}:?([0-9]{2})?))$"

_JSON_FIELD_NAME = "_json_field_name"
_JSON_FIELD_REQUIRED = "_json_field_required"
_JSON_FIELD_MODE = "_json_field_mode"

_PY2 = 2


class ConfigurationError(Exception):
    """
    The passed :class:`JSONObject` was not configured correctly.
    """
    pass


class ConstraintViolationError(Exception):
    """
    A constraint which has been defined on a :func:`field` has been violated.
    """
    pass


class MissingObjectError(Exception):
    """
    No :class:`JSONObject` which matches the signature of the passed JSON document could be found.
    """
    pass


class JSONObject(object):
    """
    Every entity/class which is intended to be encodable and decodable to a JSON document **MUST** inherit/extend this
    class.
    """
    pass


class FieldMode(object):
    """
    The :class:`FieldMode` describes the behavior of the :func:`field` during the encoding/decoding process. It marks
    that the :func:`field` should not be in the JSON document when the :class:`JSONObject` is encoded but it should be
    decoded and vice versa.
    """
    ENCODE = "e"
    """
    Indicates that the :func:`field` can **ONLY** be encoded.
    """

    DECODE = "d"
    """
    Indicates that the :func:`field` can **ONLY** be decoded.
    """

    ENCODE_DECODE = "ed"
    """
    Indicates that the :func:`field` can be encoded **AND** decoded.
    """


@decorator
def field(func, field_name=None, required=False, mode=FieldMode.ENCODE_DECODE, *args, **kwargs):
    """
    The :func:`field` decorator is used to mark that a :class:`property` inside a :class:`JSONObject` is a JSON field so
    it will appear in the JSON document when the :class:`JSONObject` is encoded or decoded.

    .. note::
        * The brackets `()` after the @field decorator are important even when no additional arguments are given
        * The :class:`property` decorator must be at the top or else the function won't be recognized as a property

    :param func: The method which is decorated with @property decorator.
    :param field_name: (optional) A name/alias for the field (how it should appear in the JSON document) since by \
    default the name of the property will be used.
    :param required: (optional) A `bool` which indicates if this field is mandatory for the decoding process. When a \
    field which is marked as required does NOT exist in the JSON document from which the JSONObject is decoded from, \
    a ConstraintViolationError will be raised. (False by default)
    :param mode: (optional) The FieldMode of the field. (ENCODE_DECODE by default)
    """
    if not hasattr(func, _JSON_FIELD_NAME):
        setattr(func, _JSON_FIELD_NAME, field_name or func.__name__)
    if not hasattr(func, _JSON_FIELD_REQUIRED):
        setattr(func, _JSON_FIELD_REQUIRED, required)
    if not hasattr(func, _JSON_FIELD_MODE):
        setattr(func, _JSON_FIELD_MODE, mode)

    return func(*args, **kwargs)


class JSONEncoder(object):
    """
    This class offers methods to encode a :class:`JSONObject` into JSON document. A :class:`JSONObject` can be encoded
    to

    - an `str`
    - a `dict`
    - a `write()` supporting file-like object
    """
    DATE_FORMAT = "%Y-%m-%d"
    DATETIME_TZ_FORMAT = "%Y-%m-%dT%H:%M:%S%z"
    DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"

    def to_json_str(self, json_object):
        """
        Encode an instance of a :class:`JSONObject` into an `str` which contains a JSON document.

        :param json_object: The instance of the JSONObject which should be encoded

        :raises ConfigurationError: When the JSONObject of which an instance was passed does NOT define any JSON fields
        :raises TypeError: When the type of a field in the JSONObject is not encodable

        :return: An str which contains the JSON representation of the passed JSONObject
        """
        return json.dumps(self.to_json_dict(json_object))

    def to_json_file(self, json_object, json_file):
        """
        Encode an instance of a :class:`JSONObject` and write the result into a `write()` supporting file-like object.

        :param json_object: The instance of the JSONObject which should be encoded
        :param json_file: A write() supporting file-like object

        :raises ConfigurationError: When the JSONObject of which an instance was passed does NOT define any JSON fields
        :raises TypeError: When the type of a field in the JSONObject is not encodable
        """
        json.dump(self.to_json_dict(json_object), json_file)

    def to_json_dict(self, json_object):
        """
        Encode an instance of a :class:`JSONObject` into a python `dict`.

        :param json_object: The instance of the JSONObject which should be encoded

        :raises ConfigurationError: When the JSONObject of which an instance was passed does NOT define any JSON fields
        :raises TypeError: When the type of a field in the JSONObject is not encodable

        :return: A dict which represents the passed JSONObject and is JSON conform
        """
        result = {}
        properties = _JSONCommon.get_decorated_properties(json_object)
        if not properties.keys():
            raise ConfigurationError("The class doesn't define any fields which can be serialized into JSON")

        for key in properties.keys():
            property_value = properties[key].fget(json_object)

            field_mode = _JSONFieldAttributes.get_mode(properties[key].fget)
            if field_mode == FieldMode.ENCODE or field_mode == FieldMode.ENCODE_DECODE:
                result[key] = self._get_sanitized_value(property_value)

        return result

    def _get_sanitized_value(self, value):
        """
        Sanitizes a value so that it can be encoded to a JSON document.

        :param value: The value which should be be sanitized

        :raises TypeError: When the value is not JSON encodable

        :return: The sanitized value
        """
        if value is None:
            return value
        elif _JSONCommon.value_is_simple_type(value):
            return value
        elif isinstance(value, dict):
            result = {}
            for key in value.keys():
                result[key] = self._get_sanitized_value(value[key])

            return result
        elif _JSONCommon.value_not_str_and_iterable(value):
            result = []
            for item in value:
                result.append(self._get_sanitized_value(item))

            return result
        elif isinstance(value, JSONObject):
            return dumpd(value)
        elif isinstance(value, datetime.datetime):
            if value.tzinfo:
                return value.strftime(self.DATETIME_TZ_FORMAT)
            else:
                return value.strftime(self.DATETIME_FORMAT)
        elif isinstance(value, datetime.date):
            return value.strftime(self.DATE_FORMAT)
        else:
            raise TypeError("The object type `{}` is not JSON encodable".format(type(value)))


class JSONDecoder(object):
    """
    This class offers methods to decode a JSON document into a :class:`JSONObject`. A :class:`JSONObject` can be decoded
    from

    - an `str`
    - a `dict`
    - a `write()` supporting file-like object
    """
    _KEY_OCCURRENCES = "occurrences"
    _KEY_OBJECT = "object"
    _KEY_PROPERTIES_AMOUNT = "properties_amount"

    def from_json_str(self, json_str, target=None):
        """
        Decode an `str` into a :class:`JSONObject`. The `str` **MUST** contain a JSON document.

        :param json_str: The str which should be decoded
        :param target: (optional) The type of the target JSONObject into which this str should be decoded. When this \
        is empty then the target JSONObject will be searched automatically

        :raises ConfigurationError: When the target JSONObject does NOT define any JSON fields
        :raises TypeError: When the signature of the passed target did NOT match the signature of the JSON document \
        which was inside the passed str i.e. they had no fields in common
        :raises MissingObjectError: When no target JSONObject was specified AND no matching JSONObject could be found
        :raises ConstraintViolationError: When a field of the JSON document which was inside the str violated a \
        constraint which is defined on the target JSONObject e.g. a required field is missing

        :return: A JSONObject which matched the signature of the JSON document from the str and with the values of it
        """
        return self.from_json_dict(json.loads(json_str), target)

    def from_json_file(self, json_file, target=None):
        """
        Decode a `read()` supporting file-like object into a :class:`JSONObject`. The file-like object **MUST** contain
        a valid JSON document.

        :param json_file: The read() supporting file-like object which should be decoded into a JSONObject
        :param target: (optional) The type of the target JSONObject into which this file-like object should be \
        decoded. When this is empty then the target JSONObject will be searched automatically

        :raises ConfigurationError: When the target JSONObject does NOT define any JSON fields
        :raises TypeError: When the signature of the passed target did NOT match the signature of the JSON document \
        which was read from the passed file-like object i.e. they had no fields in common
        :raises MissingObjectError: When no target JSONObject was specified AND no matching JSONObject could be found
        :raises ConstraintViolationError: When a field of the JSON document which was read from the file-like object \
        violated a constraint which is defined on the target JSONObject e.g. a required field is missing

        :return: A JSONObject which matched the signature of the JSON document which the read() supporting file-like \
        object returned and with the values of it
        """
        return self.from_json_dict(json.load(json_file), target)

    def from_json_dict(self, json_dict, target=None):
        """
        Decode a python `dict` into a :class:`JSONObject`. The `dict` **MUST** be JSON conform so it cannot contain
        other object instances.

        :param json_dict: The dict which should be decoded
        :param target: (optional) The type of the target JSONObject into which this dict should be decoded. When this \
        is empty then the target JSONObject will be searched automatically

        :raises ConfigurationError: When the target JSONObject does NOT define any JSON fields
        :raises TypeError: When the signature of the passed target did NOT match the signature of the passed dict i.e. \
        they had no fields in common
        :raises MissingObjectError: When no target JSONObject was specified AND no matching JSONObject could be found
        :raises ConstraintViolationError: When a field inside the dict violated a constraint which is defined on the \
        target JSONObject e.g. a required field is missing

        :return: A JSONObject which matched the signature of the dict and with the values of it
        """
        if target is None:
            target = self._get_most_matching_json_object(json_dict)

        result = target()
        self.validate_required_fields(result, json_dict)
        properties = _JSONCommon.get_decorated_properties(result)
        if not properties:
            raise ConfigurationError("The JSONObject `{}` doesn't define any fields".format(target.__name__))
        if all(properties.get(key) is None for key in json_dict.keys()):
            raise TypeError("No matching fields found to build a JSONObject with the type `{}`".format(type(result)))

        for key in properties.keys():
            field_mode = _JSONFieldAttributes.get_mode(properties[key].fget)

            if field_mode == FieldMode.DECODE or field_mode == FieldMode.ENCODE_DECODE:
                value = self._revert_sanitized_value(json_dict.get(key))
                properties[key].fset(result, value)

        return result

    def _revert_sanitized_value(self, sanitized_value):
        """
        Revert the sanitization of a value *e.g.* passing a date `str` like '2018-08-09' would return a
        :class:`datetime.date` with the appropriate date.

        :param sanitized_value: The sanitized value which should be reverted

        :raises TypeError: When the sanitized value cannot be reverted
        :raises ValueError: When the passed value did not match the expectations e.g. a datetime.datetime - hour was 90

        :return: The reverted value of the sanitized value
        """
        if sanitized_value is None:
            return sanitized_value
        elif _JSONCommon.value_is_simple_type(sanitized_value):
            if isinstance(sanitized_value, str) or sys.version_info.major == _PY2 and isinstance(sanitized_value,
                                                                                                 unicode):
                if re.match(_DATE_FORMAT_REGEX, sanitized_value):
                    return parser.isoparse(sanitized_value).date()
                elif re.match(_DATETIME_FORMAT_REGEX, sanitized_value):
                    return parser.isoparse(sanitized_value)

            return sanitized_value
        elif isinstance(sanitized_value, dict):
            try:
                return loadd(sanitized_value)
            except MissingObjectError:
                pass

            return {key: self._revert_sanitized_value(sanitized_value[key]) for key in sanitized_value.keys()}
        elif isinstance(sanitized_value, list):
            result = []
            for item in sanitized_value:
                result.append(self._revert_sanitized_value(item))

            return result
        else:
            raise TypeError(
                "The sanitization for the object type `{}` cannot be reverted".format(type(sanitized_value))
            )

    def _get_most_matching_json_object(self, json_dict):
        """
        Given a `dict` get the :class:`JSONObject` which matches it the most.

        :param json_dict: The dict for which a JSONObject should be searched

        :raises MissingObjectError: When no matching JSONObject could be found

        :return: The type of the matching JSONObject
        """

        def search_by_json_object(json_object):
            result = []

            for obj in json_object.__subclasses__():
                property_occurrences = 0
                properties = _JSONCommon.get_decorated_properties(obj())

                for dict_property in json_dict.keys():
                    for json_object_property in properties.keys():
                        if dict_property == json_object_property:
                            property_occurrences += 1
                            break

                if property_occurrences:
                    result.append({
                        self._KEY_OCCURRENCES: property_occurrences,
                        self._KEY_OBJECT: obj,
                        self._KEY_PROPERTIES_AMOUNT: len(properties.keys())
                    })

                matching_sub_objects = search_by_json_object(obj)
                for matched_object in matching_sub_objects:
                    result.append(matched_object)

            return result

        matching_objects = search_by_json_object(JSONObject)
        if matching_objects:
            matching_objects = sorted(matching_objects, key=lambda x: x[self._KEY_OCCURRENCES], reverse=True)
            most_matching_objects = [
                item for item in next(itertools.groupby(matching_objects, lambda x: x[self._KEY_OCCURRENCES]))[1]
            ]

            # search if there is an object which has the exact same amount of properties as the passed dict
            for match in most_matching_objects:
                if match[self._KEY_PROPERTIES_AMOUNT] == len(json_dict.keys()):
                    return match[self._KEY_OBJECT]

            return most_matching_objects[0][self._KEY_OBJECT]

        raise MissingObjectError("No matching JSONObject could be found")

    @staticmethod
    def validate_required_fields(json_object, json_dict):
        """
        Validate if a `dict` which will be decoded satisfied all required fields of the :class:`JSONObject` into which
        it will be decoded.

        :param json_object: The instance of the JSONObject into which the dict will be decoded
        :param json_dict: The dict which should be validated

        :raises ConstraintValidationError: When a required field is missing
        """
        required_field_names = []
        properties = _JSONCommon.get_decorated_properties(json_object)
        for key in properties.keys():
            if _JSONFieldAttributes.get_required(properties[key].fget):
                required_field_names.append(key)

        for field_name in required_field_names:
            if field_name not in json_dict.keys():
                raise ConstraintViolationError(
                    "The field `{}` is missing in the object `{}`".format(field_name, json_object.__class__.__name__)
                )


class _JSONCommon(object):
    @classmethod
    def get_decorated_properties(cls, json_object):
        """
        Get all properties from a :class:`JSONObject` which are annotated with the :func:`field()` decorator.

        :param json_object: The instance of the JSONObject of which the decorated properties should be extracted

        :return: A `dict` containing all properties which are decorated with the field() decorator with the pattern \
        {"fieldName": <property getter function>}
        """
        result = {}

        for member in inspect.getmembers(type(json_object)):
            if isinstance(member[1], property):
                if hasattr(member[1].fget, "__wrapped__"):
                    member[1].fget(json_object)
                    wrapper = member[1].fget.__wrapped__

                    if _JSONFieldAttributes.get_field_name(wrapper):
                        result[_JSONFieldAttributes.get_field_name(wrapper)] = member[1]

        return result

    @classmethod
    def value_is_simple_type(cls, value):
        """
        Check if a value is a 'simple' type *i.e.* a type which does **NOT** require further work to be encoded/decoded.

        :param value: The value which should be checked

        :return: True if the type of the value is simple; False otherwise
        """
        result = (
                isinstance(value, str) or
                isinstance(value, int) or
                isinstance(value, float) or
                isinstance(value, bool)
        )

        if not result and sys.version_info.major == _PY2:
            result = isinstance(value, unicode)

        return result

    @classmethod
    def value_not_str_and_iterable(cls, value):
        """
        Check if the type of a value is **NOT** `str`/`unicode` and if the value **IS** iterable.

        :param value: The value which should be checked

        :return: True if the value is iterable and NOT an str/unicode; False otherwise
        """
        if sys.version_info.major == _PY2:
            if isinstance(value, unicode):
                return False

        if isinstance(value, str):
            return False

        return isinstance(value, collections.Iterable)


class _JSONFieldAttributes(object):
    @classmethod
    def get_field_name(cls, func):
        """
        Get the value of the _JSON_FIELD_NAME attribute of a method which is annotated with the :class:`property`
        and the :func:`field` decorator.

        :param func: The method which is annotated with the property and the field decorator

        :return: The name of the field/property (how it will appear in a JSON document)
        """
        return cls._get_field_attribute(func, _JSON_FIELD_NAME)

    @classmethod
    def get_required(cls, func):
        """
        Get the value of the _JSON_FIELD_REQUIRED attribute of a method which is annotated with the :class:`property`
        and the :func:`field` decorator.

        :param func: The method which is annotated with the property and the field decorator

        :return: True if the field/property is required: False otherwise
        """
        return cls._get_field_attribute(func, _JSON_FIELD_REQUIRED) or False

    @classmethod
    def get_mode(cls, func):
        """
        Get the value of the _JSON_FIELD_MODE attribute of a method which is annotated with the :class:`property` and
        the :func:`field` decorator.

        :param func: The method which is annotated with the property and the field decorator

        :return: The FieldMode of the field/property
        """
        return cls._get_field_attribute(func, _JSON_FIELD_MODE)

    @classmethod
    def _get_field_attribute(cls, func, attr_name):
        if hasattr(func, attr_name):
            return getattr(func, attr_name)

        if hasattr(func, "__wrapped__"):
            return cls._get_field_attribute(func.__wrapped__, attr_name)

        return None


_encoder = JSONEncoder()
_decoder = JSONDecoder()


def dump(json_object, json_file):
    """
    Shortcut for instantiating a new :class:`JSONEncoder` and calling the :func:`to_json_file` function.

    .. seealso::
        For more information you can look at the doc of :func:`JSONEncoder.to_json_file`.
    """
    _encoder.to_json_file(json_object, json_file)


def dumps(json_object):
    """
    Shortcut for instantiating a new :class:`JSONEncoder` and calling the :func:`to_json_str` function.

    .. seealso::
        For more information you can look at the doc of :func:`JSONEncoder.to_json_str`.
    """
    return _encoder.to_json_str(json_object)


def dumpd(json_object):
    """
    Shortcut for instantiating a new :class:`JSONEncoder` and calling the :func:`to_json_dict` function.

    .. seealso::
        For more information you can look at the doc of :func:`JSONEncoder.to_json_dict`.
    """
    return _encoder.to_json_dict(json_object)


def load(json_file, target=None):
    """
    Shortcut for instantiating a new :class:`JSONDecoder` and calling the :func:`from_json_file` function.

    .. seealso::
        For more information you can look at the doc of :func:`JSONDecoder.from_json_file`.
    """
    return _decoder.from_json_file(json_file, target)


def loads(json_str, target=None):
    """
    Shortcut for instantiating a new :class:`JSONDecoder` and calling the :func:`from_json_str` function.

    .. seealso::
        For more information you can look at the doc of :func:`JSONDecoder.from_json_str`.
    """
    return _decoder.from_json_str(json_str, target)


def loadd(json_dict, target=None):
    """
    Shortcut for instantiating a new :class:`JSONDecoder` and calling the :func:`from_json_dict` function.

    .. seealso::
        For more information you can look at the doc of :func:`JSONDecoder.from_json_dict`.
    """
    return _decoder.from_json_dict(json_dict, target)
