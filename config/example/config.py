class Config(object):
    # Flask Mail
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_DEFAULT_SENDER = 'hello@knowru.com'
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False


class DevelopmentConfig(Config):
    DEBUG = True
    BUCKET_NAME = 'alps-dev-s3'


class ProductionConfig(Config):
    DEBUG = False
    BUCKET_NAME = 'alps-dev-s3'


DEVELOPMENT_STAGE = 'development'

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
