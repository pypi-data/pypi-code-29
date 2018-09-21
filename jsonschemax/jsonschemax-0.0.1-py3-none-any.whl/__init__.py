from jsonschemax.validation import Validator
from jsonschemax import keywords as kw
import pkgutil
import json

__all__ = ("draft7_validator",)


draft7_keyword_map = {
    "type": kw._type,
    "enum": kw._enum,
    "const": kw._const,
    "multipleOf": kw._multiple_of,
    "maximum": kw._maximum,
    "exclusiveMaximum": kw._exclusive_maximum,
    "minimum": kw._minimum,
    "exclusiveMinimum": kw._exclusive_minimum,
    "maxLength": kw._max_length,
    "minLength": kw._min_length,
    "pattern": kw._pattern,
    "items": kw._items,
    "additionalItems": kw._additional_items,
    "maxItems": kw._max_items,
    "minItems": kw._min_items,
    "uniqueItems": kw._unique_items,
    "contains": kw._contains,
    "maxProperties": kw._max_properties,
    "minProperties": kw._min_properties,
    "required": kw._required,
    "properties": kw._properties,
    "patternProperties": kw._pattern_properties,
    "additionalProperties": kw._additional_properties,
    "dependencies": kw._dependencies,
    "propertyNames": kw._property_names,
    "if": kw._if,
    "then": kw._then,
    "else": kw._else,
    "allOf": kw._all_of,
    "anyOf": kw._any_of,
    "oneOf": kw._one_of,
    "not": kw._not,
}

draft7_meta_schema = json.loads(
    pkgutil.get_data("jsonschemax", "meta_schemas/draft-07.json").decode("utf-8")
)

draft7_validator = Validator(draft7_keyword_map, draft7_meta_schema)
