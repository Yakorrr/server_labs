from files.imports import Schema, fields


class UserSchema(Schema):
    ID = fields.Str(dump_only=True)
    Username = fields.Str(required=True)


class CategorySchema(Schema):
    ID = fields.Int(dump_only=True)
    Name = fields.Str(required=True)


class RecordQuery(Schema):
    User_ID = fields.Str(required=True)
    Category_ID = fields.Str()


class RecordSchema(Schema):
    ID = fields.Str(dump_only=True)
    User_ID = fields.Str(required=True)
    Category_ID = fields.Str(required=True)
    Amount = fields.Float(required=True)
