from database import db


class AuthorsBooks(db.Model):
    __tablename__ = 'authors_books'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    second_name = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(100), nullable=False)

