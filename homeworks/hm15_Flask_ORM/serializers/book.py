from marshmallow import Schema, fields
from marshmallow.validate import Length


class BooksSchema(Schema):
    id = fields.Integer(required=True, dump_only=True)
    title = fields.String(required=True, validate=Length(min=2, max=100))
    genre = fields.String(required=True, validate=Length(min=2, max=100))