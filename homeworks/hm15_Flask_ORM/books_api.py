import http

from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from database import db
from models.books import Books
from serializers.book import BooksSchema

book_router = Blueprint('book', __name__, url_prefix='/book')


@book_router.route('')
def get():
    book_schema = BooksSchema()

    books = Books.query.order_by(Books.title)
    books_json = book_schema.dump(books, many=True)
    return jsonify(books_json)


@book_router.route('/<int:id_>')
def retrieve(id_):
    book_schema = BooksSchema()
    book = Books.query.filter_by(id=id_).first()
    book_json = book_schema.dump(book)
    return jsonify(book_json)


@book_router.route('', methods=['POST'])
def create():
    data = request.get_json(force=True)

    schema = BooksSchema()
    try:
        book_data = schema.load(data)
        new_book = Books(title=book_data['title'], genre=book_data['genre'])
        db.session.add(new_book)
        db.session.commit()

        new_book_json = schema.dump(new_book)
    except ValidationError as e:
        return {'errors': e.messages}, http.HTTPStatus.UNPROCESSABLE_ENTITY

    return new_book_json


@book_router.route('/<int:id_>', methods=['PUT'])
def update(id_):
    data = request.get_json(force=True)

    schema = BooksSchema()
    try:
        book_data = schema.load(data)
        book = Books.query.filter_by(id=id_).first()
        book.title = book_data['title']
        db.session.add(book)
        db.session.commit()

        new_book_json = schema.dump(book)
    except ValidationError as e:
        return {'errors': e.messages}, http.HTTPStatus.UNPROCESSABLE_ENTITY

    return new_book_json


@book_router.route('/<int:id_>', methods=['DELETE'])
def delete(id_):
    Books.query.filter_by(id=id_).delete()
    db.session.commit()
    return {}, http.HTTPStatus.NO_CONTENT
