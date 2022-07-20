from database import db


class Games(db.Model):
    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(99), nullable=False, unique=True)
