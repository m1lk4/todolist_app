from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

from src.core import board

tag_blueprint = Blueprint("tag", __name__, url_prefix="/tags")


@tag_blueprint.get("/")
def index():
    tags = board.list_tags()

    return render_template("tags/index.html", tags=tags)


@tag_blueprint.get("/new")
def new():

    return render_template("tags/new.html")


@tag_blueprint.post("/new")
def create():
    tag_name = request.form.get("name")
    board.create_tag(tag_name)

    return redirect(url_for("tag.index"))
