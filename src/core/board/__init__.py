from src.models.list import List
from src.database.todolist_db import db


def list_lists():
    return List.query.all()


def create_list(**kwargs):
    list = List(**kwargs)
    db.session.add(list)
    db.session.commit()


def update_list(id, name):
    list = List.query.get(id)
    list.name = name
    db.session.commit()


def get_list(identifier):
    return List.query.get(identifier)
