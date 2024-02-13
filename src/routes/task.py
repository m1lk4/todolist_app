from flask import Blueprint
from flask import render_template

task_blueprint = Blueprint("task", __name__, url_prefix="/lists/<int:id>/tasks")


@task_blueprint.get("/")
def new(id):

    return render_template("tasks/new.html", id=id)
