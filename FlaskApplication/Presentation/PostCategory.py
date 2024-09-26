from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)

from FlaskApplication.Presentation.Blog import get_post

bp = Blueprint('postCategory', __name__)

@bp.route('/<int:id_post>/addPostCategory', methods=('GET', 'POST'))
def add_post_to_category(id_post):
    post = get_post(id_post)
    if request.method == 'POST':
        name_category = request.form['search_for_the_category']
        error = None

        if not name_category:
            error = 'Category is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO post_category (id_post, id_category)'
                ' VALUES (?, ?)',
                (id_post, id_category)
            )
            db.commit()
            return redirect(url_for('blog.index'))
    db = get_db()
    categories_exist = db.execute(
        'SELECT c.id, name FROM category c'
    ).fetchall()
    return render_template('postCategory/addPostCategory.html', post = post, categories = categories_exist)