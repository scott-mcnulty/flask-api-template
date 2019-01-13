from flask_restful import Resource
from flasgger.utils import swag_from


class HelloAPI(Resource):

    @swag_from('../docs/hello.yml')
    def get(self):
        return {'hello': 'world'}

    @swag_from('../docs/hello.yml')
    def post(self):
        return {'hello': 'world'}

    @swag_from('../docs/hello.yml')
    def put(self):
        return {'hello': 'world'}

    @swag_from('../docs/hello.yml')
    def delete(self):
        return {'hello': 'world'}
