from flask import Blueprint
from flask import render_template, redirect
from flask import request
from flask import flash

from src.models.list_model import List
from src.database.todolist_db import db

list_blueprint = Blueprint("list", __name__, url_prefix="/lists")


@list_blueprint.get("/")
def index():
    lists = List.query.all()
    return render_template("index.html", lists=lists)


@list_blueprint.get("/new")
def new():
    return render_template("new.html")


@list_blueprint.post("/")
def create():
    list = List(name=request.form.get("name"))
    db.session.add(list)
    db.session.commit()

    return redirect("/lists")


@list_blueprint.get("/<int:id>")
def edit(id):
    list = List.query.get(id)
    name = list.name
    return render_template("edit.html", name=name, id=id)


@list_blueprint.post("/<int:id>")
def update(id):
    new_name = request.form["name"]
    list = List.query.get(id)
    list.name = new_name
    db.session.commit()

    flash("Ha editado la lista")

    return redirect("/lists")


@list_blueprint.get("/delete/<int:id>")
def delete(id):
    list = List.query.get(id)
    db.session.delete(list)
    db.session.commit()

    return redirect("/lists")
