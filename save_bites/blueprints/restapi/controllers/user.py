from flask_restx import Resource, Namespace
from save_bites.blueprints.restapi.services.user import UserService
from flask import request




api = Namespace('users', description='Users operations')



user_service = UserService()



@api.route('')
class Users(Resource):

    def post(self):
        user_data = request.json
        user_service.create_user_by_clerk_hook(user_data)   