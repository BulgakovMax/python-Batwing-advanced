from main import db
from models.user import User, Games

if __name__ == '__main__':
    db.create_all()
    db.session.commit()
    db.session.add(User(email="andrii@gmail.com"))
    db.session.add(Games(title="7 Wonders"))
    db.session.commit()
    print("created tables")
