# admin/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, IntegerField, FloatField, DateField
from wtforms.validators import DataRequired, InputRequired, Email, Regexp, NumberRange, Optional
from wtforms import SubmitField


class AddCourseForm(FlaskForm):
    professor = StringField("Profesor:", validators=[DataRequired(message="Nombre del profesor")])
    title = StringField("Titulo:", validators=[DataRequired(message="Ingresa el título del curso")])
    description = TextAreaField("Descripción:", validators=[DataRequired(message="Ingresa la descripción")])
    link = StringField("Url del curso:", validators=[DataRequired(message="Ingresa la url del curso")])


class ReservationForm(FlaskForm):
    booking_id = SelectField('Booking ID', validators=[DataRequired()])
    start_date = StringField('Fecha de Inicio', validators=[
        DataRequired(),
        Regexp(r'^\d{4}-\d{2}-\d{2}$', message="Formato de fecha incorrecto, debe ser YYYY-MM-DD")
    ])
    start_time = StringField('Hora de Inicio', validators=[
        DataRequired(),
        Regexp(r'^\d{2}:\d{2}$', message="Formato de hora incorrecto, debe ser HH:MM")
    ])
    end_date = StringField('Fecha de Fin', validators=[
        DataRequired(),
        Regexp(r'^\d{4}-\d{2}-\d{2}$', message="Formato de fecha incorrecto, debe ser YYYY-MM-DD")
    ])
    end_time = StringField('Hora de Fin', validators=[
        DataRequired(),
        Regexp(r'^\d{2}:\d{2}$', message="Formato de hora incorrecto, debe ser HH:MM")
    ])
    type = SelectField('Tipo', choices=[('Single', 'Single'), ('Double', 'Double'), ('Deluxe', 'Deluxe')], validators=[DataRequired(message="Seleccione el tipo de reserva")])
    requirement = SelectField('Requisito', choices=[('No Preference', 'No Preference'), ('Non Smoking', 'Non Smoking'), ('Smoking', 'Smoking')], validators=[DataRequired(message="Seleccione el requisito")])
    adults = IntegerField('Adultos', validators=[DataRequired(message="Ingrese el número de adultos")])
    children = IntegerField('Niños', default=0)
    requests = TextAreaField('Solicitudes Especiales')


class BookingForm(FlaskForm):
    cid = SelectField('Cliente', coerce=int, validators=[DataRequired()])
    status = SelectField('Estado', choices=[('PENDING', 'PENDING'), ('CONFIRMED', 'CONFIRMED'), ('CANCELLED', 'CANCELLED')], validators=[DataRequired()])
    notes = TextAreaField('Notas')


class CustomerForm(FlaskForm):
    identifier = StringField('Identificador completo', validators=[DataRequired()])
    fullname = StringField('Nombre completo', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Teléfono')


class PricingForm(FlaskForm):
    booking_id = SelectField('Booking', validators=[DataRequired()])
    nights = IntegerField('Nights', validators=[InputRequired()])
    total_price = FloatField('Total Price', validators=[InputRequired()])
    booked_date = DateField('Booked Date', validators=[InputRequired()], format='%Y-%m-%d')
    submit = SubmitField('Agregar Precio')


class AccountForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    type = SelectField('Type', choices=[('ASSET', 'ASSET'), ('LIABILITY', 'LIABILITY'), ('EQUITY', 'EQUITY'), ('REVENUE', 'REVENUE'), ('EXPENSE', 'EXPENSE')], validators=[DataRequired()])
    balance = FloatField('Balance', validators=[DataRequired(), NumberRange(min=0)])
    submit = SubmitField('Submit')


class CashFlowForm(FlaskForm):
    date = DateField('Date', validators=[DataRequired()])
    type = SelectField('Type', choices=[('INCOME', 'INCOME'), ('EXPENSE', 'EXPENSE')], validators=[DataRequired()])
    amount = FloatField('Amount', validators=[DataRequired(), NumberRange(min=0)])
    description = TextAreaField('Description', validators=[Optional()])
    account_id = SelectField('Account', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Submit')


class InvoiceForm(FlaskForm):
    booking_id = IntegerField('Booking ID', validators=[DataRequired()])
    issue_date = DateField('Issue Date', validators=[DataRequired()])
    due_date = DateField('Due Date', validators=[DataRequired()])
    subtotal = FloatField('Subtotal', validators=[DataRequired(), NumberRange(min=0)])
    taxes = FloatField('Taxes', validators=[DataRequired(), NumberRange(min=0)])
    total = FloatField('Total', validators=[DataRequired(), NumberRange(min=0)])
    status = SelectField('Status', choices=[('PENDING', 'PENDING'), ('PAID', 'PAID'), ('OVERDUE', 'OVERDUE')], validators=[DataRequired()])
    submit = SubmitField('Submit')


class SupplierForm(FlaskForm):
    identifier = StringField('Identificador completo', validators=[DataRequired()])
    fullname = StringField('Nombre completo', validators=[DataRequired()])
    contact = StringField('Contact', validators=[DataRequired()])
    address = TextAreaField('Address', validators=[Optional()])
    submit = SubmitField('Submit')


class SupplyForm(FlaskForm):
    supplier_id = SelectField('Supplier', coerce=int, validators=[DataRequired()])
    item = StringField('Item', validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired(), NumberRange(min=1)])
    cost = FloatField('Cost', validators=[DataRequired(), NumberRange(min=0)])
    date = DateField('Date', validators=[DataRequired()])
    submit = SubmitField('Submit')


class BankForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    account_id = SelectField('Account', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Submit')













































