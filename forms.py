from flask_wtf import FlaskForm
from wtforms import StringField, DateField, DecimalField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, EqualTo

#login form
class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember me")
    login = SubmitField("Login")

# registration form
class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    register = SubmitField("Register")

# settings form
class SettingsForm(FlaskForm):
    price = DecimalField("price", validators=[DataRequired()])