import jwt
import time
from flask import session


def generate_token(username):
    """
    Function to generate a JWT token
    :param username: Str with the user to use the token
    :return token: token generated
    """
    token = jwt.encode(
        {"user": username, "expires": time.time() + 60}, "secretKey", algorithm="HS256"
    )
    return token


def verify_token(token):
    """
    Function to validate a JWT token
    To the token validations this methods checks:
    - if the token is expired
    - if the token has rigth structure
    :param token: token to validate
    :return bool: True if the token is valid False if not
    """
    decript = jwt.decode(token, "secretKey", algorithms=["HS256"])
    return (
        "user" in decript.keys()
        and "expires" in decript.keys()
        and decript.get("expires") >= time.time()
    )


def login_required(func):
    """
    Decorator to check if a user loged or no
    :param func: A pointer to the function with this constraint
    :return func: the func with the constraint
    """

    def validator(*args, **kwargs):
        if (
            "user" in session.keys()
            and "token" in session.keys()
            and verify_token(session.get("token"))
        ):
            return func(*args, **kwargs)
        else:
            return "forbiden", 403

    return validator
