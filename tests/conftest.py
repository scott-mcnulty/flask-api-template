import json
import pytest

from myapi.app import create_app
from myapi.extensions import db as _db
from myapi import config


@pytest.fixture
def app():
    _app = create_app(testing=True)
    ctx = _app.test_request_context()
    ctx.push()
    yield _app
    ctx.pop()


@pytest.fixture
def client():
    _app = create_app(testing=True)
    _client = _app.test_client()
    yield _client


@pytest.fixture
def db(app):
    _db.app = app

    with app.app_context():
        _db.create_all()

    yield _db

    _db.session.close()
    _db.drop_all()


@pytest.fixture
def auth_header(client):
    data = {
        'username': 'Us3rnam3',
        'password': 'P@ssw0rd'
    }
    r = client.post(
        '/auth',
        data=json.dumps(data),
        headers={'content-type': 'application/json'}
    )

    token = r.get_json()['access_token']
    return {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer {}'.format(token)
    }


@pytest.fixture
def example_product_json():
    return {
        "name": "The Greatest Showman (Blu-ray + DVD + Digital)",
        "value": 19.99
    }

