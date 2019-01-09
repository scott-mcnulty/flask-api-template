from flask_restful import Resource

class HelloAPI(Resource):

    def get(self):
        return {'hello': 'world (get)'}

    def post(self):
        return {'hello': 'world (post)'}

    def put(self):
        return {'hello': 'world (put)'}

    def delete(self):
        return {'hello': 'world (delete)'}