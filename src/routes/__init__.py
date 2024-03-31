from flask import Blueprint
from flask import render_template

home_blueprint = Blueprint("home", __name__, url_prefix="/")


@home_blueprint.get("/")
def homepage():

    return render_template("home.html")
