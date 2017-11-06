from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_moment import Moment
from flask_debugtoolbar import DebugToolbarExtension

from .config import config_by_name

db = SQLAlchemy()

# Configure authentication
login_manager = LoginManager()
login_manager.session_protection = 'strong'  # basic | strong | None
login_manager.login_view = 'auth.login'

# for displaying timestamps
moment = Moment()

# Flask Debug Toolbar
toolbar = DebugToolbarExtension()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    login_manager.init_app(app)  # Authentication
    moment.init_app(app)  # Date and time lib
    toolbar.init_app(app)  # Debug Toolbar

    from .api import bp as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    # register more blueprint here

    return app
