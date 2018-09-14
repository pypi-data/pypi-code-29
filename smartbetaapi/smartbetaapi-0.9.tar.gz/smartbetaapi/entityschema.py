from marshmallow import Schema, fields

class EntitySchema(Schema):
    entity_id = fields.Integer(data_key="entityId")
    entity_type = fields.Integer(data_key="entityType")
    entity_type_name = fields.String(data_key="entityTypeName")
    entity_name = fields.String(data_key="entityName", allow_none=True)

