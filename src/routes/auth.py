from flask import Blueprint
from flask import render_template

auth_blueprint = Blueprint("auth", __name__)


@auth_blueprint.get("/signup")
def signup():

    return render_template("auth/signup.html")


@auth_blueprint.get("/login")
def login():

    return render_template("auth/login.html")
