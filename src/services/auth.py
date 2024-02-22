from src.models.user_model import User
from src.database.todolist_db import db


def create_user(name, email, password):
    new_user = User(name=name, email=email, password=password)

    db.session.add(new_user)
    db.session.commit()
