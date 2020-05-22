import hashlib

from functools import wraps

from flask import Blueprint, session, redirect, render_template, request

from models import User
from database import db

bp = Blueprint("users", __name__)


def hash(password):
    return hashlib.sha3_256(password.encode("UTF-8")).hexdigest()


def requires_login(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        user_id = session.get("user_id")
        if user_id:
            return fn(*args, **kwargs)
        else:
            return "Please login"
    return wrapper


def requires_admin(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        user_id = session.get("user_id")
        user = db.session.query(User).filter_by(id=user_id).one_or_none()
        if user and user.is_admin:
            return fn(*args, **kwargs)
        else:
            return "Only admin can see this"
    return wrapper


@bp.route("/secret")
@requires_login
def secret():
    return hash("Very secret")


@bp.route("/secret2")
@requires_admin
def secret2():
    return hash("Very secret2")


@bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        data = request.form
        if data["password1"] != data["password2"]:
            return redirect("/user/register")
        username = data["username"]
        password_hash = hash(data["password1"])

        user = User(username=username, password_hash=password_hash)
        db.session.add(user)
        db.session.commit()
        return redirect("/user/login")


@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        data = request.form
        user = db.session.query(User).filter_by(username=data.get("username")).one_or_none()
        if user and user.password_hash == hash(data.get("password")):
            session["user_id"] = user.id
            return redirect("/user/secret")
        else:
            if "user_id" in session:
                del session["user_id"]
            return redirect("/user/login")


@bp.route("/logout")
def logout():
    if "user_id" in session:
        del session["user_id"]
    return redirect("/user/login")

