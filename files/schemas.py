from marshmallow import Schema, fields


class UserSchema(Schema):
    ID = fields.Str(dump_only=True)
    Username = fields.Str(required=True)


class CategorySchema(Schema):
    ID = fields.Str(dump_only=True)
    Name = fields.Str(required=True)


class RecordSchema(Schema):
    ID = fields.Str(dump_only=True)
    Username = fields.Str(required=True)
    Category = fields.Str(required=True)
    Amount = fields.Float(required=True)
