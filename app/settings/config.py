import logging
import os

logger = logging.getLogger('covid_stats')
mongo_db_password = os.environ.get("mongo_db_password", default=None)


class Config(object):
    """Parent configuration class."""
    DEBUG = False
    NAME = "development"  # change it to APP_ENV
    MONGO_DB_URL = "mongodb://localhost:27017/covid"


class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True


class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    DEBUG = True
    NAME = "testing"
    MONGO_DB_URL = "mongodb://localhost:27017/covid"


class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False
    NAME = "production"
    MONGO_DB_URL = ""


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
