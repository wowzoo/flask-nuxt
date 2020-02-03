from flask import Flask
from config.config import app_config
from app.exceptions import init_error_handlers
from app.extensions import db, ma, migrate, swag
from app import www, api


def create_app(config_name='development') -> Flask:
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('sensitive.py')

    app.url_map.strict_slashes = False

    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    swag.init_app(app)

    www.init_app(app)
    api.init_app(app)

    # error handler
    init_error_handlers(app)

    return app