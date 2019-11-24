from flask import Flask
from app import views
from config.config import app_config


def create_app(config_name='development'):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('sensitive.py')

    app.register_blueprint(views.bp)

    return app
