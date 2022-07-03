from cerberus import Validator
from flask import request, jsonify, session
from src.traders import Trader
from src.helpers import auth


def login():
    """
    Method used as handler for the login API route
    Given a post request in /login with the following request Ie:
    {
        "username":"user1",
        "password":"secure_password"
    }
    When a trader is trying to login int the API
    Then validate the user information
    and check if is registred
    and check if the password if right
    """
    expected_request = {
        "username": {"type": "string"},
        "password": {"type": "string"},
    }
    user_name = request.json.get("username")
    validator = Validator()
    validator.schema = expected_request
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
    """
    Method used as a handler to the logout API rout
    Given a trader
    When is loging out from the API
    Then clean the session object
    """
    session.pop("token")
    session.pop("user")
    return jsonify({"message": "See you later"}), 200
