from flask import Blueprint
from src.views import traders as view

traders = Blueprint("traders", __name__, url_prefix="/traders")

traders.add_url_rule(
    "/symbols", "following_symbols", view.get_following_investments, methods=["GET"]
)
traders.add_url_rule(
    "/symbols/update",
    "update investments",
    view.update_following_investments,
    methods=["PUT","POST"],
)
