from src.helpers import auth as authHelper
from src.investments import Investment
from flask import request, jsonify
from botocore.exceptions import ClientError
from flask import send_file


@authHelper.login_required
def available_investments():
    """
    Method to handle the route /investments/symbols
    GIVEN a trader
    WHEN making a GET request to retrieve available symbols on the API
    THEN calls to investment controller to retrieve those information
    """
    investment_type = request.environ.get("REQUEST_URI").split("/")[-1]
    investment_type = investment_type.capitalize()
    controller = Investment(investment_type)
    output = controller.get_investments_available()
    return jsonify({investment_type: output}), 200


@authHelper.login_required
def price_investments(investment_name, start_date, end_date):
    """
    Method to handle the routes
    /investments/stocks/<investment_mane>/<start_date>
    /investments/stocks/<investment_mane>/<start_date>/<end_date>
    GIVEN a stock , start_date, end_date (optional)
    WHEN a trader trying to get the prices from a stocks in a timeframe
    THEN calls the investment controller to retrieve those information
    """
    try:
        investment_type = request.environ.get("REQUEST_URI").split("/")[2]
        investment_type = investment_type.capitalize()
        investment_name = investment_name.capitalize()
        controller = Investment(investment_type)
        data = controller.get_investment_prices(investment_name, start_date, end_date)
        if data != []:
            return jsonify(data), 200
        else:
            return jsonify({"Message": "Not prices registred on this timeframe"}), 200
    except ClientError:
        return (
            jsonify(
                {
                    "Message": "The first payment date must be previus than today or the end date"
                }
            ),
            400,
        )
    except Exception:
        return (
            jsonify(
                {"Message": "The first payment date must has the format dd-mm-yyyy"}
            ),
            400,
        )


@authHelper.login_required
def export():
    """
    Method to handle the route
    /investments/stocks/export
    GIVEN a GET request
    WHEN a trader trying to export all the symbol prices
    THEN calls the investment controller to build the .csv file
    AND bring them to the trader
    """
    try:
        investment_type = request.environ.get("REQUEST_URI").split("/")[2]
        investment_type = investment_type.capitalize()
        controller = Investment(investment_type)
        file = controller.export_all_investment_prices()
        return send_file(file, attachment_filename="data.csv")
    except:
        return jsonify({"Message": "Something went wrong"}), 500
