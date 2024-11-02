from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length, Regexp, EqualTo

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[
        DataRequired(), 
        Email(message="Please enter a valid email address"),
        Length(max=120)
    ])
    username = StringField('Username', validators=[
        DataRequired(), 
        Length(min=3, max=30),
        Regexp('^[A-Za-z0-9_]+$', message="Username must contain only letters, numbers, and underscores")
    ])
    password = PasswordField('Password', validators=[
        DataRequired(),
        Length(min=8, max=128, message="Password must be between 8 and 128 characters")
    ])
    password_repeat = PasswordField('Confirm Password', validators=[
        DataRequired(),
        EqualTo('password', message="Passwords must match")
    ])
