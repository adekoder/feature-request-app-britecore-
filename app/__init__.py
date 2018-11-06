from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import configuration

db = SQLAlchemy();


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(configuration[config_name])

    db.init_app(app)

    from .main import main as main_bluprint
    app.register_blueprint(main_bluprint, url_prefix='/')

    return app