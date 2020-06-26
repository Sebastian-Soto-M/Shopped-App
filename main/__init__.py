import os
import jinja2
import cloudinary
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# Constants
CLOUDINARY_CLOUD_NAME = 'snsm-img'
CLOUDINARY_API_KEY = '539871227625762'
CLOUDINARY_API_SECRET = '1I3msDYBT5xsMZPbWAOFqkpdABI'

# Init flask app
app = Flask(__name__)
app.config.from_pyfile(os.path.join('..', 'config.cfg'))

# Init jinja environment
template_dir = os.path.join('.', 'templates')
loader = jinja2.FileSystemLoader(template_dir)
environment = jinja2.Environment(loader=loader)

# Init bcrypt
bcrypt = Bcrypt(app)

# Init login_manager
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

# Init Cloudinary
cloudinary.config(
    cloud_name=CLOUDINARY_CLOUD_NAME,
    api_key=CLOUDINARY_API_KEY,
    api_secret=CLOUDINARY_API_SECRET
)

# Init routes
with app.app_context():
    import main.routes
