from marshmallow import Schema, fields
from marshmallow.validate import Length


class AuthorsBooksSchema(Schema):
    id = fields.Integer(required=True, dump_only=True)
    name = fields.String(required=True, validate=Length(min=2, max=100))
    second_name = fields.String(required=True, validate=Length(min=2, max=100))
    title = fields.String(required=True, validate=Length(min=2, max=100))


