from flask import Blueprint


def user():
    return "here"


traders = Blueprint("traders", __name__, url_prefix="/traders")

traders.add_url_rule("/symbols", "following_symbols", user)
traders.add_url_rule("/update/investments", "update investments", user)
