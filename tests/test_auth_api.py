import json

import pytest


@pytest.mark.usefixtures('client')
class TestAuthAPI:

    def test_post_to_auth_api_with_no_username(self, client):
        r = client.post('/auth')
        assert r.status_code == 400

    def test_post_to_auth_api_with_no_password(self, client):

        creds = {'username': 'test'}
        headers = {'content-type': 'application/json'}
        r = client.post(
            '/auth',
            data=json.dumps(creds),
            headers=headers)
        assert r.status_code == 400

    def test_post_to_auth_api_with_bad_username(self, client):

        creds = {'username': 'test', 'password': 'P@ssw0rd'}
        headers = {'content-type': 'application/json'}
        r = client.post(
            '/auth',
            data=json.dumps(creds),
            headers=headers)
        assert r.status_code == 401

    def test_post_to_auth_api_with_bad_password(self, client):

        creds = {'username': 'Us3rnam3', 'password': 'test'}
        headers = {'content-type': 'application/json'}
        r = client.post(
            '/auth',
            data=json.dumps(creds),
            headers=headers)
        assert r.status_code == 401

    def test_post_to_auth_api_successful(self, client):

        creds = {'username': 'Us3rnam3', 'password': 'P@ssw0rd'}
        headers = {'content-type': 'application/json'}
        r = client.post(
            '/auth',
            data=json.dumps(creds),
            headers=headers)
        assert r.status_code == 200
        assert 'access_token' in r.get_json().keys()

    def test_get_to_auth_api_using_token(self, client):

        creds = {'username': 'Us3rnam3', 'password': 'P@ssw0rd'}
        headers = {'content-type': 'application/json'}
        r = client.post(
            '/auth',
            data=json.dumps(creds),
            headers=headers)
        
        json_data = r.get_json()
        assert r.status_code == 200
        assert 'access_token' in r.get_json().keys()

        headers['Authorization'] = 'Bearer {}'.format(json_data['access_token'])
        r = client.get(
            '/auth',
            headers=headers)

        json_data = r.get_json()
        assert r.status_code == 200
        assert json_data == {'message': 'Hello, Us3rnam3'}
