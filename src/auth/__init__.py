from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

from src.models.user import User
from src.database.todolist import db


def create_user(username, email, password):
    password = generate_password_hash(password)
    new_user = User(username=username, email=email, password=password)

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
