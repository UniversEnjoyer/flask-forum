
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
        description='Default Home description',
        posts=Post.query.all()
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

@app.route('/view/<int:post_id>', methods = ['GET', 'POST'])
def view_post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template(
        'view_post.html',
        post=post
    )