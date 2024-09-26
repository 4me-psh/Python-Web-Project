
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from FlaskApplication.Application.Services.PostOrchestrator import PostOrchestrator
from FlaskApplication.Domain.Models.Post.Post import Post
from FlaskApplication.Infrastructure.Repositories.PostRepository import PostRepository
from FlaskApplication.Presentation.Decorators import login_required

post_service = PostOrchestrator(PostRepository())

bp = Blueprint('blog', __name__)

@bp.route('/')
def index():
    posts = post_service.get_all_posts()
    return render_template('blog/index.html', posts=posts)

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            post_service.create_post(Post(title=title, body=body, author_id=g.user['id'], post_id=None, created_date=None))
            return redirect(url_for('blog.index'))

    return render_template('blog/create.html')


def get_post(id_post, check_author=True):
    post = post_service.get_post_by_id(post_id=id_post)

    if post is None:
        abort(404, f"Post id {id_post} doesn't exist.")

    if check_author and post.author_id != g.user['id']:
        abort(403)

    return post

@bp.route('/<int:id_post>/update', methods=('GET', 'POST'))
@login_required
def update(id_post):
    post = post_service.get_post_by_id(post_id=id_post)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            post_service.update_post(Post(post_id=id_post, title=title, body=body, author_id=g.user['id'], created_date=None))
            return redirect(url_for('blog.index'))

    return render_template('blog/update.html', post=post)

@bp.route('/<int:id_post>/delete', methods=('POST',))
@login_required
def delete(id_post):
    post_service.delete_post(post_id=id_post)
    return redirect(url_for('blog.index'))