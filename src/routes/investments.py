from flask import Blueprint
import datetime
from src.views import investments as view


investments = Blueprint("investments", __name__, url_prefix="/investments")

investments.add_url_rule(
    "/symbols", "available_symbols", view.available_symbols, methods=["GET"]
)
investments.add_url_rule(
    "/stocks/price/<investment_name>/<start_date>/<end_date>",
    "symbols prices",
    view.price_symbols,
    methods=["GET"],
)
investments.add_url_rule(
    "/stocks/price/<investment_name>/<start_date>",
    "symbols prices",
    view.price_symbols,
    methods=["GET"],
    defaults={"end_date": datetime.datetime.now().strftime("%d-%m-%Y")},
)
investments.add_url_rule(
    "/stocks/export", "export investments", view.export, methods=["GET"]
)
