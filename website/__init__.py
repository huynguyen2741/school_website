from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'temp key'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .models import Course, Student

    create_database(app)

    from .auth import auth
    # from .models import Student, Course
    app.register_blueprint(auth, url_prefix='/')

    return app


def create_database(app):
    # if the database does not exist in "website" folder, create it.
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Database created')
