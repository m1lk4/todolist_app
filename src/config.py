from os import environ


# Base configuration
class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = environ.get("SECRET_KEY")
    SESSION_COOKIE_SECURE = True


# Production configuration
class ProductionConfig(Config):
    DB_USER = environ.get("DB_USER")
    DB_PASS = environ.get("DB_PASS")
    DB_HOST = environ.get("DB_HOST")
    DB_NAME = environ.get("DB_NAME")
    SESSION_TYPE = "filesystem"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")


# Development configuration
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
    SESSION_TYPE = "filesystem"
    SESSION_COOKIE_SECURE = False


# Testing configuration
class TestingConfig(Config):
    TESTING = True


config = {
    "development": DevelopmentConfig,
    "test": TestingConfig,
    "production": ProductionConfig,
}
