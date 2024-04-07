from flask import Blueprint
from flask import render_template, redirect, url_for
from flask import request
from flask import flash

from src.core import board
from src import auth

list_blueprint = Blueprint("list", __name__, url_prefix="/lists")


@list_blueprint.get("/")
@auth.login_required
def index():
    lists = board.list_lists()
    return render_template("lists/index.html", lists=lists)


@list_blueprint.get("/new")
@auth.login_required
def new():
    return render_template("lists/new.html")


@list_blueprint.post("/")
def create():
    name = request.form.get("name")
    description = request.form.get("description")
    board.create_list(name=name, description=description)
    flash("List created", "success")

    return redirect(url_for("list.index"))


@list_blueprint.get("/<int:list_id>/edit")
@auth.login_required
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
@auth.login_required
def delete(list_id):
    list = board.get_list(list_id)
    board.delete_list(list)

    flash("List deleted", "success")

    return redirect(url_for("list.index"))


@list_blueprint.get("/<int:list_id>")
@auth.login_required
def show(list_id):
    list = board.get_list(list_id)
    tasks = board.list_tasks(list_id=list_id)

    return render_template("lists/show.html", list=list, tasks=tasks)
