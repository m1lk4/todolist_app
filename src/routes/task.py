from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect, url_for

from src.database.todolist_db import db
from src.models.task_model import Task

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
