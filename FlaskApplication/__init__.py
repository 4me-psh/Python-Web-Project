import os

from flask import Flask

def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'FlaskApplication.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from FlaskApplication.Infrastructure import DB
    DB.init_app(app)

    from FlaskApplication.Presentation import Category
    app.register_blueprint(Category.bp)
    app.add_url_rule('/category', endpoint='category', view_func=Category.index_category)

    from FlaskApplication.Presentation import Auth
    app.register_blueprint(Auth.bp)

    from FlaskApplication.Presentation import Blog
    app.register_blueprint(Blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app