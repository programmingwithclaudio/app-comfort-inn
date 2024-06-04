# auth/form.py
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SelectField, TextAreaField, TelField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class LoginForm(FlaskForm):
    email = StringField("Email:", validators=[DataRequired(message="Enter your email address.")])
    password = PasswordField("Password:", validators=[DataRequired(message="Enter your password.")])
    submit = SubmitField('Sign In')

class SignupForm(FlaskForm):
    firstname = StringField("First Name:", render_kw={"placeholder": "First Name"},
                            validators=[DataRequired(message="Enter your first name.")])
    lastname = StringField("Last Name:", render_kw={"placeholder": "Last Name"},
                           validators=[DataRequired(message="Enter your last name.")])
    email = EmailField(render_kw={"placeholder": "Email"}, validators=[DataRequired(message="Enter an email address."), Email(message="Enter a valid email address.")])
    password = PasswordField("Password:", render_kw={"placeholder": "Password"},
                             validators=[DataRequired(message="Enter your password.")])
    phone = StringField("Phone:", render_kw={"placeholder": "Phone"},
                        validators=[DataRequired(message="Enter your phone number.")])
    role = SelectField("Role:", choices=[('user', 'User'), ('admin', 'Administrator')],
                       validators=[DataRequired(message="Select a role.")])
    submit = SubmitField('Sign Up')

class ComplaintForm(FlaskForm):
    name = StringField("Full Name",
                       render_kw={"placeholder": "Full Name"},
                       validators=[DataRequired(message="Enter your full name."),
                                   Length(max=80, message="Name cannot exceed 80 characters.")])

    email = StringField("Email",
                        render_kw={"placeholder": "Your Email"},
                        validators=[DataRequired(message="Enter your email address."),
                                    Email(message="Enter a valid email address.")])

    phone = StringField("Phone",
                        render_kw={"placeholder": "Your Phone Number"},
                        validators=[DataRequired(message="Enter your phone number.")])

    complaints_details = TextAreaField("Complaints",
                                       render_kw={"placeholder": "Enter your complaints..."},
                                       validators=[DataRequired(message="Please enter your complaints.")])

    submit = SubmitField("Submit")


