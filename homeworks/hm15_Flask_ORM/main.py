from flask import Flask

from config import Config
from database import db
from authors_api import author_router
from authors_books_api import author_book_router
from books_api import book_router


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    app.register_blueprint(author_router)
    app.register_blueprint(author_book_router)
    app.register_blueprint(book_router)
    return app


def setup_db(app):
    with app.app_context():
        db.create_all()
        db.session.commit()


if __name__ == '__main__':
    app = create_app()
    setup_db(app)
    app.run(host="0.0.0.0")
