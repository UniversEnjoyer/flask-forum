"""Forms declaration"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField(
        'Username',
        [
            DataRequired()
        ])
    email = StringField(
        'Email',
        [
            DataRequired()
        ])
    password = PasswordField(
        'Password',
        [
            DataRequired()
        ]
    )
    confirm = PasswordField(
        'Repeat Password',
        [
            DataRequired()
        ]
    )
    submit = SubmitField('Submit')

class LoginForm(FlaskForm):
    username = StringField(
        'Username',
        [
            DataRequired()
        ])
    password = PasswordField(
        'Password',
        [
            DataRequired()
        ]
    )
    submit = SubmitField('Log In')