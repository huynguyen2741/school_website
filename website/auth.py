from flask import Blueprint, render_template, request, flash
from . import db
from .models import Student
from flask_login import login_user, logout_user, current_user


auth = Blueprint('auth', __name__)


@auth.route('/')
def home():
    return render_template("index.html")
    # return "<h1>hi</h1>"


@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        # role = request.form.get('role')

        if len(username) < 2:
            flash("username can\'t be less than 2 characters", category='error')
        elif password1 != password2:
            flash("Password does not match", category='error')
        elif len(password1) < 5:
            flash("Password can\'t be less than 5 characters", category='error')
        else:
            new_student = Student(username=username, password=password1)
            db.session.add(new_student)
            db.session.commit()
            flash('Sign up success', category='success')
    return render_template("sign_up.html")
