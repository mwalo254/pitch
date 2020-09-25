import os

class Config:
    #SECRET_KEY = os.environ.get('SECRET_KEY')
    SECRET_KEY = 'many random bytes'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2:///pitch'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    SUBJECT_PREFIX = 'Pitch'
    SENDER_EMAIL = 'mwalonick@gmail.com'

    @staticmethod
    def init_app(app):
        pass

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2:///pitch_test'


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")



class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2:///pitch'
    DEBUG = True


    
config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig,
}