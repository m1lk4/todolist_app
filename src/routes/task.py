from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect, url_for
from flask import flash

from datetime import datetime
import src.core.board as listfun

task_blueprint = Blueprint("task", __name__, url_prefix="/lists/<int:list_id>/tasks")


@task_blueprint.get("/")
def new(list_id):
    list = listfun.get_list(list_id)
    status = listfun.task_status
    list_users_fullname = listfun.list_user_fullname()

    return render_template(
        "tasks/new.html",
        task_status=status,
        list=list,
        list_users_fullname=list_users_fullname,
    )


@task_blueprint.post("/")
def create(list_id):
    name = request.form.get("name")
    status = request.form.get("status")
    due_date = request.form.get("due_date")
    user_fullname = request.form.get("assigned_to")
    userid = listfun.list_user_fullname(user_fullname)
    if userid:
        user_id = userid
    listfun.create_task(
        name=name,
        status=status,
        list_id=list_id,
        due_date=due_date,
        user_id=user_id,
    )
    flash("Task created", "success")

    return redirect(url_for("list.show", list_id=list_id))


@task_blueprint.get("/<int:task_id>/edit")
def edit(list_id, task_id):
    list = listfun.get_list(list_id)
    task = listfun.get_task(task_id)

    return render_template(
        "/tasks/edit.html", list=list, task=task, task_status=listfun.task_status
    )


@task_blueprint.post("/<int:task_id>/edit")
def update(list_id, task_id):
    name = request.form["name"]
    status = request.form["status"]
    listfun.update_task(task_id, name, status)
    flash("Task edited", "success")

    return redirect(url_for("list.show", list_id=list_id))


@task_blueprint.get("/delete/<int:task_id>")
def delete(list_id, task_id):
    task = listfun.get_task(task_id)
    listfun.delete_task(task)
    flash("Task deleted", "success")

    return redirect(url_for("list.show", list_id=list_id))
