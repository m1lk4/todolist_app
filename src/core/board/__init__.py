from src.models.list import List
from src.models.task import Task
from src.models.user import User
from src.models.tag import Tag
from src.database.todolist import db


def list_lists():
    return List.query.all()


def create_list(**kwargs):
    db.session.add(List(**kwargs))
    db.session.commit()


def update_list(id, name, description):
    list = List.query.get(id)
    list.name = name
    list.description = description
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


def update_task(id, name, status):
    task = Task.query.get(id)
    task.name = name
    task.status = status
    db.session.commit()


def delete_task(task):
    db.session.delete(task)
    db.session.commit()


task_status = ["New", "Pending", "In progress", "On hold", "Needs review", "Done"]


def list_user_fullname(user_fullname=None):
    list_fullname = []
    for row in User.query.all():
        fullname = row.name + " " + row.lastname
        list_fullname.append(fullname)
        if fullname == user_fullname:
            userid = row.id
            return userid

    return list_fullname


def create_tag(name):
    if name and name != "":
        try:
            db.session.add(Tag(name=name))
            db.session.commit()
        except Exception as e:
            print("Error desconocido:", e)


def list_tags():
    tags_list = [row.name for row in Tag.query.all()]

    return tags_list
