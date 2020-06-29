import os

import jinja2
from flask import Flask

import config
from main.routes import register_blueprints


def create_app(conf: config.Config = config.DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config)
    register_blueprints(app)
    template_dir = os.path.join('.', 'templates')
    loader = jinja2.FileSystemLoader(os.path.join('.', template_dir))
    environment = jinja2.Environment(loader=loader)
    if app.app_context():
        return app
