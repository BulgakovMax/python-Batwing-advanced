from marshmallow import Schema, fields
from marshmallow.validate import Length


class GamesSchema(Schema):
    id = fields.Integer(required=True, dump_only=True)
    title = fields.String(required=True, validate=Length(min=2, max=99))
