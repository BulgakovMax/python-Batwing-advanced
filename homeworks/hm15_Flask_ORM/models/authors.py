from database import db


class Authors(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    second_name = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)
