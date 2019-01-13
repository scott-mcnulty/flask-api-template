from flask import Flask

from myapi import api, config
from myapi.extensions import db, jwt, migrate, ma, cache, cors, swagger, metrics
from myapi.api import api
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

    register_extensions(app, testing)
    return app


def register_extensions(app, testing=False):

    jwt.init_app(app)
    ma.init_app(app)
    cache.init_app(app)
    cors.init_app(app)
    swagger.init_app(app)
    api.init_app(app)
    
    # Getting: ValueError: Duplicated timeseries in CollectorRegistry: {'flask_http_request_duration_seconds_sum', 'flask_http_request_duration_seconds_count', 'flask_http_request_duration_seconds_bucket', 'flask_http_request_duration_seconds_created'}
    # Seems to be from virtualenv?
    if not testing:
        metrics.init_app(app)

    with app.app_context():
        db.init_app(app)
        db.create_all()
