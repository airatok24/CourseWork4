from marshmallow import Schema, fields


class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)