from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SelectField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    email = StringField("Email:", validators=[DataRequired(message="Enter your email address.")])
    password = PasswordField("Password:", validators=[DataRequired(message="Enter your password.")])


class SignupForm(FlaskForm):
    firstname = StringField("First Name:", render_kw={"placeholder": "First Name"},
                            validators=[DataRequired(message="Enter your first name.")])
    lastname = StringField("Last Name:", render_kw={"placeholder": "Last Name"},
                           validators=[DataRequired(message="Enter your last name.")])
    email = EmailField(render_kw={"placeholder": "Email" }, validators=[DataRequired(message="Enter an email address."), Email(message="Enter a valid email address.")])
    password = PasswordField("Password:", render_kw={"placeholder": "Password"},
                             validators=[DataRequired(message="Enter your password.")])
    phone = StringField("Phone:", render_kw={"placeholder": "Phone"},
                        validators=[DataRequired(message="Enter your phone number.")])
    role = SelectField("Role:", choices=[('user', 'User'), ('admin', 'Administrator')],
                       validators=[DataRequired(message="Select a role.")])

