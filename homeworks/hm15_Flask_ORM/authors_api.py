import http

from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from database import db
from models.authors import Authors
from serializers.author import AuthorsSchema

author_router = Blueprint('author', __name__, url_prefix='/author')


@author_router.route('')
def get():
    author_schema = AuthorsSchema()

    authors = Authors.query.order_by(Authors.name)
    authors_json = author_schema.dump(authors, many=True)
    return jsonify(authors_json)


@author_router.route('/<int:id_>')
def retrieve(id_):
    author_schema = AuthorsSchema()
    author = Authors.query.filter_by(id=id_).first()
    author_json = author_schema.dump(author)
    return jsonify(author_json)


@author_router.route('', methods=['POST'])
def create():
    data = request.get_json(force=True)

    schema = AuthorsSchema()
    try:
        author_data = schema.load(data)
        new_author = Authors(name=author_data['name'], second_name=author_data['second_name'],
                             country=author_data['country'])
        db.session.add(new_author)
        db.session.commit()

        new_author_json = schema.dump(new_author)
    except ValidationError as e:
        return {'errors': e.messages}, http.HTTPStatus.UNPROCESSABLE_ENTITY

    return new_author_json


@author_router.route('/<int:id_>', methods=['PUT'])
def update(id_):
    data = request.get_json(force=True)

    schema = AuthorsSchema()
    try:
        author_data = schema.load(data)
        author = Authors.query.filter_by(id=id_).first()
        author.name = author_data['name']
        db.session.add(author)
        db.session.commit()

        new_author_json = schema.dump(author)
    except ValidationError as e:
        return {'errors': e.messages}, http.HTTPStatus.UNPROCESSABLE_ENTITY

    return new_author_json


@author_router.route('/<int:id_>', methods=['DELETE'])
def delete(id_):
    Authors.query.filter_by(id=id_).delete()
    db.session.commit()
    return {}, http.HTTPStatus.NO_CONTENT
