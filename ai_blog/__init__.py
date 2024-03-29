import os

from flask import Flask
from flask_ckeditor import CKEditor

from flask_ngrok2 import run_with_ngrok


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)


    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'ai_blog.sqlite'),
    )

    app.config['AUDIO_STORE_BASE_URL'] = 'https://audio.cobiadigital.com'
    app.config['BASE_URL'] = 'https://aiblog.cobiadigital.com'

    ckeditor = CKEditor()
    ckeditor.init_app(app)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', view_func=blog.index)

    return app

app = create_app()
run_with_ngrok(app)
