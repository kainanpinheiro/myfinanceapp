import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'finance crypt rs'
    SQLALCHEMY_TRACK_MODIFICATION = False
    SQLALCHEMY_RECORD_QUERIES = True


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite://' + os.path.join(basedir, 'data-dev.sqlite')


config = {
    'development': DevelopmentConfig,
}
