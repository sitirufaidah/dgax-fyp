from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000), nullable=False)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    date = db.Column(db.DateTime)
    hydrogen = db.Column(db.Integer)
    methane = db.Column(db.Integer)
    acetylene = db.Column(db.Integer)
    ethylene = db.Column(db.Integer)
    ethane = db.Column(db.Integer)
    carbonmonoxide = db.Column(db.Integer)
    carbondioxide = db.Column(db.Integer)
    tdcg = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')
    records = db.relationship('Record')

#    def __init__(self, email, password, first_name):
#        self.email = email
#        self.password = password
#        self.first_name = first_name
