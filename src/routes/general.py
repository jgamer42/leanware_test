from flask import Blueprint
from src.views import general as view


general = Blueprint("general", __name__)
general.add_url_rule(
    "/",
    "main_page",
    view.main_page,
)
general.add_url_rule("/login", "login", view.login, methods=["POST"])
general.add_url_rule("/logout", "logout", view.logout, methods=["POST", "GET"])
