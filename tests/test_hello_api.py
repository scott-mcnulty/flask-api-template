import pytest


@pytest.mark.usefixtures('client')
class TestHelloAPI:

    def test_get(self, client):

        r = client.get('/hello')
        assert r.status_code == 200
        assert r.get_json() == {'hello': 'world (get)'}

    def test_post(self, client):
        r = client.post('/hello')
        assert r.status_code == 200
        assert r.get_json() == {'hello': 'world (post)'}

    def test_put(self, client):
        r = client.put('/hello')
        assert r.status_code == 200
        assert r.get_json() == {'hello': 'world (put)'}

    def test_delete(self, client):
        r = client.delete('/hello')
        assert r.status_code == 200
        assert r.get_json() == {'hello': 'world (delete)'}
