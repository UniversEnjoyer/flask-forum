
from flask import render_template, url_for, redirect
from flask import current_app as app
from flask_login import current_user, login_user, login_required, logout_user

from .forms import RegistrationForm, LoginForm
from .models import User, db

from . import loginManger

@loginManger.user_loader
def load_user(user_id):
    if user_id is not None:
        return User.query.get(user_id)
    return None

@app.route('/register', methods = ['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user is None:
            user = User(
                username=form.username.data,
                email=form.email.data,
                password=form.password.data
            )
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect(url_for('home'))
    print(form.errors)
    return render_template(
        'register.html',
        form=form
    )

@app.route('/login', methods = ['GET', 'POST'])
def signin():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            return redirect(url_for('home'))
    return render_template(
        'login.html',
        form=form
    )

@app.route('/logout', methods = ['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('signin'))