from jsonschemax.errors import InvalidSchemaError
from jsonschemax import types

type_map = {
    "null": types.is_null,
    "boolean": types.is_boolean,
    "object": types.is_object,
    "array": types.is_array,
    "number": types.is_number,
    "string": types.is_string,
    "integer": types.is_integer,
}
