from marshmallow import Schema, fields
from marshmallow.validate import Length


class UserSchema(Schema):
    id = fields.Integer(required=True, dump_only=True)
    email = fields.Email(required=True, validate=Length(min=10, max=355))


class GamesSchema(Schema):
    id = fields.Integer(required=True, dump_only=True)
    title = fields.String(required=True, validate=Length(min=2, max=99))
