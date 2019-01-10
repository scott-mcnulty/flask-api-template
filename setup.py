from setuptools import setup, find_packages

__version__ = '0.1'


setup(
    name='myapi',
    version=__version__,
    packages=find_packages(exclude=['tests', 'sql', 'venv', 'docker-testing']),
    install_requires=[
        'flask',
        'flask-sqlalchemy',
        'flask-restful',
        'flask-migrate',
        'flask-jwt-extended',
        'flask-marshmallow',
        'flask-caching',
        'marshmallow-sqlalchemy',
        'psycopg2',
        'gunicorn'
    ]
)
