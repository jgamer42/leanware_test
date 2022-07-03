from src.helpers import auth
from src.traders import Trader
from src.investments import Investment
from cerberus import Validator
from flask import jsonify, session, request


@auth.login_required
def get_following_investments():
    """
    Method to handle the route /traders/symbols
    GIVEN a GET request
    WHEN trader is trying to check wich symbols he follows
    THEN calls the trader controller to retrieve this information
    """
    try:
        output = {}
        investment_type = request.environ.get("REQUEST_URI").split("/")[-1]
        investment_type = investment_type.capitalize()
        user = session.get("user")
        trader_controller = Trader(user)
        investment_controller = Investment(investment_type)
        following_investment = trader_controller.get_follwing_investment(
            investment_type
        )
        for investment in following_investment:
            output[investment] = investment_controller.get_last_price_investment(
                investment
            )

        return jsonify(output), 200
    except Exception as E:
        return jsonify({"message": f"woops something went wrong,{E.message}"}), 500


@auth.login_required
def update_following_investments():
    """
    Method to handle the route /traders/symbols/update
    GIVEN a PUT request
    WHEN trader is trying tu update the symbols that he follows
    THEN calls the investment controller and the trader controller
    AND checks if the request is correct, the request may have the following structure
    {
        "Symbols":["List with the symbols to follow and exists in the API"]
    }
    AND retrieve the information
    """
    try:
        stock_controller = Investment("Stocks")
        symbol_controller = Investment("Symbols")
        investment_type = request.environ.get("REQUEST_URI").split("/")[2]
        investment_type = investment_type.capitalize()
        user = session.get("user")
        expected_request = {
            "Stocks": {
                "required": investment_type == "Stocks",
                "type": "list",
                "schema": {"type": "string"},
                "allowed": list(stock_controller.get_investments_available()),
            },
            "Symbols": {
                "required": investment_type == "Symbols",
                "type": "list",
                "schema": {"type": "string"},
                "allowed": list(symbol_controller.get_investments_available()),
            },
        }
        validator = Validator()
        validator.schema = expected_request
        if not validator.validate(request.json):
            return jsonify({"message": "bad request", "details": validator.errors}), 500
        trader_controller = Trader(user)
        new_investments = request.json.get(investment_type)
        output = trader_controller.update_user_investment(
            investment_type, new_investments
        )
        return jsonify(output), 200
    except Exception as E:
        return jsonify({"message": f"woops something went wrong, {E}"}), 500
