from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect, url_for

from src.database.todolist_db import db
from src.models.task_model import Task
from src.models.list_model import List

task_blueprint = Blueprint("task", __name__, url_prefix="/lists/<int:id>/tasks")


@task_blueprint.get("/")
def new(id):

    return render_template("tasks/new.html", id=id)


@task_blueprint.post("/")
def create(id):
    task = Task(name=request.form.get("name"))
    db.session.add(task)
    db.session.commit()

    return redirect(url_for("list.show", id=id))


@task_blueprint.get("/<int:task_id>/edit")
def edit(id, task_id):
    list = List.query.get(id)
    task = Task.query.get(task_id)

    return render_template("/tasks/edit.html", list=list, task=task)


@task_blueprint.post("/<int:task_id>/edit")
def update(id, task_id):
    task_name = request.form["name"]
    task = Task.query.get(task_id)
    task.name = task_name
    db.session.commit()

    return redirect(url_for("list.show", id=id))


@task_blueprint.get("/delete/<int:task_id>")
def delete(id, task_id):
    task = Task.query.get(task_id)
    db.session.delete(task)
    db.session.commit()

    return redirect(url_for("list.show", id=id))
