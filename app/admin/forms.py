from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, IntegerField
from wtforms.validators import DataRequired
from wtforms import SubmitField


class AddCourseForm(FlaskForm):
    professor = StringField("Profesor:", validators=[DataRequired(message="Nombre del profesor")])
    title = StringField("Titulo:", validators=[DataRequired(message="Ingresa el título del curso")])
    description = TextAreaField("Descripción:", validators=[DataRequired(message="Ingresa la descripción")])
    link = StringField("Url del curso:", validators=[DataRequired(message="Ingresa la url del curso")])


class ReservationForm(FlaskForm):
    start = StringField('Inicio', validators=[DataRequired(message="Ingrese la fecha de inicio")])
    end = StringField('Fin', validators=[DataRequired(message="Ingrese la fecha de fin")])
    type = SelectField('Tipo', choices=[('Single', 'Single'), ('Double', 'Double'), ('Deluxe', 'Deluxe')], validators=[DataRequired(message="Seleccione el tipo de reserva")])
    requirement = SelectField('Requisito', choices=[('No Preference', 'No Preference'), ('Non Smoking', 'Non Smoking'), ('Smoking', 'Smoking')], validators=[DataRequired(message="Seleccione el requisito")])
    adults = IntegerField('Adultos', validators=[DataRequired(message="Ingrese el número de adultos")])
    children = IntegerField('Niños', default=0)
    requests = TextAreaField('Solicitudes Especiales')
    booking_id = SelectField('Reserva', coerce=int, validators=[DataRequired(message="Seleccione una reserva existente")])























































