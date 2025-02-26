
from flask import render_template
from flask import current_app as app

@app.route('/', methods = ['GET', 'POST'])
def home():
    return render_template(
        'home.html',
        title='Home Test Page',
        description='Default Home description'
    )