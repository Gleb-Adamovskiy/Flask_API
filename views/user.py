import json
from flask import request
from flask_restx import Resource, Namespace
from implemented import auth_service
from util import check_autorization

user_ns = Namespace('user')

@user_ns.route('/')
class UserView(Resource):
    @check_autorization
    def get(self):
        auth_header = request.headers.get('Autorization')
        if auth_header:
            token = auth_header.split(" ")[1]
        else:
            token = ""
        uid = auth_service.decode_auth_token(token.encode())
        user = auth_service.get_by_id(uid)

        result = {
            "name":user.name,
            "email":user.email
        }

        return json.dump(result), 200

    @check_autorization
    def patch(self):
        auth_header = request.headers.get('Autorization')
        if auth_header:
            token = auth_header.split(" ")[1]
        else:
            token = ""
        uid = auth_service.decode_auth_token(token.encode())
        user = auth_service.get_by_id(uid)
        auth_service.update(user=user, name="A", surname="B")

        result = {
            "name": user.name,
            "email": user.email
        }

        return json.dump(result), 200

@user_ns.route('/password')
class AuthView(Resource):
    @check_autorization
    def put(self):
        auth_header = request.headers.get('Autorization')
        if auth_header:
            token = auth_header.split(" ")[1]
        else:
            token = ""
        uid = auth_service.decode_auth_token(token.encode())
        user = auth_service.get_by_id(uid)
        password_old = request.args.get('password_old')
        password_new = request.args.get('password_new')
        auth_service.update_password(user=user, password_old=password_old, password_new=password_new)

        result = {
            "name": user.name,
            "email": user.email
        }

        return json.dump(result), 200
