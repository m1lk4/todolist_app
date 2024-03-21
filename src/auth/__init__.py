from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

from src.models.user import User
from src.database.todolist import db


def create_user(name, email, password):
    password = generate_password_hash(password)
    new_user = User(name=name, email=email, password=password)

    db.session.add(new_user)
    db.session.commit()


def has_account(name, email=None):
    return (
        User.query.filter_by(name=name).first()
        or User.query.filter_by(email=email).first()
    )


def check_password(name, password):
    user = User.query.filter_by(name=name).first()

    return check_password_hash(user.password, password)
