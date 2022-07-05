from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String, nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    hydrogen = db.Column(db.Integer, nullable=False)
    methane = db.Column(db.Integer, nullable=False)
    acetylene = db.Column(db.Integer, nullable=False)
    ethylene = db.Column(db.Integer, nullable=False)
    ethane = db.Column(db.Integer, nullable=False)
    carbonmonoxide = db.Column(db.Integer, nullable=False)
    carbondioxide = db.Column(db.Integer, nullable=False)
    tdcg = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    username = db.Column(db.String(150))
    records = db.relationship('Record')

    def __init__(self, email, password, username):
        self.email = email
        self.password = password
        self.username = username
