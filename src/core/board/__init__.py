from src.models.list import List
from src.models.task import Task
from src.models.user import User
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
            print(userid)
            return userid
    print(list_fullname)

    return list_fullname
