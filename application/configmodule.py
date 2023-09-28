# Config Module to change config based on environment


class Config(object):
    TESTING = True
    DEBUG = True
    SERVER_NAME = "localhost:2050"


class ProductionConfig(Config):
    # Use Production Server - This has been provided as example
    SERVER_NAME = "localhost:4050"
    TESTING = False


class DevelopmentConfig(Config):
    SERVER_NAME = "localhost:3050"
    DEBUG = False


class TestingConfig(Config):
    # This is technically unnecessary as each environment class inherits base config class
    TESTING = True
