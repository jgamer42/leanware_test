import re
from cerberus import Validator
from flask import request, jsonify, session
from src.trader import Trader
from src.helpers import auth


def login():
    expected_request_model = {
        "username": {"type": "string"},
        "password": {"type": "string"},
    }
    user_name = request.json.get("username")
    validator = Validator()
    validator.schema = expected_request_model
    if not validator.validate(request.json):
        return jsonify({"message": "Bad request"}), 404
    user = Trader(user_name)
    if not user.login(request.json.get("password")):
        return jsonify({"message": "bad password or user"}), 401
    token = auth.generate_token(user_name)
    session["token"] = token
    session["user"] = user_name
    return jsonify({"message": "welcome to the API"}), 200


@auth.login_required
def logout():
    session.pop("token")
    session.pop("user")
    return jsonify({"message": "See you later"}), 200
