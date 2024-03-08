from src.models.list import List
from src.models.task import Task
from src.database.todolist import db


def list_lists():
    return List.query.all()


def create_list(**kwargs):
    db.session.add(List(**kwargs))
    db.session.commit()


def update_list(id, name):
    list = List.query.get(id)
    list.name = name
    db.session.commit()


def get_list(identifier):
    return List.query.get(identifier)


def delete_list(list):
    db.session.delete(list)
    db.session.commit()


def list_tasks(**kwargs):
    return Task.query.filter_by(**kwargs).all()


def get_task(identifier):
    return Task.query.get(identifier)


def create_task(**kwargs):
    db.session.add(Task(**kwargs))
    db.session.commit()


def update_task(id, name):
    task = Task.query.get(id)
    task.name = name
    db.session.commit()


def delete_task(task):
    db.session.delete(task)
    db.session.commit()
