from marshmallow import Schema, fields


class GenreSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)