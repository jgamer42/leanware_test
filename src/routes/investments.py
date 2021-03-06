from flask import Blueprint
import datetime
from src.views import investments as view


investments = Blueprint("investments", __name__, url_prefix="/investments")

investments.add_url_rule(
    "/symbols", "available_symbols", view.available_investments, methods=["GET"]
)
investments.add_url_rule(
    "/stocks/price/<investment_name>/<start_date>/<end_date>",
    "symbols prices",
    view.price_investments,
    methods=["GET"],
)
investments.add_url_rule(
    "/stocks/price/<investments_name>/<start_date>",
    "symbols prices v2",
    view.price_investments,
    methods=["GET"],
    defaults={"end_date": datetime.datetime.now().strftime("%d-%m-%Y")},
)
investments.add_url_rule(
    "/stocks/export", "export investments", view.export, methods=["GET"]
)
