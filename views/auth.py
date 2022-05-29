import json
from flask import request, jsonify
from flask_restx import Resource, Namespace
from implemented import auth_service

auth_ns = Namespace('auth')

@auth_ns.route('/register')
class AuthView(Resource):
    def post(self):
        req_json = request.json
        user = auth_service.create_new_user(email=req_json.get('email'),
                                            password=req_json.get('password'))
        token = auth_service.encode_auth_token(user.id)
        return jsonify({"access_token":token.decode()}), 201

@auth_ns.route('/login')
class AuthView(Resource):
    def post(self):
        req_json = request.json
        user = auth_service.get_by_email(email=req_json.get('email'))
        token = auth_service.decode_auth_token(req_json.get("access_token").encode())
        result = int(token) == int(user.id)
        return jsonify({"result":result}), 200

    def put(self):
        req_json = request.json
        token = auth_service.decode_auth_token(req_json.get("access_token").encode())
        refresh_token = auth_service.decode_auth_token(req_json.get("refresh_token").encode())
        if token == refresh_token:
            token = auth_service.encode_auth_token(token, days=10)
            return jsonify(token), 201
