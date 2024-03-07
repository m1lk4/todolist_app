from flask import Blueprint
from flask import render_template, url_for
from flask import request, redirect
from flask import flash

from src.models.user import User
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

    if not name or (not email) or (not password):
        fields = {"name": name, "email": email, "password": password}
        unfield = []
        for field_name, field in fields.items():
            if not field:
                unfield.append(field_name)

        return render_template(
            "/auth/signup.html",
            fields=unfield,
        )

    if name and email and password:
        if (
            User.query.filter_by(name=name).first()
            or User.query.filter_by(email=email).first()
        ):
            flash(
                "User or email already exist. Please choose another name or email",
                "danger",
            )
            return redirect(url_for("auth.signup"))

        create_user(name, email, password)
        flash("Registration successful. You can now log in.", "success")
        return redirect(url_for("list.index"))


@auth_blueprint.get("/login")
def login():

    return render_template("auth/login.html")
