from flask import session, redirect, url_for, flash
from functools import wraps

from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

from src.models.user import User
from src.database.todolist import db


def create_user(username, name, lastname, email, password):
    password = generate_password_hash(password)
    new_user = User(
        username=username, name=name, lastname=lastname, email=email, password=password
    )

    db.session.add(new_user)
    db.session.commit()


def has_account(username, email=None):
    return (
        User.query.filter_by(username=username).first()
        or User.query.filter_by(email=email).first()
    )


def check_password(username, password):
    user = User.query.filter_by(username=username).first()

    return check_password_hash(user.password, password)


def get_user(username):
    user = User.query.filter_by(username=username).first()

    return user


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if "user_id" in session:
            return f(*args, **kwargs)
        else:
            flash("You need to login first", "danger")
            return redirect(url_for("auth.login"))

    return wrap
