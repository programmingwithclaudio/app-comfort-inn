# app/models.py
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from app import db


class User(db.Model, UserMixin):
    __tablename__ = "user_login"
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(64), nullable=False)
    lastname = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(32), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)
    phone = db.Column(db.String(25))  # Nuevo campo para el teléfono
    role = db.Column(db.String(10), nullable=False, default='user')  # Campo para el rol del usuario

    def set_password(self, password):
        self.password = generate_password_hash(password)

    # para verificar la contraseña del usuario
    def verify_password(self, password):
        return check_password_hash(self.password, password)

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_by_email(email):
        return User.query.filter_by(email=email).first()

    @staticmethod
    def get_by_id(user_id):
        return User.query.get(user_id)


class Complaint(db.Model):
    __tablename__ = "complaint"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    complaints_details = db.Column(db.Text, nullable=False)

    def __init__(self, name, email, phone, complaints_details):
        self.name = name
        self.email = email
        self.phone = phone
        self.complaints_details = complaints_details

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, complaint_id):
        return cls.query.get(complaint_id)

    @staticmethod
    def get_by_name(name):
        return Complaint.query.filter_by(name=name).first()

    @staticmethod
    def get_by_email(email):
        return Complaint.query.filter_by(email=email).first()

    @staticmethod
    def get_by_phone(phone):
        return Complaint.query.filter_by(phone=phone).first()

    @staticmethod
    def get_by_complaints_details(complaints_details):
        return Complaint.query.filter_by(complaints_details=complaints_details).first()
