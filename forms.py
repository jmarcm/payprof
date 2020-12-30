from flask_wtf import FlaskForm
from wtforms import StringField, DateField, DecimalField, PasswordField, BooleanField, HiddenField, SubmitField, FormField, FieldList, IntegerField
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

# course form
class CourseForm(FlaskForm):
    name = StringField("Course name", validators=[DataRequired()])
    meeting_day = StringField("Day", validators=[DataRequired()])
    meeting_time = StringField("Time", validators=[DataRequired()])
    price = DecimalField("Price", validators=[DataRequired()])
    send = SubmitField("Send")

# add session form
class AddSessionForm(FlaskForm):
    date = DateField("Date",format="%d/%m/%Y", validators=[DataRequired()])
    paid = BooleanField("Paid")
    add = SubmitField("Add")

# paysession form
class PaySessionForm(FlaskForm):
    id = HiddenField("Id")
    date = DateField("Date", format="%d/%m/%Y", validators=[DataRequired()])
    paid = BooleanField("Paid")

# update session form
class UpdateSessionForm(FlaskForm):
    sessions = FieldList(FormField(PaySessionForm))
    update = SubmitField("Update")

class TelephoneForm(FlaskForm):
    country_code = IntegerField('Country Code', validators=[DataRequired()])
    area_code    = IntegerField('Area Code/Exchange', validators=[DataRequired()])
    number       = StringField('Number')

class ContactForm(FlaskForm):
    first_name   = StringField()
    last_name    = StringField()
    mobile_phone = FormField(TelephoneForm)
    office_phone = FormField(TelephoneForm)