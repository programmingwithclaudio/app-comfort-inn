# auth/routes.py
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
from .forms import LoginForm, SignupForm, ComplaintForm
from app.models import User, Complaint
from . import auth_bp
from app import login_manager
from app import db


@auth_bp.route("/")
def index():
    return redirect(url_for('auth.signin'))


@auth_bp.route("/signup", methods=["POST", "GET"])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for("admin.dashboard"))
    form = SignupForm()
    if form.validate_on_submit() and request.method == "POST":
        firstname = request.form["firstname"]
        lastname = request.form["lastname"]
        email = request.form["email"]
        password = request.form["password"]
        phone = request.form["phone"]
        role = request.form["role"]
        user = User( firstname=firstname, lastname=lastname, email=email, phone=phone, role=role)
        user.set_password(password)
        user.save()
        return redirect(url_for("auth.signin"))
    return render_template("auth/signup.html", form=form)


@auth_bp.route("/signin", methods=["POST", "GET"])
def signin():
    if current_user.is_authenticated:
        return redirect(url_for('admin.dashboard'))
    form = LoginForm()
    if form.validate_on_submit() and request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = User.get_by_email(email)
        if user is not None and user.verify_password(password):
            login_user(user)
            return redirect(url_for("admin.dashboard"))
    return render_template("auth/signin.html", form=form)

@auth_bp.route("/logout/")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.signin"))

# Cargar usuarios
@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(int(user_id))


@auth_bp.route("/contact-us", methods=["GET", "POST"])
def contact_us():
    form = ComplaintForm()
    if form.validate_on_submit() and request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        complaints_details = request.form["complaints_details"]

        # Guardar la queja en la base de datos
        complaint = Complaint(name=name, email=email, phone=phone, complaints_details=complaints_details)
        complaint.save()

        flash("Tu queja ha sido enviada con éxito.", "success")

        # Redirige a la misma página después de enviar el formulario
        return redirect(url_for("auth.signin"))

    return render_template('auth/contact_us.html', form=form)
