from flask import Blueprint
from flask import render_template, redirect
from flask import request

from src.models.list_model import List
from src.database.todolist_db import db

list_blueprint = Blueprint("list", __name__, url_prefix="/list")


@list_blueprint.get("/")
def show():
    return render_template("view.html")


@list_blueprint.get("/new")
def new():
    return render_template("new.html")


@list_blueprint.post("/")
def create():
    name = List(name=request.form.get("name"))
    db.session.add(name)
    db.session.commit()

    return redirect("/list")
