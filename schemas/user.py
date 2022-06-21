from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Int()
    email = fields.Str(required=True)
    password = fields.Str(required=True)
    role = fields.Str(required=True)
    name = fields.Str()
    surname = fields.Str()
    favorite_genre = fields.Str()