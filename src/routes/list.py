from flask import Blueprint
from flask import render_template, redirect, url_for
from flask import request
from flask import flash

from src.core import board
from src.models.task import Task
from src.database.todolist_db import db

list_blueprint = Blueprint("list", __name__, url_prefix="/lists")


@list_blueprint.get("/")
def index():
    lists = board.list_lists()
    return render_template("lists/index.html", lists=lists)


@list_blueprint.get("/new")
def new():
    return render_template("lists/new.html")


@list_blueprint.post("/")
def create():
    name = request.form.get("name")
    board.create_list(name=name)
    flash("List created", "success")

    return redirect(url_for("list.index"))


@list_blueprint.get("/<int:list_id>/edit")
def edit(list_id):
    list = board.get_list(list_id)

    return render_template("lists/edit.html", list=list)


@list_blueprint.post("/<int:list_id>/edit")
def update(list_id):
    name = request.form["name"]
    board.update_list(list_id, name)
    flash("List edited", "success")

    return redirect(url_for("list.index"))


@list_blueprint.get("/delete/<int:list_id>")
def delete(list_id):
    list = board.get_list(list_id)
    db.session.delete(list)
    db.session.commit()

    flash("List deleted", "success")

    return redirect(url_for("list.index"))


@list_blueprint.get("/<int:list_id>")
def show(list_id):
    list = board.get_list(list_id)
    tasks = Task.query.all()

    return render_template("lists/show.html", list=list, tasks=tasks)
