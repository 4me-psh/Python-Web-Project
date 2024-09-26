from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)

from FlaskApplication.Application.Services.CategoryOrchestrator import CategoryOrchestrator
from FlaskApplication.Domain.Models.Category.Category import Category
from FlaskApplication.Infrastructure.Repositories.CategoryRepository import CategoryRepository
from FlaskApplication.Presentation.Decorators import login_required

category_service = CategoryOrchestrator(CategoryRepository())

bp = Blueprint('category', __name__)

@bp.route('/category')
def index_category():
    categories = category_service.get_all_categories()
    return render_template('category/index.html', categories=categories)

@bp.route('/createCategory', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        error = None

        if not name:
            error = 'Name is required.'
        if  not description:
            error = 'Description is required.'
        if error is not None:
            flash(error)
        else:
            category_service.create_category(Category(category_id=None, name=name, description=description))
            return redirect(url_for('category.index_category'))

    return render_template('category/create.html')

