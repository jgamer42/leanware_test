import jwt
import time
from flask import session


def generate_token(username):
    token = jwt.encode(
        {"user": username, "expires": time.time() + 60}, "secretKey", algorithm="HS256"
    )
    return token


def verify_token(token):
    decript = jwt.decode(token, "secretKey", algorithms=["HS256"])
    return (
        "user" in decript.keys()
        and "expires" in decript.keys()
        and decript.get("expires") >= time.time()
    )


def login_required(func):
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
