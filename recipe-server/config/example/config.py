import os
import secrets

# this means ../config
basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class BaseConfig(object):
    SECRET_KEY = secrets.token_urlsafe(16)

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask Mail
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False

    # Swagger
    SWAGGER = {
        'title': 'Flasgger RESTful',
        'uiversion': 2
    }


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = False

    SQLALCHEMY_DATABASE_URI = f'sqlite:///{basedir}/app-dev.db'


class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False

    SQLALCHEMY_DATABASE_URI = ''

    # flask-restful's error handler does not throw it's error to
    # flask's error handler when DEBUG = False
    # PROPAGATE_EXCEPTIONS = True will resolve this problem
    PROPAGATE_EXCEPTIONS = True


class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{basedir}/app-test.db'


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'test': TestConfig
}
