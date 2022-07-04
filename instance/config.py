import os


class Config(object):
    DEBUG = True
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://wuluoyu:password@localhost/backend'
    TESTING = False


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://wuluoyu:password@localhost/backend_test'
    TESTING = True

