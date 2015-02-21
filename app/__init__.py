import os
from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or \
                                            'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    db.init_app(app)

    from .main import app as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
