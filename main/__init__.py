import os

import jinja2
from flask import Flask

from main.routes import register_blueprints


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile(os.path.join('..', 'config.cfg'))
    register_blueprints(app)
    template_dir = os.path.join('.', 'templates')
    loader = jinja2.FileSystemLoader(os.path.join('.', template_dir))
    environment = jinja2.Environment(loader=loader)
    if app.app_context():
        return app
