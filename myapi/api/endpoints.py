from flask import Blueprint
from flask_restful import Api

from myapi.api.modules import (
    HelloAPI,
    AuthAPI,
    ProductAPI,
    ProductsAPI
)

api = Api()

api.add_resource(HelloAPI, '/hello')
api.add_resource(AuthAPI, '/auth')
api.add_resource(ProductAPI,
    '/product',
    '/product/<int:product_id>')
api.add_resource(ProductsAPI, '/products')
