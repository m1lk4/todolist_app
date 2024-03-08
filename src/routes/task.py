from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect, url_for
from flask import flash

from src.core import board

task_blueprint = Blueprint("task", __name__, url_prefix="/lists/<int:list_id>/tasks")


@task_blueprint.get("/")
def new(list_id):
    list = board.get_list(list_id)
    print("Este es el id:", list_id)

    return render_template("tasks/new.html", list=list)


@task_blueprint.post("/")
def create(list_id):
    name = request.form.get("name")
    board.create_task(name=name, list_id=list_id)
    flash("Task created", "success")

    return redirect(url_for("list.show", list_id=list_id))


@task_blueprint.get("/<int:task_id>/edit")
def edit(list_id, task_id):
    list = board.get_list(list_id)
    task = board.get_task(task_id)

    return render_template("/tasks/edit.html", list=list, task=task)


@task_blueprint.post("/<int:task_id>/edit")
def update(list_id, task_id):
    name = request.form["name"]
    board.update_task(task_id, name)
    flash("Task edited", "success")

    return redirect(url_for("list.show", list_id=list_id))


@task_blueprint.get("/delete/<int:task_id>")
def delete(list_id, task_id):
    task = board.get_task(task_id)
    board.delete_task(task)
    flash("Task deleted", "success")

    return redirect(url_for("list.show", list_id=list_id))
