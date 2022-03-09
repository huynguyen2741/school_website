from flask import Blueprint, render_template, request, flash
from . import db
from .models import Student, Course
from flask_login import login_user, logout_user, current_user, login_required


auth = Blueprint('auth', __name__)
isAuthenticated = False


# @login_required
@auth.route('/logout')
def logout():
    logout_user()
    return render_template('index.html')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    student = Student.query.filter_by(username=username).first()
    if student:
        if password == student.password:
            # login_user(student)
            isAuthenticated = True
            flash('login success')
            # render_template("index.html", isAuthenticated=True,
            #                 username=username, password=password)
        else:
            flash('wrong password')
    else:
        flash('No user found')
    return render_template("login.html", isAuthenticated=True,
                           username=username, password=password)


@auth.route('/')
def home():
    courses = Course.query.filter().all()
    return render_template("index.html", courses=courses)


@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        # role = request.form.get('role')

        # check if student exist
        if Student.query.filter_by(username=username).first():
            flash("Student exist", category='error')
        elif len(username) < 2:
            flash("username can\'t be less than 2 characters", category='error')
        elif password1 != password2:
            flash("Password does not match", category='error')
        elif len(password1) < 5:
            flash("Password can\'t be less than 5 characters", category='error')
        else:
            new_student = Student(username=username, password=password1)
            db.session.add(new_student)
            db.session.commit()
            # login_user(new_student, remember=True)
            isAuthenticated = True
            flash('Sign up success', category='success')
            return render_template("index.html", isAuthenticated=True,
                                   username=username, password=password1)
    return render_template("sign_up.html")
