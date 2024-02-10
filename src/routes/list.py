from flask import Blueprint
from flask import render_template, redirect
from flask import request

from src.models.list_model import List
from src.database.todolist_db import db

list_blueprint = Blueprint("list", __name__, url_prefix="/lists")


@list_blueprint.get("/")
def index():
    lists = List.query.all()
    print(lists)
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
