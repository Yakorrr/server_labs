from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Str(dump_only=True)
    username = fields.Str(required=True)


class CategorySchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)


class RecordSchema(Schema):
    id = fields.Str(dump_only=True)
    username = fields.Str(required=True)
    category = fields.Str(required=True)
    amount = fields.Float(required=True)
