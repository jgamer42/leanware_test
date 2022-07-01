from flask import Blueprint


def user():
    return "here"


general = Blueprint("general", __name__)
general.add_url_rule("/login", "test", user)
general.add_url_rule("/logout", "test", user)
