import pytest
import requests
import json

from myapi import config
import myapi.api.modules.product as product


@pytest.mark.usefixtures('client', 'auth_header', 'example_product_json')
class TestProductAPI:

    def test_get_non_existing_product(self, client):

        example_id = 0
        r = client.get('/product/{}'.format(example_id))
        
        json_data = r.get_json()
        assert r.status_code == 200
        assert json_data == {}

    def test_no_product_id_supplied(self, client):

        r = client.get('/product')
        assert r.status_code == 400

    def test_create_new_product(self, client, auth_header, example_product_json):

        r = client.put(
            '/product',
            data=json.dumps(example_product_json),
            headers=auth_header
        )

        new_product_json_data = r.get_json()
        new_product_id = new_product_json_data['product_id']

        # Check that the record in the db matches what we supplied
        r = client.get('/product/{}'.format(new_product_id))
        
        json_data = r.get_json()
        assert r.status_code == 200
        assert json_data['product_id'] == new_product_json_data['product_id']
        assert json_data['name'] == new_product_json_data['name']
        assert json_data['value'] == new_product_json_data['value']

    # def test_product_id_field_in_get_response(self, client):

    #     r = client.get('/product/{}'.format(example_id))
        
    #     json_data = r.get_json()
    #     assert r.status_code == 200
    #     assert bool(json_data['product_id'])

    # def test_product_name_field_in_get_response(self, client):

    #     example_id = 13860428
    #     r = client.get('/product/{}'.format(example_id))
        
    #     json_data = r.get_json()
    #     assert r.status_code == 200
    #     assert bool(json_data['name'])

    # def test_product_value_field_in_get_response(self, client):

    #     example_id = 13860428
    #     r = client.get('/product/{}'.format(example_id))
        
    #     json_data = r.get_json()
    #     assert r.status_code == 200
    #     assert bool(json_data['value'])

    def test_response_for_non_numeric_product_id(self, client):
        """Used <int:product_id> when assigning the route to the api
        so giving string makes it think you're trying to find a diff url"""

        example_id = 'word'
        r = client.get('/product/{}'.format(example_id))
        json_data = r.get_json()
        assert r.status_code == 404

    def test_cannot_update_product_without_auth(self, client, example_product_json):

        r = client.put(
            '/product',
            data=json.dumps(example_product_json)
        )

        assert r.status_code == 401

    # def test_create_product_record_using_put(self, client, auth_header, example_product_json):

    #     r = client.put(
    #         '/product/{}'.format(example_product_json['id']),
    #         data=json.dumps(example_product_json),
    #         headers=auth_header
    #     )

    #     # Check that the record in the db matches what we supplied
    #     r = client.get('/product/{}'.format(example_product_json['id']))
        
    #     json_data = r.get_json()
    #     assert r.status_code == 200
    #     assert int(json_data['id']) == example_product_json['id']
    #     assert json_data['name'] == example_product_json['name']
    #     assert float(json_data['current_price']['value']) == example_product_json['current_price']['value']
    #     assert json_data['current_price']['currency_code'] == example_product_json['current_price']['currency_code']

    # def test_update_product_record_using_put(self, client, auth_header, example_product_json):

    #     r = client.put(
    #         '/product/{}'.format(example_product_json['id']),
    #         data=json.dumps(example_product_json),
    #         headers=auth_header
    #     )

    #     # Change the record we just made
    #     new_product_data = {
    #         "id": 123456789,
    #         "name": "FAKE NAME",
    #         "current_price": {
    #             "value": -10000,
    #             "currency_code": "CAD"
    #         }
    #     }
        
    #     r = client.put(
    #         '/product/{}'.format(new_product_data['id']),
    #         data=json.dumps(new_product_data),
    #         headers=auth_header
    #     )

    #     # Check that the record in the db matches what we supplied
    #     r = client.get('/product/{}'.format(new_product_data['id']))
        
    #     json_data = r.get_json()
    #     assert r.status_code == 200
    #     assert int(json_data['id']) == new_product_data['id']
    #     assert json_data['name'] == new_product_data['name']
    #     assert float(json_data['current_price']['value']) == new_product_data['current_price']['value']
    #     assert json_data['current_price']['currency_code'] == new_product_data['current_price']['currency_code']

    # def test_delete_non_existing_product_record(self, client, example_product_json, auth_header):

    #     r = client.delete(
    #         '/product/{}'.format(example_product_json['id']),
    #         data=json.dumps(example_product_json),
    #         headers=auth_header
    #     )

    #     assert r.status_code == 200
    #     assert r.get_json() == product.ProductAPIResponseMessages.no_product_to_delete(example_product_json['id'])

    # def test_delete_product_record(self, client, example_product_json, auth_header):

    #     r = client.put(
    #         '/product/{}'.format(example_product_json['id']),
    #         data=json.dumps(example_product_json),
    #         headers=auth_header
    #     )

    #     r = client.delete(
    #         '/product/{}'.format(example_product_json['id']),
    #         data=json.dumps(example_product_json),
    #         headers=auth_header
    #     )

    #     assert r.status_code == 200
    #     assert r.get_json() == product.ProductAPIResponseMessages.product_deleted(example_product_json['id'])

