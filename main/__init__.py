# import os

# import cloudinary
# import jinja2
# from flask import Flask
# from flask_bcrypt import Bcrypt
# from flask_login import LoginManager


# def init_couldinary():
# CLOUDINARY_CLOUD_NAME = 'snsm-img'
# CLOUDINARY_API_KEY = '539871227625762'
# CLOUDINARY_API_SECRET = '1I3msDYBT5xsMZPbWAOFqkpdABI'

# cloudinary.config(
# cloud_name=CLOUDINARY_CLOUD_NAME,
# api_key=CLOUDINARY_API_KEY,
# api_secret=CLOUDINARY_API_SECRET
# )


# def create_app(conf: config.Config = config.DevelopmentConfig):
# app = Flask(__name__)
# # app.config.from_pyfile(os.path.join('..', 'config.cfg'))
# # template_dir = os.path.join('.', 'templates')
# # loader = jinja2.FileSystemLoader(template_dir)
# # environment = jinja2.Environment(loader=loader)
# # bcrypt = Bcrypt(app)
# # login_manager = LoginManager(app)
# # login_manager.login_view = 'login'
# # login_manager.login_message_category = 'info'
# with app.app_context():
# import main.routes
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "hola jime"


if __name__ == "__main__":
    app.run()
