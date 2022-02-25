# from flask import Blueprint
# from flask_login import UserMixin
from . import db
# from sqlalchemy.ext.declarative import declarative_base

# models = Blueprint('models', __name__)
# Base = declarative_base()


student_course = db.Table('student_course',
                          db.Column('student_id', db.ForeignKey(
                              'student.id'), primary_key=True),
                          db.Column('course_id', db.ForeignKey('course.id'), primary_key=True))


class Course (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))


class Student (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    # role = db.Column(db.String(150))
    taking = db.relation(
        'Course', secondary=student_course, backref='students')
