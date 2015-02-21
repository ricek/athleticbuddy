from datetime import datetime
from . import db

class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_id =  db.Column(db.Integer, db.ForeignKey('category.id'))
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'))
    instructor_id = db.Column(db.Integer, db.ForeignKey('instructor.id'))
    title = db.Column(db.String(128))
    time = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    note = db.Column(db.Text)

    def __repr__(self):
        return '<Activity %r>' % self.category

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    activities = db.relationship('Activity', backref='category', lazy='dynamic')

    def __repr__(self):
        return '<Category %r>' % self.name

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room = db.Column(db.Integer, unique=True)
    activities = db.relationship('Activity', backref='location', lazy='dynamic')

    def __repr__(self):
        return '<Location %r>' % self.room

class Instructor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(64))
    lname = db.Column(db.String(64))
    activities = db.relationship('Activity', backref='instructor', lazy='dynamic')

    def __repr__(self):
        return '<Category %r>' % self.lname
