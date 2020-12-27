from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

# user model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(55), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    registration_date = db.Column(
        db.DateTime(), default=datetime.utcnow, index=True)
    courses = db.relationship("Course", backref="student", lazy="dynamic")

    def __repr__(self):
        return "<User {}".format(self.username)

    def setPassword(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# course model
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(125), index=True, unique=True)
    meeting_date = db.Column(db.DateTime())
    price = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    sessions = db.relationship("Session", backref="cours", lazy="dynamic")

# session model
class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(), index=True)
    paid = db.Column(db.Boolean)
    lesson_id = db.Column(db.Integer, db.ForeignKey("course.id"))
