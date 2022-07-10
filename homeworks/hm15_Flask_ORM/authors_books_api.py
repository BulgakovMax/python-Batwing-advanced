from flask import Blueprint, jsonify
import http

from database import db
from models.authors import Authors
from models.authors_books import AuthorsBooks
from models.books import Books
from serializers.author import AuthorsSchema
from serializers.author_book import AuthorsBooksSchema
from serializers.book import BooksSchema

author_book_router = Blueprint('author_book', __name__, url_prefix='/author_book')


@author_book_router.route('')
def get():
    author_book_schema = AuthorsBooksSchema()

    authors_books = AuthorsBooks.query.order_by(AuthorsBooks.id)
    authors_books_json = author_book_schema.dump(authors_books, many=True)
    return jsonify(authors_books_json)


@author_book_router.route("/<int:author_id>/<int:book_id>", methods=["POST"])
def create(author_id, book_id):
    author_schema = AuthorsSchema()
    author = Authors.query.filter_by(id=author_id).first()

    book_schema = BooksSchema()
    book = Books.query.filter_by(id=book_id).first()

    schema = AuthorsBooksSchema()

    if not author is None and not book is None:
        book_json = book_schema.dump(book)
        author_json = author_schema.dump(author)
        new_author_book = AuthorsBooks(name=author_json["name"], second_name=author_json["second_name"],
                                       title=book_json["title"])
        db.session.add(new_author_book)
        db.session.commit()

        new_author_book_json = schema.dump(new_author_book)

        return jsonify(new_author_book_json)
    elif author is None:
        return "Author with this id does`t exist"
    elif book is None:
        return "Book with this id does`t exist"


@author_book_router.route("/<int:id_>", methods=["DELETE"])
def delete(id_):
    authors_books = AuthorsBooks.query.filter_by(id=id_).first()
    if not authors_books is None:
        AuthorsBooks.query.filter_by(id=id_).delete()
        db.session.commit()
        return {}, http.HTTPStatus.NO_CONTENT
    else:
        return "Incorrect data", http.HTTPStatus.BAD_REQUEST
