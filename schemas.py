from marshmallow import Schema, fields


class UserSchema(Schema):
    ID = fields.Int(dump_only=True)
    Username = fields.Str(required=True)


class CategorySchema(Schema):
    ID = fields.Int(dump_only=True)
    Name = fields.Str(required=True)


class RecordQuerySchema(Schema):
    User_ID = fields.Int(required=True)
    Category_ID = fields.Int()


class RecordSchema(Schema):
    ID = fields.Int(dump_only=True)
    User_ID = fields.Int(required=True)
    Category_ID = fields.Int(required=True)
    Amount = fields.Float(required=True)
