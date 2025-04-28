from flask_restx import Resource, Namespace
from save_bites.blueprints.restapi.services.hello import hello_service



api = Namespace('hello', description='Hello World')



@api.route('/')
class Hello(Resource):
    def get(self):
        return hello_service()

