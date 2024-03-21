from flask import Blueprint
from flask import render_template, url_for
from flask import request, redirect
from flask import flash

from src import auth

auth_blueprint = Blueprint("auth", __name__)


@auth_blueprint.get("/signup")
def signup():

    return render_template("auth/signup.html")


@auth_blueprint.post("/signup")
def create():
    username = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password")

    if not username or (not email) or (not password):
        fields = {"username": username, "email": email, "password": password}
        unfield = []
        for field_name, field in fields.items():
            if not field:
                unfield.append(field_name)

        return render_template(
            "/auth/signup.html",
            fields=unfield,
        )

    if username and email and password:
        if auth.has_account(username, email):
            flash(
                "User or email already exist. Please choose another username or email",
                "danger",
            )
            return redirect(url_for("auth.signup"))

        auth.create_user(username, email, password)
        flash("Registration successful. You can now log in.", "success")
        return redirect(url_for("auth.login"))


@auth_blueprint.get("/login")
def login():

    return render_template("auth/login.html")


@auth_blueprint.post("/login")
def authenticate():
    username = request.form.get("username")
    password = request.form.get("password")
    if auth.has_account(username=username) and auth.check_password(username, password):

        return redirect(url_for("list.index"))

    return redirect(url_for("auth.login"))
