"""Different application configurations"""
import os


class BaseConfig(object):

    DEBUG = os.environ.get('DEBUG', True)
    TESTING = os.environ.get('TESTING', True)
    SECRET_KEY = os.environ.get('SECRET_KEY', 'SECRET_KEY')

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'SQLALCHEMY_DATABASE_URI',
        'sqlite:////tmp/myapi.db'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get(
        'SQLALCHEMY_TRACK_MODIFICATIONS',
        False
    )

    # JWT

    # Flasgger
    SWAGGER = {
        'title': 'Myapi swagger docs.',
        'doc_dir': './myapi/api/docs/'
    }


class TestConfig(BaseConfig):
    """Used for when we run tests"""

    # Use in memory so database + tables can be recreated and 
    # dropped as a fixture step in pytest
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"


class ProdConfig(BaseConfig):
    """Deployment config"""
    
    TESTING = False
