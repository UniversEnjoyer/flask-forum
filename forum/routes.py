from pydoc import describe

from flask import render_template, url_for
from flask import current_app as app
from werkzeug.utils import redirect

from forum import db
from forum.forms import PostForm
from forum.models import Post


@app.route('/', methods = ['GET', 'POST'])
def home():
    return render_template(
        'home.html',
        title='Home Test Page',
        description='Default Home description'
    )

@app.route('/post', methods = ['GET', 'POST'])
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(
            title=form.title.data,
            description=form.description.data
        )
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template(
        'create_post.html',
        form=form
    )