import os
import jwt
import time
from flask import session


def generate_token(username):
    """
    Function to generate a JWT token
    :param username: Str with the user to use the token
    :return token: token generated
    """
    token_life = int(os.getenv("TOKEN_LIFETIME", 60))
    secret_key = os.getenv("SECRET_KEY", "default_key")
    token = jwt.encode(
        {"user": username, "expires": time.time() + token_life},
        secret_key,
        algorithm="HS256",
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
    secret_key = os.getenv("SECRET_KEY", "default_key")
    decript = jwt.decode(token, secret_key, algorithms="HS256")
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
