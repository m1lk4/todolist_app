from flask import Blueprint
from flask import render_template, redirect
from flask import request

from src.models.list_model import List
from src.database.todolist_db import db

list_blueprint = Blueprint("list", __name__, url_prefix="/list")


@list_blueprint.get("/")
def list_view():
    return render_template("list_view.html")


@list_blueprint.get("/new")
def list_new():
    return render_template("list_new.html")


@list_blueprint.post("/")
def list_add():
    name = List(name=request.form.get("name"))
    db.session.add(name)
    db.session.commit()

    return redirect("/list")
