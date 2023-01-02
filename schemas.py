from marshmallow import Schema, fields, validate


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True, validate=validate.Length(min=1))


class CategorySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1))


class RecordQuerySchema(Schema):
    user_id = fields.Int(required=True, validate=validate.Range(min=1))
    category_id = fields.Int(validate=validate.Range(min=1))


class RecordSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True, validate=validate.Range(min=1))
    category_id = fields.Int(required=True, validate=validate.Range(min=1))
    amount = fields.Float(required=True, validate=validate.Range(min=0))


class AccountSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True, validate=validate.Range(min=1))
    balance = fields.Float(required=True, validate=validate.Range(min=0))
