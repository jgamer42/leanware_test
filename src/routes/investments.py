from flask import Blueprint


def user():
    return "here"


investments = Blueprint("investments", __name__, url_prefix="/investments")

investments.add_url_rule("/symbols", "available_symbols", user)
investments.add_url_rule("/symbols/price", "symbols prices", user)
investments.add_url_rule("/stocks/export", "export investments", user)
