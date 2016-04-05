from cfblog2 import db


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Unicode(length=128))
    password = db.Column(db.Unicode(length=128))
