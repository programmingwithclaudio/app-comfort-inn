# admin/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, IntegerField, FloatField, DateField
from wtforms.validators import DataRequired, Email, Regexp, NumberRange
from wtforms import SubmitField
from wtforms.validators import InputRequired


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
    nights = IntegerField('Nights', validators=[InputRequired()])
    total_price = FloatField('Total Price', validators=[InputRequired()])
    booked_date = DateField('Booked Date', validators=[InputRequired()], format='%Y-%m-%d')
















































