from flask import Blueprint
from flask import render_template, url_for
from flask import request, redirect
from flask import flash
from flask import session

from src.core import auth

auth_blueprint = Blueprint("auth", __name__)


@auth_blueprint.get("/signup")
def signup():

    return render_template("auth/signup.html")


@auth_blueprint.post("/signup")
def create():
    username = request.form.get("username")
    name = request.form.get("name")
    lastname = request.form.get("lastname")
    email = request.form.get("email")
    password = request.form.get("password")
    rpassword = request.form.get("rpassword")

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
        elif password == rpassword:
            auth.create_user(username, name, lastname, email, password)
            flash("Registration successful. You can now log in.", "success")
            return redirect(url_for("auth.login"))
        else:
            flash("Password is incorrect.", "danger")
            return redirect(url_for("auth.signup"))


@auth_blueprint.get("/login")
def login():

    return render_template("auth/login.html")


@auth_blueprint.post("/login")
def authenticate():
    username = request.form.get("username")
    password = request.form.get("password")
    if auth.has_account(username=username) and auth.check_password(username, password):
        user = auth.get_user(username)
        session["user_id"] = user.id
        flash("You have logged in successfully.", "success")

        return redirect(url_for("home.homepage"))

    return redirect(url_for("auth.login"))


@auth_blueprint.get("/logout")
@auth.login_required
def logout():
    del session["user_id"]
    session.clear()
    flash("The session has been closed successfully.", "success")

    return redirect(url_for("auth.login"))
