from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
from flask_login import login_user, current_user, logout_user, login_required

from backend import db, bcrypt
from backend.models import User
from backend.auth.forms import RegistrationForm, LoginForm
from backend.utils import redirect_dashboard

auth = Blueprint("auth", __name__)


@auth.route("/register/<role>", methods=["GET", "POST"])
def register_role(role):
    if role not in ["client", "coach"]:
        abort(404)

    if current_user.is_authenticated:
        return redirect_dashboard(current_user)

    form = RegistrationForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data
        ).decode("utf-8")

        user = User(
            username=form.username.data,
            email=form.email.data,
            password=hashed_password,
            role=role
        )

        db.session.add(user)
        db.session.commit()

        flash(f"Compte créé pour {form.username.data} !", "success")
        return redirect(url_for("auth.login"))

    return render_template("register.html", form=form)


@auth.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect_dashboard(current_user)

    form = LoginForm()

    if form.validate_on_submit():
        identifier = form.username_or_email.data

        user = User.query.filter(
            (User.email == identifier) | (User.username == identifier)
        ).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)

            next_page = request.args.get("next")
            return redirect(next_page) if next_page else redirect_dashboard(current_user)

        flash(
            "Connexion échouée. Vérifie ton email/nom d'utilisateur ou ton mot de passe.",
            "danger"
        )

    return render_template("login.html", form=form)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))