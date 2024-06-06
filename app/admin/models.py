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


class Account(db.Model):
    __tablename__ = "account"
    account_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.Enum('ASSET', 'LIABILITY', 'EQUITY', 'REVENUE', 'EXPENSE', name='account_type'), nullable=False)
    balance = db.Column(db.Float, nullable=False)

    cashflows = db.relationship('CashFlow', backref='account', lazy=True, cascade='all, delete-orphan')

    @classmethod
    def find_by_id(cls, account_id):
        return cls.query.get(account_id)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class CashFlow(db.Model):
    __tablename__ = "cashflow"
    flow_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.Date, nullable=False)
    type = db.Column(db.Enum('INCOME', 'EXPENSE', name='flow_type'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(500), nullable=True)
    account_id = db.Column(db.Integer, db.ForeignKey('account.account_id'), nullable=False)  # Foreign key added

    @classmethod
    def find_by_id(cls, flow_id):
        return cls.query.get(flow_id)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Invoice(db.Model):
    __tablename__ = "invoice"
    invoice_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    booking_id = db.Column(db.Integer, db.ForeignKey('booking.id'), nullable=False)
    issue_date = db.Column(db.Date, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    subtotal = db.Column(db.Float, nullable=False)
    taxes = db.Column(db.Float, nullable=False)
    total = db.Column(db.Float, nullable=False)
    status = db.Column(db.Enum('PENDING', 'PAID', 'OVERDUE', name='invoice_status'), default='PENDING')

    @classmethod
    def find_by_id(cls, invoice_id):
        return cls.query.get(invoice_id)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Supplier(db.Model):
    __tablename__ = "supplier"
    supplier_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    identifier = db.Column(db.String(20), nullable=False, unique=True)
    fullname = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200), nullable=True)

    supplies = db.relationship('Supply', backref='supplier', lazy=True, cascade='all, delete-orphan')

    @classmethod
    def find_by_id(cls, supplier_id):
        return cls.query.get(supplier_id)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Supply(db.Model):
    __tablename__ = "supply"
    supply_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    supplier_id = db.Column(db.Integer, db.ForeignKey('supplier.supplier_id'), nullable=False)
    item = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    cost = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, nullable=False)

    @classmethod
    def find_by_id(cls, supply_id):
        return cls.query.get(supply_id)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Bank(db.Model):
    __tablename__ = "bank"
    bank_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.account_id'), nullable=False)

    @classmethod
    def find_by_id(cls, bank_id):
        return cls.query.get(bank_id)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

