from flask import Flask
from config.config import app_config
from app.extensions import db, migrate
from app import www, api


def create_app(config_name='development') -> Flask:
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('sensitive.py')

    app.url_map.strict_slashes = False

    db.init_app(app)
    migrate.init_app(app, db)

    www.init_app(app)
    api.init_app(app)

    return app
