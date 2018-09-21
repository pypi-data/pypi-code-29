#!/usr/bin/env python
import unittest

from gcloud.metric_data_upload_client.schema_builder import SchemaBuilder


class TestSchemaBuilder(unittest.TestCase):
  repeated_string_field = {
      'name': 'i_am_a_repeated_string',
      'mode': 'REPEATED',
  }

  string_field = {'name': 'i_am_a_string'}

  float_field = {'name': 'i_am_a_float', 'type': 'FLOAT'}

  def setUp(self):
    self.table_schema = [
        self.string_field,
        self.repeated_string_field,
        self.float_field,
        {
            'name': 'i_am_a_record',
            'type': 'RECORD',
            'fields': [self.string_field, self.float_field]
        },
        {
            'name': 'i_am_a_repeated_record',
            'type': 'RECORD',
            'mode': 'REPEATED',
            'fields': [self.string_field]
        },
    ]

  def test_build_schema(self):
    builder = SchemaBuilder()

    schema = builder.build_schema_field_list(self.table_schema)

    self.assertEqual(len(self.table_schema), len(schema))

    self.assert_on_expected_string_schema_field(schema)
    self.assert_on_expected_repeated_string_schema_field(schema)
    self.assert_on_expected_record_schema_field(schema)
    self.assert_on_expected_repeated_record_schema_field(schema)

  def assert_on_expected_string_schema_field(self, schema):
    string_field_index = self.table_schema.index(self.string_field)
    self.assertEqual(self.string_field['name'], schema[string_field_index].name)
    self.assertEqual('NULLABLE', schema[string_field_index].mode)
    self.assertEqual('STRING', schema[string_field_index].field_type)

  def assert_on_expected_repeated_string_schema_field(self, schema):
    repeated_string_field_index = self.table_schema.index(
        self.repeated_string_field)
    self.assertEqual(self.repeated_string_field['name'],
                     schema[repeated_string_field_index].name)
    self.assertEqual('REPEATED', schema[repeated_string_field_index].mode)
    self.assertEqual('STRING', schema[repeated_string_field_index].field_type)

  def assert_on_expected_record_schema_field(self, schema):
    record_field_index = 3
    record_subfield_len = 2
    self.assertEqual('i_am_a_record', schema[record_field_index].name)
    self.assertEqual('NULLABLE', schema[record_field_index].mode)
    self.assertEqual('RECORD', schema[record_field_index].field_type)

    record_subfields = schema[record_field_index].fields
    self.assertEqual(record_subfield_len, len(record_subfields))

    self.assertEqual(self.string_field['name'], record_subfields[0].name)
    self.assertEqual('NULLABLE', record_subfields[0].mode)
    self.assertEqual('STRING', record_subfields[0].field_type)

    self.assertEqual(self.float_field['name'], record_subfields[1].name)
    self.assertEqual('NULLABLE', record_subfields[1].mode)
    self.assertEqual('FLOAT', record_subfields[1].field_type)

  def assert_on_expected_repeated_record_schema_field(self, schema):
    record_field_index = 4
    record_subfield_len = 1
    self.assertEqual('i_am_a_repeated_record', schema[record_field_index].name)
    self.assertEqual('REPEATED', schema[record_field_index].mode)
    self.assertEqual('RECORD', schema[record_field_index].field_type)

    record_subfields = schema[record_field_index].fields
    self.assertEqual(record_subfield_len, len(record_subfields))

    self.assertEqual(self.string_field['name'], record_subfields[0].name)
    self.assertEqual('NULLABLE', record_subfields[0].mode)
    self.assertEqual('STRING', record_subfields[0].field_type)


if __name__ == '__main__':
  unittest.main()
