from marshmallow import Schema, fields
from marshmallow.validate import Length


class AuthorsSchema(Schema):
    id = fields.Integer(required=True, dump_only=True)
    name = fields.String(required=True, validate=Length(min=2, max=100))
    second_name = fields.String(required=True, validate=Length(min=2, max=100))
    country = fields.String(required=True, validate=Length(min=2, max=100))

