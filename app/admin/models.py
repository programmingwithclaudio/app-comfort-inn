# admin/models.py
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from app import db
from sqlalchemy import Enum
from datetime import datetime


class Customer(db.Model, UserMixin):
    __tablename__ = "customer"
    cid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    identifier = db.Column(db.String(20), nullable=False, unique=True)
    fullname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    phone = db.Column(db.String(25), nullable=True)

    # Renombramos el backref
    customer_bookings = db.relationship('Booking', backref='customer', lazy=True)

    @classmethod
    def find_by_id(cls, cid):
        return cls.query.get(cid)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Booking(db.Model):
    __tablename__ = "booking"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cid = db.Column(db.Integer, db.ForeignKey('customer.cid'), nullable=False)
    status = db.Column(db.Enum('PENDING', 'CONFIRMED', 'CANCELLED', name='booking_status'), default='PENDING')
    notes = db.Column(db.String(500), nullable=True)

    # Se usa 'customer_detail' para el backref
    customer_detail = db.relationship('Customer', backref='bookings')

    reservations = db.relationship('Reservation', backref='booking', lazy=True, cascade='all, delete-orphan')
    pricings = db.relationship('Pricing', backref='booking', lazy=True)

    @classmethod
    def find_by_id(cls, booking_id):
        return cls.query.get(booking_id)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Pricing(db.Model):
    __tablename__ = "pricing"
    pricing_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    booking_id = db.Column(db.Integer, db.ForeignKey('booking.id'), nullable=False)
    nights = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    booked_date = db.Column(db.Date, nullable=False)

    @classmethod
    def find_by_id(cls, pricing_id):
        return cls.query.get(pricing_id)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Reservation(db.Model):
    __tablename__ = "reservation"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    booking_id = db.Column(db.Integer, db.ForeignKey('booking.id'), nullable=False)
    start = db.Column(db.DateTime, nullable=False)
    end = db.Column(db.DateTime, nullable=False)
    type = db.Column(db.Enum('Single', 'Double', 'Deluxe', name='reservation_type'), default='Single')
    requirement = db.Column(db.Enum('No Preference', 'Non Smoking', 'Smoking', name='prevention'), default='No Preference')
    adults = db.Column(db.Integer, nullable=False)
    children = db.Column(db.Integer, default=0)
    requests = db.Column(db.String(500), nullable=True)
    timestamp = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    hash = db.Column(db.String(100), nullable=True)

    @classmethod
    def find_by_id(cls, reservation_id):
        return cls.query.get(reservation_id)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
