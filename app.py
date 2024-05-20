#!/usr/bin/env python3

from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from forms import LoginForm, SignupForm
from models import User, db_user, get_user

app = Flask(__name__)
app.config["SECRET_KEY"] = "so-secret"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view= "signin"


@app.route("/")
def index():
    return redirect(url_for('signin'))

@app.route("/signup", methods=["POST", "GET"])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))
    form = SignupForm()
    if form.validate_on_submit() and request.method == "POST":
        firstname = request.form["firstname"]
        lastname = request.form["lastname"]
        email = request.form["email"]
        password = request.form["password"]
        user = User(id=len(db_user)+1 ,firstname=firstname, lastname=lastname, email=email, password=password)
        db_user.append(user)
        print(db_user)
        return redirect(url_for("signin"))
    return render_template("signup.html", form=form)


@app.route("/signin", methods=["POST", "GET"])
def signin():
    form = LoginForm()
    if form.validate_on_submit() and request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = get_user(email)
        print(user)
        if user is not None and user.verify_password(password):
            print(user.password)
            login_user(user)
            return redirect(url_for("dashboard"))
            
        #return render_template("signin.html")
    return render_template("signin.html", form=form)


@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("signin"))


@login_manager.user_loader
def load_user(user_id):
    for user in db_user:
        if user.id == int(user_id):
            return user
        return None
