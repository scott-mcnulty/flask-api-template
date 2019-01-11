import json

from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required

from myapi.models import Product, ProductSchema
from myapi import config
from myapi.commons.log import log
from myapi.commons.paginate import paginate
from myapi.extensions import ma, db


class ProductAPI(Resource):

    def __init__(self):

        # Json parser for creating/updating a product record
        product_parser = reqparse.RequestParser()
        product_parser.add_argument('name', type=str, required=True, help='No `name` supplied.', location='json')
        product_parser.add_argument('value', type=float, required=True, help='No `value` supplied.', location='json')
        self.product_parser = product_parser

    def get(self, product_id):
        """Handles GET requets"""

        # Check our storage for the product
        product = Product.query.filter_by(product_id=product_id).first()
        log('got product {} from database'.format(product), 'debug')

        if product:
            return ProductAPIResponseMessages.product_record_info_json(product)

        return ProductAPIResponseMessages.no_product_with_id(product_id)

    # def post(self):
    #     return ProductAPIResponseMessages.not_implemented()

    @jwt_required
    def put(self, product_id=None):
        """Handles PUT requests"""

        # Gets the supplied args
        args = self.product_parser.parse_args()
        log('got arguments: {}'.format(args))
        name = args.get('name')
        value = args.get('value')

        product = Product(
            product_id=product_id,
            name=name,
            value=value
        ).save()

        return ProductAPIResponseMessages.product_record_info_json(product)
    
    @jwt_required
    def delete(self, product_id):
        """Handles delete"""

        product = Product.query.filter_by(product_id=product_id).first()
        log('Got product to delete: {}'.format(product), 'debug')

        if product:
            product.delete()
            return ProductAPIResponseMessages.product_deleted(product_id)

        return ProductAPIResponseMessages.no_product_to_delete(product_id)



class ProductsAPI(Resource):

    def get(self):
        product_list_schema = ProductSchema(many=True)
        query = Product.query
        return paginate(query, product_list_schema)

    # def post(self):
    #     pass

    # def put(self):
    #     pass

    # def delete(self):
    #     pass




class ProductAPIResponseMessages(object):
    """Common product api response messages."""

    @staticmethod
    def product_record_info_json(product):
        product_schema = ProductSchema()
        return product_schema.dump(product).data

    @staticmethod
    def no_product_with_id(product_id):
        return {'message': 'No product with id: {}'.format(product_id)}
        
    @staticmethod
    def no_product_to_delete(product_id):
        return {'message': 'No product to delete with id: {}'.format(product_id)}

    @staticmethod
    def product_deleted(product_id):
        return {'message': 'Deleted product with id: {}'.format(product_id)}

    @staticmethod
    def not_implemented():
        return {'message': 'Method not implemented'}