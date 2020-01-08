from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField, SelectMultipleField, RadioField, SelectField
from wtforms.fields.html5 import EmailField, DateField, IntegerField
from wtforms.validators import InputRequired, Email, Length, Regexp, ValidationError, NumberRange, DataRequired
from wtforms.widgets import ListWidget, CheckboxInput


class AdminLogin(FlaskForm):
    # Username = StringField('Username', validators=[InputRequired()])
    # by doing this we dont need check_password anymore (just for this assignment purpose)
    Username = StringField('Username', validators=[InputRequired()])
    Password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('login')


# future use for a page where users fill in a form
class CharacterForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired(), Length(4, 64), Regexp('^[A-Za-z][A-Za-z]*$', 0, 'Names must start with a letter and must have only letters (if contains anything else... you weird')])
    password = PasswordField('Password', validators=[InputRequired(), Length(4)])
    age = IntegerField('Age', validators=[InputRequired(), NumberRange(1, 100)])
    dob = DateField('Date of birth', validators=[InputRequired()])
    username = StringField('Username', validators=[InputRequired(), Length(4, 64), Regexp('^[A-Za-z0-9_.]*$', 0, 'Usernames can be anything')])
    select = SelectField('Favorite DarkSouls Game', validators=[InputRequired()], choices=[('1', 'DarkSouls'), ('2', 'DarkSouls2'), ('3', 'DarkSouls3')])
    submit = SubmitField('Submit')
