from marshmallow import Schema, fields


class MovieSchema(Schema):
    id = fields.Int()
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    trailer = fields.Str(required=True)
    year = fields.Int(required=True)
    rating = fields.Float(required=True)
    genre_id = fields.Int(required=True)
    director_id = fields.Int(required=True)