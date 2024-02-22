from flask import Blueprint
from flask import render_template, url_for
from flask import request, redirect
from flask import flash

from src.models.user_model import User
from src.services.auth import create_user

auth_blueprint = Blueprint("auth", __name__)


@auth_blueprint.get("/signup")
def signup():

    return render_template("auth/signup.html")


@auth_blueprint.post("/signup")
def create():
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")

    if User.query.filter_by(name=name).first():
        flash("User already exist. Please choose another name", "danger")
        return redirect(url_for("auth.signup"))

    else:
        create_user(name, email, password)
        flash("Registration successful. You can now log in.", "sucess")
        return redirect(url_for("list.index"))


@auth_blueprint.get("/login")
def login():

    return render_template("auth/login.html")
