from jsonschemax.errors import InvalidSchemaError


class Validator:
    def __init__(self, keyword_map: dict, meta_schema: dict) -> None:
        self._keyword_map = keyword_map
        self._meta_schema = meta_schema

    def check_schema(self, schema):
        if not self.validate(
            schema=self._meta_schema, instance=schema, check_schema=False
        ):
            raise InvalidSchemaError()

    def validate(self, schema, instance, *, check_schema=True) -> bool:
        if check_schema:
            self.check_schema(schema)

        assert isinstance(schema, (bool, dict))
        if isinstance(schema, bool):
            return schema
        else:
            for keyword_name, value in schema.items():
                # A JSON Schema MAY contain properties which are not schema keywords.
                # Unknown keywords SHOULD be ignored.
                # http://json-schema.org/latest/json-schema-core.html#rfc.section.4.3.1
                if keyword_name in self._keyword_map:
                    keywork_func = self._keyword_map[keyword_name]
                    if not keywork_func(value, instance, validator=self):
                        return False
            return True
