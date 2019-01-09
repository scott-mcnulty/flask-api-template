from flask import Flask

from myapi import api, config
from myapi.extensions import db, jwt, migrate, ma, cache, cors, metrics
from myapi.commons.log import log


def create_app(testing=False):

    app = Flask('myapi')

    log('Using base config: {}'.format(config.BaseConfig.__dict__), 'debug')
    if testing:
        _config = config.TestConfig
    else:
        _config = config.ProdConfig
    app.config.from_object(_config)
    log('Set app config using `{}` with values: {}'.format(_config.__name__, _config.__dict__), 'debug')

    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app):

    jwt.init_app(app)
    ma.init_app(app)
    cache.init_app(app)
    cors.init_app(app)
    metrics.init_app(app)

    with app.app_context():
        db.init_app(app)
        db.create_all()


def register_blueprints(app):
    app.register_blueprint(api.endpoints.blueprint)
