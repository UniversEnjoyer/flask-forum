
from flask import render_template, url_for, redirect
from flask import current_app as app

from .forms import RegistrationForm

@app.route('/register', methods = ['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        return redirect(url_for('home'))
    print(form.errors)
    return render_template(
        'register.html',
        form=form
    )

@app.route('/', methods = ['GET', 'POST'])
def home():
    return render_template(
        'home.html',
        title='Home Test Page',
        description='Default Home description'
    )