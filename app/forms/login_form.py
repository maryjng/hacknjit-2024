from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length, Regexp, EqualTo

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[
        DataRequired(), 
        Email(message="Please enter a valid email address"),
        Length(max=120)
    ])
        
    password = PasswordField('Password', validators=[
        DataRequired(),
        Length(min=8, max=128, message="Password must be between 8 and 128 characters")
    ])