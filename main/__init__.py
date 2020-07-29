import os

import jinja2
from flask import Flask
from werkzeug.utils import import_string

import config


def create_app(cfg: str):
    app = Flask(__name__)
    # app.config.from_pyfile(os.path.join('..', 'config.cfg'))
    obj = import_string(cfg)
    app.config.from_object(obj)
    template_dir = os.path.join('.', 'templates')
    loader = jinja2.FileSystemLoader(os.path.join('.', template_dir))
    environment = jinja2.Environment(loader=loader)
    if app.app_context():
        from main.routes import register_blueprints
        register_blueprints(app)
        return app
