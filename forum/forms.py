"""Forms declaration"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField(
        'Username',
        [
        ])
    email = StringField(
        'Email',
        [
        ])
    password = PasswordField(
        'Password',
        [
        ]
    )
    confirm = PasswordField(
        'Repeat Password',
        [
        ]
    )
    submit = SubmitField('Submit')