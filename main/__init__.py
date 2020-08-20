import os

import jinja2
from flask import Flask

import cloudinary
import config
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

conf = config.DevelopmentConfig

app = Flask(__name__)

API_URL = conf.API_URL

app.config.from_object(conf)

# Init bcrypt
bcrypt = Bcrypt(app)

# Init login_manager
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

# Init Cloudinary
CLOUDINARY_CLOUD_NAME = 'snsm-img'
CLOUDINARY_API_KEY = '539871227625762'
CLOUDINARY_API_SECRET = '1I3msDYBT5xsMZPbWAOFqkpdABI'

cloudinary.config(
    cloud_name=CLOUDINARY_CLOUD_NAME,
    api_key=CLOUDINARY_API_KEY,
    api_secret=CLOUDINARY_API_SECRET
)

template_dir = os.path.join('.', 'templates')
loader = jinja2.FileSystemLoader(os.path.join('.', template_dir))
environment = jinja2.Environment(loader=loader)

if app.app_context():
    import main.routes
