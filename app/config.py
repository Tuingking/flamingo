import os

from app.common.constants import DEBUG, DB_NAME

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # os.urandom(24)
    SECRET_KEY = '\x87\xd7\x14j\xee\x87\xbcS\x80\x98\xbc\x966q\xea\xd4\x03\x94s-\x96\x8d\x06\xbe'
    DEBUG = DEBUG
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
        os.path.join(basedir, DB_NAME)


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
        os.path.join(basedir, DB_NAME)
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
        os.path.join(basedir, DB_NAME)


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)
